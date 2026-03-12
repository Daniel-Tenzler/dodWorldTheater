---
title: Sphere modding
category: guide
tags: [diplomacy]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Sphere_modding
---

## Quick Reference

**File Locations:**
- `history/units/TAG_oob.txt` - 1836 sphere definitions
- `history/units/1861/TAG_oob.txt` - 1861 sphere definitions
- `history/countries/TAG - Name.txt` - References OOB files

**Sphere Structure (in OOB files):**
```paradox
TAG = {
    value = 125              # Relations (-200 to 200)
    level = 5                # Sphere level (0-5)
    influence_value = 25     # Unused influence points
}
```

**Sphere Levels:**
| Level | Opinion | Description |
|-------|---------|-------------|
| 0 | Hostile | Base enemy status |
| 1 | Opposed | Dislikes country |
| 2 | Neutral | Default (no influence) |
| 3 | Cordial | Friendly |
| 4 | Friendly | Very friendly |
| 5 | Sphere | In sphere of influence |

**Common Tasks:**
| Task | File | Effect/Command |
|------|------|----------------|
| Add country to sphere | `history/units/TAG_oob.txt` | `TARGET = { level = 5 }` |
| Add sphere via event | Event effect | `add_to_sphere = THIS` |
| Remove from sphere | Event effect | `remove_from_sphere = THIS` |
| Check sphere membership | Trigger block | `in_sphere = TAG` |
| Check sphere owner | Trigger block | `sphere_owner = { tag = TAG }` |
| Get influence | Event effect | `diplomacy_influence = { who = TAG value = 10 }` |

**Setting Up Starting Spheres:**
1. Create/edit `history/units/TAG_oob.txt` for GP
2. Add sphere member blocks:
```paradox
LIB = {
    value = 125
    level = 5              # 5 = in sphere
    influence_value = 25
}
```
3. Reference OOB in country history:
```paradox
# In history/countries/USA - United States.txt
oob = "USA_oob.txt"
```

**Common Pitfalls:**
- **Sphere not applying** → Check country history file references OOB
- **Wrong date folder** → 1836 uses root, 1861 uses `/1861/` folder
- **Level 5 not working** → Target must not be GP or in another sphere
- **OOB not loading** → File must be referenced in country history

**See Also:**
- [QUICKSTART.md](QUICKSTART.md) - Task workflows
- [PATTERNS.md](PATTERNS.md) - Pattern 5: Sphere of Influence
- [Full_list_of_effects.md](Full_list_of_effects.md) - Sphere effects

---

Sphere modding is the modding of historical spheres of influence in Victoria 2.

Files

The files you need to change this are in the history/units files. In vanilla Victoria 2, this folder will contain many files, they are usually in the format _oob, with 'oob' meaning 'order of battle'. These files are used to specify both the units and relations of a country in 1936, and can also be used to mod unit history. There will also be another folder, history/units/1861, the files in here are used the same, but in the 1861 starting date.

These files will not automatically work, but need to be specified in the history/countries file of the country. For example, the file ABU - Abu Dhabi.txt contains:

oob = "ABU_oob.txt" #'oob=' automatically refers to the 'history/units' folder, so you only need to specify the name of the file if the file is not in the '/1861' folder.


and

1861.1.1 = {
	oob = "/1861/ABU_oob.txt" #'oob=' automatically refers to the 'history/units' folder, so you have to add '/1861/' if the file is in the 'history/countries/1861' folder.
}


The first one is used for 1836, the second one for 1861. The first one doesn't really need to have a specified date, because the 1836 bookmark is the first bookmark. The second one does need to have a date specified.

Modding

Inside the files in the history/units and history/units/1861 folders, some countries will contain references to other countries. They look like this:

TAG = { #The tag of the country you want to sphere
	value = between -200 and 200 #This specifies the relation between the countries
	level = between 0 and 5 #specifies their opinion, '5' means that the country that uses this 'oob' file has a sphere over the country specified
	influence_value = from 0 #This specifies how much unused influence points that the country that uses this 'oob' file has over the country specified
}


For example, this is in the file USA_oob:

LIB = { #Liberia
	value = 125 #The USA and Liberia have relations of 125
	level = 5 #Liberia is in the sphere of the USA
	influence_value = 25 #The USA has 25 unused influence points that can be used on Liberia
}


Usually, you'll want to have the sphere in both bookmarks, and you'll have to mod the same thing in both of the _oob files.


Note: the levels determine the opinion, these are: 0 = hostile, 1 = opposed, 2 = neutral, 3 = cordial, 4 = friendly & 5 = sphere. 2 = neutral is the default option if influence is not specified.

Example

In this example, Spain will get a sphere over the Netherlands:

Inside the SPA_oob (and/or the 1861/SPA_oob) file, you have to add:

NET = { 
	value = 125 #You can choose anything, but 100 or 125 is usual.
	level = 5 #5 = sphere
	influence_value = 25 #25 is usual, but anything can be chosen.
}
