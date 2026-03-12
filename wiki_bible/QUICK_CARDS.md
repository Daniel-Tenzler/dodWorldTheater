---
title: Victoria 2 Quick Reference Cards
category: guide
tags: [quick-reference, cheat-sheet]
source: Modding Community
url: https://vic2.paradoxwikis.com/ (Community compilation)
---

# Victoria 2 Quick Reference Cards

One-page reference cards for common Victoria 2 modding tasks. Print or keep these handy while working.

---

## 📋 Card 1: Event Syntax Quick Reference

### Basic Event Structure
```paradox
country_event = {
    id = 10001                    # Required: Unique ID
    title = "KEY.T"                # Required: Localization key
    desc = "KEY.D"                 # Required: Localization key
    picture = "name"                # Optional: Event picture

    trigger = {                    # Optional: When event can fire
        tag = ENG
        owns = 2414
    }

    mean_time_to_happen = {       # Random timing (remove if triggered_only)
        months = 120
    }

    is_triggered_only = yes        # Optional: Only fires when triggered

    option = {                     # Required: At least one option
        name = "KEY.A"             # Required: Option text key
        ai_chance = { factor = 50 } # Optional: AI behavior
        # Effects here...
    }
}
```

### Must-Have Components
- [ ] Unique `id`
- [ ] `title` and `desc` keys
- [ ] At least one `option` with `name`
- [ ] Balanced braces `{ }`
- [ ] Spaces around `=` signs

### Common Triggers
| Trigger | Purpose |
|---------|---------|
| `tag = TAG` | Specific country |
| `owns = PROV_ID` | Owns province |
| `controls = PROV_ID` | Controls province |
| `war = yes` | At war |
| `is_greater_power = yes` | Great Power |
| `prestige = X` | Minimum prestige |
| `has_country_flag = name` | Has flag |
| `NOT = { }` | Invert condition |

### Common Effects
| Effect | Purpose |
|--------|---------|
| `prestige = X` | Add prestige |
| `add_core = TAG` | Add core claim |
| `secede_province = TAG` | Transfer province |
| `country_event = ID` | Fire event |
| `set_country_flag = name` | Set flag |
| `change_tag = TAG` | Become country |
| `casus_belli = { }` | Grant CB |

---

## 📋 Card 2: Decision Syntax Quick Reference

### Basic Decision Structure
```paradox
political_decisions = {
    decision_name = {
        picture = "DecisionPicture"   # Optional

        potential = {                   # When visible
            tag = ENG
        }

        allow = {                      # When can take
            is_greater_power = yes
        }

        effect = {                     # What happens
            prestige = 20
        }

        ai_will_do = {                  # AI behavior
            factor = 1
        }
    }
}
```

### Block Functions
| Block | Purpose | Checked When |
|-------|---------|--------------|
| `potential` | Visibility | Constantly |
| `allow` | Requirements | On click |
| `effect` | Consequences | After taking |
| `ai_will_do` | AI weight | When AI decides |

### Common Potential Conditions
- `tag = TAG` - Only this country
- `NOT = { has_global_flag = done }` - Not already done

### Common Allow Conditions
- `is_greater_power = yes` - Must be GP
- `prestige = X` - Minimum prestige
- `war = no` - Must be at peace
- `all_core = { }` - Check all cores

### Localization Keys
- `decision_name_title` - Auto-generated
- `decision_name_desc` - Auto-generated

---

## 📋 Card 3: Scope Switching Quick Reference

### Country to Province
```paradox
country_event = {
    option = {
        # Scope to capital province
        capital_scope = {
            fort = 1
        }

        # Scope to all owned provinces
        any_owned = {
            limit = {
                trade_goods = coal
            }
            life_rating = 5
        }

        # Scope to specific province
        2414 = {
            add_core = TAG
        }
    }
}
```

### Province to Country
```paradox
province_event = {
    option = {
        # Scope to owning country
        owner = {
            prestige = 10
        }

        # Scope to controlling country
        controller = {
            relation = { who = THIS value = 50 }
        }
    }
}
```

### Country to Country
```paradox
country_event = {
    option = {
        # Scope to specific country
        ENG = {
            prestige = 10
        }

        # Scope to all countries
        any_country = {
            limit = {
                in_sphere = THIS
            }
            add_to_sphere = THIS
        }
    }
    }
}
```

---

## 📋 Card 4: MTTH Modifiers Quick Reference

### MTTH Structure
```paradox
mean_time_to_happen = {
    months = 120                    # Base MTTH

    modifier = {
        factor = 0.5                  # Halves MTTH (faster)
        trigger = { war = yes }
    }

    modifier = {
        factor = 2.0                  # Doubles MTTH (slower)
        trigger = {
            ruling_party = {
                ideology = liberal
            }
        }
    }
}
```

### MTTH Formulas
| Factor | Effect | Example |
|--------|--------|--------|
| 0.5 | 50% faster | event happens in 5 months instead of 10 |
| 2.0 | 50% slower | event happens in 20 months instead of 10 |
| 0.1 | 90% faster | Very fast trigger |
| 10.0 | 10x slower | Very slow trigger |

---

## 📋 Card 5: Common Boolean Patterns

### OR Pattern
```paradox
OR = {
    tag = GER
    tag = AUS                      # Germany OR Austria
}
```

### AND Pattern
```paradox
AND = {
    tag = GER
    is_greater_power = yes        # Germany AND is GP
}
```

### NOT Pattern
```paradox
NOT = {
    war = yes                      # NOT at war
}
```

### Complex Pattern
```paradox
OR = {
    tag = GER
    AND = {
        culture = north_german
        NOT = {
            continent = europe
        }
    }
}
```

---

## 📋 Card 6: Flag System Quick Reference

### Setting Flags
| Command | Scope | Duration |
|---------|-------|----------|
| `set_country_flag = name` | Single country | Until cleared |
| `set_global_flag = name` | All countries | Until cleared |
| `set_province_flag = name` | Single province | Until cleared |

### Clearing Flags
| Command | Effect |
|---------|--------|
| `clr_country_flag = name` | Remove country flag |
| `clr_global_flag = name` | Remove global flag |

### Checking Flags
| Command | Effect |
|---------|--------|
| `has_country_flag = name` | Has country flag |
| `has_global_flag = name` | Has global flag |
| `has_province_flag = name` | Has province flag |

---

## 📋 Card 7: Localization Quick Reference

### CSV Format
```csv
key;English;French;German;Polish;Spanish;Italian;Swedish;Czech;Hungarian;Dutch;Portuguese;Russian;Finnish;
```

### Key Naming Conventions
| Type | Format | Example |
|------|--------|---------|
| Event Title | `KEY.T` | `EVT_50001.T` |
| Event Description | `KEY.D` | `EVT_50001.D` |
| Event Option | `KEY.A`, `.B` | `EVT_50001.A` |
| Decision Title | `name_title` | `annex_tibet_title` |
| Decision Description | `name_desc` | `annex_tibet_desc` |

### Special Characters
- New line: `\n`
- Tab: `\t`
- Quote: `\"` or `''`

### Validation
- Exactly 14 semicolons per line
- File encoding: ANSI

---

## 📋 Card 8: File Location Quick Reference

| Task | File Location |
|------|---------------|
| Add event | `events/[filename].txt` |
| Add decision | `decisions/[filename].txt` |
| Add country definition | `common/countries/TAG - Name.txt` |
| Add country history | `history/countries/TAG - Name.txt` |
| Add province history | `history/provinces/[region]/ID - Name.txt` |
| Add localization | `localisation/[filename].csv` |
| Add CB type | `common/cb_types.txt` |
| Add technology | `technologies/[category]_tech.txt` |
| Add flag | `gfx/flags/TAG.tga` |
| Add event picture | `gfx/pictures/events/[name].dds` |

---

## 📋 Card 9: Debugging Quick Reference

### Console Commands
| Command | Effect |
|---------|--------|
| `event [ID] [TAG]` | Fire event for country |
| `debug showid` | Show province IDs on hover |
| `debug fow` | Toggle fog of war |
| `debug yesmen` | AI always accepts |
| `tag [TAG]` | Switch to play as country |
| `money [amount]` | Add money |
| `prestige [amount]` | Add prestige |
| `instantresearch` | Instant research |

### Log Files (Victoria II directory)
| File | Purpose |
|------|---------|
| `error.log` | Parse errors, unknown tokens |
| `game.log` | Runtime errors |
| `history.log` | History loading errors |

---

## 📋 Card 10: Common Validation Checks

### Before Testing
- [ ] All braces `{ }` balanced
- [ ] Spaces around `=` signs
- [ ] Event IDs are unique
- [ ] Localization keys exist
- [ ] Province IDs are valid
- [ ] Files use ANSI encoding
- [ ] CSV has 14 semicolons per line

### Common Parse Errors
| Error | Cause | Fix |
|-------|-------|-----|
| "Unexpected end of file" | Missing `}` | Count braces, add missing |
| "Unknown token" | Typo in command | Check spelling |
| "Unexpected token" | Missing space around `=` | Add spaces |
| "Duplicate event" | ID already exists | Change ID |

---

## See Also

- [QUICKSTART.md](QUICKSTART.md) - Step-by-step workflows
- [PATTERNS.md](PATTERNS.md) - Common patterns
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Symptom-based help
- [TEMPLATES.md](TEMPLATES.md) - Ready-to-use templates
