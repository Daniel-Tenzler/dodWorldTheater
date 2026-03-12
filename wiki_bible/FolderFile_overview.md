---
title: FolderFile Overview
category: other
tags: [structure]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/FolderFile_overview
---

## Quick Reference

**Mod File Requirements:**
- `.mod` file in mod directory with `name` and `path` lines
- See `mod_file.md` for complete reference

**Essential Folders:**
| Folder | Contains |
|--------|----------|
| `common/` | Game definitions (buildings, countries, cultures, governments, etc.) |
| `events/` | Event files |
| `decisions/` | Decision files |
| `history/` | Starting data (countries, provinces, POPs, diplomacy, wars) |
| `localisation/` | CSV translation files |
| `map/` | Province definitions, terrain, regions |
| `technologies/` | Tech trees (army, commerce, culture, industry, navy) |
| `gfx/` | Graphics (flags, event pictures, UI) |

**Common Pitfalls:**
- **File in wrong location** → Game won't load, crash on startup
- **Wrong encoding** → Files must be ANSI, not UTF-8
- **Missing folder** → Create required folders (events/, decisions/, localisation/)

**File Extensions:**
- `.txt` - Script files (events, decisions, common definitions)
- `.csv` - Localization files (semicolon-separated)
- `.lua` - Game defines and configuration
- `.mod` - Mod descriptor file
- `.tga/.dds` - Graphics files

**See Also:**
- [mod_file.md](mod_file.md) - Mod descriptor file syntax
- [Event_modding.md](Event_modding.md) - Event file creation
- [Decision_modding.md](Decision_modding.md) - Decision file creation
- [Localisation.md](Localisation.md) - CSV file format

---

Overview

This is a list of what the files and folders inside the main Victoria 2 folder mean, knowing what files go where, and where to make changes is the most important part of modding, as something in the wrong place can easily lead to a fatal crash.

Note that Victoria II's files need to be saved with ANSI encoding in order to work properly in the game. Additionally, some files seem to be encoded in a weird manner (such as some of the province history files), resulting in the game reading their contents as a single line. This can be fixed by creating a new .txt file with ANSI encoding with Notepad++ and copying the contents of the old file to it, deleting the old one and replacing it with the new.


## The Files

### Root Folder Files

| File/Folder | What it contains |
|-------------|------------------|
| `Victoria II\battleplans` | Settings for battle plan editor |

### Victoria II\common\ - General Information

| File | Description |
|------|-------------|
| `bookmarks.txt` | Defines scenarios/start dates |
| `buildings.txt` | Building statistics |
| `cb_types.txt` | Casus belli attributes and types |
| `countries.txt` | Which tag is linked to which .txt in common\countries |
| `country_colors.txt` | RGB code for each country |
| `crime.txt` | All crimes and effects |
| `cultures.txt` | Culture groups, names and colors along with cultural unions |
| `defines.lua` | POP, general, diplomatic, economic and military variables |
| `event_modifiers.txt` | All event and province modifiers and their effects |
| `goods.txt` | All goods with their starting price and color |
| `governments.txt` | All government types with their ideology and effects |
| `ideologies.txt` | All ideologies and their views on reforms |
| `issues.txt` | All reforms (political, social and civilizing) and party issues and their effects |
| `national_focus.txt` | All national focusses and their effects |
| `nationalvalues.txt` | All national values and the effects |
| `on_actions.txt` | Specially triggered effects |
| `pop_types.txt` | Mean Time To Happen (MTTH) for POP actions (promotion, assimilation etc.) |
| `production_types.txt` | Production statistics |
| `rebel_types.txt` | All rebel types, their goals and chances for rebelling |
| `religion.txt` | All religions, their icons and colors |
| `static_modifiers.txt` | All difficulty, rank and standard modifiers |
| `technology.txt` | Technology data |
| `traits.txt` | Traits of leaders and their effects |
| `triggered_modifiers.txt` | Empty by default |
| `country\.txt` | Color, political parties and ship names |

### Game Folders

| Folder | Description |
|--------|-------------|
| `Victoria II\decision\` | Decisions folder, all decisions are stored here |
| `Victoria II\events\` | Events folder, all event files are kept here |
| `Victoria II\gfx\` | Graphics |
| `Victoria II\history\` | Data on each province, diplomatic relations, country, units and POPs |
| `Victoria II\interface\` | Interface Graphics |
| `Victoria II\inventions\` | All inventions together with requirements, invention chances and effects |
| `Victoria II\launcher\` | Launcher graphics and configuration |
| `Victoria II\localisation\` | All text data for things like country names and event description, has options for other languages |
| `Victoria II\map\` | Map settings, province shapes, continents, regions etc. |
| `Victoria II\mod\` | Folder for storing mods and .mod files |
| `Victoria II\movies\` | Game intro movie |
| `Victoria II\music\` | Music used by the game |
| `Victoria II\news\` | All news stories |
| `Victoria II\poptypes\` | All POP data for each specific POP type |
| `Victoria II\script\` | All scripts |
| `Victoria II\sound\` | All sounds except music |
| `Victoria II\technologies\` | Technologies with their effects and attributes |
| `Victoria II\tutorial\` | Tutorial configuration |
| `Victoria II\units\` | All military unit attributes, for each specific unit |

**Note:** POP files: Issue and Ideology modifiers are multipliers, all other seem to be additions.
