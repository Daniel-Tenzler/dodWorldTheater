import argparse
import csv
import json
from collections import deque
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_CONFIG = {
    "schema_version": "1.0.0",
    "distances": {
        "max_distance": 7,
        "warning_distance": 6,
        "unreachable_value": -1,
    },
    "graph": {
        "include_straits": True,
        "include_adjacency_types": ["land", "sea"],
        "exclude_sea_nodes": True,
        "ignore_island_components": True,
        "island_component_max_size": 20,
    },
    "rebalance": {
        "enabled": True,
        "suggestion_actions": ["replace", "swap"],
        "count_delta_limit_percent": 5,
        "max_suggestions": 200,
        "confidence_threshold": 0.7,
        "exclude_target_goods": ["sulphur"],
        "exclude_unreachable_for_iron": True,
    },
    "locking": {
        "locked_provinces": [],
        "locked_goods_by_province": {},
        "locked_regions": [],
        "locked_country_tags": [],
    },
    "io": {
        "write_graph_edges": False,
        "write_patch_csv": True,
    },
}


PROVINCE_CSV_HEADERS = [
    "id",
    "name",
    "is_land",
    "is_sea",
    "good",
    "dist_to_iron",
    "dist_to_coal",
    "paired_score",
    "status",
    "owner_tag",
    "start_pop",
    "total_life_rating",
]

SUGGESTION_CSV_HEADERS = [
    "priority",
    "action",
    "target_province_id",
    "target_name",
    "current_good",
    "suggested_good",
    "donor_province_id",
    "donor_name",
    "donor_current_good",
    "donor_suggested_good",
    "expected_paired_before",
    "expected_paired_after",
    "reason",
    "locked_violation",
    "confidence",
]

PATCH_CSV_HEADERS = [
    "province_id",
    "province_name",
    "file_path",
    "line_hint",
    "old_good",
    "new_good",
    "change_type",
    "source_suggestion_priority",
]


def deep_merge_dict(base, override):
    merged = dict(base)
    for key, value in override.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = deep_merge_dict(merged[key], value)
        else:
            merged[key] = value
    return merged


def load_config(config_path):
    if not config_path.exists():
        return DEFAULT_CONFIG
    raw = config_path.read_text(encoding="utf-8")
    if not raw.strip():
        return DEFAULT_CONFIG
    data = None
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        try:
            import yaml

            data = yaml.safe_load(raw)
        except Exception as exc:
            raise ValueError(f"Could not parse config file {config_path}: {exc}") from exc
    if data is None:
        return DEFAULT_CONFIG
    return deep_merge_dict(DEFAULT_CONFIG, data)


def parse_default_map(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    max_provinces = 0
    sea_starts = set()
    in_sea = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("max_provinces"):
            _, rhs = stripped.split("=", 1)
            max_provinces = int(rhs.strip())
        if stripped.startswith("sea_starts"):
            in_sea = True
        if in_sea:
            tokens = stripped.replace("{", " ").replace("}", " ").split()
            for token in tokens:
                if token.isdigit():
                    sea_starts.add(int(token))
            if "}" in stripped:
                in_sea = False
    return max_provinces, sea_starts


def parse_definition(path, sea_starts):
    def parse_int_token(token):
        value = token.strip()
        if not value:
            raise ValueError("Empty numeric token")
        if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
            return int(value)
        return int(float(value))

    provinces = {}
    color_to_id = {}
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader, None)
        for row in reader:
            if len(row) < 5:
                continue
            if not row[0].isdigit():
                continue
            pid = int(row[0])
            red = parse_int_token(row[1])
            green = parse_int_token(row[2])
            blue = parse_int_token(row[3])
            name = row[4].strip()
            is_sea = pid in sea_starts
            provinces[pid] = {
                "id": pid,
                "name": name,
                "is_sea": is_sea,
                "is_land": not is_sea,
                "good": None,
                "owner_tag": "",
                "start_pop": "",
                "total_life_rating": "",
                "history_file": "",
                "history_line_hint": "",
            }
            color_to_id[(red, green, blue)] = pid
    return provinces, color_to_id


def parse_history_provinces(history_root, provinces):
    for path in sorted(history_root.rglob("*.txt")):
        province_id = None
        prefix = path.name.split(" ", 1)[0]
        if prefix.isdigit():
            province_id = int(prefix)
        if province_id is None or province_id not in provinces:
            continue

        good = None
        owner = ""
        life_rating = ""
        hint_line = ""
        for index, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if "=" not in stripped:
                continue
            key, value = stripped.split("=", 1)
            key = key.strip()
            value = value.strip()
            if key == "trade_goods" and not good:
                good = value
                hint_line = str(index)
            elif key == "owner" and not owner:
                owner = value
            elif key == "life_rating" and not life_rating:
                life_rating = value

        provinces[province_id]["good"] = good
        provinces[province_id]["owner_tag"] = owner
        provinces[province_id]["total_life_rating"] = life_rating
        provinces[province_id]["history_file"] = str(path)
        provinces[province_id]["history_line_hint"] = hint_line


def parse_adjacencies(path, allowed_types):
    edges = set()
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            parts = stripped.split(";")
            if len(parts) < 3:
                continue
            if not parts[0].isdigit() or not parts[1].isdigit():
                continue
            edge_type = parts[2].strip().lower()
            if edge_type not in allowed_types:
                continue
            a = int(parts[0])
            b = int(parts[1])
            if a == b:
                continue
            edges.add((min(a, b), max(a, b), edge_type, "adjacencies_csv"))
    return edges


def build_edges_from_bmp(bmp_path, color_to_id):
    with bmp_path.open("rb") as f:
        data = f.read()

    if data[0:2] != b"BM":
        raise ValueError(f"Unsupported BMP header in {bmp_path}")

    pixel_offset = int.from_bytes(data[10:14], "little")
    dib_size = int.from_bytes(data[14:18], "little")
    if dib_size < 40:
        raise ValueError("Unsupported BMP DIB header size")

    width = int.from_bytes(data[18:22], "little", signed=True)
    height = int.from_bytes(data[22:26], "little", signed=True)
    bits_per_pixel = int.from_bytes(data[28:30], "little")
    compression = int.from_bytes(data[30:34], "little")

    if compression != 0:
        raise ValueError("Compressed BMP formats are not supported")
    if bits_per_pixel not in (24, 32):
        raise ValueError(f"Unsupported BMP bpp: {bits_per_pixel}. Expected 24 or 32.")

    abs_width = abs(width)
    abs_height = abs(height)
    bytes_per_pixel = bits_per_pixel // 8
    row_stride = ((abs_width * bytes_per_pixel + 3) // 4) * 4

    edges = set()
    prev_row = None

    for row_index in range(abs_height):
        row_start = pixel_offset + row_index * row_stride
        row_bytes = data[row_start : row_start + row_stride]
        row_ids = []

        cursor = 0
        for _ in range(abs_width):
            blue = row_bytes[cursor]
            green = row_bytes[cursor + 1]
            red = row_bytes[cursor + 2]
            cursor += bytes_per_pixel
            pid = color_to_id.get((red, green, blue), 0)
            row_ids.append(pid)

        for col in range(abs_width - 1):
            left = row_ids[col]
            right = row_ids[col + 1]
            if left and right and left != right:
                edges.add((min(left, right), max(left, right), "land", "bmp_border"))

        if prev_row is not None:
            for col in range(abs_width):
                up = prev_row[col]
                down = row_ids[col]
                if up and down and up != down:
                    edges.add((min(up, down), max(up, down), "land", "bmp_border"))

        prev_row = row_ids

    return edges


def build_graph(provinces, bmp_edges, extra_edges, exclude_sea_nodes):
    graph = {pid: set() for pid in provinces}

    for a, b, _, _ in bmp_edges:
        if a in graph and b in graph:
            graph[a].add(b)
            graph[b].add(a)

    for a, b, _, _ in extra_edges:
        if a in graph and b in graph:
            graph[a].add(b)
            graph[b].add(a)

    if exclude_sea_nodes:
        sea_ids = {pid for pid, p in provinces.items() if p["is_sea"]}
        for pid in sea_ids:
            graph[pid].clear()
        for pid, neighbors in graph.items():
            if pid in sea_ids:
                continue
            graph[pid] = {nid for nid in neighbors if nid not in sea_ids}

    return graph


def find_island_province_ids(graph, provinces, island_component_max_size):
    visited = set()
    islands = set()

    for pid, province in provinces.items():
        if not province.get("is_land"):
            continue
        if pid in visited:
            continue

        component = set()
        stack = [pid]
        visited.add(pid)

        while stack:
            node = stack.pop()
            component.add(node)
            for neighbor in graph.get(node, set()):
                if neighbor in visited:
                    continue
                if not provinces.get(neighbor, {}).get("is_land"):
                    continue
                visited.add(neighbor)
                stack.append(neighbor)

        if len(component) <= island_component_max_size:
            islands.update(component)

    return islands


def compute_multi_source_distances(graph, source_nodes, unreachable_value=-1):
    distances = {node: unreachable_value for node in graph}
    queue = deque()
    for source in source_nodes:
        if source in graph:
            distances[source] = 0
            queue.append(source)

    while queue:
        node = queue.popleft()
        current_distance = distances[node]
        for neighbor in graph[node]:
            if distances[neighbor] == unreachable_value:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)
    return distances


def classify_status(is_land, dist_to_iron, dist_to_coal, max_distance, warning_distance):
    if not is_land:
        return "SEA"
    if dist_to_iron < 0 or dist_to_coal < 0:
        return "FAIL"
    if dist_to_iron > max_distance or dist_to_coal > max_distance:
        return "FAIL"
    if max(dist_to_iron, dist_to_coal) >= warning_distance:
        return "WARN"
    return "PASS"


def build_province_rows(provinces, dist_iron, dist_coal, max_distance, warning_distance, island_ids):
    rows = []
    for pid in sorted(provinces.keys()):
        province = provinces[pid]
        if province["is_land"]:
            d_iron = dist_iron.get(pid, -1)
            d_coal = dist_coal.get(pid, -1)
            paired = max(d_iron, d_coal) if d_iron >= 0 and d_coal >= 0 else -1
        else:
            d_iron = -1
            d_coal = -1
            paired = -1

        if pid in island_ids:
            status = "ISLAND"
        else:
            status = classify_status(
                province["is_land"],
                d_iron,
                d_coal,
                max_distance,
                warning_distance,
            )

        rows.append(
            {
                "id": pid,
                "name": province["name"],
                "is_land": province["is_land"],
                "is_sea": province["is_sea"],
                "good": province.get("good") or "",
                "dist_to_iron": d_iron,
                "dist_to_coal": d_coal,
                "paired_score": paired,
                "status": status,
                "owner_tag": province.get("owner_tag", ""),
                "start_pop": province.get("start_pop", ""),
                "total_life_rating": province.get("total_life_rating", ""),
            }
        )
    return rows


def percentile_int(values, p):
    if not values:
        return -1
    values_sorted = sorted(values)
    index = int((len(values_sorted) - 1) * p)
    return values_sorted[index]


def build_summary(provinces, rows, max_provinces, max_distance, warning_distance, include_straits):
    land_rows = [r for r in rows if r["is_land"] and r["status"] != "ISLAND"]
    island_rows = [r for r in rows if r["status"] == "ISLAND"]
    pass_rows = [r for r in land_rows if r["status"] == "PASS"]
    warn_rows = [r for r in land_rows if r["status"] == "WARN"]
    fail_rows = [r for r in land_rows if r["status"] == "FAIL"]

    iron_d = [r["dist_to_iron"] for r in land_rows if r["dist_to_iron"] >= 0]
    coal_d = [r["dist_to_coal"] for r in land_rows if r["dist_to_coal"] >= 0]
    paired_d = [r["paired_score"] for r in land_rows if r["paired_score"] >= 0]

    def stat_block(vals):
        if not vals:
            return {"min": -1, "p50": -1, "p90": -1, "max": -1}
        return {
            "min": min(vals),
            "p50": percentile_int(vals, 0.5),
            "p90": percentile_int(vals, 0.9),
            "max": max(vals),
        }

    iron_count = sum(1 for p in provinces.values() if p.get("good") == "iron")
    coal_count = sum(1 for p in provinces.values() if p.get("good") == "coal")

    worst = sorted(
        land_rows,
        key=lambda r: (
            9999 if r["paired_score"] < 0 else r["paired_score"],
            r["id"],
        ),
        reverse=True,
    )[:20]

    pass_percent = round((len(pass_rows) / len(land_rows) * 100.0), 2) if land_rows else 0.0

    return {
        "schema_version": "1.0.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "input": {
            "mod_root": "",
            "max_provinces": max_provinces,
            "max_distance": max_distance,
            "warning_distance": warning_distance,
            "include_straits": include_straits,
        },
        "counts": {
            "total_provinces": len(provinces),
            "land_provinces": len(land_rows),
            "sea_provinces": len([r for r in rows if r["is_sea"]]),
            "island_ignored_provinces": len(island_rows),
            "iron_provinces": iron_count,
            "coal_provinces": coal_count,
        },
        "compliance": {
            "pass_count": len(pass_rows),
            "warn_count": len(warn_rows),
            "fail_count": len(fail_rows),
            "pass_percent": pass_percent,
        },
        "distance_stats": {
            "iron": stat_block(iron_d),
            "coal": stat_block(coal_d),
            "paired_score": stat_block(paired_d),
        },
        "worst_provinces": [
            {
                "id": r["id"],
                "name": r["name"],
                "good": r["good"] or None,
                "dist_to_iron": r["dist_to_iron"],
                "dist_to_coal": r["dist_to_coal"],
                "paired_score": r["paired_score"],
                "status": r["status"],
            }
            for r in worst
        ],
        "notes": [
            "Distances are edge-count shortest paths on province graph",
            "Sea provinces excluded from compliance",
            "Small island components are excluded from compliance",
        ],
    }


def needed_good_for_row(row):
    d_iron = row["dist_to_iron"]
    d_coal = row["dist_to_coal"]
    if d_iron < 0 and d_coal < 0:
        return "coal"
    if d_iron < 0:
        return "iron"
    if d_coal < 0:
        return "coal"
    return "iron" if d_iron >= d_coal else "coal"


def generate_suggestions(
    provinces,
    province_rows,
    locked_provinces,
    max_suggestions,
    suggestion_actions,
    exclude_target_goods,
    exclude_unreachable_for_iron,
):
    suggestions = []
    failed = [r for r in province_rows if r["status"] == "FAIL" and r["id"] not in locked_provinces]
    failed.sort(key=lambda r: (9999 if r["paired_score"] < 0 else r["paired_score"]), reverse=True)

    donors = [
        r
        for r in province_rows
        if r["status"] == "PASS"
        and r["paired_score"] >= 0
        and r["paired_score"] <= 3
        and provinces[r["id"]].get("good") in {"iron", "coal"}
        and r["id"] not in locked_provinces
    ]

    donor_pool = {"iron": [], "coal": []}
    for d in donors:
        donor_pool[provinces[d["id"]]["good"]].append(d)

    priority = 1
    used_donors = set()
    for row in failed:
        if len(suggestions) >= max_suggestions:
            break
        target = provinces[row["id"]]
        need = needed_good_for_row(row)
        current_good = target.get("good") or ""

        if current_good.lower() in exclude_target_goods:
            continue
        if exclude_unreachable_for_iron and need == "iron" and row["dist_to_iron"] < 0:
            continue

        # Prefer direct replacement when both actions are enabled.
        if "replace" in suggestion_actions:
            suggestions.append(
                {
                    "priority": priority,
                    "action": "replace",
                    "target_province_id": row["id"],
                    "target_name": target["name"],
                    "current_good": current_good,
                    "suggested_good": need,
                    "donor_province_id": "",
                    "donor_name": "",
                    "donor_current_good": "",
                    "donor_suggested_good": "",
                    "expected_paired_before": row["paired_score"],
                    "expected_paired_after": max(0, row["paired_score"] - 3) if row["paired_score"] >= 0 else 7,
                    "reason": "Remote fail cluster; nearest required resource too far",
                    "locked_violation": False,
                    "confidence": 0.86,
                }
            )
            priority += 1
            continue

        if "swap" in suggestion_actions and current_good not in {"iron", "coal"}:
            candidates = [d for d in donor_pool.get(need, []) if d["id"] not in used_donors]
            if candidates:
                donor = candidates[0]
                used_donors.add(donor["id"])
                donor_province = provinces[donor["id"]]
                suggestions.append(
                    {
                        "priority": priority,
                        "action": "swap",
                        "target_province_id": row["id"],
                        "target_name": target["name"],
                        "current_good": current_good,
                        "suggested_good": need,
                        "donor_province_id": donor["id"],
                        "donor_name": donor_province["name"],
                        "donor_current_good": need,
                        "donor_suggested_good": current_good,
                        "expected_paired_before": row["paired_score"],
                        "expected_paired_after": max(0, row["paired_score"] - 4),
                        "reason": "Donor in oversupplied cluster; preserves global totals",
                        "locked_violation": False,
                        "confidence": 0.78,
                    }
                )
                priority += 1
                continue

    return suggestions


def write_summary_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def write_csv(path, headers, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_province_csv(path, rows):
    write_csv(path, PROVINCE_CSV_HEADERS, rows)


def write_suggestions_csv(path, rows):
    write_csv(path, SUGGESTION_CSV_HEADERS, rows)


def write_patch_csv(path, suggestions, provinces):
    rows = []
    for suggestion in suggestions:
        priority = suggestion["priority"]
        if suggestion["action"] == "replace":
            pid = suggestion["target_province_id"]
            p = provinces[pid]
            rows.append(
                {
                    "province_id": pid,
                    "province_name": p["name"],
                    "file_path": p.get("history_file", ""),
                    "line_hint": p.get("history_line_hint", ""),
                    "old_good": suggestion["current_good"],
                    "new_good": suggestion["suggested_good"],
                    "change_type": "replace",
                    "source_suggestion_priority": priority,
                }
            )
        elif suggestion["action"] == "swap":
            t_id = suggestion["target_province_id"]
            d_id = suggestion["donor_province_id"]
            t = provinces[t_id]
            d = provinces[d_id]
            rows.append(
                {
                    "province_id": t_id,
                    "province_name": t["name"],
                    "file_path": t.get("history_file", ""),
                    "line_hint": t.get("history_line_hint", ""),
                    "old_good": suggestion["current_good"],
                    "new_good": suggestion["suggested_good"],
                    "change_type": "swap_target",
                    "source_suggestion_priority": priority,
                }
            )
            rows.append(
                {
                    "province_id": d_id,
                    "province_name": d["name"],
                    "file_path": d.get("history_file", ""),
                    "line_hint": d.get("history_line_hint", ""),
                    "old_good": suggestion["donor_current_good"],
                    "new_good": suggestion["donor_suggested_good"],
                    "change_type": "swap_donor",
                    "source_suggestion_priority": priority,
                }
            )
    write_csv(path, PATCH_CSV_HEADERS, rows)


def write_graph_edges(path, edges):
    path.parent.mkdir(parents=True, exist_ok=True)
    headers = ["from_id", "to_id", "edge_type", "source"]
    rows = [
        {
            "from_id": a,
            "to_id": b,
            "edge_type": edge_type,
            "source": source,
        }
        for a, b, edge_type, source in sorted(edges)
    ]
    write_csv(path, headers, rows)


def find_resource_sets(provinces):
    iron_ids = {pid for pid, p in provinces.items() if p.get("good") == "iron" and p["is_land"]}
    coal_ids = {pid for pid, p in provinces.items() if p.get("good") == "coal" and p["is_land"]}
    return iron_ids, coal_ids


def run_analyzer(mod_root, config_path, reports_dir, patches_dir):
    config = load_config(config_path)

    max_distance = config["distances"]["max_distance"]
    warning_distance = config["distances"]["warning_distance"]
    unreachable_value = config["distances"]["unreachable_value"]
    include_straits = config["graph"]["include_straits"]
    include_types = set(config["graph"]["include_adjacency_types"])
    exclude_sea_nodes = config["graph"]["exclude_sea_nodes"]
    ignore_island_components = config["graph"].get("ignore_island_components", True)
    island_component_max_size = int(config["graph"].get("island_component_max_size", 20))

    max_provinces, sea_starts = parse_default_map(mod_root / "map" / "default.map")
    provinces, color_to_id = parse_definition(mod_root / "map" / "definition.csv", sea_starts)
    parse_history_provinces(mod_root / "history" / "provinces", provinces)

    bmp_edges = build_edges_from_bmp(mod_root / "map" / "provinces.bmp", color_to_id)
    extra_edges = set()
    if include_straits:
        extra_edges = parse_adjacencies(mod_root / "map" / "adjacencies.csv", include_types)

    graph = build_graph(provinces, bmp_edges, extra_edges, exclude_sea_nodes)
    island_ids = set()
    if ignore_island_components:
        island_ids = find_island_province_ids(graph, provinces, island_component_max_size)

    iron_ids, coal_ids = find_resource_sets(provinces)

    dist_iron = compute_multi_source_distances(graph, iron_ids, unreachable_value)
    dist_coal = compute_multi_source_distances(graph, coal_ids, unreachable_value)

    province_rows = build_province_rows(
        provinces,
        dist_iron,
        dist_coal,
        max_distance,
        warning_distance,
        island_ids,
    )

    summary = build_summary(
        provinces,
        province_rows,
        max_provinces,
        max_distance,
        warning_distance,
        include_straits,
    )
    summary["input"]["mod_root"] = str(mod_root)

    locked = set(config["locking"].get("locked_provinces", []))
    suggestions = []
    if config["rebalance"].get("enabled", True):
        exclude_target_goods = {
            str(g).strip().lower() for g in config["rebalance"].get("exclude_target_goods", []) if str(g).strip()
        }
        suggestions = generate_suggestions(
            provinces=provinces,
            province_rows=province_rows,
            locked_provinces=locked,
            max_suggestions=config["rebalance"].get("max_suggestions", 200),
            suggestion_actions=config["rebalance"].get("suggestion_actions", ["replace", "swap"]),
            exclude_target_goods=exclude_target_goods,
            exclude_unreachable_for_iron=bool(config["rebalance"].get("exclude_unreachable_for_iron", True)),
        )

    write_summary_json(reports_dir / "resource_proximity_summary.json", summary)
    write_province_csv(reports_dir / "resource_proximity_provinces.csv", province_rows)
    write_suggestions_csv(reports_dir / "resource_rebalance_suggestions.csv", suggestions)

    if config["io"].get("write_patch_csv", True):
        write_patch_csv(patches_dir / "province_good_changes_v1.csv", suggestions, provinces)

    if config["io"].get("write_graph_edges", False):
        all_edges = set(bmp_edges)
        all_edges.update(extra_edges)
        write_graph_edges(reports_dir / "province_graph_edges.csv", all_edges)

    return {
        "summary_path": reports_dir / "resource_proximity_summary.json",
        "provinces_path": reports_dir / "resource_proximity_provinces.csv",
        "suggestions_path": reports_dir / "resource_rebalance_suggestions.csv",
        "patch_path": patches_dir / "province_good_changes_v1.csv",
        "land_count": summary["counts"]["land_provinces"],
        "fail_count": summary["compliance"]["fail_count"],
    }


def parse_args():
    parser = argparse.ArgumentParser(description="Analyze iron/coal proximity and generate rebalance suggestions.")
    parser.add_argument(
        "--mod-root",
        default="dodWorldTheater",
        help="Path to mod root containing map/ and history/ directories.",
    )
    parser.add_argument(
        "--config",
        default="config/resource_proximity.yaml",
        help="Path to analyzer config file.",
    )
    parser.add_argument(
        "--reports-dir",
        default="reports",
        help="Output directory for report files.",
    )
    parser.add_argument(
        "--patches-dir",
        default="patches",
        help="Output directory for patch suggestion files.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    result = run_analyzer(
        mod_root=Path(args.mod_root),
        config_path=Path(args.config),
        reports_dir=Path(args.reports_dir),
        patches_dir=Path(args.patches_dir),
    )
    print(f"Wrote summary: {result['summary_path']}")
    print(f"Wrote province report: {result['provinces_path']}")
    print(f"Wrote suggestions: {result['suggestions_path']}")
    print(f"Wrote patch CSV: {result['patch_path']}")
    print(f"Land provinces: {result['land_count']}; FAIL provinces: {result['fail_count']}")


if __name__ == "__main__":
    main()
