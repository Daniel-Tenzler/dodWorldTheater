---
title: Bookmark modding
category: guide
tags: [utility]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Bookmark_modding
---

## Quick Reference

**File Location:** `common/bookmarks.txt`

**Bookmark Structure:**
```paradox
bookmark = {
    name = "GC_NAME"       # Localization key
    desc = "GC_DESC"       # Localization key
    date = 1836.1.1        # Start date (year.month.day)
    cameraX = 2950         # Camera position (pixels from left)
    cameraY = 1550         # Camera position (pixels from top)
}
```

**Common Tasks:**
| Task | File | Action |
|------|------|--------|
| Add new bookmark | `common/bookmarks.txt` | Add `bookmark = { }` block |
| Add bookmark POP data | `history/pops/YYYY.M.D/` | Create folder for date |
| Add bookmark history | `history/countries/` | Add dated blocks |
| Check date range | `common/defines.lua` | Verify within `start_date`/`end_date` |

**Required Components for New Bookmarks:**

1. **Bookmark definition** (in `common/bookmarks.txt`):
```paradox
bookmark = {
    name = "ACW_NAME"      # Define in localisation
    desc = "ACW_DESC"
    date = 1861.4.12       # American Civil War start
    cameraX = 2200
    cameraY = 1400
}
```

2. **Date range** (in `common/defines.lua`):
```paradox
start_date = 1836.1.1
end_date = 1936.1.1        # Must be ≥ your bookmark date
```

3. **POP data** (in `history/pops/1861.4.12/`):
- Create folder matching bookmark date
- Add province POP files

4. **Localization** (in `localisation/*.csv`):
```csv
ACW_NAME;American Civil War;;;;;;;;;;;;;
ACW_DESC;The United States fractures in civil war;;;;;;;;;;;;;
```

**Common Pitfalls:**
- **Bookmark not appearing** → Date must be within defines.lua range
- **Crash on load** → Missing POP data folder for date
- **Wrong camera position** - Use pixels from left/top of provinces.bmp
- **POP data not loading** → Folder name must match date exactly (YYYY.M.D)

**Vanilla Bookmarks:**
| Name | Date | Description |
|------|------|-------------|
| Grand Campaign | 1836.1.1 | Main start date |
| American Civil War | 1861.4.12 | US Civil War start |

**See Also:**
- [FolderFile_overview.md](FolderFile_overview.md) - Folder structure
- [Population_modding.md](Population_modding.md) - POP setup
- [Localisation.md](Localisation.md) - Adding text

---

This page documents the formatting and creation of bookmarks.

What does a bookmark look like?

Bookmarks are found within bookmarks.txt.

bookmark =
{
	name = "(bookmark)_NAME"    #defined in localization
	desc = "(bookmark)_DESC"    #defined in localization
	date = (yyyy.m.d)
	cameraX = (x)               #Starting camera distance, in pixels, from left side of provinces.bmp
	cameraY = (y)               #Starting camera distance, in pixels, from top side of provinces.bmp
}


example, from vanilla:

bookmark =
{
	name = "GC_NAME"    
	desc = "GC_DESC"    
	date = 1836.1.1     
	cameraX = 2950      
	cameraY = 1550      
}


This creates a bookmark on January 1, 1836 that has the camera centered on Europe.

Creating a new bookmark

There are a number of steps required when creating a new bookmark to ensure it works properly:

It must be defined in bookmarks.txt
Its date must be within the range of "start_date" and "end_date" in defines.lua
There must be a corresponding pops folder defining the population for that date
If the bookmark is the earliest date, all undated province and history data will belong to it by default. You will have to manually change those to the later dates
If the bookmark is a later date, the default province and history data will be used as well. You must manually define the data for later dates
