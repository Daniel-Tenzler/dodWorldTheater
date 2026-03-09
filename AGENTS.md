# AGENTS.md - Development Guidelines for dodWorldTheater

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

## Build/Test/Lint Commands

No automated build system. Manual testing in Victoria II required:

- Load mod in game to verify syntax
- Check game logs for errors  
- Test new events/decisions in gameplay

## Code Style Guidelines

### File Format

- Use `.txt` for game configs, `.lua` for scripts, `.csv` for localization
- Encoding: UTF-8 without BOM
- Use tabs for indentation (not spaces)

### Paradox Script Syntax

#### Basic Structure

- Key-value pairs: `key = value`
- Block structures: `block_name = { ... }`
- Comments start with `#`
- String values in quotes when containing spaces
- Equals sign must have spaces: `tag = ENG` (not `tag=ENG`)

#### Event Structure

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

#### Decision Structure

```
political_decisions = {
    form_usca = {
        potential = {
            NOT = { part_of_sphere = yes }
            primary_culture = central_american
        }
        
        allow = {
            NOT = { war = yes }
        }
        
        effect = {
            prestige = 10
            any_country = {
                limit = { primary_culture = central_american }
                annex = THIS
            }
        }
    }
}
```

#### Building/Unit Structure

```
aeroplane_factory = {
    type = factory
    goods_cost = {
        machine_parts = 200
        steel = 600
    }
    time = 365
    visibility = yes
    production_type = aeroplane_factory
}
```

#### Country Tags

- Format: `TAG = "path/to/file.txt"`
- Tags are 3-letter uppercase codes
- Special tag: `REB` for rebels
- Dynamic tags use `dynamic_tags = yes` prefix

#### Localization (CSV Format)

```
key;English;French;German;;;;;;;;;;;
key_desc;Description text;;;;;;;;;;;
```

### Naming Conventions

- Compound names: `aeroplane_factory` (underscores)
- Country tags: 3-letter uppercase codes: "ENG", "FRA"
- Files: lowercase with underscores
- Events: numeric IDs (typically 5 digits, often with prefixes)
- Localization keys: `KEY_NAME`, `KEY_NAME_DESC`, `KEY_NAME.T`, `KEY_NAME.D`, `KEY_NAME.A/B/C`

### Logical Operators

- `AND` (default): multiple conditions in same block
- `OR`: `OR = { condition1 condition2 }`
- `NOT`: `NOT = { condition }`
- Country scope: `THIS` (current country), `FROM` (triggering country)

### Common Patterns

- Conditions: `limit = { }`
- Effects: `effect = { }`
- Triggers: `trigger = { }`
- AI behavior: `ai_chance = { factor = X }`
- Province effects: `PROV_ID = { add_core = TAG }`
- Country effects: `TAG = { relation = { who = FROM value = 50 } }`

### File Organization

- Group related entries logically
- Alphabetize where appropriate (especially country tags)
- Use descriptive comments for complex blocks
- Maintain consistent ordering across similar files
- Keep files focused on single aspect when possible

### Error Prevention

- Always balance braces { }
- Check for missing spaces around `=`
- Verify province IDs exist
- Ensure localization keys match event/decision references
- Test event chains sequentially

## Common Directory Reference

The `common/` directory contains core game data definitions. For detailed documentation of each file's purpose and function, see **[common_files_documentation.md](common_files_documentation.md)**.

Key files include:
- `buildings.txt` - Factory and building definitions
- `countries.txt` - Country tag registry
- `defines.lua` - Core game constants
- `goods.txt` - Tradeable commodities
- `cultures.txt` - Cultural groups
- `governments.txt` - Government types
- `ideologies.txt` - Political ideologies
- `issues.txt` - Political issues
- `national_focus.txt` - State development priorities
- `nationalvalues.txt` - National value systems
- `rebel_types.txt` - Rebellion definitions
- `pop_types.txt` - Population types
- `production_types.txt` - Economic production
- `cb_types.txt` - Casus Belli (war justifications)
- `religion.txt` - Religious definitions
- `technology.txt` - Technology categories
- `traits.txt` - Military leader traits
- `event_modifiers.txt` - Event-applied modifiers
- `triggered_modifiers.txt` - Conditional modifiers
- `on_actions.txt` - Event scheduling
- `crime.txt` - Provincial crime types
- `bookmarks.txt` - Game starting scenarios
- `country_colors.txt` - Military unit colors

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
