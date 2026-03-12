---
title: Modding Validation Checklist
category: guide
tags: [validation, testing, quality]
source: Modding Community
url: https://vic2.paradoxwikis.com/ (Community compilation)
---

# Victoria 2 Modding Validation Checklist

Use this checklist to verify your mod content before testing or releasing. Each section covers specific validation tasks with commands to help verify correctness.

## Pre-Flight Checklist (Before Testing)

### File Structure Verification

- [ ] **Mod file exists** (`.mod` file in mod directory)
  - [ ] `name = "Your Mod Name"` is set
  - [ ] `path = "mod/YourModFolder"` points to correct location
  - [ ] File uses `.mod` extension

- [ ] **Folder structure is correct**
  - [ ] `events/` folder exists for event files
  - [ ] `decisions/` folder exists for decision files
  - [ ] `localisation/` folder exists for CSV files
  - [ ] `common/` folder contains required files
  - [ ] `history/` folder contains history files

### Encoding Verification

- [ ] **All text files use ANSI encoding**
  - Victoria II requires ANSI for proper file reading
  - Use Notepad++ or similar to convert UTF-8 files to ANSI

---

## Event Validation

### Event Structure

For each event file, verify:

- [ ] **Event ID is unique**
  ```bash
  # Search existing events for duplicate IDs
  grep -r "id = [YOUR_EVENT_ID]" events/
  ```

- [ ] **Event has required fields**
  ```paradox
  country_event = {
      id = 10001              # Required
      title = "KEY.T"         # Required
      desc = "KEY.D"          # Required
      # picture = "name"      # Optional
      # trigger = { }         # Optional
      # mean_time_to_happen   # Optional
      # is_triggered_only     # Optional
      option = {              # At least one required
          name = "KEY.A"
      }
  }
  ```

- [ ] **Braces are balanced**
  - Count opening `{` and closing `}` braces
  - Each `option` block must be closed
  - `trigger` and `effect` blocks must be closed

- [ ] **Spaces around `=`**
  - `id = 10001` ✓
  - `tag = ENG` ✓
  - `prestige = 50` ✓
  - NOT: `id=10001` ✗

### Event Triggers

- [ ] **Trigger conditions are valid**
  - Check against [List_of_conditions.md](List_of_conditions.md)
  - All condition names are spelled correctly
  - Boolean logic is correct (AND/OR/NOT usage)

- [ ] **Trigger doesn't conflict with `is_triggered_only`**
  - If `is_triggered_only = yes`: MTTH is ignored (OK)
  - If `mean_time_to_happen` exists: Should NOT have `is_triggered_only`

### Event Options

- [ ] **Each option has a name**
  ```paradox
  option = {
      name = "EVT_10001_A"    # Required
      # Effects here...
  }
  ```

- [ ] **Option names follow naming convention**
  - `EVT_[ID]_A` for first option
  - `EVT_[ID]_B` for second option
  - `EVT_[ID]_C` for third option, etc.

- [ ] **AI has behavior defined**
  ```paradox
  option = {
      name = "EVT_10001_A"
      ai_chance = { factor = 50 }  # For country events
  }
  ```

### Event Effects

- [ ] **All effects are valid**
  - Check against [Full_list_of_effects.md](Full_list_of_effects.md)
  - Effect names are spelled correctly

- [ ] **Scope switching is correct**
  - Using appropriate scopes for target type
  - Check [Full_list_of_scopes.md](Full_list_of_scopes.md)

- [ ] **No circular event chains**
  - Event A → Event B → Event A (BAD!)
  - Use flags to prevent loops

### Event Localization

- [ ] **All localization keys exist**
  ```csv
  EVT_10001_T;Event Title;;;;;;;;;;;;
  EVT_10001_D;Event description text;;;;;;;;;;;;
  EVT_10001_A;First option;;;;;;;;;;;;
  EVT_10001_B;Second option;;;;;;;;;;;;
  ```

- [ ] **Keys match exactly**
  - Title key in code = key in CSV (exact match, including underscores)

- [ ] **Semicolon count is correct**
  - CSV format requires 14 semicolons per line
  - Format: `key;English;French;German;Polish;Spanish;Italian;Swedish;Czech;Hungarian;Dutch;Portuguese;Russian;Finnish;`

---

## Decision Validation

### Decision Structure

For each decision file, verify:

- [ ] **Decision is wrapped in correct block**
  ```paradox
  political_decisions = {
      your_decision = {
          # decision content
      }
  }
  ```

- [ ] **Decision has all required blocks**
  ```paradox
  your_decision = {
      potential = { }      # Required - makes visible
      allow = { }          # Required - enables taking
      effect = { }         # Required - what happens
      ai_will_do = { }     # Optional but recommended
  }
  ```

### Decision potential Block

- [ ] **`potential` block defines visibility**
  - Conditions that make decision appear in UI
  - Typically includes `tag = XXX` for country-specific decisions

- [ ] **Conditions are valid triggers**
  - Check against [List_of_conditions.md](List_of_conditions.md)

### Decision allow Block

- [ ] **`allow` block defines requirements**
  - Conditions that must be met to take decision
  - Checked when player clicks decision button

- [ ] **Conditions are valid triggers**
  - All trigger names are correct

### Decision effect Block

- [ ] **All effects are valid**
  - Check against [Full_list_of_effects.md](Full_list_of_effects.md)
  - Scope switching is correct

### Decision AI Behavior

- [ ] **`ai_will_do` block is defined**
  ```paradox
  ai_will_do = {
      factor = 1          # Base weight
      modifier = {
          factor = 2      # Conditional modifier
          trigger = { }
      }
  }
  ```

### Decision Localization

- [ ] **Localization keys exist**
  ```csv
  your_decision_title;Decision Name;;;;;;;;;;;;
  your_decision_desc;Decision description;;;;;;;;;;;;
  ```

- [ ] **Keys match decision name exactly**
  - Decision `annex_tibet` → keys `annex_tibet_title` and `annex_tibet_desc`

---

## Province Validation

### Province ID Verification

- [ ] **Province IDs are valid**
  ```bash
  # Check if province exists in definition.csv
  grep "^[PROVINCE_ID]," map/definition.csv
  ```

- [ ] **Province history files exist**
  - Format: `history/provinces/[region]/[ID] - Name.txt`
  - Example: `history/provinces/germany/1680 - Berlin.txt`

### Province History Files

- [ ] **Required fields are present**
  ```paradox
  owner = TAG              # Required
  controller = TAG         # Required
  # add_core = TAG        # Optional
  # trade_goods = good    # Optional
  # life_rating = 35      # Optional
  # terrain = plains      # Optional
  ```

- [ ] **Owner tag exists**
  - Check [Countries.md](Countries.md) for valid tags

- [ ] **Trade good is valid**
  - Check `common/goods.txt` for valid goods
  - Common goods: `grain`, `cotton`, `coal`, `iron`, `timber`, etc.

### Province References in Events/Decisions

- [ ] **Province IDs are valid**
  - All `owns = PROV_ID` use valid IDs
  - All `controls = PROV_ID` use valid IDs
  - All `PROV_ID = { }` scopes use valid IDs

---

## Country Validation

### Country Tag Verification

- [ ] **Country tags are valid**
  - 3-letter uppercase codes (ENG, FRA, GER, etc.)
  - Check [Countries.md](Countries.md) for vanilla tags

- [ ] **Country definition files exist**
  - `common/countries/TAG - Country Name.txt`

- [ ] **Country history files exist**
  - `history/countries/TAG - Country Name.txt`

### Country Definition Files

- [ ] **Required fields are present**
  ```paradox
  color = { R G B }        # Required - RGB color values
  graphical_culture = western  # Required
  # unit_names = { }      # Optional
  ```

### Country History Files

- [ ] **Required fields are present**
  ```paradox
  capital = PROV_ID        # Required
  primary_culture = culture    # Required
  religion = religion          # Required
  government = government_type # Required
  # civilized = yes/no         # Optional
  # prestige = X               # Optional
  # ruling_party = party_id    # Optional
  ```

---

## Localization Validation

### CSV File Format

- [ ] **CSV files use correct format**
  ```csv
  key;English;French;German;Polish;Spanish;Italian;Swedish;Czech;Hungarian;Dutch;Portuguese;Russian;Finnish;
  ```

- [ ] **File uses correct encoding**
  - ANSI encoding required
  - Convert from UTF-8 if necessary

- [ ] **Semicolon count is correct**
  - Exactly 14 semicolons per line
  - Last character is a semicolon

### Localization Key Verification

- [ ] **All referenced keys exist**
  ```bash
  # Find all keys used in events
  grep -E '(title|desc|name) = ' events/*.txt | sed 's/.*"\(.*\)".*/\1/' | sort -u

  # Verify each key exists in localisation
  grep -f <(above_command) localisation/*.csv
  ```

- [ ] **No duplicate keys**
  ```bash
  # Check for duplicate keys in CSV files
  cut -d';' -f1 localisation/*.csv | sort | uniq -d
  ```

---

## Script Syntax Validation

### Bracket and Brace Balance

- [ ] **All braces are balanced**
  ```bash
  # Count opening and closing braces
  grep -o '{' yourfile.txt | wc -l  # Opening braces
  grep -o '}' yourfile.txt | wc -l  # Closing braces
  # Numbers should match!
  ```

### Quote Balance

- [ ] **All quotes are balanced**
  ```bash
  # Count opening and closing quotes
  grep -o '"' yourfile.txt | wc -l  # Should be even number
  ```

### Space Around Equals Signs

- [ ] **All `=` have spaces**
  ```bash
  # Find lines without spaces around =
  grep -E '([^ ]=|=[^ ])' yourfile.txt
  # Should return nothing (or only false positives like "==")
  ```

---

## Testing Checklist

### Basic Load Test

- [ ] **Game launches without crashing**
  - No crash on startup
  - No crash on loading mod

- [ ] **No parse errors in error.log**
  - Check `error.log` in Victoria II directory
  - Should be empty or only contain known issues

### In-Game Testing

- [ ] **Events fire correctly**
  - Use console: `event [EVENT_ID] [TAG]`
  - Event displays with correct text
  - Options work as expected

- [ ] **Decisions appear**
  - Check decisions panel
  - Decision becomes visible under correct conditions
  - Decision can be taken when requirements met

- [ ] **Localization displays**
  - No `KEY_NAME` appearing in UI
  - All text displays correctly

- [ ] **No runtime errors**
  - Check `game.log` for errors during play

---

## Common Error Messages and Solutions

| Error Message | Cause | Solution |
|---------------|-------|----------|
| `Unexpected end of file` | Unbalanced braces | Count `{` and `}`, add missing `}` |
| `Unknown token` | Typo in command name | Check spelling, verify against reference |
| `Unexpected token` | Syntax error | Check for missing spaces around `=` |
| `Duplicate event` | Event ID already exists | Change to unique ID |
| `Missing localization` | Key not found in CSV | Add key to appropriate CSV file |
| `Invalid province` | Province ID doesn't exist | Check `map/definition.csv` for valid IDs |

---

## Automated Validation Script

Create a `validate_mod.sh` script:

```bash
#!/bin/bash

echo "=== Victoria 2 Mod Validator ==="

# Check for unbalanced braces
echo "Checking brace balance..."
for file in events/*.txt decisions/*.txt; do
    open=$(grep -o '{' "$file" | wc -l)
    close=$(grep -o '}' "$file" | wc -l)
    if [ $open -ne $close ]; then
        echo "WARNING: Unbalanced braces in $file ({$open vs }$close)"
    fi
done

# Check for missing spaces around =
echo "Checking spaces around =..."
grep -rn '[^ ]=[^ ]' events/*.txt decisions/*.txt | head -n 10

# Check for duplicate event IDs
echo "Checking for duplicate event IDs..."
grep -rh 'id = ' events/*.txt | sort | uniq -d

echo "=== Validation complete ==="
```

---

## See Also

- [COMMON_PITFALLS.md](COMMON_PITFALLS.md) - Common errors and how to fix them
- [Event_modding.md](Event_modding.md) - Event creation guide
- [Decision_modding.md](Decision_modding.md) - Decision creation guide
- [List_of_conditions.md](List_of_conditions.md) - All available triggers
- [Full_list_of_effects.md](Full_list_of_effects.md) - All available effects
