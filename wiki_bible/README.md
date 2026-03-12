# Victoria 2 Modding Bible

An LLM-compatible reference guide for Victoria 2 modding, scraped from the Victoria 2 Wiki.

Each file includes YAML frontmatter with `title`, `category`, `tags`, `source`, and `url` for LLM context.

---

## For LLM Agents

When working with this Victoria 2 mod documentation, AI agents should follow this workflow:

### 1. Task-Based Workflow
- **Start here**: [QUICKSTART.md](QUICKSTART.md) for step-by-step workflows
- **Find patterns**: [PATTERNS.md](PATTERNS.md) for copy-paste code templates
- **Search keywords**: [KEYWORDS.md](KEYWORDS.md) to find relevant documentation

### 2. File Search Strategy
| Task Type | First File | Then Check |
|-----------|------------|-------------|
| Add Event | `QUICKSTART.md` (Task 1) | `Event_modding.md`, `PATTERNS.md` |
| Add Decision | `QUICKSTART.md` (Task 2) | `Decision_modding.md`, `PATTERNS.md` |
| Add Country | `QUICKSTART.md` (Task 3) | `Country_modding.md` |
| Add CB/War | `QUICKSTART.md` (Task 5) | `Casus_belli_modding.md`, `War_modding.md` |
| Add Text/Localization | `QUICKSTART.md` (Task 4) | `Localisation.md` |
| Find Effect | `Full_list_of_effects.md` | `PATTERNS.md`, `COMMON_PITFALLS.md` |
| Find Trigger | `List_of_conditions.md` | `Event_modding.md`, `COMMON_PITFALLS.md` |
| Find Scope | `Full_list_of_scopes.md` | `PATTERNS.md`, `Event_modding.md` |
| Debug Error | `COMMON_PITFALLS.md` | `VALIDATION_CHECKLIST.md` |

### 3. Cross-Reference Pattern
Most files have "See Also" sections linking to related documentation. Always follow these links for complete context.

### 4. Validation Before Completion
Before marking any modding task complete:
1. Check `VALIDATION_CHECKLIST.md` for validation steps
2. Review `COMMON_PITFALLS.md` for common errors
3. Verify syntax: brace balance, spaces around `=`, valid IDs

### 5. File Naming Conventions
- Events: `events/[region].txt` or `events/[TAG]Flavor.txt`
- Decisions: `decisions/[TAG] - [Name].txt` or `decisions/[Topic].txt`
- Countries: `common/countries/TAG - Name.txt` + `history/countries/TAG - Name.txt`
- Provinces: `history/provinces/[region]/[ID] - Name.txt`

### 6. Key Mod-Specific Notes for dodWorldTheater
- Event ID ranges: 98XXX for Amazonia, 33XXX for Arcadia
- Uses HPM (Historical Project Mod) as base
- Project docs in parent `MODDING_OVERVIEW.md`

### 7. Quick Troubleshooting
| Symptom | Check File |
|---------|------------|
| Event doesn't fire | `COMMON_PITFALLS.md` → "Event Not Firing" |
| Parse error | `COMMON_PITFALLS.md` → "Brace Balance Issues" |
| Missing text | `COMMON_PITFALLS.md` → "Localization Key Mismatches" |
| Decision not visible | `COMMON_PITFALLS.md` → "Decision potential vs allow" |

### 8. Essential Reference Files (Keep Open)
- `Full_list_of_effects.md` - All possible effects
- `List_of_conditions.md` - All possible triggers
- `Full_list_of_scopes.md` - Scope switching
- `CLAUDE.md` (parent) - Project-specific conventions

---

## Quick Start

**For beginners:**
1. Read [QUICKSTART.md](QUICKSTART.md) for step-by-step task workflows
2. Browse [PATTERNS.md](PATTERNS.md) for copy-paste code templates
3. Use [KEYWORDS.md](KEYWORDS.md) to find specific topics

**For experienced modders:**
1. Read [Folder/File_overview.md](Folder/File_overview.md) to understand mod structure
2. Configure your `.mod` file using [mod_file.md](mod_file.md) as reference
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

### LLM/Developer Guides

| File | Description |
|------|-------------|
| [MOD_SPECIFICS.md](MOD_SPECIFICS.md) | **START HERE** - dodWorldTheater-specific conventions |
| [QUICKSTART.md](QUICKSTART.md) | Step-by-step workflows for common tasks |
| [PATTERNS.md](PATTERNS.md) | Common modding patterns and code recipes |
| [KEYWORDS.md](KEYWORDS.md) | Keyword index for finding relevant documentation |
| [COMMON_PITFALLS.md](COMMON_PITFALLS.md) | Common modding errors and how to fix them |
| [VALIDATION_CHECKLIST.md](VALIDATION_CHECKLIST.md) | Validation checklist for mod content |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Symptom-based troubleshooting guide |
| [TEMPLATES.md](TEMPLATES.md) | Ready-to-use code templates for common tasks |
| [QUICK_CARDS.md](QUICK_CARDS.md) | One-page reference cards for quick lookup |

---

For the full documentation in one file, see `combined.md`.

See also: [MODDING_OVERVIEW.md](../MODDING_OVERVIEW.md) for project-level context.
