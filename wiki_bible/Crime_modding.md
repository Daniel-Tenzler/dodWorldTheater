---
title: Crime modding
category: guide
tags: [rebels]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Crime_modding
---

## Quick Reference

**File Location:** `common/crime.txt`

**Crime Structure:**
```paradox
crime_name = {
    pop_consciousness_modifier = 0.05  # Effect on province
    local_rgo_output = -0.1            # RGO output modifier
    life_rating = -0.02                # Life rating modifier
    icon = 1                           # Icon index (1-8)
    trigger = {                        # When crime can appear
        crime = no                     # No existing crime
        consciousness = 5              # Minimum consciousness
    }
}
```

**Common Tasks:**
| Task | File | Effect/Command |
|------|------|----------------|
| Add new crime | `common/crime.txt` | Add crime block |
| Modify crime effects | `common/crime.txt` | Edit modifier values |
| Add crime requirements | `common/crime.txt` | Add `trigger = { }` block |
| Trigger crime via event | Event effect | `PROV_ID = { trigger_crime = crime_name }` |
| Remove crime | Event effect | `PROV_ID = { remove_crime = yes }` |

**Vanilla Crime Types:**
| Crime | Effect |
|-------|--------|
| `anarchic_bomb_throwers` | +5% consciousness |
| `citizen_guard` | -2% life rating, -10% RGO output |
| `machine_oligarchy_destruction` | Various negative effects |
| `brotherhood_disciples` | Various effects |

**Crime Trigger Conditions:**
Common triggers include:
- `consciousness = X` - Minimum consciousness
- `literacy = X` - Minimum literacy
- `is_primary_culture = yes/no` - Culture restrictions
- `life_needs = X` - Life needs satisfaction
- `crime = no` - No existing crime in province

**Common Pitfalls:**
- **Crime not appearing** → Check `trigger = { }` conditions are met
- **Crime not clearing** → Need event/decision with `remove_crime = yes`
- **Wrong icon** → Icon must be 1-8 (crime icon strip)
- **Modifiers not working** → Use valid modifier names from `event_modifiers.txt`

**See Also:**
- [QUICKSTART.md](QUICKSTART.md) - Step-by-step workflows
- [Province_history_modding.md](Province_history_modding.md) - Province setup
- [Event_modding.md](Event_modding.md) - Crime via events
- [Modifier_effects.md](Modifier_effects.md) - All available modifiers

---

This page documents the how to edit to effects of crime effects and how to add new ones. The documents needed is crimes.txt found in the Victoria 2 -> Common folder.

Editing and creating Crime modifiers

This part details how you create a new national type of crime or edit an existing one.

The units in crime.txt document should look like this:

anarchic_bomb_throwers = {
	pop_consciousness_modifier = 0.05
	icon = 1	
	
	trigger = {
	}	
}

citizen_guard = {
	life_rating = -0.02
	local_rgo_output = -0.1
	icon = 2	
	
	trigger = {
	}		
}


This is an example of some of the existing types of crime modifiers. In total there should be 8 different types of crime modifiers. To create a new one, another at the bottom and put in the effects, you want.

Icons

The icon mentioned in to a file in the GFX folder.
