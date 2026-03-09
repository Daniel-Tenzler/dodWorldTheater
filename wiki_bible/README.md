# Victoria 2 Modding Bible

An LLM-compatible reference guide for Victoria 2 modding, scraped from the Victoria 2 Wiki.

Each file includes YAML frontmatter with `title`, `category`, `tags`, `source`, and `url` for LLM context.

## Quick Start

1. Read `Folder/File_overview.md` to understand mod structure
2. Configure your `.mod` file using `mod_file.md` as reference
3. Use specific guides below based on what you're adding

## Documentation Index

### Core Guides

| File | Description |
|------|-------------|
| [Folder/File_overview.md](Folder/File_overview.md) | Victoria 2 mod folder structure and file organization |
| [mod_file.md](mod_file.md) | .mod descriptor file syntax |
| [Localisation.md](Localisation.md) | Adding translated text for events, decisions, UI |
| [Dynamic_localisation.md](Dynamic_localisation.md) | Dynamic text based on in-game conditions |

### Game Mechanics

| File | Description |
|------|-------------|
| [Event_modding.md](Event_modding.md) | Scripted events with triggers, flags, variables, MTTH |
| [Decision_modding.md](Decision_modding.md) | Player-triggered decisions |
| [Country_modding.md](Country_modding.md) | Creating new nations, starting traits, flags |
| [Map_modding.md](Map_modding.md) | Province map, terrain, resources |
| [Event_picture_modding.md](Event_picture_modding.md) | Custom event artwork |

### Common Systems

| File | Description |
|------|-------------|
| [Building_modding.md](Building_modding.md) | Factories, forts, naval bases |
| [Culture_modding.md](Culture_modding.md) | Cultures and culture groups |
| [Government_modding.md](Government_modding.md) | Government types and reforms |
| [Religion_modding.md](Religion_modding.md) | Religions and religious groups |
| [Casus_belli_modding.md](Casus_belli_modding.md) | War justifications and CB types |
| [Crime_modding.md](Crime_modding.md) | Crime types and rebels |
| [National_focus_modding.md](National_focus_modding.md) | Country priorities |
| [National_value_modding.md](National_value_modding.md) | National values |

### Historical Data

| File | Description |
|------|-------------|
| [Population_modding.md](Population_modding.md) | POP types, ideologies |
| [Province_history_modding.md](Province_history_modding.md) | Province ownership, buildings |
| [Alliance_modding.md](Alliance_modding.md) | Alliances between nations |
| [Puppet_modding.md](Puppet_modding.md) | Puppet states |
| [Sphere_modding.md](Sphere_modding.md) | Great power spheres |
| [War_modding.md](War_modding.md) | Wars and war goals |

### Graphics & UI

| File | Description |
|------|-------------|
| [Flag_modding.md](Flag_modding.md) | Country flags (.tga format) |

### Reference Data

| File | Description |
|------|-------------|
| [Full_list_of_effects.md](Full_list_of_effects.md) | All scriptable effects |
| [List_of_conditions.md](List_of_conditions.md) | All conditional commands |
| [Full_list_of_scopes.md](Full_list_of_scopes.md) | Scope commands |
| [Modifier_effects.md](Modifier_effects.md) | Bonuses and penalties |
| [Provinces.md](Provinces.md) | Province IDs, resources, terrain |
| [Countries.md](Countries.md) | Country tags |
| [Defaultmap.md](Defaultmap.md) | Map configuration |

### Utilities

| File | Description |
|------|-------------|
| [Bookmark_modding.md](Bookmark_modding.md) | Custom bookmarks |
| [Save-game_editing.md](Save-game_editing.md) | Save file editing |
| [IF_Emulation.md](IF_Emulation.md) | Victoria 1 emulation |

---

For the full documentation in one file, see `combined.md`.

See also: [MODDING_OVERVIEW.md](../MODDING_OVERVIEW.md) for project-level context.
