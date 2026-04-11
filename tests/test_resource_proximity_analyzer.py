import tempfile
import unittest
from pathlib import Path

from tools.resource_proximity_analyzer import (
    classify_status,
    find_island_province_ids,
    compute_multi_source_distances,
    generate_suggestions,
    parse_definition,
    write_province_csv,
    write_summary_json,
)


class ResourceProximityAnalyzerTests(unittest.TestCase):
    def test_compute_multi_source_distances(self):
        graph = {
            1: {2},
            2: {1, 3},
            3: {2, 4},
            4: {3},
            5: set(),
        }
        distances = compute_multi_source_distances(graph, {1})
        self.assertEqual(distances[1], 0)
        self.assertEqual(distances[2], 1)
        self.assertEqual(distances[4], 3)
        self.assertEqual(distances[5], -1)

    def test_classify_status_thresholds(self):
        self.assertEqual(classify_status(True, 4, 5, 7, 6), "PASS")
        self.assertEqual(classify_status(True, 6, 5, 7, 6), "WARN")
        self.assertEqual(classify_status(True, 8, 5, 7, 6), "FAIL")
        self.assertEqual(classify_status(False, 2, 2, 7, 6), "SEA")

    def test_generate_suggestions_replace_for_failed_targets(self):
        provinces = {
            1: {"id": 1, "name": "A", "is_land": True, "good": "timber"},
            2: {"id": 2, "name": "B", "is_land": True, "good": "timber"},
            3: {"id": 3, "name": "Iron", "is_land": True, "good": "iron"},
            4: {"id": 4, "name": "Coal", "is_land": True, "good": "coal"},
        }
        rows = [
            {"id": 1, "paired_score": 11, "dist_to_iron": 10, "dist_to_coal": 11, "status": "FAIL"},
            {"id": 2, "paired_score": 9, "dist_to_iron": 9, "dist_to_coal": 8, "status": "FAIL"},
            {"id": 3, "paired_score": 0, "dist_to_iron": 0, "dist_to_coal": 3, "status": "PASS"},
            {"id": 4, "paired_score": 0, "dist_to_iron": 3, "dist_to_coal": 0, "status": "PASS"},
        ]

        suggestions = generate_suggestions(
            provinces=provinces,
            province_rows=rows,
            locked_provinces={2},
            max_suggestions=10,
            suggestion_actions=["replace"],
            exclude_target_goods=set(),
            exclude_unreachable_for_iron=False,
        )

        self.assertEqual(len(suggestions), 1)
        self.assertEqual(suggestions[0]["target_province_id"], 1)
        self.assertIn(suggestions[0]["suggested_good"], {"iron", "coal"})

    def test_generate_suggestions_excludes_sulphur_targets(self):
        provinces = {
            1: {"id": 1, "name": "Sulphur Target", "is_land": True, "good": "sulphur"},
            2: {"id": 2, "name": "Grain Target", "is_land": True, "good": "grain"},
        }
        rows = [
            {"id": 1, "paired_score": 37, "dist_to_iron": 31, "dist_to_coal": 37, "status": "FAIL"},
            {"id": 2, "paired_score": 36, "dist_to_iron": 30, "dist_to_coal": 36, "status": "FAIL"},
        ]
        suggestions = generate_suggestions(
            provinces=provinces,
            province_rows=rows,
            locked_provinces=set(),
            max_suggestions=10,
            suggestion_actions=["replace"],
            exclude_target_goods={"sulphur"},
            exclude_unreachable_for_iron=False,
        )
        self.assertEqual(len(suggestions), 1)
        self.assertEqual(suggestions[0]["target_province_id"], 2)

    def test_generate_suggestions_excludes_unreachable_iron_targets(self):
        provinces = {
            1: {"id": 1, "name": "Unreachable Iron", "is_land": True, "good": "grain"},
            2: {"id": 2, "name": "Reachable Iron", "is_land": True, "good": "fish"},
        }
        rows = [
            {"id": 1, "paired_score": -1, "dist_to_iron": -1, "dist_to_coal": 5, "status": "FAIL"},
            {"id": 2, "paired_score": 9, "dist_to_iron": 9, "dist_to_coal": 5, "status": "FAIL"},
        ]
        suggestions = generate_suggestions(
            provinces=provinces,
            province_rows=rows,
            locked_provinces=set(),
            max_suggestions=10,
            suggestion_actions=["replace"],
            exclude_target_goods=set(),
            exclude_unreachable_for_iron=True,
        )
        self.assertEqual(len(suggestions), 1)
        self.assertEqual(suggestions[0]["target_province_id"], 2)

    def test_generate_suggestions_prefers_replace_over_swap(self):
        provinces = {
            1: {"id": 1, "name": "Target", "is_land": True, "good": "grain"},
            2: {"id": 2, "name": "Donor Iron", "is_land": True, "good": "iron"},
        }
        rows = [
            {"id": 1, "paired_score": 9, "dist_to_iron": 9, "dist_to_coal": 5, "status": "FAIL"},
            {"id": 2, "paired_score": 2, "dist_to_iron": 0, "dist_to_coal": 2, "status": "PASS"},
        ]
        suggestions = generate_suggestions(
            provinces=provinces,
            province_rows=rows,
            locked_provinces=set(),
            max_suggestions=10,
            suggestion_actions=["replace", "swap"],
            exclude_target_goods=set(),
            exclude_unreachable_for_iron=False,
        )
        self.assertEqual(len(suggestions), 1)
        self.assertEqual(suggestions[0]["action"], "replace")

    def test_writers_create_expected_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            summary_path = out / "summary.json"
            provinces_path = out / "provinces.csv"

            summary_payload = {
                "schema_version": "1.0.0",
                "input": {"max_distance": 7},
                "counts": {"land_provinces": 2},
            }
            rows = [
                {
                    "id": 1,
                    "name": "A",
                    "is_land": True,
                    "is_sea": False,
                    "good": "iron",
                    "dist_to_iron": 0,
                    "dist_to_coal": 2,
                    "paired_score": 2,
                    "status": "PASS",
                    "owner_tag": "USA",
                    "start_pop": "",
                    "total_life_rating": 35,
                }
            ]

            write_summary_json(summary_path, summary_payload)
            write_province_csv(provinces_path, rows)

            self.assertTrue(summary_path.exists())
            self.assertTrue(provinces_path.exists())
            self.assertIn("schema_version", summary_path.read_text(encoding="utf-8"))
            first_line = provinces_path.read_text(encoding="utf-8").splitlines()[0]
            self.assertTrue(first_line.startswith("id,name,is_land,is_sea,good"))

    def test_parse_definition_tolerates_decimal_color_tokens(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "definition.csv"
            path.write_text(
                "province;red;green;blue;x;x\n1825;208;17;223.;Zouar;x\n",
                encoding="utf-8",
            )
            provinces, colors = parse_definition(path, sea_starts=set())
            self.assertIn(1825, provinces)
            self.assertIn((208, 17, 223), colors)

    def test_find_island_province_ids_by_component_size(self):
        provinces = {
            1: {"id": 1, "is_land": True},
            2: {"id": 2, "is_land": True},
            3: {"id": 3, "is_land": True},
            4: {"id": 4, "is_land": True},
            5: {"id": 5, "is_land": True},
            6: {"id": 6, "is_land": False},
        }
        graph = {
            1: {2},
            2: {1, 3},
            3: {2},
            4: {5},
            5: {4},
            6: set(),
        }
        islands = find_island_province_ids(graph, provinces, island_component_max_size=2)
        self.assertEqual(islands, {4, 5})


if __name__ == "__main__":
    unittest.main()
