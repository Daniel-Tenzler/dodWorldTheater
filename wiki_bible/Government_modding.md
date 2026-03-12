---
title: Government modding
category: guide
tags: [government, politics]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Government_modding
---

## Quick Reference

**File Location:** `common/governments.txt`

**Government Type Structure:**
```paradox
government_type = {
    liberal = yes              # Allowed ideologies
    socialist = yes
    conservative = yes
    reactionary = yes

    election = yes             # Has elections?
    duration = 48             # Months between elections (if yes)
    appoint_ruling_party = yes # Player can appoint ruling party
    flagType = monarchy        # Flag type: monarchy/republic/fascist/communist/other
}
```

**Common Tasks:**
| Task | File | Effect/Command |
|------|------|----------------|
| Add new government | `common/governments.txt` | Add government block |
| Set starting government | `history/countries/TAG - Name.txt` | `government = type_name` |
| Change government via event | Event effect | `government = democracy` |
| Trigger election | Event effect | `hold_election = yes` |
| Check government type | Trigger block | `government = democracy` |
| Reform lock/unlock | `common/issues.txt` | `allow = { }` blocks |

**All Government Types:**
| Type | Elections | Appoint Ruling Party | Flag Type | Ideologies Allowed |
|------|-----------|---------------------|-----------|-------------------|
| `absolute_monarchy` | No | Yes | monarchy | liberal, conservative, reactionary |
| `democracy` | Yes (48mo) | No | republic | All ideologies |
| `hms_government` | Yes (48mo) | Yes | monarchy | All ideologies |
| `prussian_constitutionalism` | Yes (48mo) | Yes | monarchy | liberal, socialist, conservative, reactionary |
| `presidential_dictatorship` | No | Yes | republic | reactionary, fascist, conservative |
| `bourgeois_dictatorship` | No | Yes | republic | anarcho_liberal |
| `fascist_dictatorship` | No | Yes | fascist | fascist |
| `proletarian_dictatorship` | No | Yes | communist | communist |
| `feudal_monarchy` | No | Yes | monarchy | conservative, reactionary |
| `theocracy` | No | Yes | - | reactionary, conservative |
| `merchant_republic` | Yes (48mo) | No | republic | liberal, socialist, conservative, reactionary |

**Flag Types:**
- `monarchy` → Uses `TAG_monarchy.tga`
- `republic` → Uses `TAG_republic.tga`
- `fascist` → Uses `TAG_fascist.tga`
- `communist` → Uses `TAG_communist.tga`
- `other` → Uses `TAG_other.tga`
- (none) → Uses `TAG.tga`

**Common Pitfalls:**
- **Wrong ideology in government** → Check party ideologies match government allowances
- **Election duration too short** → Must be at least longer than 6-month campaign
- **Flag file missing** → Game will crash if flag file doesn't exist
- **Government not set in history** → Countries start with random allowed government

**See Also:**
- [QUICKSTART.md](QUICKSTART.md) - Step-by-step workflows
- [Country_modding.md](Country_modding.md) - Setting up countries
- [Event_modding.md](Event_modding.md) - Government change events
- [PATTERNS.md](PATTERNS.md) - Common modding patterns

---

This file contains the list of all possible government types. For each government, it lists allowed parties, if there are elections, if appointing ruling parties is allowed and the flag type. For example:

prussian_constitutionalism = {
	liberal = yes
	socialist = yes
	conservative = yes
	reactionary = yes
	
	election = yes
	duration = 48
	appoint_ruling_party = yes
	flagType = monarchy
}

	[ideology] = yes 

Lists the ideologies of the parties that are allowed to be appointed to power, if the government form allows appointment. It has no effect in elections.

	elections = (yes/no)


Defines if the government form allows elections elections. Elections can happen by player action, the election effect, or regular elections, as follows.

	duration = X


If set the duration is the number of months between the end of an election and the beginning of the next electoral campaign. Keep in mind that the election campaign itself takes 6 months.

	appoint_ruling_party = (yes/no)


This defines if the player (the AI never uses this) can change the ruling party manually.

	flagType = (monarchy/republic/fascist/communist/other)


Chooses the flag type for the government. If none is selected then the TAG.tga flag in gfx/flags is used. The other default flags are TAG_monarchy.tga, TAG_republic.tga, TAG_fascist.tga, TAG_communist.tga, but any can be added, as long as all countries have a TAG_other.tga file. Note that the flag choice here can be overridden by the country file in history/countries.

The starting government of each country can be set in the country history files.

See Also
Government types
How to make a country
