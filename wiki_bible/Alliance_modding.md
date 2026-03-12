---
title: Alliance modding
category: guide
tags: [diplomacy]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Alliance_modding
---

## Quick Reference

**File Location:** `history/diplomacy/alliances`

**Alliance Structure:**
```paradox
alliance = {
    first = PEU           # First ally
    second = BOL          # Second ally
    start_date = 1836.1.1
    end_date = 1936.1.1
}
```

**Common Tasks:**
| Task | File | Effect/Command |
|------|------|----------------|
| Add starting alliance | `history/diplomacy/alliances` | `alliance = { first/second }` |
| Create alliance via event | Event effect | `create_alliance = { target = TAG }` |
| Break alliance via event | Event effect | `TAG = { break_alliance = THIS }` |
| Check alliance | Trigger block | `alliance_with = TAG` / `has_alliance_with = TAG` |
| Call to arms | Event effect | `war = { target = TAG type = cb_name called_by = THIS }` |

**Alliance Mechanics:**
- Allies are automatically called to defensive wars
- Can call allies to offensive wars (they may refuse)
- Alliance affects AI willingness to join wars
- Breaking alliance causes relations penalty

**Event Effects:**
```paradox
# Create alliance
create_alliance = {
    target = TAG
    mutual = yes    # Both directions
}

# Break alliance
TAG = { break_alliance = THIS }
```

**Common Pitfalls:**
- **Alliance not showing** → Check file is in `history/diplomacy/` folder
- **Order doesn't matter** - `first` and `second` are interchangeable
- **Date issues** → `start_date` must be before bookmark date
- **Not being called to war** - Check alliance type and CB

**See Also:**
- [QUICKSTART.md](QUICKSTART.md) - Task workflows
- [War_modding.md](War_modding.md) - War mechanics
- [Full_list_of_effects.md](Full_list_of_effects.md) - Alliance effects
- [Diplomacy keywords](KEYWORDS.md) - Diplomacy-related commands

---

This page documents the formatting and creation of alliances.

Creation of a new alliance

The file governing starting alliances are found within history\diplomacy. You are looking for the "alliances" file.

Each relationship contains four informations:

first =
second =
start_date =
end_date =

The two allies are described by tags in the lines first = and second =. It does not matter, which country tag you put in first and which you put in second. The start date should be before the intented start date. Any date before 1836.1.1 is just for flavour. If you intend the alliance to only be present in the 'American Civil War' scenario, use the start date 1861.1.1 instead. The end date does not have an effect, so just use 1936.1.1.

Example: 

alliance = {
	
first = PEU
	
second = BOL
	
start_date = 1836.1.1
	
end_date = 1949.1.1
}


This case creates the starting alliance between Peru and Bolivia.
