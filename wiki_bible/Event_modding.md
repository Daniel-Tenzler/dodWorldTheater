---
title: Event modding
category: guide
tags: [events]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Event_modding
---

## Quick Reference

**Key Commands:**
- `trigger = { }` - Conditions that must be met for event to fire
- `mean_time_to_happen = { months = X }` - Average time until event fires (50% chance)
- `is_triggered_only = yes` - Event only fires when triggered by other events/decisions
- `option = { name = "KEY.A" }` - Player choices (at least one required)

**Common Pitfalls:**
- Missing spaces around `=` (use `tag = ENG` not `tag=ENG`)
- Unbalanced braces `{ }` - every opening brace must have a closing brace
- Using both `is_triggered_only` and `mean_time_to_happen` (they conflict!)
- Circular event chains - use flags to prevent infinite loops

**Basic Event Template:**
```paradox
country_event = {
    id = 10001                    # Unique event ID
    trigger = {
        tag = ENG                 # Conditions to fire
    }
    mean_time_to_happen = {       # Remove if using is_triggered_only
        months = 12
    }
    title = "EVT_10001.T"         # Localization key for title
    desc = "EVT_10001.D"          # Localization key for description
    picture = "event_name"        # Optional: gfx/pictures/events/event_name.dds
    option = {
        name = "EVT_10001.A"      # Localization key for option
        ai_chance = { factor = 50 }
        # Effects here...
    }
}
```

**See Also:**
- [Decision_modding.md](Decision_modding.md) - Player-triggered decisions
- [List_of_conditions.md](List_of_conditions.md) - All available triggers
- [Full_list_of_effects.md](Full_list_of_effects.md) - All available effects
- [Full_list_of_scopes.md](Full_list_of_scopes.md) - Scope switching
- [COMMON_PITFALLS.md](COMMON_PITFALLS.md) - Common errors and solutions

---

This page will show how to create more advanced events, it is recommend to learn the basics first.


Using Boolean Combinations

Boolean commands are at their finest when combined with other Boolean commands. Consider the following:

OR = {
	tag = GER
	AND = {
		culture = north_german
		NOT = {
			continent = europe
		}
	}
}

This complex-looking string is actually quite simple.

We begin with the "or" command, which is the root command, stating that it will be satisfied if any one of the listed commands in its tier are satisfied.
We then have a simple "tag = " command, which simply checks if the country in question matches its own.
Now we have an "and" command, which demands that all of the commands listed in its tier be satisfied before it returns true.
Contained within this "and" command is a "culture = " command, this time demanding the primary culture of the country in question be North German.
Then, we have a "not" command, which demands that the country in question not be in Europe; that is, it must be on some other continent.


From all of this information, we can derive the meaning of this command. The command will return true if:

The country in question is Germany
OR
The country in question has North German as its primary culture and resides outside of the European continent


Using these Boolean commands, one could create immensely complex sets of requirements for events, decisions, and limits. Enjoy them, but be wary of creating scenarios so specific they will never be satisfied!

Using Flags

Flags can be used to select certain countries, but can also be used to say whether something has happened. A flag has no direct effect on the game, however it can have indirect effects, through other events. The following commands can be used for flags.

The flag effects:

set_country_flag = (name)

Sets country flag (name).


set_global_flag = (name)

Sets global flag (name).


clr_country_flag = (name)

Removes country flag (name).


clr_global_flag = (name)

Removes global flag (name).

The flag triggers:

has_country_flag = (name)

Returns true if the country has (name).


has_global_flag = (name)

Returns true if (name) is a global flag.

Using Scopes

Scopes are a way to switch the target between:

countries
Provinces
POPs

They can be used for example if a province event depends (partly or entirely) on the country that owns the province. Or if a POP is affected by a country event.

Using Variables

Variables are simple numbers that work like flags, so they do not directly influence the game, but through other events.

The variables effects:

set_variable = { 
	which = (name)
	value = n
}

Sets (name) to n.


change_variable = {
	which = (name)
	value = n
}

Adds n to (name).

The variables triggers:

check_variable = {
	which = "name"
	value = n
}

Returns true if (name) is more than n.


NOT = {
	check_variable = {
		which = "name"
		value = n
	}
}

Returns true if (name) is less than n.


The code above works fine for values that are above or below n, but to trigger when (name) ≈ n both codes are needed (see below).


check_variable = {
	which = "name"
	value = (n-0.01)
}
NOT = {
	check_variable = {
		which = "(name)"
		value = (n+0.01)
	}
}

Returns true if (name) ≈ n.

Mean Time To Happen
How to make an event fire randomly

If you want to make events happen randomly, you'll have to remove the line called

 is_triggered_only = yes 

From now on the event will be happening randomly, instead of having to be fired using on_actions, decisions or other events.

First, an event that can only be triggered by decisions:

country_event = {
	id = (id)

	trigger = {
		(trigger)
	}

	title = (title)
	desc = (desc)
	picture = (picture)

        is_triggered_only = yes

	option = {
		name = (name)
		(effect)
	}
}

And here is one that can happen randomly, note that the only_if_triggered line is gone:

country_event = {
	id = (id)

	trigger = {
		(trigger)
	}

	title = (title)
	desc = (desc)
	picture = (picture)

	option = {
		name = (name)
		(effect)
	}
}
Mean Time To Happen

This also brings a problem, because now the event will fire once every month, which is not what you want. To fix this problem you should use 'Mean Time To Happen'. This basically says over what time period the event will have a 50% chance of firing. If you want the event to only fire in a average of around every ten years, you can use this line of code:

mean_time_to_happen =  {
	months = 60
}

After the line is implemented (make sure the location you put it isn't inside the space of the trigger or one of the options).

This one will work:

country_event = {
	id = (id)

	trigger = {
		(trigger)
	}

        mean_time_to_happen  {
	        months = 12
        }

	title = (title)
	desc = (desc)
	picture = (picture)

	option = {
		name = (name)
		(effect)
	}
}

This one won't work, note that the line is put inside the option instead of directly in the event:

country_event = {
	id = (id)

	trigger = {
		(trigger)
	}

	title = (title)
	desc = (desc)
	picture = (picture)

	option = {
                mean_time_to_happen  {
	                months = 12
                }
		name = (name)
		(effect)
	}
}

This one will fire every month because there isn't a mean time to happen and there it isn't triggered:

country_event = {
	id = (id)

	trigger = {
		(trigger)
	}

	title = (title)
	desc = (desc)
	picture = (picture)

	option = {
		name = (name)
		(effect)
	}
}
Using a series of events

For large scaled events involving multiple countries it may be necessary to create a series of events. In such a serie one event will trigger other events either directly (triggered_only = yes and country_event = ) or indirectly (using variables, flags or modifiers). The Rock-Paper-Scissors is an example of an event serie.

Examples
Flag/Event Serie example: Rock-Paper-Scissors (RPS)

This example will show how flags can be used in an event serie to play RPS.


It is not a single event, but an event serie, each linked to another (see picture).


The event system of RPS.

It requires a starting event (1) which has no trigger, so it must be triggered by another event or manually.
The game requires 2 players:

player 1=ORGIN
player 2=TAG

TAG is the country that receives event 1 (the start).
ORGIN is the country chosen in event 1, either a country with flag ORGIN or a random country.


RPS events
