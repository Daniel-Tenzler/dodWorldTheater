---
title: Victoria 2 Modding Templates
category: guide
tags: [templates, recipes, quick-reference]
source: Modding Community
url: https://vic2.paradoxwikis.com/ (Community compilation)
---

# Victoria 2 Modding Templates

Ready-to-use code templates for common Victoria 2 modding tasks. Copy, paste, and adapt these templates for your needs.

## Table of Contents

1. [Country Event Template](#country-event-template)
2. [Province Event Template](#province-event-template)
3. [Decision Template](#decision-template)
4. [Political Decision Template](#political-decision-template)
5. [Unification Decision Template](#unification-decision-template)
6. [MTTH Event Template](#mtth-event-template)
7. [Triggered-Only Event Template](#triggered-only-event-template)
8. [Event Chain Template](#event-chain-template)
9. [POP Event Template](#pop-event-template)
10. [CB Grant Event Template](#cb-grant-event-template)
11. [Localization Template](#localization-template)
12. [Country Creation Template](#country-creation-template)

---

## Country Event Template

Use this for events that affect entire countries.

```paradox
country_event = {
    id = 50001                            # Unique event ID (use reserved range)
    title = "YOUR_EVENT.T"
    desc = "YOUR_EVENT.D"
    picture = "event_picture_name"        # Optional: gfx/pictures/events/event_picture_name.dds

    trigger = {
        tag = TAG                          # Only for specific country
        # Add more conditions...
    }

    mean_time_to_happen = {               # Remove if using is_triggered_only
        months = 120
        # Add modifiers...
    }

    option = {
        name = "YOUR_EVENT.A"
        # Effects here...
    }

    option = {
        name = "YOUR_EVENT.B"
        # Alternative effects...
    }
}
```

---

## Province Event Template

Use this for events that affect specific provinces.

```paradox
province_event = {
    id = 50002
    title = "YOUR_EVENT.T"
    desc = "YOUR_EVENT.D"

    trigger = {
        owner = {
            tag = TAG                     # Country owning province
        }
        trade_goods = coal                 # Province produces coal
    }

    mean_time_to_happen = {
        months = 180
    }

    option = {
        name = "YOUR_EVENT.A"
        owner = {
            prestige = 10                  # Effect on owning country
        }
        life_rating = 5                     # Effect on province
    }
}
```

---

## Decision Template

Basic decision structure with visibility, requirements, and effects.

```paradox
political_decisions = {
    your_decision = {
        picture = "DecisionPicture"       # gfx/pictures/decisions/DecisionPicture.dds

        potential = {
            tag = TAG                         # Decision visible to this country
            NOT = { has_global_flag = decision_done }
        }

        allow = {
            is_greater_power = yes            # Must be a GP
            prestige = 50                      # Minimum prestige
        }

        effect = {
            prestige = 20
            set_global_flag = decision_done     # Prevent reuse
        }

        ai_will_do = {
            factor = 1
        }
    }
}
```

---

## Political Decision Template

Decision that changes political or social reforms.

```paradox
political_decisions = {
    political_reform = {
        picture = "reform_picture"

        potential = {
            tag = TAG
            NOT = {
                political_reform = { level = 2 }  # Not already at level 2
            }
        }

        allow = {
            prestige = 100
            militancy = 6                    # High militancy
        }

        effect = {
            political_reform = { level = 2 }    # Enact reform
            prestige = -10                     # Cost
        }

        ai_will_do = {
            factor = 0.5                      # AI reluctant
        }
    }
}
```

---

## Unification Decision Template

Decision to unify a region into one country.

```paradox
political_decisions = {
    form_unified_country = {
        picture = "UnifyTAG"

        potential = {
            tag = TAG1                        # Primary country
            OR = {
                tag = TAG1
                tag = TAG2
                tag = TAG3
            }
            NOT = { exists = UNIFIED }
        }

        allow = {
            is_greater_power = yes
            war = no
            all_core = {                       # Check all cores of unified tag
                OR = {
                    owned_by = THIS
                    owner = {
                        in_sphere = THIS
                    }
                }
            }
        }

        effect = {
            prestige = 50
            change_tag = UNIFIED
            add_accepted_culture = culture1
            add_accepted_culture = culture2
            set_global_flag = unified_formed
        }

        ai_will_do = {
            factor = 1
        }
    }
}
```

---

## MTTH Event Template

Event that fires randomly based on Mean Time To Happen.

```paradox
country_event = {
    id = 50003
    title = "RANDOM_EVENT.T"
    desc = "RANDOM_EVENT.D"

    trigger = {
        tag = TAG
        is_greater_power = yes
    }

    mean_time_to_happen = {
        months = 120                         # Base: 50% chance after 10 years

        modifier = {
            factor = 0.5                      # Halves MTTH (doubles chance)
            trigger = {
                war = yes                     # When at war
            }
        }

        modifier = {
            factor = 2.0                      # Doubles MTTH (halves chance)
            trigger = {
                ruling_party = {
                    ideology = liberal
                }
            }
        }
    }

    option = {
        name = "RANDOM_EVENT.A"
        prestige = 10
    }
}
```

---

## Triggered-Only Event Template

Event that only fires when triggered by other events/decisions.

```paradox
country_event = {
    id = 50004
    title = "TRIGGERED_EVENT.T"
    desc = "TRIGGERED_EVENT.D"
    is_triggered_only = yes                  # No MTTH, must be triggered

    trigger = {
        tag = TAG
        has_country_flag = flag_name         # Required flag
    }

    option = {
        name = "TRIGGERED_EVENT.A"
        clr_country_flag = flag_name
        # Effects...
    }
}
```

---

## Event Chain Template

Sequence of events that fire one after another.

```paradox
# Event 1: Start chain
country_event = {
    id = 50100
    title = "CHAIN_1.T"
    desc = "CHAIN_1.D"

    trigger = {
        tag = TAG
        NOT = { has_country_flag = chain_complete }
    }

    mean_time_to_happen = {
        months = 6
    }

    option = {
        name = "CHAIN_1.A"
        set_country_flag = chain_started
        country_event = 50101              # Fire Event 2
    }
}

# Event 2: Middle of chain
country_event = {
    id = 50101
    title = "CHAIN_2.T"
    desc = "CHAIN_2.D"
    is_triggered_only = yes

    option = {
        name = "CHAIN_2.A"
        country_event = 50102              # Fire Event 3
    }
}

# Event 3: End of chain
country_event = {
    id = 50102
    title = "CHAIN_3.T"
    desc = "CHAIN_3.D"
    is_triggered_only = yes

    option = {
        name = "CHAIN_3.A"
        set_country_flag = chain_complete
        prestige = 10
    }
}
```

---

## POP Event Template

Event that affects specific POPs based on conditions.

```paradox
country_event = {
    id = 50200
    title = "POP_EVENT.T"
    desc = "POP_EVENT.D"

    trigger = {
        tag = TAG
        any_pop = {
            limit = {
                consciousness = 5             # Conscious POPs
                is_primary_culture = no       # Not primary culture
            }
        }
    }

    mean_time_to_happen = {
        months = 12
    }

    option = {
        name = "POP_EVENT.A"

        # Change consciousness for specific POPs
        any_pop = {
            limit = {
                is_primary_culture = no
                consciousness = 5
            }
            consciousness = -1               # Reduce consciousness
        }

        # Change militancy
        any_pop = {
            limit = {
                is_accepted_culture = no
            }
            militancy = 2
        }
    }
}
```

---

## CB Grant Event Template

Event that grants a Casus Belli to the country.

```paradox
country_event = {
    id = 50300
    title = "CB_GRANT.T"
    desc = "CB_GRANT.D"

    trigger = {
        tag = TAG
        owns = 2414                       # Own specific province
        NOT = {
            has_casus_belli = {
                target = ENEMY
                type = conquest
            }
        }
    }

    mean_time_to_happen = {
        months = 12
    }

    option = {
        name = "CB_GRANT.A"
        casus_belli = {
            target = ENEMY                   # Grant CB on ENEMY
            type = conquest
            months = 12                     # CB valid for 12 months
        }
    }

    option = {
        name = "CB_GRANT.B"
        prestige = 5                         # Small prestige for waiting
    }
}
```

---

## Localization Template

CSV format for event/decision text.

```csv
# Event Localization
YOUR_EVENT.T;Your Event Title;;;;;;;;;;;;;
YOUR_EVENT.D;This is the description that players will read. It can be quite long and detailed.\n\nUse \n for line breaks.;;;;;;;;;;;;;
YOUR_EVENT.A;First option;;;;;;;;;;;;;
YOUR_EVENT.B;Second option;;;;;;;;;;;;;

# Decision Localization (auto-generates _title and _desc)
your_decision_title;Your Decision Name;;;;;;;;;;;;;
your_decision_desc;Description of what this decision does and when it can be taken.;;;;;;;;;;;;;

# Country Localization
TAG;Country Name;;;;;;;;;;;;;
TAG_ADJ;Countryman;;;;;;;;;;;;;
```

**Important:**
- Exactly **14 semicolons** per line
- File encoding must be **ANSI**
- Add to `localisation/` folder with appropriate prefix number

---

## Country Creation Template

All files needed to create a new country.

### 1. Country Definition
**File:** `common/countries/NEW - New Country.txt`

```paradox
color = { 100 150 200 }
graphical_culture = western

ship_names = {
    "HMS First Ship"
    "HMS Second Ship"
}

army_names = {
    "First Army"
    "Second Army"
}

monarch_names = {
    "John Smith"
    "Jane Doe"
}
```

### 2. Country History
**File:** `history/countries/NEW - New Country.txt`

```paradox
capital = 1001                          # Province ID
primary_culture = british
religion = protestant
government = absolute_monarchy
plurality = 0.0
nationalvalue = nv_order
literacy = 0.04

# Starting reforms (select applicable ones)
slavery = no_slavery
upper_house_composition = appointed
vote_franschise = none_voting
public_meetings = yes_meeting
press_rights = state_press
trade_unions = no_trade_unions

# Social reforms
wage_reform = no_minimum_wage
work_hours = no_work_hour_limit
safety_regulations = no_safety
health_care = no_health_care

ruling_party = NEW_conservative
upper_house = {
    fascist = 0
    liberal = 10
    conservative = 70
    reactionary = 20
}
```

### 3. Starting Units
**File:** `history/units/NEW_O.txt` (Armies)

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

**File:** `history/units/NEW_P.txt` (Navies)

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

### 4. Localization
**File:** `localisation/countries.csv`

```csv
NEW;New Country;;;;;;;;;;;;;
NEW_ADJ;New Countryman;;;;;;;;;;;;;
```

### 5. Flag
**File:** `gfx/flags/NEW.tga`
- Format: TGA with alpha channel
- Size: Usually 128x128 or 256x128

---

## Template Usage Tips

1. **Copy and adapt** - Don't use templates blindly
2. **Check ID ranges** - Use reserved ranges for your mod
3. **Validate syntax** - Check braces, spaces, quotes
4. **Add localization** - Every text needs a CSV entry
5. **Test in-game** - Use console commands to verify

---

## See Also

- [QUICKSTART.md](QUICKSTART.md) - Step-by-step workflows
- [Event_modding.md](Event_modding.md) - Event details
- [Decision_modding.md](Decision_modding.md) - Decision details
- [PATTERNS.md](PATTERNS.md) - Common patterns
- [VALIDATION_CHECKLIST.md](VALIDATION_CHECKLIST.md) - Before finalizing
