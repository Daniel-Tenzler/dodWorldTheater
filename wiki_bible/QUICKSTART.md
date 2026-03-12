---
title: Victoria 2 Modding Quickstart Guide
category: guide
tags: [tutorial, workflow, beginner]
source: Modding Community
url: https://vic2.paradoxwikis.com/ (Community compilation)
---

# Victoria 2 Modding Quickstart Guide

Step-by-step workflows for common modding tasks in Victoria 2. Each task includes required files, validation steps, and testing commands.

## Table of Contents

1. [Add a New Event](#task-1-add-a-new-event)
2. [Add a Decision](#task-2-add-a-decision)
3. [Create a New Country](#task-3-create-a-new-country)
4. [Add Localization](#task-4-add-localization)
5. [Create a Casus Belli](#task-5-create-a-casus-belli)
6. [Add a Technology](#task-6-add-a-technology)
7. [Test Your Content](#task-7-test-your-content)
8. [Debug Common Issues](#task-8-debug-common-issues)

---

## Task 1: Add a New Event

### What You'll Create
A country event that fires under specific conditions and presents the player with choices.

### Files to Modify
- `events/[your_file].txt` - Event definition
- `localisation/[your_file].csv` - Event text

### Step 1: Choose a Unique Event ID
```
Check existing event ranges:
- 10XXX-11XXX: Early game/tutorial
- 12XXX-12XXX: General events
- 33XXX: Arcadia region
- 98XXX: Amazonia region
- 50XXX-89XXX: Available for mods

Your ID should be unique across all mods!
```

### Step 2: Create the Event File
Create or edit: `events/your_events.txt`

```paradox
country_event = {
    id = 50001                                    # Unique ID
    title = "YOUR_EVENT.T"                        # Localization key
    desc = "YOUR_EVENT.D"

    trigger = {
        tag = ENG                                 # Only for England
        owns = 2414                               # That owns London
        is_greater_power = yes                    # And is a GP
    }

    mean_time_to_happen = {                       # Remove if using is_triggered_only
        months = 120
    }

    option = {
        name = "YOUR_EVENT.A"                     # First option
        ai_chance = { factor = 50 }               # AI behavior
        prestige = 10                             # Effect
    }

    option = {
        name = "YOUR_EVENT.B"                     # Second option
        treasury = 1000                           # Different effect
    }
}
```

### Step 3: Add Localization
Create or edit: `localisation/your_mod.csv`

```csv
YOUR_EVENT.T;Your Event Title;;;;;;;;;;;;;
YOUR_EVENT.D;This is the description that players will read.;;;;;;;;;;;;;
YOUR_EVENT.A;Accept the proposal;;;;;;;;;;;;;
YOUR_EVENT.B;Reject the proposal;;;;;;;;;;;;;
```

**Important:** Use exactly 14 semicolons per line!

### Step 4: Test Your Event
1. Launch Victoria II with your mod
2. Press `~` to open console
3. Type: `event 50001 ENG`
4. Verify the event displays with correct text

### Validation Checklist
- [ ] Event ID is unique (grep all event files)
- [ ] Braces `{ }` are balanced
- [ ] Spaces around `=` signs
- [ ] Localization keys match exactly
- [ ] At least one `option` block exists
- [ ] `ai_chance` defined in each option

---

## Task 2: Add a Decision

### What You'll Create
A player-triggered decision with visibility conditions, requirements, and effects.

### Files to Modify
- `decisions/[your_file].txt` - Decision definition
- `localisation/[your_file].csv` - Decision text

### Step 1: Create the Decision File
Create or edit: `decisions/your_decisions.txt`

```paradox
political_decisions = {
    your_decision = {
        potential = {
            tag = ENG                             # Visible to England
            NOT = { has_global_flag = your_decision_done }
        }

        allow = {
            is_greater_power = yes                # Must be a GP
            prestige = 50                         # Need 50 prestige
            owns = 2414                           # Must own London
        }

        effect = {
            prestige = 20                         # Gain prestige
            treasury = 500                        # Gain money
            set_global_flag = your_decision_done  # Prevent reuse
        }

        ai_will_do = {
            factor = 1                            # AI will take it
        }
    }
}
```

### Step 2: Add Localization
Create or edit: `localisation/your_mod.csv`

```csv
your_decision_title;Your Decision Name;;;;;;;;;;;;;
your_decision_desc;Description of what this decision does;;;;;;;;;;;;;
```

**Note:** Decision names automatically generate `_title` and `_desc` keys!

### Step 3: Test Your Decision
1. Launch the game as England
2. Open the decisions panel
3. Verify your decision appears
4. Try taking it (check requirements are met)

### Common Mistakes
- ❌ Putting conditions in `allow` instead of `potential` → decision won't be visible
- ❌ Forgetting `ai_will_do` → AI will never take it
- ❌ Missing flag check → decision can be taken infinitely

---

## Task 3: Create a New Country

### What You'll Create
A fully functional new country with history, localization, and graphics.

### Files to Create/Modify
1. `common/countries/TAG - Country Name.txt` - Country definition
2. `history/countries/TAG - Country Name.txt` - Starting data
3. `history/units/[TAG]_O.txt` - Starting armies
4. `history/units/[TAG]_P.txt` - Starting navies
5. `localisation/countries.csv` - Country name translations
6. `gfx/flags/TAG.tga` - Country flag

### Step 1: Choose a Country Tag
- Use 3-letter uppercase codes
- Check `Countries.md` for used tags
- Example: `NEW`, `ARC`, `VIN`

### Step 2: Create Country Definition
Create: `common/countries/NEW - New Country.txt`

```paradox
color = { 100 150 200 }                # RGB color
graphical_culture = western            # Unit graphics

# Optional: Ship names
ship_names = {
    "HMS First Ship"
    "HMS Second Ship"
}

# Optional: Unit names
army_names = {
    "First Army"
    "Second Army"
}

# Optional: Monarch names
monarch_names = {
    "John Smith"
    "Jane Doe"
}
```

### Step 3: Create Country History
Create: `history/countries/NEW - New Country.txt`

```paradox
capital = 1001                          # Province ID of capital
primary_culture = british
religion = protestant
government = absolute_monarchy
plurality = 0.0
nationalvalue = nv_order
literacy = 0.04

# Starting reforms
slavery = no_slavery
upper_house_composition = appointed
vote_franschise = none_voting
public_meetings = yes_meeting
press_rights = state_press
trade_unions = no_trade_unions
voting_system = first_past_the_post
political_parties = underground_parties

# Social reforms
wage_reform = no_minimum_wage
work_hours = no_work_hour_limit
safety_regulations = no_safety
health_care = no_health_care
unemployment_subsidies = no_subsidies
pensions = no_pensions
school_reforms = no_schools

# Ruling party and upper house
ruling_party = NEW_conservative
upper_house = {
    fascist = 0
    liberal = 10
    conservative = 70
    reactionary = 20
}

# Optional: Starting prestige
prestige = 5
```

### Step 4: Create Starting Units
Create: `history/units/NEW_O.txt` (Armies)

```paradox
unit = {
    name = "First Army"
    location = 1001
    regiment = {
        name = "First Regiment"
        type = infantry
        home = 1001
        strength = 1.0
        org = 1.0
    }
}
```

Create: `history/units/NEW_P.txt` (Navies)

```paradox
unit = {
    name = "First Fleet"
    location = 1001
    ship = {
        name = "First Ship"
        type = frigate
        home = 1001
        strength = 1.0
    }
}
```

### Step 5: Add Localization
Add to: `localisation/countries.csv`

```csv
NEW;New Country;;;;;;;;;;;;;
NEW_ADJ;New Countryman;;;;;;;;;;;;;
```

### Step 6: Create Flag
Place: `gfx/flags/NEW.tga`
- Format: TGA with alpha channel
- Size: Usually 128x128 or 256x128

### Validation Checklist
- [ ] Tag is 3 letters, uppercase
- [ ] Capital province exists in `map/definition.csv`
- [ ] Color has valid RGB values (0-255)
- [ ] Culture exists in `common/cultures.txt`
- [ ] Religion exists in `common/religion.txt`
- [ ] Government type exists in `common/governments.txt`

---

## Task 4: Add Localization

### What You'll Do
Add translated text for events, decisions, countries, and more.

### File Format
CSV with semicolon separators, 14 semicolons per line:

```csv
key;English;French;German;Polish;Spanish;Italian;Swedish;Czech;Hungarian;Dutch;Portuguese;Russian;Finnish;
```

### Localization Key Naming

| Type | Format | Example |
|------|--------|---------|
| Event Title | `KEYNAME.T` | `EVT_50001.T` |
| Event Description | `KEYNAME.D` | `EVT_50001.D` |
| Event Options | `KEYNAME.A`, `.B`, `.C` | `EVT_50001.A` |
| Decision Title | `decision_title` | `annex_tibet_title` |
| Decision Description | `decision_desc` | `annex_tibet_desc` |
| Country Name | `TAG` | `ENG` |
| Country Adjective | `TAG_ADJ` | `ENG_ADJ` |

### Special Characters
- New line: `\n`
- Tab: `\t`
- Quote: `\"` or `''`

### Example: Complete Event Localization
```csv
EVT_50001.T;The Industrial Revolution;;;;;;;;;;;;;
EVT_50001.D;Our nation is undergoing a profound transformation. New factories are springing up across the land, and the old ways are giving way to modern industry.\n\nHow shall we respond to this change?;;;;;;;;;;;;;
EVT_50001.A;Embrace progress;;;;;;;;;;;;;
EVT_50001.B;Maintain traditions;;;;;;;;;;;;;
```

### Validation Commands
```bash
# Check for missing semicolons
grep -v '^[^;]*;\([^;]*;\)\{14\}$' your_file.csv

# Check for duplicate keys
cut -d';' -f1 your_file.csv | sort | uniq -d
```

---

## Task 5: Create a Casus Belli

### What You'll Create
A custom war justification (CB) type with specific goals and peace options.

### Files to Modify
- `common/cb_types.txt` - CB definition

### Step 1: Define the CB Type
Add to: `common/cb_types.txt`

```paradox
your_custom_cb = {
    is_valid = {
        target = {
            continent = europe                 # Must target Europe
        }
        owner = {
            continent = europe                 # Must be in Europe
        }
    }

    construction_speed = 0.5                  # 50% faster to fabricate

    badboy_factor = 0.5                       # 50% infamy of normal conquest

    is_triggered_only = yes                   # Only via event/decision

    good_relation_effect = {
        who = target
        value = -20                           # Lose 20 relations
    }

    can_use = {
        OR = {
            is_greater_power = yes
            is_secondary_power = yes
        }
    }

    on_add = {
        owner = {
            add_country_modifier = {
                name = "fabricating_claims"
                duration = 180
            }
        }
    }

    peace_cost = 0.5                          # 50% war score cost

    # Peace options available with this CB
    peace_price = {
        po_transfer_provinces = 1.0
        po_demand_state = 0.7
        po_annex = 2.0
        po_puppet = 1.5
    }

    winner = {
        prestige = 10
        militancy = 2
    }

    loser = {
        prestige = -10
        militancy = 1
    }
}
```

### Step 2: Grant CB via Event/Decision
```paradox
casus_belli = {
    target = TAG
    type = your_custom_cb
    months = 12                               # CB valid for 12 months
}
```

### Step 3: Test the CB
1. Use console to fire event granting CB
2. Check diplomacy screen → "Fabricate Casus Belli"
3. Verify CB appears with correct name
4. Attempt to justify and declare war

---

## Task 6: Add a Technology

### What You'll Create
A new technology with prerequisites, effects, and invention triggers.

### Files to Modify
- `technologies/[category]_tech.txt` - Technology definition
- `localisation/technologies.csv` - Tech names

### Step 1: Choose Category
- `army_tech.txt` - Land warfare
- `commerce_tech.txt` - Economic
- `culture_tech.txt` - Social/cultural
- `industry_tech.txt` - Industrial
- `navy_tech.txt` - Naval

### Step 2: Define Technology
Add to: `technologies/army_tech.txt`

```paradox
your_tech = {
    area = army_tech                          # Tech category

    year = 1840                               # Available from this year

    cost = 7200                               # Research points needed

    unit = {
        infantry = active                     # Enables unit type
        guard = active
    }

    ai_chance = {
        factor = 1                            # Base weight
        modifier = {
            factor = 2
            culture_group = germanic
        }
    }

    effect = {
        country_event = 50001                 # Event when researched
    }
}
```

### Step 3: Add Localization
Add to: `localisation/technologies.csv`

```csv
your_tech;Your Technology Name;;;;;;;;;;;;;
your_tech_desc;Description of what this technology does;;;;;;;;;;;;;
```

### Tech Effects Reference
| Effect | Syntax | Description |
|--------|--------|-------------|
| Enable unit | `unit = { infantry = active }` | Unit becomes buildable |
| Enable building | `building = { factory = active }` | Building becomes available |
| Add modifier | `activate_technology = tech_name` | Grant another tech |
| Trigger event | `country_event = ID` | Fire event on research |
| Add RPs | `research_points = 100` | Grant research points |

---

## Task 7: Test Your Content

### Pre-Launch Checklist
- [ ] All files in correct folders
- [ ] Localization keys exist
- [ ] Event IDs are unique
- [ ] Province IDs are valid
- [ ] Country tags are valid
- [ ] Braces are balanced
- [ ] Spaces around `=` signs

### Launch Testing
1. **Load Test**
   - Start Victoria II launcher
   - Select your mod
   - Click Play
   - Check for crashes on startup

2. **Log Check**
   - Open `error.log` in Victoria II directory
   - Look for parse errors
   - Fix any "unknown token" errors

3. **In-Game Test**
   - Start a new game
   - Use console commands to test events
   - Check decisions panel
   - Verify localization displays

### Console Commands
Press `~` to open console, then use:

| Command | Effect |
|---------|--------|
| `event 50001 TAG` | Fire event for country |
| `debug showid` | Show province IDs on hover |
| `debug fow` | Toggle fog of war |
| `debug yesmen` | AI always accepts proposals |
| `tag TAG` | Switch to play as country |
| `money 10000` | Add money to treasury |
| `prestige 100` | Add prestige |
| `instantresearch` | Instant research |

---

## Task 8: Debug Common Issues

### Event Not Firing
**Symptoms:** Event never appears

**Solutions:**
1. Check trigger conditions with `debug showid`
2. Verify `mean_time_to_happen` isn't too high
3. Check for `is_triggered_only = yes` (requires trigger)
4. Verify event ID isn't duplicated

```paradox
# Debug: Add log output
country_event = {
    id = 50001
    trigger = {
        tag = ENG
    }
    option = {
        name = "A"
        # This will print to game.log
    }
}
```

### Missing Localization
**Symptoms:** Text appears as `KEY_NAME`

**Solutions:**
1. Verify key name matches exactly (case-sensitive!)
2. Check CSV has 14 semicolons
3. Ensure file is named correctly (e.g., `0_mod.csv` loads first)
4. Check encoding is ANSI, not UTF-8

### Province Doesn't Exist
**Symptoms:** Crash on load, "invalid province" error

**Solutions:**
1. Open `map/definition.csv`
2. Search for province ID
3. Use correct ID (numbers only)

### Decision Not Visible
**Symptoms:** Decision doesn't appear in list

**Solutions:**
1. Check `potential` block conditions
2. Verify tag matches your country
3. Look for `NOT = { has_global_flag = xxx }`
4. Ensure file is in `decisions/` folder

### Circular Event Chain
**Symptoms:** Game freezes, infinite loop

**Solutions:**
```paradox
# WRONG: Event 1 → Event 2 → Event 1
# Event 1
country_event = {
    id = 50001
    option = {
        name = "A"
        country_event = 50002
    }
}

# Event 2
country_event = {
    id = 50002
    option = {
        name = "A"
        country_event = 50001    # INFINITE LOOP!
    }
}

# CORRECT: Use flags to prevent loop
# Event 1
country_event = {
    id = 50001
    trigger = {
        NOT = { has_country_flag = event_1_done }
    }
    option = {
        name = "A"
        set_country_flag = event_1_done
        country_event = 50002
    }
}

# Event 2
country_event = {
    id = 50002
    option = {
        name = "A"
        # No loop back to 50001
    }
}
```

---

## Quick Reference: Essential Files

| File | Purpose |
|------|---------|
| `events/*.txt` | Event definitions |
| `decisions/*.txt` | Decision definitions |
| `localisation/*.csv` | Text translations |
| `common/countries/*.txt` | Country definitions |
| `history/countries/*.txt` | Country starting data |
| `common/goods.txt` | Trade goods list |
| `map/definition.csv` | Province IDs |
| `common/cb_types.txt` | Casus Belli types |

---

## Next Steps

1. **Learn Advanced Patterns:** See [PATTERNS.md](PATTERNS.md) for common modding recipes
2. **Reference Full Documentation:** See [Full_list_of_effects.md](Full_list_of_effects.md) and [List_of_conditions.md](List_of_conditions.md)
3. **Validate Your Work:** See [VALIDATION_CHECKLIST.md](VALIDATION_CHECKLIST.md) for complete validation
4. **Avoid Common Mistakes:** See [COMMON_PITFALLS.md](COMMON_PITFALLS.md) for troubleshooting

---

## Need Help?

- **Search Terms:** See [KEYWORDS.md](KEYWORDS.md) to find relevant documentation
- **Scope Issues:** See [Full_list_of_scopes.md](Full_list_of_scopes.md)
- **Effect Reference:** See [Full_list_of_effects.md](Full_list_of_effects.md)
- **Trigger Reference:** See [List_of_conditions.md](List_of_conditions.md)
