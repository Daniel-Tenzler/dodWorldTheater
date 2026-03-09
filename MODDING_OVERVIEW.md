# Victoria 2 Modding Overview

This document provides an overview of the Victoria 2 modding ecosystem, with references to the wiki bible documentation in `wiki_bible/`.

## Project Structure

```
dodWorldTheater/
├── wiki_bible/           # Scraped Victoria 2 wiki documentation
│   ├── combined.md       # All docs combined (~400KB)
│   ├── README.md         # Table of contents
│   └── [36 topic files]  # Individual modding guides
├── scripts/
│   └── scrape_vic2_wiki.py
└── dodWorldTheater/      # Your mod files
```

## Modding Documentation Index

### Core Guides

| File | Description |
|------|-------------|
| [wiki_bible/FolderFile_overview.md](wiki_bible/FolderFile_overview.md) | Explains the Victoria 2 mod folder structure, .mod file format, and how the game loads mod files |
| [wiki_bible/mod_file.md](wiki_bible/mod_file.md) | Details the .mod descriptor file syntax required to enable a mod in the launcher |
| [wiki_bible/Localisation.md](wiki_bible/Localisation.md) | Covers how to add translated text for events, decisions, and UI elements |

### Game Mechanics

| File | Description |
|------|-------------|
| [wiki_bible/Event_modding.md](wiki_bible/Event_modding.md) | Creating scripted events with triggers, options, flags, variables, and Mean Time to Happen mechanics |
| [wiki_bible/Event_picture_modding.md](wiki_bible/Event_picture_modding.md) | Adding custom event pictures and artwork to events |
| [wiki_bible/Decision_modding.md](wiki_bible/Decision_modding.md) | Adding player-triggered decisions with allow/potential conditions and effects |
| [wiki_bible/Country_modding.md](wiki_bible/Country_modding.md) | Creating new nations, defining starting traits, colors, and historical data |
| [wiki_bible/Map_modding.md](wiki_bible/Map_modding.md) | Modifying the province map, terrain, resources, and strategic regions |
| [wiki_bible/Dynamic_localisation.md](wiki_bible/Dynamic_localisation.md) | Dynamic text that changes based on in-game conditions using region names |

### Common Systems

| File | Description |
|------|-------------|
| [wiki_bible/Building_modding.md](wiki_bible/Building_modding.md) | Adding factories, infrastructure, and buildings with input/output goods |
| [wiki_bible/Culture_modding.md](wiki_bible/Culture_modding.md) | Defining cultures, culture groups, and primary/accepted cultures for nations |
| [wiki_bible/Government_modding.md](wiki_bible/Government_modding.md) | Creating government types with reforms, party ideologies, and voting systems |
| [wiki_bible/Religion_modding.md](wiki_bible/Religion_modding.md) | Adding religions and religious groups |
| [wiki_bible/Casus_belli_modding.md](wiki_bible/Casus_belli_modding.md) | Defining war justifications and CB types |
| [wiki_bible/Crime_modding.md](wiki_bible/Crime_modding.md) | Creating crime types and rebel factions |
| [wiki_bible/National_focus_modding.md](wiki_bible/National_focus_modding.md) | Setting country priorities like military, economy, or diplomacy |
| [wiki_bible/National_value_modding.md](wiki_bible/National_value_modding.md) | Defining national values like collectivist, anarchist, or liberal |

### Historical Data

| File | Description |
|------|-------------|
| [wiki_bible/Population_modding.md](wiki_bible/Population_modding.md) | Setting up POP types, ideologies, and historical population data |
| [wiki_bible/Province_history_modding.md](wiki_bible/Province_history_modding.md) | Defining province ownership, buildings, and POPs over time |
| [wiki_bible/Alliance_modding.md](wiki_bible/Alliance_modding.md) | Creating alliances between nations |
| [wiki_bible/Puppet_modding.md](wiki_bible/Puppet_modding.md) | Setting up puppet states and vassal relationships |
| [wiki_bible/Sphere_modding.md](wiki_bible/Sphere_modding.md) | Great power sphere mechanics and influence |
| [wiki_bible/War_modding.md](wiki_bible/War_modding.md) | Defining wars, battles, and war goals |

### Graphics & UI

| File | Description |
|------|-------------|
| [wiki_bible/Flag_modding.md](wiki_bible/Flag_modding.md) | Creating country flags using sprite files |

### Reference Data

| File | Description |
|------|-------------|
| [wiki_bible/Full_list_of_effects.md](wiki_bible/Full_list_of_effects.md) | Complete list of all scriptable effects (on_actions, event results) |
| [wiki_bible/List_of_conditions.md](wiki_bible/List_of_conditions.md) | All conditional commands for triggers, limits, and allow sections |
| [wiki_bible/Full_list_of_scopes.md](wiki_bible/Full_list_of_scopes.md) | Scope commands to switch between country, province, and POP contexts |
| [wiki_bible/Modifier_effects.md](wiki_bible/Modifier_effects.md) | Bonuses and penalties like +5% research or +2 consciousness |
| [wiki_bible/Provinces.md](wiki_bible/Provinces.md) | Complete province ID list with resources and terrain (156KB) |
| [wiki_bible/Countries.md](wiki_bible/Countries.md) | Default country tags and starting nations |
| [wiki_bible/Defaultmap.md](wiki_bible/Defaultmap.md) | Map configuration file structure |

### Utilities

| File | Description |
|------|-------------|
| [wiki_bible/Bookmark_modding.md](wiki_bible/Bookmark_modding.md) | Creating custom historical bookmarks |
| [wiki_bible/Save-game_editing.md](wiki_bible/Save-game_editing.md) | Manual save file editing techniques |
| [wiki_bible/IF_Emulation.md](wiki_bible/IF_Emulation.md) | Emulating Vicky 1 features and mechanics in Vicky 2 mods |

## Quick Start for New Modders

1. **Start here**: Read `wiki_bible/FolderFile_overview.md` to understand the file structure
2. **Enable your mod**: Configure `wiki_bible/mod_file.md` 
3. **Pick a system**: Choose a modding guide based on what you want to add
4. **Use reference**: Keep `wiki_bible/combined.md` or specific reference pages open while scripting

## Tools

- **The Validator**: Find errors in mod files (forum link in wiki_bible)
- **Clausewitz Positions Editor**: Map coordinate editing
- **SirRunner's Modding Tools**: Various utilities (GitHub)

For the full documentation, see `wiki_bible/combined.md` (404KB, all content in one file).
