---
title: Victoria 2 Modding Troubleshooting Index
category: guide
tags: [debugging, errors, troubleshooting]
source: Modding Community
url: https://vic2.paradoxwikis.com/ (Community compilation)
---

# Victoria 2 Modding Troubleshooting Index

A symptom-based troubleshooting guide for Victoria 2 modding. Find your symptom, identify the likely cause, and jump to the solution.

## Table of Contents

- [Event Issues](#event-issues)
- [Decision Issues](#decision-issues)
- [Localization Issues](#localization-issues)
- [Province/Country Issues](#provincecountry-issues)
- [Syntax/Parse Errors](#syntaxparse-errors)
- [Game Crashes](#game-crashes)
- [Performance Issues](#performance-issues)

---

## Event Issues

| Symptom | Likely Cause | See |
|---------|--------------|-----|
| Event doesn't fire | Trigger conditions too restrictive | [Event_modding.md](Event_modding.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md#event-doesnt-fire) |
| Event fires repeatedly | Missing flag check | [Event_modding.md](Event_modding.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md#circular-event-chains) |
| Event fires instantly | MTTH too low or missing | [Event_modding.md](Event_modding.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md#mtth-vs-is_triggered_only) |
| Event text doesn't show | Localization key mismatch | [Localisation.md](Localisation.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md#localization-key-mismatches) |
| Event has no picture | Picture file missing/incorrect | [Event_picture_modding.md](Event_picture_modding.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md#missing-event-pictures) |
| Event options not working | Effects invalid or wrong scope | [Full_list_of_effects.md](Full_list_of_effects.md), [Full_list_of_scopes.md](Full_list_of_scopes.md) |
| Event chain loops | Circular reference without flags | [Event_modding.md](Event_modding.md), [PATTERNS.md](PATTERNS.md#pattern-4-event-chain-with-flags) |

---

## Decision Issues

| Symptom | Likely Cause | See |
|---------|--------------|-----|
| Decision not visible | `potential` block conditions not met | [Decision_modding.md](Decision_modding.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md#decision-not-visible) |
| Decision grayed out | `allow` block conditions not met | [Decision_modding.md](Decision_modding.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md#decision-potential-vs-allow-blocks) |
| Decision does nothing | `effect` block empty or invalid | [Full_list_of_effects.md](Full_list_of_effects.md), [Decision_modding.md](Decision_modding.md) |
| Decision can be taken infinitely | Missing flag check in `potential` | [PATTERNS.md](PATTERNS.md#pattern-1-country-unification-decision), [QUICKSTART.md](QUICKSTART.md#task-2-add-a-decision) |
| AI never takes decision | Missing or wrong `ai_will_do` | [Decision_modding.md](Decision_modding.md), [PATTERNS.md](PATTERNS.md#pattern-15-ai-weight-modifiers) |
| Decision text doesn't show | Localization key mismatch | [Localisation.md](Localisation.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md#localization-key-mismatches) |

---

## Localization Issues

| Symptom | Likely Cause | See |
|---------|--------------|-----|
| Text shows as `KEY_NAME` | Key not in CSV or mismatch | [Localisation.md](Localisation.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md#localization-key-mismatches) |
| Text cut off mid-sentence | Special characters not escaped | [Localisation.md](Localisation.md) |
| Wrong number of semicolons | CSV format error | [Localisation.md](Localisation.md), [VALIDATION_CHECKLIST.md](VALIDATION_CHECKLIST.md) |
| Text displays as gibberish | Wrong file encoding (not ANSI) | [FolderFile_overview.md](FolderFile_overview.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md) |
| Country name not showing | Missing country localization | [Localisation.md](Localisation.md), [QUICKSTART.md](QUICKSTART.md#task-3-create-a-new-country) |

---

## Province/Country Issues

| Symptom | Likely Cause | See |
|---------|--------------|-----|
| "Invalid province ID" error | Province doesn't exist | [Provinces.md](Provinces.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md#province-id-validation) |
| "Unknown country" error | TAG doesn't exist | [Countries.md](Countries.md), [Country_modding.md](Country_modding.md) |
| Province won't transfer | Wrong effect or ownership | [Full_list_of_effects.md](Full_list_of_effects.md), [PATTERNS.md](PATTERNS.md#pattern-2-province-transfer-via-event) |
| Core not adding | Province invalid or scope wrong | [Full_list_of_effects.md](Full_list_of_effects.md), [Full_list_of_scopes.md](Full_list_of_scopes.md) |
| Country not appearing | Missing definition or history file | [Country_modding.md](Country_modding.md), [QUICKSTART.md](QUICKSTART.md#task-3-create-a-new-country) |
| Wrong flag showing | Flag file missing or wrong flagType | [Flag_modding.md](Flag_modding.md), [Government_modding.md](Government_modding.md) |

---

## Syntax/Parse Errors

| Symptom | Likely Cause | See |
|---------|--------------|-----|
| "Unexpected end of file" | Unbalanced braces `{ }` | [COMMON_PITFALLS.md](COMMON_PITFALLS.md#brace-balance-issues), [VALIDATION_CHECKLIST.md](VALIDATION_CHECKLIST.md) |
| "Unknown token" error | Typo in command name | [Full_list_of_effects.md](Full_list_of_effects.md), [List_of_conditions.md](List_of_conditions.md) |
| "Unexpected token" error | Missing space around `=` | [COMMON_PITFALLS.md](COMMON_PITFALLS.md#missing-spaces-around-), [VALIDATION_CHECKLIST.md](VALIDATION_CHECKLIST.md) |
| "Duplicate event" error | Event ID already exists | [Event_modding.md](Event_modding.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md#event-id-conflicts) |
| File won't load | Wrong file extension/location | [FolderFile_overview.md](FolderFile_overview.md), [VALIDATION_CHECKLIST.md](VALIDATION_CHECKLIST.md) |

---

## Game Crashes

| Symptom | Likely Cause | See |
|---------|--------------|-----|
| Crash on startup | Missing required file/folder | [FolderFile_overview.md](FolderFile_overview.md), [VALIDATION_CHECKLIST.md](VALIDATION_CHECKLIST.md) |
| Crash on load | Parse error in any file | Check `error.log`, [COMMON_PITFALLS.md](COMMON_PITFALLS.md) |
| Crash during gameplay | Circular event chain or invalid scope | [COMMON_PITFALLS.md](COMMON_PITFALLS.md#circular-event-chains), [Full_list_of_scopes.md](Full_list_of_scopes.md) |
| Crash on hover | Province missing from definition | [Provinces.md](Provinces.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md#province-id-validation) |
| Crash with decisions | Decision file syntax error | [Decision_modding.md](Decision_modding.md), [VALIDATION_CHECKLIST.md](VALIDATION_CHECKLIST.md) |

---

## Performance Issues

| Symptom | Likely Cause | See |
|---------|--------------|-----|
| Long load times | Too many events checking every day | [Event_modding.md](Event_modding.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md) |
| Game slows down | Large event chains without flags | [PATTERNS.md](PATTERNS.md#pattern-4-event-chain-with-flags) |
| Lag during month | POP calculations or multiple checks | [Population_modding.md](Population_modding.md), [COMMON_PITFALLS.md](COMMON_PITFALLS.md) |

---

## Debugging Tools

### Console Commands (Press `~` to open)
```bash
event [EVENT_ID] [TAG]        # Fire event for country
debug showid                  # Show province IDs on hover
debug fow                     # Toggle fog of war
debug yesmen                  # AI always accepts
tag [TAG]                     # Switch to play as country
```

### Log Files (Victoria II directory)
- **`error.log`** - Parse errors, unknown tokens
- **`game.log`** - Runtime errors
- **`history.log`** - History loading errors

---

## Quick Fix Checklist

Before asking for help, verify:
- [ ] All braces `{ }` are balanced
- [ ] All `=` have spaces on both sides
- [ ] Event IDs are unique
- [ ] All localization keys exist in CSV files
- [ ] Province IDs are valid (check `map/definition.csv`)
- [ ] Event chains don't create infinite loops
- [ ] Flags are set before being checked
- [ ] `is_triggered_only` is used correctly
- [ ] Scope switches are valid
- [ ] Files are in correct folders

---

## See Also

- [COMMON_PITFALLS.md](COMMON_PITFALLS.md) - Detailed error explanations
- [VALIDATION_CHECKLIST.md](VALIDATION_CHECKLIST.md) - Complete validation guide
- [QUICKSTART.md](QUICKSTART.md) - Task 8: Debug Common Issues
- [Event_modding.md](Event_modding.md) - Event creation and debugging
- [Decision_modding.md](Decision_modding.md) - Decision creation and debugging
