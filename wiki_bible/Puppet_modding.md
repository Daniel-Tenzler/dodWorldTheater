---
title: Puppet modding
category: guide
tags: [diplomacy]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Puppet_modding
---

## Quick Reference

**File Location:** `history/diplomacy/puppetstates` (or `unions`)

**Puppet Structure:**
```paradox
vassal = {
    first = ENG          # Overlord (parent)
    second = GWA         # Puppet (child)
    start_date = 1836.1.1
    end_date = 1936.1.1
}
```

**Common Tasks:**
| Task | File | Effect/Command |
|------|------|----------------|
| Add starting puppet | `history/diplomacy/puppetstates` | `vassal = { first/second }` |
| Release puppet via event | Event effect | `release_vassal = POL` |
| Release independent | Event effect | `POL = { release = POL }` |
| Check puppet status | Trigger block | `vassal_of = TAG` / `is_substate = yes` |
| Annex puppet | Event effect | `annex = THIS` / `inherit = TAG` |
| Check overlord | Trigger block | `overlord = { tag = TAG }` |

**Puppet Types:**
| Type | Effect |
|------|--------|
| `vassal` (puppet) | Semi-independent, in sphere |
| `substate` | Similar to vassal but different mechanics |
| `dominion` | Some autonomy variations |

**Event Effects for Puppets:**
```paradox
# Release as puppet
release_vassal = POL

# Release as independent
POL = { release = POL }

# Annex puppet
annex = THIS        # If THIS is the puppet
inherit = POL       # If THIS is the overlord
```

**Common Pitfalls:**
- **Puppet not showing** → Check file is in `history/diplomacy/` folder
- **Wrong first/second** → `first` = overlord, `second` = puppet
- **Date issues** → `start_date` must be before bookmark date
- **Puppet too independent** → Check `vassal_of` vs `is_substate` differences

**See Also:**
- [QUICKSTART.md](QUICKSTART.md) - Task workflows
- [PATTERNS.md](PATTERNS.md) - Pattern 14: Release Puppet/Vassal
- [Full_list_of_effects.md](Full_list_of_effects.md) - Puppet effects
- [Sphere_modding.md](Sphere_modding.md) - Sphere of influence

---

This page documents the formatting and creation of puppets.

Creation of new puppet relationships

The files governing puppet relations are found within history\diplomacy. You are looking for the "unions" file and the "puppetstates" file. It does not matter which file you use, as long as it is within the correct folder.

Each relationship is made up of four informations:

first =
second =
start_date =
end_date =

You should note the overlord tag in first = and the puppet in second =. The start date should be before the intented start date. Any date before 1836.1.1 is just for flavour. If you intend the relationship to only be present for the 'American Civil War' scenario, use the start date 1861.1.1 instead. The end date does not have an effect, so just use 1936.1.1.

Example: 

vassal = {
	
first = ENG
	
second = GWA
	
start_date = 1836.1.1
	
end_date = 1949.1.1
}


This case creates the starting puppet relation between United Kingdom and Gwalior.
