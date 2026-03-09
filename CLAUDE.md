# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Documentation Resources

**Before starting any modding work**, consult these key documentation files:

| File | Purpose |
|------|---------|
| **[MODDING_OVERVIEW.md](MODDING_OVERVIEW.md)** | Complete modding documentation index with quick start guide |
| **[wiki_bible/](wiki_bible/)** | Scraped Victoria 2 wiki documentation (36+ topic files) |
| **[wiki_bible/combined.md](wiki_bible/combined.md)** | All wiki docs in one file (~400KB) for reference |
| **[wiki_bible/README.md](wiki_bible/README.md)** | Table of contents for wiki bible files |

### Key Wiki Bible References

- **[Event_modding.md](wiki_bible/Event_modding.md)** - Creating events with triggers, MTTH, flags
- **[Decision_modding.md](wiki_bible/Decision_modding.md)** - Adding decisions with potential/allow/effect
- **[Full_list_of_effects.md](wiki_bible/Full_list_of_effects.md)** - All scriptable effects
- **[List_of_conditions.md](wiki_bible/List_of_conditions.md)** - All triggers and conditions
- **[Full_list_of_scopes.md](wiki_bible/Full_list_of_scopes.md)** - Scope switching reference
- **[FolderFile_overview.md](wiki_bible/FolderFile_overview.md)** - Victoria 2 mod folder structure
- **[Localisation.md](wiki_bible/Localisation.md)** - Adding translated text

## Project Overview

**dodWorldTheater** is a total conversion mod for Victoria II (Paradox Interactive's grand strategy game), based on HPM (Historical Project Mod). It uses Paradox Script, a custom DSL for game configuration.

### Mod Structure Overview

The mod contains approximately **9,739 files** organized into **63 directories** within `dodWorldTheater/`:

| Directory | Files | Description |
|-----------|-------|-------------|
| **events/** | 125+ | Country events driving historical narratives |
| **decisions/** | 95+ | Political decisions with potential/allow/effect blocks |
| **history/** | 3,500+ | Historical starting data (countries, provinces, pops, diplomacy, wars) |
| **technologies/** | 5 | Tech trees: army, commerce, culture, industry, navy |
| **inventions/** | 28 | Technology inventions unlocked by research |
| **poptypes/** | 13 | Pop type definitions (aristocrats, artisans, bureaucrats, etc.) |
| **common/** | 30+ | Core game data (buildings, defines, goods, cultures, countries) |
| **localisation/** | 50+ | CSV translation files for all text content |
| **map/** | 10+ | Province definitions, continents, topology, terrain |
| **units/** | 26 | Military unit definitions (army & navy) |
| **interface/** | 30+ | GUI definitions and interface files |
| **gfx/interface/** | 100+ | UI graphics (icons, strips, terrain images) |
| **gfx/pictures/** | Subdirs | Event/decision/tech pictures |
| **gfx/flags/** | - | Country flag graphics |
| **battleplans/** | 1 | Battle plan settings |
| **news/** | 8 | Newspaper/news event definitions |

### Key Entry Points

- `dodWorldTheater.mod` - Mod descriptor (path: `mod/dodWorldTheater`)
- `dodWorldTheater/settings.txt` - Game configuration (language, graphics, audio)
- `dodWorldTheater/common/defines.lua` - Core game mechanics (200+ constants)
- `dodWorldTheater/common/buildings.txt` - Factory and building definitions
- `dodWorldTheater/common/goods.txt` - All trade goods (47 goods in 4 categories)

### Key Entry Points

- `dodWorldTheater.mod` - Mod descriptor (path is `mod/dodWorldTheater`)
- `dodWorldTheater/settings.txt` - Game configuration
- `dodWorldTheater/common/defines.lua` - Core game mechanics (200+ constants)
- `dodWorldTheater/common/buildings.txt` - Factory and building definitions

## Development Workflow

**No automated build system exists.** Testing is manual through Victoria II:

1. Copy mod folder to Victoria II's `/mod/` directory
2. Load mod in-game to verify syntax
3. Check game logs for errors (primary error reporting mechanism):
   - `error.log` - Parse errors, missing tokens
   - `game.log` - Runtime errors
4. Test events/decisions through gameplay

### Mod Installation Path
The `.mod` file specifies: `path = "mod/dodWorldTheater"`
Install to: `[Victoria II]/mod/dodWorldTheater/`

### Quick Validation Checks
- **Brace balance**: Every `{` must have a matching `}`
- **Quote balance**: Every `"` must be closed
- **Event ID uniqueness**: IDs must be unique across all event files
- **Localization keys**: Must exist for all referenced text
- **Province IDs**: Must be valid (check `map/definition.csv`)

### Common Error Types
1. **Missing brace**: `}` not closed - cascading parse failures
2. **Unknown token**: Typo in condition/effect name
3. **Invalid province ID**: Province doesn't exist
4. **Missing localization**: Key not found in CSV files
5. **Circular event chains**: Events that trigger each other infinitely

## Detailed Directory Structure

### common/ - Core Game Data
```
common/
├── backup/                    # Backup files
├── countries/                 # 645+ country definition files (TAG - Name.txt)
├── bookmarks.txt             # Historical bookmarks
├── buildings.txt             # Factory/building types and inputs/outputs
├── cb_types.txt              # Casus Belli types (war goals)
├── countries.txt             # Country color mappings
├── country_colors.txt        # Country color definitions
├── crime.txt                 # Crime types and modifiers
├── cultures.txt              # All culture definitions and groups
├── defines.lua               # ~200 game constants and mechanics
├── event_modifiers.txt       # Country/province modifiers
├── goods.txt                 # 47 trade goods in 4 categories
├── governments.txt           # Government types
├── ideologies.txt            # Political ideologies
├── issues.txt                # Political and social reform issues
├── national_focus.txt        # National focus types
├── nationalvalues.txt        # National value modifiers
├── on_actions.txt            # Triggers for specific game events
├── pop_types.txt             # POP type definitions
├── production_types.txt      # Factory/production templates
├── rebel_types.txt           # Rebel faction types
├── religion.txt              # Religions
├── static_modifiers.txt      # Base game modifiers
├── technology.txt            # Technology categories
├── traits.txt                # Leader traits
└── triggered_modifiers.txt   # Condition-triggered modifiers
```

### events/ - Game Events (125+ files)
Named by region or topic:
- `African Uncivs.txt`, `Amazonia.txt`, `Arabia.txt`
- `Canals Construction.txt`, `CBsAndCores.txt`
- `ColonialNation-1356XX.txt`, `China.txt`
- Country-specific: `CHIFlavor.txt`, `AUSFlavor.txt`, `BAYFlavor.txt`
- Thematic: `archaeology.txt`, `AssimilationTroubles.txt`, `CrimeAndPunishment.txt`

### decisions/ - Political Decisions (95+ files)
- Country-specific: `ARC - Arcadia.txt`, `BRGdecisions.txt`, `ETH.txt`
- Regional: `ArabiaUnite.txt`, `EthiopiaUnite.txt`, `Colombia.txt`
- Thematic: `Canals.txt`, `China.txt`, `civilising.txt`, `Colonies.txt`
- Economic: `Economy.txt`

### history/ - Starting Game Data
```
history/
├── countries/        # 645 country history files (TAG - Country Name.txt)
├── diplomacy/        # Starting diplomatic relations (wars, alliances, etc.)
├── pops/             # Population data by date
│   └── 1836.1.1/     # Starting POP distribution
├── provinces/        # 2,775 province history files by region
│   ├── africa/
│   ├── asia/
│   ├── australia/
│   ├── austria/
│   ├── balkan/
│   ├── canada/
│   ├── carribean/
│   ├── central asia/
│   ├── china/
│   ├── france/
│   ├── germany/
│   ├── india/
│   ├── indonesia/
│   ├── italy/
│   ├── japan/
│   ├── low countries/
│   ├── mexico/
│   ├── pacific island/
│   ├── portugal/
│   ├── scandinavia/
│   ├── south america/
│   ├── soviet/
│   ├── spain/
│   ├── united kingdom/
│   └── usa/
├── units/            # Starting military units (O, P format)
└── wars/             # Starting wars
```

### technologies/ - Tech Trees (5 files)
- `army_tech.txt` - Land warfare technology
- `commerce_tech.txt` - Economic/trade technology
- `culture_tech.txt` - Social/cultural technology
- `industry_tech.txt` - Industrial production technology
- `navy_tech.txt` - Naval warfare technology

### inventions/ - Technology Inventions (28 files)
```
PUIR_* files (PDM/PUIR inventions):
- agriculture, casualties, colonisation, economic_thinkers
- forestry_plantations, ideology, industry, military
- military_industry, mining, mobilisation, navy
- new_pop_growth, noninterventionism, philosophers
- psychologists, rare_goods, social_scientists

Core inventions:
- army_inventions.txt, commerce_inventions.txt
- culture_inventions.txt, industry_inventions.txt
- navy_inventions.txt
```

### poptypes/ - Population Types (13 files)
Each POP type has needs, promotion, and demotion mechanics:
- `aristocrats.txt`, `artisans.txt`, `bureaucrats.txt`
- `capitalists.txt`, `clergymen.txt`, `clerks.txt`
- `craftsmen.txt`, `farmers.txt`, `labourers.txt`
- `officers.txt`, `soldiers.txt`, `slaves.txt`

### units/ - Military Units (26 files)
**Land Units:** infantry, infantry_offensive, infantry_defensive, cavalry, dragoon, hussar, cuirassier, irregular, engineer, guard, artillery, artillery_offensive, artillery_defensive, tank, plane

**Naval Units:** frigate, manowar, clipper_transport, steam_transport, ironclad, monitor, commerce_raider, cruiser, battleship, dreadnought

### localisation/ - Translation Files (50+ CSV files)
Naming scheme with prefix numbers (load order):
- `0_common.csv` - Mod-specific localization
- `00_HPM_*.csv` - HPM base content
- `02_NNM_*.csv` - NNM content
- Custom mod files for specific features

### map/ - Map Data
```
map/
├── adjacencies.csv       # Province adjacencies
├── climate.txt           # Climate zones
├── continent.txt         # Continent definitions
├── default.map           # Map settings
├── definition.csv        # Province ID to color mapping
├── positions.txt         # Unit/city positions on map
├── province_flag_sprites/
├── provinces.bmp         # Province map image
├── region.txt            # Strategic regions
├── rivers.bmp            # River map image
├── terrain/              # Terrain type definitions
├── terrain.bmp           # Terrain map image
└── terrain.txt           # Terrain type settings
```

### interface/ - GUI Definitions (30+ files)
```
interface/
├── battleplansinterface.gfx
├── buildings.gfx
├── buildunit.gui
├── combat.gfx
├── core.gfx
├── country_budget.gfx/gui
├── country_diplomacy.gfx/gui
├── country_military.gfx
├── country_politics.gfx/gui
├── country_trade.gui
├── general_gfx.gfx
├── mapitems.gfx
├── menubar.gui
├── messagetypes.txt      # Message notification settings
├── province_interface.gfx/gui
├── sound.sfx
└── unitpanel.gfx/gui
```

### gfx/ - Graphics
```
gfx/
├── anims/                # Animations
├── flags/                # Country flags
├── interface/
│   ├── leaders/          # Leader portraits
│   ├── *.dds/*.tga       # UI icons and strips
│   ├── terrain_*.tga     # Terrain icons (35+ terrain types)
│   └── unit_*.dds        # Unit icons
└── pictures/
    ├── decisions/        # Decision pictures
    ├── events/           # Event pictures
    └── tech/             # Technology pictures
```

### news/ - Newspaper System (8 files)
- `news_ai_afraid_of.txt`
- `news_ai_likes_very_much.txt`
- `news_game_event_default.txt`
- `news_invention.txt`
- `news_layout.txt`
- `news_new_party.txt`
- `news_rebel_break_country.txt`
- `news_research_complete.txt`
- `news_war_declared.txt`

## Code Architecture

### Event System

Events trigger based on conditions and can chain into other events:

```
country_event = {
    id = 98401
    title = "AMA1.T"
    desc = "AMA1.D"

    trigger = {
        tag = AMA
        owns = 2414
        NOT = { has_global_flag = congress_of_panama }
    }

    mean_time_to_happen = {
        months = 2
    }

    option = {
        name = "98401.A"
        prestige = 3
        ai_chance = { factor = 99 }
    }
}
```

### Decision System

Decisions have three phases: `potential` (visibility), `allow` (requirements), `effect` (consequences):

```
political_decisions = {
    form_arcadia_vinland = {
        picture = "UniteARC"

        potential = {
            tag = VIN
            NOT = { ARC = { exists = yes } }
            has_country_flag = vin_manifest_destiny
        }

        allow = {
            war = no
            all_core = {
                OR = {
                    owned_by = THIS
                    owner = { OR = { in_sphere = THIS vassal_of = THIS } }
                }
            }
        }

        effect = {
            prestige = 20
            change_tag = ARC
        }

        ai_will_do = { factor = 1 }
    }
}
```

### Tag and Country System

- Country tags are 3-letter uppercase codes (ENG, FRA, AMA, ARC, VIN)
- Dynamic tags prefixed with `dynamic_tags = yes`
- **Country definition files**: `common/countries/TAG - Country Name.txt`
- **Country history files**: `history/countries/TAG - Country Name.txt`
- Country data includes: capital, culture, religion, government, reforms, parties, upper_house, ruling_party

### Province System

- Province IDs are numeric (e.g., 1680, 2414, 2629)
- **Province history files**: `history/provinces/[region]/PROV_ID - Province Name.txt`
- Province data includes: owner, controller, core claims, trade_goods, life_rating
- Regions are defined for strategic grouping (e.g., BRZ_2408)

### Goods System (4 categories, 47 goods)

**military_goods**: ammunition, small_arms, artillery, canned_food, barrels, aeroplanes
**raw_material_goods**: cotton, dye, wool, silk, coal, sulphur, iron, timber, tropical_wood, rubber, oil, precious_metal, precious_goods
**industrial_goods**: steel, cement, machine_parts, glass, fuel, fertilizer, explosives, clipper_convoy, steamer_convoy, electric_gear, cotton_fabric, wool_fabric, leather_fabric, lumber
**consumer_goods**: paper, cattle, fish, fruit, grain, tobacco, tea, coffee, opium, automobiles, telephones, wine, liquor, regular_clothes, warm_clothes, durable_clothes, luxury_clothes, furniture, luxury_furniture, radio

### Technology System

Five technology categories with prerequisites and year-based availability:
- `army_tech.txt`
- `commerce_tech.txt`
- `culture_tech.txt`
- `industry_tech.txt`
- `navy_tech.txt`

Each tech has: `area`, `year`, `cost`, `ai_chance`, and effects (unit activation, building activation, modifier changes)

### Localization

CSV format with semicolon separators:
```
key;English;French;German;;;;;;;;;;;
key_desc;Description text;;;;;;;;;;;
```

Naming conventions:
- Titles: `KEY.T`
- Descriptions: `KEY.D`
- Options: `KEY.A`, `KEY.B`, `KEY.C`, etc.

## Code Style (from AGENTS.md)

- **Indentation**: Tabs only (no spaces)
- **Spacing**: Spaces around `=` signs (`tag = ENG` not `tag=ENG`)
- **Comments**: `#` for comments
- **Compound names**: Underscores (`aeroplane_factory`)
- **Event IDs**: Typically 5 digits, often with prefixes
- **Braces**: Must be balanced - manual verification required

## Logical Operators

- **AND** (default): Multiple conditions in same block
- **OR**: `OR = { condition1 condition2 }`
- **NOT**: `NOT = { condition }`
- **Country scope**: `THIS` (current country), `FROM` (triggering country)
- **Conditions**: `limit = { }`
- **Effects**: `effect = { }`
- **Triggers**: `trigger = { }`

## Common Patterns

- Province effects: `PROV_ID = { add_core = TAG }`
- Province scoped: `PROV_ID = { owned_by = TAG }` or `BRZ_2408 = { secede_province = AMA }`
- Country effects: `TAG = { relation = { who = FROM value = 50 } }`
- AI behavior: `ai_chance = { factor = X }` (events) or `ai_will_do = { factor = X }` (decisions)
- Event chains: `TAG = { country_event = XXXXX }`
- Scope triggers: `is_triggered_only = yes` for events only fired by other events
- Flag checks: `has_global_flag = flag_name`, `has_country_flag = flag_name`
- Flag setting: `set_country_flag = flag_name`, `set_global_flag = flag_name`
- Province ownership: `any_owned = { limit = { region = BRZ_2408 } ... }`
- Core manipulation: `add_core = TAG`, `remove_core = TAG`

### Country History File Format

`history/countries/TAG - Country Name.txt`:
```
capital = 1095
primary_culture = circassian
religion = orthodox
government = absolute_monarchy
plurality = 0.0
nationalvalue = nv_order
literacy = 0.04
non_state_culture_literacy = 0.02
civilized = yes
prestige = 2

# Political reforms
slavery = no_slavery
upper_house_composition = appointed
vote_franschise = none_voting
public_meetings = yes_meeting
press_rights = state_press
trade_unions = no_trade_unions
voting_system = first_past_the_post
political_parties = underground_parties

# Social Reforms
wage_reform = no_minimum_wage
work_hours = no_work_hour_limit
safety_regulations = no_safety
health_care = no_health_care
unemployment_subsidies = no_subsidies
pensions = no_pensions
school_reforms = no_schools

set_country_flag = orthodox_country

ruling_party = ABK_conservative
upper_house = {
    fascist = 0
    liberal = 15
    conservative = 68
    reactionary = 17
    anarcho_liberal = 0
    socialist = 0
    communist = 0
}
```

### Province History File Format

`history/provinces/[region]/PROV_ID - Province Name.txt`:
```
owner = SPA
controller = SPA
add_core = MGH
trade_goods = grain
life_rating = 35
```

### Factory/Production Type Format

From `common/production_types.txt`:
```
factory_template = {
    efficiency = {
        cement = 0.5
        machine_parts = 0.05
    }

    owner = {
        poptype = capitalists
        effect = input
        effect_multiplier = -2.5
    }

    employees = {
        {
            poptype = craftsmen
            effect = throughput
            amount = 0.8
        }
        {
            poptype = clerks
            effect = output
            effect_multiplier = 1.5
            amount = 0.2
        }
    }
    type = factory
    workforce = 10000
}
```

## Error Prevention

- Always balance braces `{ }`
- Check for missing spaces around `=`
- Verify province IDs exist in map definitions
- Ensure localization keys match event/decision references
- Test event chains sequentially

## File Organization

- Group related entries logically
- Alphabetize where appropriate (especially country tags)
- Use descriptive comments for complex blocks
- Maintain consistent ordering across similar files
- Keep files focused on single aspects when possible

### File Naming Conventions

**Events**: `[Region/Topic] events.txt` or `[Region].txt` or `[CountryCode]Flavor.txt`
- Examples: `Amazonia.txt`, `AUSFlavor.txt`, `China.txt`
- Event ID ranges often follow patterns (e.g., 98XXX for Amazonia, 33XXXX for Arcadia)

**Decisions**: `[Tag] - [Name].txt` or `[Topic].txt`
- Examples: `ARC - Arcadia.txt`, `China.txt`, `Canals.txt`

**Countries**: `TAG - Country Name.txt`
- Examples: `ABK - Abkhazia.txt`, `ARC - Arcadia.txt`
- Located in both `common/countries/` and `history/countries/`

**Provinces**: `PROV_ID - Province Name.txt`
- Examples: `1680 - Fez.txt`
- Located in `history/provinces/[region]/`

### Adding New Content

**New Event:**
1. Create or add to appropriate file in `events/`
2. Add localization to `localisation/0_common.csv` or appropriate file
3. Use unique event ID (check existing ranges)
4. Test triggers and conditions

**New Decision:**
1. Create or add to appropriate file in `decisions/`
2. Include `potential`, `allow`, `effect`, and `ai_will_do` blocks
3. Add localization
4. Add optional picture (place in `gfx/pictures/decisions/`)

**New Country:**
1. Create `common/countries/TAG - Name.txt` with color, unit types, etc.
2. Create `history/countries/TAG - Name.txt` with starting data
3. Add localization for country name and adjective
4. Add flag to `gfx/flags/`

**New Province:**
1. Add to `map/definition.csv` with unique ID and color
2. Create `history/provinces/[region]/PROV_ID - Name.txt`
3. Update `map/positions.txt` with unit/city position
4. Update `map/adjacencies.csv` if needed

## Important Notes

- **NO GIT OPERATIONS** - The user handles all git operations manually
- This is a Victoria II mod, not a traditional software project
- Testing requires launching the actual game
- Game logs are the primary debugging tool
- Historical accuracy is a priority (based on HPM)

---

# Comprehensive Reference Guide

## Event ID Ranges & Organization

The mod contains **1,841 events** across 125+ files with organized ID patterns. When adding new events, use appropriate ranges to prevent collisions:

| Range | Category | Examples |
|-------|----------|----------|
| `10XXX-11XXX` | Early game / tutorial events | 10000-11106 |
| `12XXX` | General events | 12000-12817 |
| `13XXX-14XXX` | Reform and political events | 13000-14640 |
| `33XXX` | Arcadia region events | 333XXX series |
| `98XXX` | Amazonia events | 98401-98900 |
| `99XXX` | Reserved/special events | 99999 |

**Best practices:**
- Reserve event ID ranges by region/country when creating content
- Document reserved ranges in a central location
- Use consistent prefixes for related event chains

## Political Systems Reference

### Government Types (11 types)

| Type | Election | Appoint Ruling Party | Flag Type | Ideologies Allowed |
|------|----------|---------------------|-----------|-------------------|
| `absolute_monarchy` | No | Yes | monarchy | liberal, conservative, reactionary |
| `democracy` | Yes (48mo) | No | republic | All ideologies |
| `hms_government` | Yes (48mo) | Yes | monarchy | All ideologies |
| `prussian_constitutionalism` | Yes (48mo) | Yes | monarchy | liberal, socialist, conservative, reactionary |
| `presidential_dictatorship` | No | Yes | republic | reactionary, fascist, conservative |
| `bourgeois_dictatorship` | No | Yes | republic | anarcho_liberal |
| `fascist_dictatorship` | No | Yes | fascist | fascist |
| `proletarian_dictatorship` | No | Yes | communist | communist |
| `feudal_monarchy` | No | Yes | monarchy | conservative, reactionary |
| `theocracy` | No | Yes | - | reactionary, conservative |
| `merchant_republic` | Yes (48mo) | No | republic | liberal, socialist, conservative, reactionary |

### Ideologies (8 types)

| Ideology | Date | Color | Reform Desires | Uncivilized |
|----------|------|-------|----------------|-------------|
| `reactionary` | - | Blue (30,30,100) | Remove all reforms | No |
| `conservative` | - | Blue (10,10,250) | Minimal reform, supports militancy movement | No |
| `liberal` | - | Yellow (255,255,0) | Add political reforms, social with militancy | No |
| `socialist` | 1845 | Red (255,0,0) | Add social reforms | No |
| `communist` | 1860 | Dark Red (150,10,10) | Add social, remove political reforms | No |
| `anarcho_liberal` | 1840 | Tan (150,150,10) | Remove all except political reforms | No |
| `fascist` | 1900 | Gray (60,60,60) | Remove reforms | No |

### National Values (7 types)

| Value | Effects |
|-------|---------|
| `nv_order` | +20% land org, +5% org regain, -1% militancy, -15% immigrant attract, -10% social reform desire, +25% unit experience |
| `nv_liberty` | +15% immigrant attract, +25% political reform desire, +5% commerce research, +2% consciousness, +20% social reform desire |
| `nv_equality` | -4% non-accepted militancy, +10% culture research |
| `nv_tradition` | -5% research, -2% militancy, -2% consciousness, -10% immigrant attract, -20% social reform desire, -20% issue change, +50% ruling party support |
| `nv_productivity` | +5% tax efficiency, +10% RGO throughput, -5% factory input, +5% factory output, +15% industry research |
| `nv_education` | +20% education efficiency, +20% research points |
| `nv_diplomacy` | +1 diplomatic points, +60% influence, +25% CB generation speed |

### Reform Systems

#### Political Reforms

**slavery**: `yes_slavery` / `no_slavery`

**upper_house_composition**: `appointed` / `wealth_weighted` / `population_weighted` / `limited_voters` / `wealth_voting` / `all_voters` / `ruling_party` / `dominant_issue`

**vote_franschise**: `none_voting` / `limited_voting` / `weighted_voting` / `universal_voting`

**public_meetings**: `yes_meeting` / `no_meeting` / `political_meetings`

**press_rights**: `state_press` / `free_press` / `censored_press` / `state_free_press`

**trade_unions**: `no_trade_unions` / `non_socialist` / `socialist` / `all_trades` / `trade_unions` / `interdiction` / `mandatory` / `controlled`

**voting_system**: `first_past_the_post` / `jefferson_method` / `sainte_laque_method`

**political_parties**: `underground_parties` / `legal_parties` / `all_parties` / `non_secret_ballot` / `secret_ballot` / `gerrymandering` / `none` / `harassment` / `illegal_socialists` / `illegal_communists` / `illegal_fascists` / `illegal_everyone` / `only_ruling_party` / `coalition` / `proportional_reasoning` / `proportional_selection` / `multi_issue` / `largest_share` / `majority_holders` / `dominant_issue` / `party_installation`

#### Social Reforms

**wage_reform**: `no_minimum_wage` / `trinket_wage` / `low_wage` / `medium_wage` / `good_wage` / `high_wage` / `fair_wage` / `living_wage` / `excellent_wage`

**work_hours**: `no_work_hour_limit` / `restricted_hours` / `sunset_to_sunset` / `10_hours` / `9_hours` / `8_hours` / `max_hour`

**safety_regulations**: `no_safety` / `first_safety` / `workplace_safety` / `injury_insurance`

**health_care**: `no_health_care` / `basic_healthcare` / `general_healthcare` / `advanced_healthcare` / `modern_healthcare`

**unemployment_subsidies**: `no_subsidies` / `trinket_subsidies` / `low_subsidies` / `medium_subsidies` / `large_subsidies` / `universal_subsidies`

**pensions**: `no_pensions` / `trinket_pensions` / `basic_pensions` / `old_age_pensions` / `general_pensions` / `universal_pensions`

**school_reforms**: `no_schools` / `basic_schooling` / `general_schooling` / `comprehensive_schooling` / `advanced_schooling` / `adult_education` / `extensive_education` / `tech_schools` / `compulsory_school` / `compulsory_edu_2` / `compulsory_edu_3` / `full_schooling`

## Terrain System (64 types)

Terrain affects movement cost, defense, RGO efficiency, supply limit, and combat width:

| Terrain | Movement | Defense | Supply | Farm | Mine | Notes |
|---------|----------|---------|--------|------|------|-------|
| `ocean` | 1.0 | - | 10 | - | - | Water only |
| `urban` | 1.0 | 2 | 10 | 0.0 | 0.0 | No RGO |
| `plains` | 1.0 | - | 10 | 0.0 | 0.0 | Default |
| `steppe` | 1.0 | - | 8 | 0.0 | 0.0 | |
| `savanna` | 1.0 | - | 10 | 0.0 | 0.0 | |
| `arctic` | 1.0 | - | - | -0.5 | -0.0 | Min railroad: 1 |
| `forest` | 1.2 | 1 | 6 | 0.0 | 0.0 | -20% combat width |
| `boreal` | 1.2 | 1 | - | -0.5 | -0.2 | Min railroad: 1, -20% combat width |
| `hills` | 1.2 | 1 | 6 | 0.0 | 0.0 | Min railroad: 1, -33% combat width |
| `dryhills` | 1.2 | 1 | 6 | 0.0 | 0.0 | Min railroad: 1, -33% combat width |
| `jungle` | 1.2 | 1 | 5 | 0.0 | -0.2 | Min railroad: 2, -25% combat width |
| `marsh` | 1.4 | 1 | 2 | 0.0 | -0.2 | Min railroad: 2, -25% combat width |
| `mountain` | 1.4 | 2 | 2 | 0.0 | -0.25 | Min railroad: 3, -66% combat width |
| `montane_tundra` | 1.4 | 2 | 2 | -0.5 | -0.45 | Min railroad: 3, -66% combat width |
| `montane_forest` | 1.4 | 2 | 2 | 0.0 | -0.25 | Min railroad: 3, -66% combat width |
| `desert` | 1.5 | - | 4 | -0.5 | 0.0 | Min railroad: 2 |
| `semidesert` | 1.2 | - | 4 | -0.5 | -0.2 | Min railroad: 1 |
| `coastal_desert` | 1.2 | - | 2 | -0.25 | 0.0 | |
| `small_island` | 1.0 | - | 10 | 0.0 | 0.0 | |
| `coral_island` | 1.0 | - | 10 | 0.0 | 0.0 | |
| `farmlands` | 1.2 | - | 10 | +0.2 | 0.0 | |
| `new_world_*` | varies | varies | varies | varies | varies | New World variants |

## Casus Belli (CB) System

From `common/cb_types.txt`, key CB types for war justification:

| CB Type | Description | Peace Options |
|---------|-------------|---------------|
| `conquest` | Take specific provinces | po_transfer_provinces |
| `conquest_any` | Take any provinces | po_transfer_provinces |
| `annex_core_country` | Annex if all cores owned | po_annex |
| `acquire_state` | Take entire state | po_demand_state |
| `acquire_all_cores` | Take all core provinces | po_transfer_provinces |
| `unification_casus_belli` | Unification wars | po_transfer_provinces |
| `add_to_sphere` | Add to sphere of influence | po_add_to_sphere |
| `remove_from_sphere` | Remove from sphere | take_from_sphere |
| `install_communist_gov_type` | Change government to communist | po_install_communist_gov_type |
| `install_fascism` | Change government to fascist | po_install_fascism |
| `install_democracy` | Change government to democracy | great_war_install_democracy |
| `place_in_the_sun` | Colonial conquest | po_colony |
| `cut_down_to_size` | Dismantle military | po_dismantle_forts |
| `dismantle_cb` | Remove GP status | Multiple |
| `liberate_country` | Release new country | po_release_puppet |
| `make_puppet` | Create puppet state | po_make_puppet |
| `humiliate` | Prestige and money | po_humiliate |
| `war_reparations` | Economic compensation | po_reparations |

## Common Triggers & Effects Reference

### Country Triggers (Conditions)
```
tag = TAG                          # Is specific country
owns = PROV_ID                     # Owns province
controls = PROV_ID                 # Controls province
has_country_flag = flag_name       # Has country flag
has_global_flag = flag_name        # Has global flag
war_with = TAG                     # At war with specific country
is_greater_power = yes             # Is a great power
is_secondary_power = yes           # Is a secondary power
civilized = yes                    # Is civilized
in_sphere = TAG                    # In sphere of influence
vassal_of = TAG                    # Is vassal
alliance_with = TAG                # Has alliance
relation = { who = TAG value = X }  # Relation value check
prestige = X                       # Prestige check
war = yes                          # Is at war
blockade = X                       # Blockade percentage check
```

### Province Triggers
```
owned_by = TAG                     # Owned by specific country
controlled_by = TAG                # Controlled by specific country
region = REGION_NAME               # In specific region
trade_goods = good_name            # Produces specific good
life_rating = X                    # Minimum life rating
has_building_type = building       # Has specific building
fort = X                           # Fort level check
railroad = X                       # Railroad level check
```

### Common Effects
```
prestige = X                       # Add prestige (can be negative)
add_core = TAG / PROV_ID           # Add core claim
remove_core = TAG                  # Remove core claim
secede_province = TAG              # Transfer province to country
country_event = EVENT_ID           # Trigger event for country
province_event = EVENT_ID          # Trigger event for province
set_country_flag = flag_name       # Set country flag
set_global_flag = flag_name        # Set global flag
clr_country_flag = flag_name       # Clear country flag
clr_global_flag = flag_name        # Clear global flag
relation = { who = TAG value = X } # Change relations
change_tag = NEW_TAG               # Change country tag
annex = THIS / TAG                 # Annex country
release = TAG                      # Release country as vassal
inherit = TAG                      # Inherit/annex country
casus_belli = { target = TAG type = cb_name } # Grant CB
add_to_sphere = TAG                # Add to sphere
remove_from_sphere = TAG           # Remove from sphere
badboy = X                         # Add infamy (can be negative)
war = { target = TAG type = cb_name } # Declare war
```

### Scope Modifiers
- `THIS` - Current country/province in scope
- `FROM` - Country that triggered the event
- `ROOT` - Original actor in a chain
- `TAG` - Specific country tag
- `PROV_ID` - Specific province ID

### Random Lists
```
random = {
    chance = 50                   # 50% chance
    effect = { ... }
}

random_list = {
    50 = { effect = { ... } }     # 50% weight
    30 = { effect = { ... } }     # 30% weight
    20 = { effect = { ... } }     # 20% weight
}
```

### Any/Every Blocks
```
any_owned = { limit = { ... } effect = { ... } }      # Any owned province
any_country = { limit = { ... } effect = { ... } }    # Any country
every_country = { limit = { ... } effect = { ... } }  # Every country

# Scope switching
any_owned = {
    limit = { region = BRZ_2408 }
    owner = {                  # Switch to province owner scope
        country_event = 12345
    }
}
```

## Mod Statistics Summary

| Category | Count | Notes |
|----------|-------|-------|
| Total Files | 9,739 | Across 63 directories |
| Countries | 644 | Defined in common/countries/ |
| Events | 1,841 | Across 125+ event files |
| Decisions | 95+ | Political decisions |
| Provinces | 2,775 | History files in 24 regions |
| Land Unit Types | 15 | Infantry, cavalry, artillery, engineers, guards, planes, tanks |
| Naval Unit Types | 11 | Frigates to dreadnoughts, transports |
| Trade Goods | 47 | In 4 categories |
| POP Types | 13 | Farmers to capitalists |
| Terrain Types | 64 | Including new world variants |
| Tech Files | 5 | army, commerce, culture, industry, navy |
| Invention Files | 28 | Including PUIR inventions |
| Localisation Files | 50+ | CSV format |

## Testing & Debugging Guide

### Game Log Locations
Located in Victoria II root directory:
- **`error.log`** - Parse errors, unknown tokens, syntax errors
- **`game.log`** - Runtime errors, missing localization
- **`history.log`** - History loading errors

### Console Commands (Press `~` to open)
```
event [EVENT_ID] [TAG]        # Fire event for country
debug fow                     # Toggle fog of war
debug yesmen                  # AI always accepts proposals
debug alwaysreform            # AI always accepts reforms
debug showid                  # Show province IDs on hover
debug diplomaticspymode       # See AI diplomatic reasoning
debug crash [yes/no]          # Toggle crash on error
instantresearch               # Instant research
money [amount]                # Add money
leadership [amount]           # Add leadership
prestige [amount]             # Add prestige
conquer [PROV_ID]             # Conquer province
tag [TAG]                     # Switch to play as country
```

### Testing Workflow
1. **Syntax Check**: Load mod in vanilla Victoria II launcher
2. **Log Check**: Review error.log for parse errors
3. **Basic Test**: Start as simple country, check decisions appear
4. **Event Chain Test**: Use console to fire events sequentially
5. **AI Test**: Run observe mode, let AI play 1-2 years
6. **Performance**: Check for lag with large events

### Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Event doesn't fire | Missing space in condition | Check `tag = ENG` not `tag=ENG` |
| Localization missing | Key typo in CSV | Verify key matches exactly |
| Decision not visible | `potential` block fails | Check all conditions |
| Game crashes | Unbalanced braces | Count `{` and `}` |
| Province doesn't exist | Wrong province ID | Check map/definition.csv |
| Event fires multiple times | No flag check | Add `has_country_flag` check |

### Debugging Event Chains
```
# Add debugging to event option:
option = {
    name = "DEBUG.A"
    TAG = { country_event = 12345 }
    log = "Event 98401 option A fired for TAG"  # Print to log
}
```

## External Resources

- **Victoria II Wiki**: https://victoria2.paradoxwikis.com
- **Paradox Modding Forum**: https://forum.paradoxplaza.com
- **HPM Documentation**: Base mod for dodWorldTheater
- **Event/Effect Reference**: Paradox Wiki modding sections
- **Province ID Map**: Check `map/definition.csv` for valid IDs
