---
title: Casus belli modding
category: guide
tags: [diplomacy, war]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Casus_belli_modding
---

## Quick Reference

**File Location:** `common/cb_types.txt`

**CB Type Structure:**
```paradox
cb_name = {
    is_triggered_only = yes       # Can only be granted by events/decisions
    months = 12                   # CB validity duration

    can_use = {                   # Who can use this CB
        NOT = { is_our_vassal = THIS }
    }

    badboy_factor = 2.2           # Infamy cost multiplier (×10)
    prestige_factor = 5           # Prestige gained on success
    peace_cost_factor = 1         # War score cost modifier
    construction_speed = 0.5      # Fabrication speed (0.5 = 2x slower)

    on_add = {                    # Effect when CB is added
        move_issue_percentage = { from = jingoism to = pro_military value = 0.25 }
    }

    po_transfer_provinces = yes   # Peace options available
    war_name = WAR_CONQUEST_NAME  # War display name
}
```

**Common Tasks:**
| Task | File | Effect/Command |
|------|------|----------------|
| Add new CB | `common/cb_types.txt` | Add CB block |
| Grant CB via event | Event effect | `casus_belli = { target = TAG type = cb_name months = 12 }` |
| Check has CB | Trigger block | `has_casus_belli = { target = TAG type = cb_name }` |
| Declare war | Event effect | `war = { target = TAG type = cb_name }` |

**Available Peace Options (po_):**
| Option | Description |
|--------|-------------|
| `po_annex` | Annex target country |
| `po_demand_state` | Take entire state |
| `po_transfer_provinces` | Take specific provinces |
| `po_add_to_sphere` | Add to sphere of influence |
| `po_make_puppet` | Release as puppet |
| `po_release_puppet` | Release puppet as independent |
| `po_disarmament` | Reduce military capacity |
| `po_reparations` | Economic compensation |
| `po_remove_prestige` | Reduce target prestige |
| `po_status_quo` | End war with no changes |
| `po_install_communist_gov_type` | Change government to communist |
| `po_colony` | Colonial expansion |
| `po_remove_cores` | Remove core claims |

**Common CB Types in Vanilla:**
| CB | Description | Peace Options |
|----|-------------|---------------|
| `conquest` | Take provinces | po_transfer_provinces |
| `acquire_state` | Take entire state | po_demand_state |
| `annex_core_country` | Annex if own all cores | po_annex |
| `liberate_country` | Release new country | po_release_puppet |
| `place_in_the_sun` | Colonial expansion | po_colony |
| `cut_down_to_size` | Dismantle military | po_disarmament |
| `humiliate` | Prestige hit | po_remove_prestige |

**Common Pitfalls:**
- **CB not triggering** → Check `is_triggered_only = yes` (requires event to grant)
- **Wrong peace options** → Must include at least one `po_XXX = yes`
- **Infamy too high** → `badboy_factor` is multiplied by 10 (2.2 = 22 infamy)
- **War name not showing** → Must use valid `WAR_XXX_NAME` from localization

**See Also:**
- [QUICKSTART.md](QUICKSTART.md) - Task 5: Create a Casus Belli
- [Event_modding.md](Event_modding.md) - Granting CBs via events
- [War_modding.md](War_modding.md) - War mechanics
- [PATTERNS.md](PATTERNS.md) - Pattern 6: Grant Casus Belli

---

This page documents the how to edit casus belli and how to add new ones. The documents needed is cb_types.txt found in the Victoria 2 -> Common folder.

The file structure

The code for a casus belli should look like this:

conquest = {
	sprite_index = 2
	is_triggered_only = yes
	months = 12
	crisis = no
	
	can_use = {
		NOT = { is_our_vassal = THIS }
		NOT = { number_of_states = 5 }
		OR = {
			AND = {
				civilized = yes
				NOT = { number_of_states = 2 }
			}
			AND = {
				civilized = no
				THIS = { civilized = no }
				NOT = { number_of_states = 2 }
			}
			AND = {
				civilized = no
				number_of_states = 2
				THIS = {
					OR = {
						NOT = { is_greater_power = yes }
						NOT = { nationalism_n_imperialism = 1 }
					}
				}
			}
		}
		is_independant = yes
	}

	badboy_factor = 2.2
	prestige_factor = 5
	peace_cost_factor = 1
	penalty_factor = 1
	
	break_truce_prestige_factor = 5
	break_truce_infamy_factor = 2
	break_truce_militancy_factor = 2
	truce_months = 0
	
	good_relation_prestige_factor = 1
	good_relation_infamy_factor = 1
	good_relation_militancy_factor = 1
	
	construction_speed = 0.5
	
	on_add = {
		move_issue_percentage = { 
			from = jingoism 
			to = pro_military
			value = 0.25
		}
	}
	
	po_annex = yes
	
	war_name = WAR_CONQUEST_NAME
}


Sprite index refers to the icon. The number refers to a certain file in the gfx folder.

Common effects

Is_triggered_only and constructing_cb accepts the values yes and no. Together they define if the casus belli can be fabricated or not. Yes in is_triggered only and No in constructing_cb indicates that it only can be created by event. They default to yes

Months define the time this CB will be valid. Only works for triggered CBs. The default is 12 months.

The content in Can_use defines who the CB can be used against.

The badboy_factor defines the infamy cost of fabricating the casus belli. The infamy cost will be ten times the value so 2.2 in the example above means it costs 22 infamy.

the prestige_factor defines the amount of prestige earned by succesfully pressing this war goal.

peace_cost_factor defines the cost of the peace options in the peace treaty.

Construction speed defines how fast it is to fabricate said casus belli. It defaults to 1, which is the base construction speed. 0.5 means the constuction takes twice as long time, while 1.5 means it is 50% faster.

On_add defines the effect on the attacking country, when the casus belli is added as a secondary war goal.

War_name defines what the war will be called, when used for the first casus belli. if WAR_NAME is used, it means that this CB is only used as a second objective and thus cannot define the war name.

The po_XXX defines what the war goal actually is about. There is a set list of possible options. They are:

po_annex
po_demand_state
po_add_to_sphere
po_disarmament
po_reparations
po_transfer_provinces
po_remove_prestige
po_make_puppet
po_release_puppet
po_status_quo
po_install_communist_gov_type
po_uninstall_communist_gov_type
po_remove_cores
po_colony
Uncommon effects

Here is a list of effects that are only used in certain circumstances:

great_war_obligatory - cb is always added to the peace offer/demand in great wars.
po_remove_cores - Removes the cores from a province taken, mostly used in independence wars. may be used only with: po_transfer_provinces, po_demand_state, po_annex
crisis - accepts yes and no. Yes means that the CB can be offered as a wargoal in a crisis.
mutual - The CB effects will also be used by the defender in peace treaties. Mostly used in civil wars where both countries completely annex the other.
Infamy / Badboy

It is possible to change the limit of infamy it takes for the great powers to get a cut down to size casus belli in the defines.lua file (default is 25).
