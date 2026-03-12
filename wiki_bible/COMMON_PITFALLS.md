---
title: Common Pitfalls in Victoria 2 Modding
category: guide
tags: [debugging, errors]
source: Modding Community
url: https://vic2.paradoxwikis.com/ (Community compilation)
---

# Common Pitfalls in Victoria 2 Modding

This page documents the most frequent errors that modders encounter when creating content for Victoria 2, along with solutions and prevention strategies.

## Quick Reference Table

| Error | Cause | How to Detect | How to Fix |
|-------|--------|---------------|------------|
| **Parse error: unexpected end of file** | Unbalanced braces (missing `}`) | Game won't load, error.log | Count `{` and `}`, ensure each has a matching pair |
| **Unknown token** | Typo in command name | error.log shows line number | Check spelling against reference docs |
| **Event doesn't fire** | Missing/wrong trigger conditions | Test in-game, console commands | Verify trigger block, use `debug showid` |
| **Missing localization** | Key not in CSV files | Text appears as `KEY_NAME` | Add to appropriate CSV file |
| **Province doesn't exist** | Invalid province ID | error.log, crash on load | Check `map/definition.csv` for valid IDs |
| **Event fires repeatedly** | Missing flag check | Event chains loop infinitely | Add `has_country_flag` or `has_global_flag` check |

---

## 1. Brace Balance Issues

### The Problem
Every opening brace `{` must have a corresponding closing brace `}`. This is the **#1 cause of parse errors**.

### Common Mistakes

```paradox
# WRONG - Missing closing brace
country_event = {
    id = 10001
    trigger = {
        tag = ENG
    # Missing } here!
    option = {
        name = "EVT_A"
    }
}
```

```paradox
# WRONG - Extra closing brace
country_event = {
    id = 10001
    trigger = {
        tag = ENG
    }
    option = {
        name = "EVT_A"
    }
}  # Extra } here!
```

### Prevention Strategy

1. **Count your braces** - Each `{` should have a matching `}`
2. **Use consistent indentation** - Each level of nesting gets one tab
3. **Close braces immediately** - Type `}` right after typing `{`, then fill in content

### Correct Template

```paradox
country_event = {
    id = 10001
    trigger = {
        tag = ENG
    }
    option = {
        name = "EVT_A"
    }
}
```

---

## 2. Missing Spaces Around `=`

### The Problem
Victoria 2's parser requires spaces around the `=` sign in most cases.

### Common Mistakes

```paradox
# WRONG - No spaces
tag=ENG
prestige=50

# WRONG - Space only on one side
tag =ENG
prestige= 50

# CORRECT - Spaces on both sides
tag = ENG
prestige = 50
```

### Prevention Strategy
Always format: `key = value` with spaces on both sides.

---

## 3. Province ID Validation

### The Problem
Using invalid province IDs causes the game to crash or fail to load.

### How to Check Valid Province IDs

1. Open `map/definition.csv`
2. Find valid province IDs (first column)
3. Province IDs are numeric (e.g., 1, 234, 1680, 2414)

### Common Mistakes

```paradox
# WRONG - Province doesn't exist
owns = 99999

# WRONG - Using tag instead of ID
owns = ENG

# CORRECT - Valid province ID
owns = 2414
```

### Prevention Strategy
- Always verify province IDs in `map/definition.csv`
- Use `debug showid` in console to see province IDs in-game
- Keep a list of commonly used province IDs for your mod

---

## 4. Localization Key Mismatches

### The Problem
Localization keys in events/decisions must exactly match keys in CSV files.

### Common Mistakes

```paradox
# In event file:
title = "EVT_10001_T"

# In localisation file (WRONG - different key)
EVT_10001_TITLE;Event Title;;;;;;;;;;;;

# In localisation file (CORRECT - exact match)
EVT_10001_T;Event Title;;;;;;;;;;;;
```

### Localization Key Naming Conventions

| Type | Format | Example |
|------|--------|---------|
| Event Title | `KEYNAME.T` | `EVT_10001.T` or `AMA1.T` |
| Event Description | `KEYNAME.D` | `EVT_10001.D` or `AMA1.D` |
| Event Options | `KEYNAME.A`, `KEYNAME.B`, etc. | `EVT_10001.A`, `EVT_10001.B` |
| Decision Title | `decision_name_title` | `form_germany_title` |
| Decision Description | `decision_name_desc` | `form_germany_desc` |

### Prevention Strategy
1. Define localization keys first, then reference them in code
2. Use consistent naming conventions
3. Double-check exact matches (including underscores)

---

## 5. Circular Event Chains

### The Problem
Events that trigger each other infinitely can freeze the game.

### Example of Circular Chain

```paradox
# Event 1 fires Event 2
country_event = {
    id = 10001
    option = {
        name = "A"
        country_event = 10002
    }
}

# Event 2 fires Event 1 (INFINITE LOOP!)
country_event = {
    id = 10002
    option = {
        name = "A"
        country_event = 10001
    }
}
```

### Solution: Use Flags

```paradox
# Event 1
country_event = {
    id = 10001
    trigger = {
        NOT = { has_country_flag = event_1_done }
    }
    option = {
        name = "A"
        set_country_flag = event_1_done
        country_event = 10002
    }
}

# Event 2
country_event = {
    id = 10002
    option = {
        name = "A"
        # No loop back to 10001
    }
}
```

---

## 6. MTTH vs is_triggered_only Confusion

### The Problem
Events that should fire randomly vs. events that should only be triggered by other events.

### is_triggered_only = yes
- Use this for events fired by:
  - Decisions
  - Other events
  - on_actions
- Event will **NEVER** fire randomly

### mean_time_to_happen
- Use this for events that should fire randomly
- Defines the average time until event fires (50% chance)
- **Must NOT** use `is_triggered_only = yes`

### Common Mistakes

```paradox
# WRONG - Trying to make triggered event random
country_event = {
    id = 10001
    is_triggered_only = yes
    mean_time_to_happen = { months = 12 }  # This will be ignored!
    option = { name = "A" }
}

# CORRECT - Random event (no is_triggered_only)
country_event = {
    id = 10001
    mean_time_to_happen = { months = 12 }
    option = { name = "A" }
}

# CORRECT - Triggered-only event
country_event = {
    id = 10001
    is_triggered_only = yes
    option = { name = "A" }
}
```

---

## 7. Scope Confusion

### The Problem
Using triggers/effects in the wrong scope (country vs. province vs. POP).

### Common Scope Mistakes

```paradox
# WRONG - Using country trigger in province scope
province_event = {
    id = 10001
    trigger = {
        is_greater_power = yes  # This is a country-only trigger!
    }
}

# CORRECT - Scope to country first
province_event = {
    id = 10001
    trigger = {
        owner = {
            is_greater_power = yes
        }
    }
}
```

### Scope Reference
- **Country scope**: `tag`, `prestige`, `is_greater_power`, etc.
- **Province scope**: `trade_goods`, `life_rating`, `fort`, etc.
- **POP scope**: `culture`, `religion`, `militancy`, `consciousness`, etc.

---

## 8. Missing Event Pictures

### The Problem
Events reference pictures that don't exist, causing the event to display no image.

### Common Mistakes

```paradox
# In event file:
country_event = {
    id = 10001
    picture = "my_custom_event"  # References gfx/pictures/events/my_custom_event.dds
    # ...
}

# But the file doesn't exist or is named differently
```

### Prevention Strategy
1. Place image files in: `gfx/pictures/events/`
2. Use `.dds` or `.tga` format
3. Reference without file extension: `picture = "filename"`
4. Verify file exists in the correct folder

---

## 9. Decision potential vs. allow Blocks

### The Problem
Confusion about when to use `potential` vs. `allow` blocks in decisions.

### Block Functions

| Block | Purpose | Checked When |
|-------|---------|--------------|
| `potential` | Makes decision visible | Constantly (determines if shown in UI) |
| `allow` | Enables taking decision | When player clicks decision |
| `effect` | What happens when taken | After decision is confirmed |
| `ai_will_do` | AI decision-making | When AI considers taking decision |

### Common Mistakes

```paradox
# WRONG - Putting everything in allow
decision = {
    potential = {
        # Empty - decision never visible!
    }
    allow = {
        tag = ENG
        is_greater_power = yes
    }
    effect = { ... }
}

# CORRECT - Split conditions properly
decision = {
    potential = {
        tag = ENG  # Decision visible to England
    }
    allow = {
        is_greater_power = yes  # Can only take if GP
    }
    effect = { ... }
}
```

---

## 10. Event ID Conflicts

### The Problem
Using an event ID that already exists in vanilla or other mods.

### Detection
- Check `error.log` for "duplicate event" warnings
- Events may not fire as expected
- Game may load wrong event text

### Prevention Strategy
1. Reserve ID ranges for your mod
2. Document reserved ranges
3. Check existing event IDs before adding new ones

### Recommended ID Ranges for Mods

| Range | Usage |
|-------|-------|
| 10,000 - 19,999 | Early game/tutorial (vanilla) |
| 33,000 - 39,999 | Regional mods (e.g., Arcadia) |
| 50,000 - 89,999 | Available for mods |
| 90,000 - 99,999 | Special/reserved |
| 98,000 - 98,999 | Amazonia region (dodWorldTheater) |

---

## Validation Checklist

Before finalizing any mod content, run through this checklist:

- [ ] All braces `{ }` are balanced
- [ ] All `=` have spaces on both sides
- [ ] Event IDs are unique
- [ ] All localization keys exist in CSV files
- [ ] Province IDs are valid (check `map/definition.csv`)
- [ ] Event chains don't create infinite loops
- [ ] Flags are set before being checked
- [ ] `is_triggered_only` is used correctly
- [ ] Scope switches are valid (country → province → POP)
- [ ] Event pictures exist in `gfx/pictures/events/`
- [ ] Decisions have both `potential` and `allow` blocks
- [ ] AI behavior defined with `ai_will_do` or `ai_chance`

---

## Debugging Tools

### Console Commands (Press `~` to open)

```bash
event [EVENT_ID] [TAG]        # Fire event for country
debug showid                  # Show province IDs on hover
debug fow                     # Toggle fog of war
debug yesmen                  # AI always accepts
```

### Log Files

Located in Victoria II root directory:
- **`error.log`** - Parse errors, unknown tokens
- **`game.log`** - Runtime errors
- **`history.log`** - History loading errors

---

## See Also

- [Event_modding.md](Event_modding.md) - Event creation guide
- [Decision_modding.md](Decision_modding.md) - Decision creation guide
- [List_of_conditions.md](List_of_conditions.md) - All available triggers
- [Full_list_of_effects.md](Full_list_of_effects.md) - All available effects
- [Full_list_of_scopes.md](Full_list_of_scopes.md) - Scope switching reference
