---
title: Victoria 2 Modding Patterns
category: guide
tags: [patterns, recipes, advanced]
source: Modding Community
url: https://vic2.paradoxwikis.com/ (Community compilation)
---

# Victoria 2 Modding Patterns

Common modding patterns and recipes for Victoria 2. Each pattern includes a template code block that you can adapt for your own needs.

## Table of Contents

1. [Country Unification Decision](#pattern-1-country-unification-decision)
2. [Province Transfer via Event](#pattern-2-province-transfer-via-event)
3. [POP Change Event](#pattern-3-pop-change-event)
4. [Event Chain with Flags](#pattern-4-event-chain-with-flags)
5. [Sphere of Influence Manipulation](#pattern-5-sphere-of-influence-manipulation)
6. [Grant Casus Belli](#pattern-6-grant-casus-belli)
7. [Random Event from List](#pattern-7-random-event-from-list)
8. [Check All Neighbors](#pattern-8-check-all-neighbors)
9. [Province Modifier Duration](#pattern-9-province-modifier-duration)
10. [Country Modifier Duration](#pattern-10-country-modifier-duration)
11. [Assimilate POPs](#pattern-11-assimilate-pops)
12. [Move POP to Province](#pattern-12-move-pop-to-province)
13. [Change Province Owner](#pattern-13-change-province-owner)
14. [Release Puppet/Vassal](#pattern-14-release-puppetvassal)
15. [AI Weight Modifiers](#pattern-15-ai-weight-modifiers)

---

## Pattern 1: Country Unification Decision

### Use Case
Create a decision that unifies a region into a single country (e.g., Germany, Italy, Scandinavia).

### Template

```paradox
political_decisions = {
    form_unified_country = {
        picture = "UnifyTAG"

        potential = {
            tag = TAG1                             # Playing as primary country
            OR = {
                tag = TAG1
                tag = TAG2
                tag = TAG3
            }
            NOT = { exists = UNIFIED }             # Unified country doesn't exist
            NOT = { has_global_flag = unified_formed }
        }

        allow = {
            is_greater_power = yes
            war = no
            all_core = {                           # Check all cores of unified tag
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
            add_to_sphere = {                     # Add all sphere members to sphere
                any_country = {
                    limit = {
                        in_sphere = THIS
                        culture_group = unified_culture
                    }
                    add_to_sphere = THIS
                }
            }

            # Event for all countries in region
            any_country = {
                limit = {
                    culture_group = unified_culture
                    in_sphere = THIS
                }
                country_event = { id = 55001 days = 1 }
            }

            # Annex willing countries
            any_country = {
                limit = {
                    culture_group = unified_culture
                    in_sphere = THIS
                    NOT = { has_country_flag = refused_unification }
                }
                    # Fire annexation event
                    country_event = { id = 55002 days = 2 }
                }
            }

            change_tag = UNIFIED                  # Become unified country
            set_global_flag = unified_formed
        }

        ai_will_do = {
            factor = 1
        }
    }
}
```

### Event for Countries Choosing Annexation

```paradox
country_event = {
    id = 55002
    is_triggered_only = yes

    title = "UNIFICATION.T"
    desc = "UNIFICATION.D"

    option = {
        name = "UNIFICATION.A"                   # Accept annexation
        ai_chance = { factor = 100 }
        set_country_flag = accepted_unification
    }

    option = {
        name = "UNIFICATION.B"                   # Refuse
        ai_chance = { factor = 0 }
        set_country_flag = refused_unification
        break_alliance = THIS
        relation = { who = THIS value = -100 }
    }
}
```

---

## Pattern 2: Province Transfer via Event

### Use Case
Transfer specific provinces from one country to another, with cores and proper cleanup.

### Template

```paradox
country_event = {
    id = 51001
    title = "TRANSFER.T"
    desc = "TRANSFER.D"

    trigger = {
        tag = FROM
        owns = 2414
        war = no
    }

    option = {
        name = "TRANSFER.A"

        # Option 1: Direct secede
        2414 = {
            owner = TAG
            controller = TAG
        }

        # Option 2: Using secede_province
        2414 = {
            secede_province = TAG
        }

        # Option 3: Multiple provinces at once
        any_owned = {
            limit = {
                region = target_region
            }
            secede_province = TAG
        }

        # Add cores if needed
        any_owned = {
            limit = {
                region = target_region
                NOT = { is_core = TAG }
            }
            add_core = TAG
        }

        # Remove old cores
        any_owned = {
            limit = {
                region = target_region
            }
            remove_core = FROM
        }
    }
}
```

---

## Pattern 3: POP Change Event

### Use Case
Change POP attributes (militancy, consciousness, ideology, issues) based on conditions.

### Template

```paradox
country_event = {
    id = 52001
    title = "POP_CHANGE.T"
    desc = "POP_CHANGE.D"

    trigger = {
        tag = ENG
        any_pop = {
            limit = {
                consciousness = 5
                is_primary_culture = no
            }
        }
    }

    mean_time_to_happen = {
        months = 12
    }

    option = {
        name = "POP_CHANGE.A"

        # Change consciousness for specific POPs
        any_pop = {
            limit = {
                is_primary_culture = no
                consciousness = 5
            }
            consciousness = -1
        }

        # Change militancy
        any_pop = {
            limit = {
                is_primary_culture = no
                is_accepted_culture = no
            }
            militancy = 2
        }

        # Change ideology support
        any_pop = {
            limit = {
                life_needs = 0.5                  # Poor POPs
            }
            ideology = {
                factor = 0.1
                value = socialist
            }
        }

        # Change dominant issue
        any_pop = {
            limit = {
                strata = rich
            }
            dominant_issue = {
                factor = 0.2
                value = jingoism
            }
        }
    }
}
```

### POP Scope Reference

| Target | Description |
|--------|-------------|
| `any_pop` | All POPs in current scope |
| `aristocrats` | All aristocrat POPs |
| `poor_strata` | Farmers, labourers, soldiers |
| `middle_strata` | Clerks, artisans, clerks |
| `rich_strata` | Capitalists, aristocrats, officers |

---

## Pattern 4: Event Chain with Flags

### Use Case
Create a sequence of events that fire one after another, preventing infinite loops.

### Template

```paradox
# Event 1: Start chain
country_event = {
    id = 53001
    title = "CHAIN_1.T"
    desc = "CHAIN_1.D"

    trigger = {
        tag = ENG
        NOT = { has_country_flag = chain_complete }
    }

    mean_time_to_happen = {
        months = 6
    }

    option = {
        name = "CHAIN_1.A"
        set_country_flag = chain_started
        country_event = 53002
    }
}

# Event 2: Middle of chain
country_event = {
    id = 53002
    is_triggered_only = yes
    title = "CHAIN_2.T"
    desc = "CHAIN_2.D"

    option = {
        name = "CHAIN_2.A"
        country_event = 53003
    }
}

# Event 3: End of chain
country_event = {
    id = 53003
    is_triggered_only = yes
    title = "CHAIN_3.T"
    desc = "CHAIN_3.D"

    option = {
        name = "CHAIN_3.A"
        set_country_flag = chain_complete
        prestige = 10
    }
}
```

### Flag Types

| Flag Type | Scope | Use When |
|-----------|-------|----------|
| `set_country_flag` | Single country | Country-specific state |
| `set_global_flag` | All countries | Game-wide state |
| `set_province_flag` | Single province | Province-specific state |

### Flag Check Pattern

```paradox
# Check before triggering
country_event = {
    id = 53004
    trigger = {
        tag = ENG
        NOT = { has_country_flag = already_done }
    }
    # ...
    option = {
        name = "A"
        set_country_flag = already_done
    }
}
```

---

## Pattern 5: Sphere of Influence Manipulation

### Use Case
Add/remove countries from sphere of influence, check sphere membership.

### Template

```paradox
country_event = {
    id = 54001
    title = "SPHERE.T"
    desc = "SPHERE.D"

    trigger = {
        tag = ENG
        is_greater_power = yes
    }

    mean_time_to_happen = {
        months = 12
    }

    option = {
        name = "SPHERE.A"

        # Add specific country to sphere
        POR = {
            add_to_sphere = THIS
        }

        # Add all countries in cultural union to sphere
        any_country = {
            limit = {
                is_cultural_union = yes
                cultural_union = THIS
                NOT = {
                    in_sphere = THIS
                }
            }
            add_to_sphere = THIS
        }

        # Add all neighbors to sphere
        any_neighbor_country = {
            limit = {
                is_greater_power = no
                NOT = { in_sphere = THIS }
            }
            add_to_sphere = THIS
        }
    }

    option = {
        name = "SPHERE.B"

        # Remove from sphere
        POR = {
            remove_from_sphere = THIS
        }

        # Remove all countries from sphere
        any_country = {
            limit = {
                in_sphere = THIS
            }
            remove_from_sphere = THIS
        }
    }
}
```

---

## Pattern 6: Grant Casus Belli

### Use Case
Grant a country a casus belli (CB) on another country with specific type and duration.

### Template

```paradox
country_event = {
    id = 55001
    title = "CB_GRANT.T"
    desc = "CB_GRANT.D"

    trigger = {
        tag = ENG
        owns = 2414
    }

    mean_time_to_happen = {
        months = 12
    }

    option = {
        name = "CB_GRANT.A"

        # Simple CB
        casus_belli = {
            target = FRA
            type = conquest
            months = 12
        }

        # CB with state target
        casus_belli = {
            target = GER
            type = acquire_state
            months = 18
            state_province_id = 1680
        }

        # Liberation CB
        casus_belli = {
            target = RUS
            type = free_peoples
            months = 24
            country = POL                     # Liberating Poland
        }
    }
}
```

### Common CB Types

| Type | Description | Peace Options |
|------|-------------|---------------|
| `conquest` | Take provinces | po_transfer_provinces |
| `acquire_state` | Take entire state | po_demand_state |
| `annex_core_country` | Annex if own all cores | po_annex |
| `liberate_country` | Release new country | po_release_puppet |
| `place_in_the_sun` | Colonial expansion | po_colony |
| `cut_down_to_size` | Dismantle military | po_dismantle_forts |
| `humiliate` | Prestige hit | po_humiliate |

---

## Pattern 7: Random Event from List

### Use Case
Event randomly selects one outcome from multiple possibilities.

### Template

```paradox
country_event = {
    id = 56001
    title = "RANDOM.T"
    desc = "RANDOM.D"

    trigger = {
        tag = ENG
    }

    mean_time_to_happen = {
        months = 24
    }

    option = {
        name = "RANDOM.A"

        # 50% chance of effect A
        random = {
            chance = 50
            prestige = 20
        }

        # 30% chance of effect B
        random = {
            chance = 30
            treasury = 1000
        }

        # 20% chance of effect C
        random = {
            chance = 20
            badboy = 5
        }
    }

    # Alternative: weighted random list
    option = {
        name = "RANDOM.B"

        random_list = {
            50 = {
                prestige = 20
            }
            30 = {
                treasury = 1000
            }
            20 = {
                badboy = 5
            }
        }
    }
}
```

---

## Pattern 8: Check All Neighbors

### Use Case
Event checks all neighboring countries and affects them based on conditions.

### Template

```paradox
country_event = {
    id = 57001
    title = "NEIGHBOR.T"
    desc = "NEIGHBOR.D"

    trigger = {
        tag = ENG
        any_neighbor_country = {
            limit = {
                is_greater_power = yes
                relation = {
                    who = THIS
                    value = -100
                }
            }
        }
    }

    mean_time_to_happen = {
        months = 12
    }

    option = {
        name = "NEIGHBOR.A"

        # Affect all GP neighbors with bad relations
        any_neighbor_country = {
            limit = {
                is_greater_power = yes
                relation = {
                    who = THIS
                    value = -100
                }
            }
            relation = {
                who = THIS
                value = -50
            }
            country_event = 57002          # Notify them
        }
    }
}
```

---

## Pattern 9: Province Modifier Duration

### Use Case
Apply a temporary modifier to a province with specific duration.

### Template

```paradox
country_event = {
    id = 58001
    title = "PROV_MOD.T"
    desc = "PROV_MOD.D"

    trigger = {
        tag = ENG
        owns = 2414
    }

    mean_time_to_happen = {
        months = 12
    }

    option = {
        name = "PROV_MOD.A"

        # Add modifier to specific province
        2414 = {
            add_province_modifier = {
                name = "industrial boom"
                duration = 365                # Days
            }
        }

        # Add modifier to all provinces in state
        capital_scope = {
            state_scope = {
                any_owned = {
                    add_province_modifier = {
                        name = "state_infrastructure"
                        duration = 730
                    }
                }
            }
        }

        # Add modifier to all coal-producing provinces
        any_owned = {
            limit = {
                trade_goods = coal
            }
            add_province_modifier = {
                name = "coal_boom"
                duration = 540
            }
        }
    }
}
```

---

## Pattern 10: Country Modifier Duration

### Use Case
Apply a temporary modifier to a country with specific duration.

### Template

```paradox
country_event = {
    id = 59001
    title = "COUNTRY_MOD.T"
    desc = "COUNTRY_MOD.D"

    trigger = {
        tag = ENG
        war = yes
    }

    mean_time_to_happen = {
        months = 6
    }

    option = {
        name = "COUNTRY_MOD.A"

        # Add country modifier
        add_country_modifier = {
            name = "war_economy"
            duration = 1095                   # 3 years in days
        }
    }
}
```

---

## Pattern 11: Assimilate POPs

### Use Case
Convert POPs to primary culture (assimilation).

### Template

```paradox
country_event = {
    id = 60001
    title = "ASSIMILATE.T"
    desc = "ASSIMILATE.D"

    trigger = {
        tag = ENG
        any_owned = {
            limit = {
                is_core = THIS
                any_pop = {
                    limit = {
                        is_primary_culture = no
                    }
                }
            }
        }
    }

    mean_time_to_happen = {
        months = 24
    }

    option = {
        name = "ASSIMILATE.A"

        # Assimilate all POPs in core provinces
        any_owned = {
            limit = {
                is_core = THIS
            }
            any_pop = {
                limit = {
                    is_primary_culture = no
                }
                # This effect changes POP to primary culture
                assimilate = yes
            }
        }

        # Alternative: Assimilate only specific cultures
        any_owned = {
            limit = {
                is_core = THIS
            }
            any_pop = {
                limit = {
                    culture = irish
                }
                assimilate = yes
            }
        }
    }
}
```

---

## Pattern 12: Move POP to Province

### Use Case
Move a POP from one province to another.

### Template

```paradox
country_event = {
    id = 61001
    title = "MOVE_POP.T"
    desc = "MOVE_POP.D"

    trigger = {
        tag = ENG
        any_pop = {
            limit = {
                culture = irish
                consciousness = 8
            }
        }
    }

    mean_time_to_happen = {
        months = 12
    }

    option = {
        name = "MOVE_POP.A"

        # Move all militant Irish POPs to capital
        any_pop = {
            limit = {
                culture = irish
                militancy = 7
            }
            move_pop = 2414                # Move to London
        }

        # Move POPs from one region to another
        any_owned = {
            limit = {
                region = ireland
            }
            any_pop = {
                limit = {
                    consciousness = 7
                }
                move_pop = {
                    capital_scope = {
                        this = this         # Move to capital
                    }
                }
            }
        }
    }
}
```

---

## Pattern 13: Change Province Owner

### Use Case
Transfer province ownership without secede_province effect.

### Template

```paradox
country_event = {
    id = 62001
    title = "CHANGE_OWNER.T"
    desc = "CHANGE_OWNER.D"

    trigger = {
        tag = ENG
        owns = 2414
    }

    option = {
        name = "CHANGE_OWNER.A"

        # Change owner and controller
        2414 = {
            owner = SCO
            controller = SCO
        }

        # Alternative: Scope to country
        SCO = {
            2414 = {
                owner = THIS
                controller = THIS
            }
        }
    }
}
```

---

## Pattern 14: Release Puppet/Vassal

### Use Case
Release a country as a puppet or independent nation.

### Template

```paradox
country_event = {
    id = 63001
    title = "RELEASE.T"
    desc = "RELEASE.D"

    trigger = {
        tag = ENG
        any_owned = {
            limit = {
                is_core = IRE
            }
        }
    }

    option = {
        name = "RELEASE.A"

        # Release as puppet
        release_vassal = IRE

        # Alternative: Full independence
        IRE = {
            release = IRE
        }

        # Alternative: Check if releasable first
        any_owned = {
            limit = {
                is_core = SCO
            }
            SCO = {
                release_vassal = THIS
            }
        }
    }
}
```

---

## Pattern 15: AI Weight Modifiers

### Use Case
Control AI decision-making with conditional weights.

### Template

```paradox
country_event = {
    id = 64001
    title = "AI_WEIGHT.T"
    desc = "AI_WEIGHT.D"

    trigger = {
        tag = ENG
    }

    mean_time_to_happen = {
        months = 12
    }

    option = {
        name = "AI_WEIGHT.A"
        ai_chance = {
            factor = 50                     # Base 50%

            modifier = {
                factor = 2                  # 2x if at war
                trigger = { war = yes }
            }

            modifier = {
                factor = 0.5                # 0.5x if GP
                trigger = { is_greater_power = yes }
            }

            modifier = {
                factor = 0                  # Never if pacifist
                trigger = {
                    nationalvalue = nv_pacifism
                }
            }
        }

        prestige = 10
    }

    option = {
        name = "AI_WEIGHT.B"
        ai_chance = {
            factor = 50

            modifier = {
                factor = 1.5
                trigger = { is_greater_power = yes }
            }

            modifier = {
                factor = 3
                trigger = {
                    treasury = 1000
                }
            }
        }

        treasury = 500
    }
}
```

---

## Quick Reference: Effect Patterns

| Pattern | When to Use |
|---------|-------------|
| `any_owned = { limit = { } effect = { } }` | Affect owned provinces matching condition |
| `any_country = { limit = { } effect = { } }` | Affect countries matching condition |
| `any_pop = { limit = { } effect = { } }` | Affect POPs matching condition |
| `TAG = { effect }` | Affect specific country |
| `PROV_ID = { effect }` | Affect specific province |
| `random = { chance = n effect = { } }` | n% chance of effect |
| `random_list = { n = { effect } }` | Weighted random selection |

---

## Quick Reference: Flag Patterns

```paradox
# Set flag
set_country_flag = flag_name
set_global_flag = flag_name
set_province_flag = flag_name

# Clear flag
clr_country_flag = flag_name
clr_global_flag = flag_name

# Check flag
has_country_flag = flag_name
has_global_flag = flag_name
has_province_flag = flag_name
```

---

## Quick Reference: Scope Patterns

```paradox
# Country to Province
country_event = {
    option = {
        capital_scope = {              # Scope to capital province
            life_rating = 5
        }
        any_owned = {                  # Scope to all owned provinces
            limit = { trade_goods = coal }
            fort = 1
        }
    }
}

# Province to Country
province_event = {
    option = {
        owner = {                      # Scope to owning country
            prestige = 10
        }
    }
}

# Country to Country
country_event = {
    option = {
        TAG = {                        # Scope to specific country
            relation = { who = THIS value = 50 }
        }
        any_country = {                # Scope to all countries
            limit = { is_greater_power = yes }
            diplomacy_influence = {
                who = THIS
                value = 10
            }
        }
    }
}
```

---

## See Also

- [QUICKSTART.md](QUICKSTART.md) - Step-by-step task workflows
- [Event_modding.md](Event_modding.md) - Event creation details
- [Decision_modding.md](Decision_modding.md) - Decision creation details
- [Full_list_of_effects.md](Full_list_of_effects.md) - All available effects
- [List_of_conditions.md](List_of_conditions.md) - All available triggers
- [Full_list_of_scopes.md](Full_list_of_scopes.md) - Scope switching reference
