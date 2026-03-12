---
title: Religion modding
category: guide
tags: [culture]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Religion_modding
---

## Quick Reference

**Files to Modify:**
- `common/religion.txt` - Religion definitions
- `gfx/interface/icon_religion.dds` - Religion icons (32x32 pixels each)
- `gfx/interface/icon_religion_small.dds` - Small icons
- `interface/core.gfx` - Icon frame count definitions
- `interface/general_gfx.gfx` - Icon frame count definitions

**Religion Structure:**
```paradox
religious_group = {
    religion_name = {
        icon = 14                      # Icon index (0-based)
        color = { 0.5 0.0 0.0 }       # RGB 0.0-1.0 (not 0-255!)
        pagan = yes                   # Only for animist religion
    }
}
```

**Common Tasks:**
| Task | File | Effect/Command |
|------|------|----------------|
| Add new religion | `common/religion.txt` | Add religion block to group |
| Add religion to country | `history/countries/TAG - Name.txt` | `religion = religion_name` |
| Add religion to POPs | `history/pops/*.txt` | `religion = religion_name` |
| Check religion in triggers | Events/Decisions | `religion = protestant` / `is_state_religion = yes` |
| Change country religion | Event effect | `religion = protestant` |

**Important Notes:**
- **Color format is different** from cultures: RGB values are `0.0-1.0`, not `0-255`
- **Icons are 32x32 pixels** arranged horizontally in the icon file
- **Icon index is 0-based**: First icon is 0, second is 1, etc.
- **Must update frame counts** in `interface/core.gfx` and `interface/general_gfx.gfx` when adding icons

**Common Pitfalls:**
- **Wrong color format** → Use `0.0-1.0` for religions, not `0-255` like cultures
- **Icon not showing** → Update `noOfFrames` in interface files
- **Missing icon file** → Game will crash if icon index exceeds frame count
- **POP religion not updating** → Edit `history/pops/` files to set starting POP religions

**See Also:**
- [QUICKSTART.md](QUICKSTART.md) - Step-by-step workflows
- [Culture_modding.md](Culture_modding.md) - Adding cultures with religions
- [Country_modding.md](Country_modding.md) - Setting up countries
- [Population_modding.md](Population_modding.md) - POP religion and culture

---

To add a religion, you must make changes to several files: the religion definition file, the graphics file that holds religious icons, and the graphics definition file.

common/religion.txt

Found at common/religion.txt, the religions in the game are defined as religious groups and their constituent religions. Each religion has a defined icon and color. Note that the color is defined as an RGB value with values from 0 to 1, as opposed to 0 to 255. The color is used to represent said religion is pie charts.

pagan = {
	animist = {
		icon = 14
		color = { 0.5 0.0 0.0 }
		pagan = yes
		
	}
}

The pagan = yes is exclusive to the animist religion. It is unknown what this line does - perhaps it is just a remnant of Europa Universalis 3 code.

Graphics

The icons are are defined in files: gfx/interface/icon_religion.dds and gfx/interface/icon_religion_small.dds. The icons are 32 x 32 in size and are defined horizontally sequentially. The icon number in the religion definition relates directly to the elements in the graphical file.

The graphical files are being called from two interface definition files: interface/core.gfx and interface/general_gfx.gfx. If you add more religions to the game, you must also tell these interface files that the icon graphics is longer than they expect, to do this, simply find the places where the religious icons are being loaded and specify the exact number of "frames" are in the image.

spriteType = {
	name = "GFX_icon_religion_small"
	texturefile = "gfx\\interface\\icon_religion_small.tga"
	noOfFrames = 13
	loadType = "INGAME"
}
spriteType = {
	name = "GFX_icon_religion"
	texturefile = "gfx\\interface\\icon_religion.tga"
	noOfFrames = 14
	norefcount = yes
}

The question of why noOfFrames is smaller in the _small graphics file is left as an exercise for the reader.
