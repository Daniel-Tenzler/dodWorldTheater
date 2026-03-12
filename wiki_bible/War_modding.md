---
title: War modding
category: guide
tags: [diplomacy]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/War_modding
---

## Quick Reference

**File Location:** `history/wars/[filename].txt`

**War Structure:**
```paradox
war_name = {
    1836.1.1 = {
        add_attacker = TAG1         # Attacker side
        add_attacker = TAG2

        add_defender = TAG3         # Defender side
        add_defender = TAG4

        war_goal = {
            casus_belli = conquest   # CB type
            actor = TAG1            # Who added goal
            receiver = TAG3         # Target of goal
            state_province_id = 2414  # Required for acquire_state
            country = POL            # Required for free_peoples
        }
    }

    # Optional: End war later
    1836.6.1 = {
        rem_attacker = TAG1
        rem_defender = TAG3
    }
}
```

**Common Tasks:**
| Task | File | Effect/Command |
|------|------|----------------|
| Add starting war | `history/wars/*.txt` | `war_name = { date = { add_attacker/defender } }` |
| Declare war via event | Event effect | `war = { target = TAG type = cb_name }` |
| End war via event | Event effect | `TAG = { end_war = { target = TAG winner = THIS } }` |
| Add war goal | Event effect | `casus_belli = { target = TAG type = cb_name }` |
| Check at war | Trigger block | `war = yes` / `war_with = TAG` |
| Check war exhaustion | Trigger block | `war_exhaustion = X` |

**CB Types for Wars:**
| CB | Description | Peace Options |
|----|-------------|---------------|
| `conquest` | Take provinces | po_transfer_provinces |
| `acquire_state` | Take entire state | po_demand_state |
| `annex_core_country` | Annex if own all cores | po_annex |
| `liberate_country` | Release country | po_release_puppet |
| `humiliate` | Prestige hit | po_remove_prestige |

**Common Pitfalls:**
- **War not showing** → Check date is before bookmark date
- **Wrong actor/receiver** → Actor = war goal creator, receiver = target
- **Missing state_province_id** → Required for `acquire_state` CB
- **War not ending** → Use `end_war` effect to properly conclude

**See Also:**
- [QUICKSTART.md](QUICKSTART.md) - Task 5: Create a Casus Belli
- [Casus_belli_modding.md](Casus_belli_modding.md) - CB types
- [PATTERNS.md](PATTERNS.md) - Pattern 6: Grant Casus Belli
- [Full_list_of_effects.md](Full_list_of_effects.md) - War effects

---

This page documents the formatting and creation of wars which are currently ongoing on the start date.

Creation of a new wars

This part details how you create a new war at the start of the game. The file governing starting alliances are found within history\wars. You can use any of the files present or create a new txt-file.

Wars are declared like so:

name =
[date] = {
  add_attacker = 
  add_defender = 
  war_goal = { 
    casus_belli = 
    actor = 
    receiver = 
    state_province_id =
    country = 
  }
}


Under add_attacker and add_defender, you add all tags you wish to be on the offensive side and defensive of the war respectively. If you want more countries on each side, you can add multiple tags.

The start date should be before the intented starting scenario. The format is year.month.day. Any date before 1836.1.1 is just for flavour, but if you intend the war to only be present for the American Civil War scenario, use 1861.1.1 instead.

The actor defines who has added the war goal, and in case of province transfers, who will receive it. The receiver defines who will be the victim of the CB. The state province id field is only required if the casus belli specifically targets a specific state - for example, an acquire state casus belli. The country field is only required if the casus belli targets another country tag - for example, a free peoples casus belli.

The name is purely for flavour.

name = "Ottoman Restoration of Tripoli"
1835.10.2 = {
	add_attacker = TUR
	add_defender = TRI

	war_goal = {
		casus_belli = conquest
		actor = TUR
		receiver = TRI 
	}
}


This case creates the starting conquest war between Ottoman Empire and Tripoli.

For wars that start in an earlier start date but are ended in a later start date, or wars that only happened prior to the game start, you must ensure that the war end is specified in the file as well.

1836.4.21 = {
	rem_attacker = MEX
	rem_defender = TEX
}


This case ends a war between Mexico and Texas.
