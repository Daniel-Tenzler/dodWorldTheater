---
title: Map modding
category: guide
tags: [map]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Map_modding
---

## Quick Reference

**Map Files Location:** `map/`

**Key Map Files:**
| File | Purpose | Format |
|------|---------|--------|
| `provinces.bmp` | Province shapes | 2048x2048 BMP, RGB colors |
| `definition.csv` | Province ID ↔ Color mapping | CSV: `R,G,B,ProvinceID,Name` |
| `terrain.bmp` | Terrain types | BMP with terrain colors |
| `rivers.bmp` | River paths | BMP with green/red/blue pixels |
| `positions.txt` | City/unit positions | Text coordinates |
| `adjacencies.csv` | Province connections | CSV adjacency data |
| `continent.txt` | Continent definitions | Text province list |
| `region.txt` | Strategic regions | Text province list |
| `climate.txt` | Climate zones | Text province list |
| `terrain.txt` | Terrain definitions | Terrain type settings |
| `default.map` | Map settings | Configuration |

**Common Tasks:**
| Task | File | Action |
|------|------|--------|
| Add province | `provinces.bmp`, `definition.csv` | Paint new province, add CSV entry |
| Change terrain | `terrain.bmp` | Paint with terrain color |
| Add river | `rivers.bmp` | Draw with green/red/blue pixels |
| Set positions | `positions.txt` | Add `position = { }` block |
| Create region | `region.txt` | Add province list to region |

**Province Colors (definition.csv):**
- Each province has unique RGB color
- Format: `Red,Green,Blue,ProvinceID,Name`
- Example: `0,0,128,1,Sitka`

**River Drawing:**
- **Green pixel** = River source
- **Red pixel** = River junction (merge)
- **Blue pixels** = River flow (darker = wider)

**Common Pitfalls:**
- **Game crashes on load** → definition.csv has duplicate colors
- **Province not selectable** → Missing from positions.txt
- **Terrain not applying** → Wrong color in terrain.bmp
- **Rivers not flowing** → Missing green source or red junction

**See Also:**
- [FolderFile_overview.md](FolderFile_overview.md) - Map folder structure
- [Provinces.md](Provinces.md) - Province list and IDs
- [Province_history_modding.md](Province_history_modding.md) - Province setup

---

This page contains information on the map files.


Province map
map\provinces.bmp
Terrain map
map\terrain.bmp
River map
map\rivers.bmp

Rivers run from a source, indicated by a green pixel, to the ocean. Rivers can combine with other rivers using red pixels. Rivers are drawn with a spectrum of blue colours which indicate the river's length at that position - darker blues resulting in wider rivers, cyan blues resulting in thinner rivers.

Editing the river map is best done with GIMP, which allows you finer controls when exporting the resulting .bmp file. Ensure you have the compatibility option "Do not write color space information" ticked.

Map elements
Adjacencies
Climate
Continent
Positions
States
Terrain types
