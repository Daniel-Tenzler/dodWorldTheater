---
title: dodWorldTheater Mod-Specific Documentation
category: guide
tags: [mod-specific, dodWorldTheater]
source: dodWorldTheater Mod
url: Internal mod documentation
---

# dodWorldTheater Mod-Specific Documentation

This document contains conventions, reserved ranges, and mod-specific information for the dodWorldTheater Victoria 2 mod.

## Mod Overview

**Mod Name:** dodWorldTheater
**Based On:** HPM (Historical Project Mod)
**Game:** Victoria II
**Project Location:** `C:\Users\reffr\Documents\github\dodWorldTheater`

## Reserved Event ID Ranges

To prevent conflicts with vanilla and other mods, the following event ID ranges are reserved:

| Range | Usage | Notes |
|-------|-------|-------|
| `1 - 9999` | Vanilla/HPM | Do not use |
| `10000 - 19999` | Vanilla events | Do not use |
| `20000 - 29999` | HPM events | Do not use |
| `30000 - 32999` | Reserved | Future use |
| `33000 - 33999` | **Arcadia region** | Arcadia-specific events |
| `34000 - 34999` | Reserved | Future use |
| `98000 - 98999` | **Amazonia region** | Amazonia-specific events |
| `99000 - 99999` | **Special/Global** | Cross-region events |

**When adding new events:**
- Arcadia content: Use `33XXX` range
- Amazonia content: Use `98XXX` range
- Other regions: Use `50000-89999` range
- Always check existing events for conflicts first

## Country Tags Used in dodWorldTheater

### Major Powers
- `ENG` - United Kingdom
- `FRA` - France
- `PRU` - Prussia
- `RUS` - Russia
- `AUS` - Austria
- `USA` - United States
- `TUR` - Ottoman Empire
- `SPA` - Spain

### Mod-Specific Countries
- `ARC` - Arcadia (formable)
- `VIN` - Vinland (formable)
- `AMA` - Amazonia (region)
- `BRZ` - Brazil
- And many others (see `common/countries/`)

## Mod File Structure

```
dodWorldTheater/
├── .mod                    # Mod descriptor
├── settings.txt            # Game settings
├── common/                 # Game definitions
│   ├── countries/          # Country definitions (644+ files)
│   ├── defines.lua         # Game constants
│   ├── buildings.txt       # Factory/building types
│   └── ...
├── events/                 # Events (125+ files)
├── decisions/              # Decisions (95+ files)
├── history/                # Starting data
│   ├── countries/          # Country history
│   ├── pops/               # Population data
│   ├── provinces/          # Province history (2775+ files)
│   ├── diplomacy/          # Wars, alliances, puppets
│   └── units/              # Starting armies/navies
├── localisation/           # Translation files (50+ CSV)
├── map/                    # Map data
├── technologies/           # Tech trees
├── inventions/             # Inventions
├── gfx/                    # Graphics
└── interface/              # UI definitions
```

## Mod-Specific Mechanics

### Migration Mechanics
Recent changes include migration nerfs - check decision files for current implementation.

### Custom Decisions
- Located in `decisions/` folder
- Country-specific: `TAG - Country Name.txt`
- Regional: `RegionName.txt` (e.g., `China.txt`, `ArabiaUnite.txt`)

### Custom Events
- Located in `events/` folder
- Region/country-specific: `RegionName.txt` or `[TAG]Flavor.txt`

## Conventions

### File Naming

**Events:**
- Country-specific: `[TAG]Flavor.txt` (e.g., `CHIFlavor.txt`)
- Regional: `[Region].txt` (e.g., `China.txt`, `Amazonia.txt`)
- Thematic: `[topic].txt` (e.g., `CrimeAndPunishment.txt`)

**Decisions:**
- Country-specific: `TAG - Country Name.txt` (e.g., `ARC - Arcadia.txt`)
- Regional: `[Topic].txt` (e.g., `China.txt`, `Colonies.txt`)

**Countries:**
- Common: `common/countries/TAG - Name.txt`
- History: `history/countries/TAG - Name.txt`

**Provinces:**
- Format: `history/provinces/[region]/[ID] - Name.txt`
- Example: `history/provinces/germany/1680 - Berlin.txt`

### Localization Keys

**Events:**
- Title: `EVT_[ID].T` or short form like `AMA1.T`
- Description: `EVT_[ID].D` or `AMA1.D`
- Options: `EVT_[ID].A`, `.B`, `.C`, etc.

**Decisions:**
- Title: `[decision_name]_title`
- Description: `[decision_name]_desc`

## Code Style

**Indentation:** Tabs (not spaces)
**Spacing:** Spaces around `=` (`tag = ENG` not `tag=ENG`)
**Comments:** `#` for comments
**Braces:** Must be balanced - every `{` must have a `}`

## Testing Workflow

1. **Syntax Check:** Load mod in Victoria II launcher
2. **Log Check:** Review `error.log` for parse errors
3. **In-Game Test:** Use console commands to test events/decisions
4. **Console Commands:** Press `~` to open
   - `event [ID] [TAG]` - Fire event
   - `debug showid` - Show province IDs
   - `debug fow` - Toggle fog of war

## Common mod Files

### Key Configuration Files
| File | Purpose |
|------|---------|
| `common/defines.lua` | Game constants (200+ settings) |
| `common/buildings.txt` | Factory types and inputs/outputs |
| `common/goods.txt` | Trade goods (47 goods) |
| `common/cb_types.txt` | Casus belli types |
| `map/definition.csv` | Province ID to color mapping |

## Known Issues

### Encoding
All text files must use **ANSI encoding**, not UTF-8.

### Province IDs
Always verify province IDs in `map/definition.csv` before using in events/decisions.

### Localization
CSV files require exactly **14 semicolons** per line.

## See Also

- [MODDING_OVERVIEW.md](../MODDING_OVERVIEW.md) - Project overview
- [CLAUDE.md](../CLAUDE.md) - Project instructions for Claude Code
- [AGENTS.md](../AGENTS.md) - Agent instructions
- [QUICKSTART.md](QUICKSTART.md) - Task-based workflows
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Symptom-based help
