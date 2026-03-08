# Common Directory Documentation

This document provides an overview of each file in the `common/` directory of the Victoria II mod. The common directory contains core game data that defines fundamental game mechanics, entities, and rules.

## Directory Structure

The `common/` directory contains configuration files that establish the foundational systems of the game. These files define everything from economic systems to political ideologies, from military units to cultural groups.

## Core Configuration Files

### bookmarks.txt
**Purpose**: Defines starting scenarios for the game.

**Function**: Each bookmark represents a historical starting point that players can select when beginning a new game. Bookmarks include a display name, description, start date, and camera position on the map. This file allows players to jump into specific historical moments rather than always starting from the default date.

### buildings.txt
**Purpose**: Defines all constructible buildings in the game.

**Function**: This comprehensive file specifies every building type that can be constructed, including factories, military installations, and infrastructure. Each building definition includes:
- Construction requirements (goods, time, cost)
- Output and production types
- Maximum building levels
- Whether the building appears on the map
- Employment capacity and workforce needs

Buildings are organized into categories such as factories (basic, strategic, luxury, late-game), military structures (forts, naval bases), and infrastructure (railroads).

### countries.txt
**Purpose**: Maps all country tags to their definition files.

**Function**: This master registry connects three-letter country identifiers (tags) to their corresponding country definition files in the `countries/` subdirectory. The file is organized alphabetically and by region (Europe, Americas, Asia, Africa, etc.). It also defines dynamic dominion tags that can be generated during gameplay. Any new country must be registered here with a unique tag.

### country_colors.txt
**Purpose**: Defines the visual appearance of each country's military units.

**Function**: Each country entry contains three color values that determine the uniform colors for their military units on the map. These colors are used for visual distinction between nations during warfare and other military interactions. The file ensures that each country has a unique and historically appropriate military appearance.

### defines.lua
**Purpose**: Contains fundamental game constants and configuration settings.

**Function**: This is one of the most critical files, establishing the mathematical foundation of game mechanics. It defines:
- Time boundaries (start and end dates)
- Economic constants (tax efficiency, loan interest, tariff rates)
- Military parameters (supply limits, organization, reinforcement rates)
- Diplomatic settings (influence mechanics, colonial rules)
- Population dynamics (growth rates, promotion chances)
- Research and technology spread mechanics

Changes to this file have profound effects on game balance and pacing.

### production_types.txt
**Purpose**: Defines the economic production system.

**Function**: This file establishes how factories and Resource Gathering Operations (RGOs) function economically. It specifies:
- Factory templates with efficiency modifiers
- Input goods required and output goods produced
- Workforce composition (which POP types work where)
- Production bonuses and throughput calculations
- Owner effects on factory performance

Every economic activity in the game relies on these production definitions.

## Political and Social Systems

### governments.txt
**Purpose**: Defines all forms of government available in the game.

**Function**: Each government type specifies which political ideologies are allowed to hold power, whether elections occur, how ruling parties are selected, and which flag graphics to use. Government types range from democracies to various forms of dictatorship (proletarian, presidential, fascist, bourgeois) and monarchies (absolute, constitutional, HMG).

### ideologies.txt
**Purpose**: Defines political ideologies and their behavior regarding reforms.

**Function**: Each ideology has defined preferences for adding or removing political and social reforms. The file specifies:
- Ideology colors for UI display
- Historical availability dates
- Whether uncivilized nations can use the ideology
- Reform desire modifiers based on militancy and movement strength

Ideologies are grouped into categories (conservative, liberal, socialist, fascist) with distinct reform behaviors.

### issues.txt
**Purpose**: Defines political issues around which parties form.

**Function**: Issues represent political debates and policy positions. The file defines multiple issue categories:
- Trade policy (protectionism vs. free trade)
- Economic policy (laissez-faire, interventionism, state capitalism, planned economy)
- Religious policy, citizenship policy, and more

Each issue position has specific game effects and rules about what actions the government can take.

### national_focus.txt
**Purpose**: Defines national focus options that guide state development.

**Function**: National focuses are selected at the state level to provide bonuses and guide development. Categories include:
- Colonial policy (immigration, agriculture, mining)
- Immigration management
- Diplomatic actions (increasing tension)
- POP promotion (encouraging specific POP types)
- Production focus (specific goods and industries)
- Party loyalty building

Each focus has conditions for availability and specific effects on the targeted state.

### nationalvalues.txt
**Purpose**: Defines national values that countries can adopt.

**Function**: National values represent a country's fundamental priorities and provide nationwide modifiers. Options include:
- Order (military organization, reduced militancy)
- Liberty (immigration attraction, political consciousness)
- Equality (reduced militancy for non-accepted cultures)
- Tradition (social stability, ruling party support)
- Productivity (economic efficiency)
- Education (research and literacy)
- Diplomacy (influence and diplomatic actions)

Countries choose one national value that shapes their national character.

### rebel_types.txt
**Purpose**: Defines all types of rebellions that can occur.

**Function**: Each rebel type specifies:
- Trigger conditions for spawning
- Ideological or cultural motivations
- Behavior when they gain power (government changes)
- Whether they defect to other countries or seek independence
- Military behavior (reinforcement, tactics, unit transfers)
- How occupation strengthens their movement

Rebel types range from reactionary rebels seeking to restore traditional order to nationalist movements seeking independence.

## Population and Culture

### cultures.txt
**Purpose**: Defines all cultural groups in the game.

**Function**: Cultures are organized into culture groups with hierarchical relationships. Each culture definition includes:
- Visual color for map display
- First names for generated characters
- Surnames for generated characters
- Military unit graphics
- Leader culture group for armies

The file also defines cultural unions (e.g., Germany for Germanic cultures) which enable unification mechanics.

### religion.txt
**Purpose**: Defines all religions in the game.

**Function**: Each religion has an icon for UI display and a color for visual identification. Religions are grouped into broader categories (Christian, Muslim, etc.). The system supports religious-based mechanics and can define religious modifiers affecting POP behavior.

### crime.txt
**Purpose**: Defines crime types that can appear in provinces.

**Function**: Each crime type represents a negative condition that can affect a province. Crimes include modifiers for:
- Reduced economic output
- Political effects (voter manipulation, party support)
- Military impacts
- Social unrest (militancy, consciousness)

Each crime has defined triggers and can be actively present in a province, causing its effects until addressed.

### pop_types.txt
**Purpose**: Defines all population types (POPs) and their characteristics.

**Function**: Each POP type (aristocrats, capitalists, craftsmen, farmers, etc.) has defined:
- Promotion/demotion chances and conditions
- Which stratum they belong to (rich, middle, poor)
- Economic needs and behaviors
- Military service eligibility
- Voting rights

The promotion system determines how POPs change types based on literacy, militancy, life needs, and other factors.

## Economic System

### goods.txt
**Purpose**: Defines all tradeable goods and commodities.

**Function**: Each good is assigned:
- Base cost for economic calculations
- Visual color for UI
- Category (military, raw material, industrial, etc.)
- Starting availability

Goods are organized into categories that affect how they're used in production and trade.

### cb_types.txt
**Purpose**: Defines all Casus Belli (justifications for war).

**Function**: Each CB type specifies:
- Conditions for construction or triggering
- Available peace options
- Badboy and prestige modifiers
- Construction speed modifiers
- Whether it can be used in crises
- War goal priority in peace treaties

CBs range from simple conquest to liberation, puppet installation, and government change.

## Military and Leadership

### traits.txt
**Purpose**: Defines personality traits for military leaders.

**Function**: Each trait provides modifiers to:
- Attack and defense capabilities
- Morale and organization
- Movement speed
- Reconnaissance ability
- Attrition resistance
- Experience gain
- Reliability (affecting POP military satisfaction)

Traits are assigned to generals and admirals, shaping their leadership style and effectiveness.

## Event and Trigger Systems

### event_modifiers.txt
**Purpose**: Defines temporary and persistent modifiers that can be applied by events.

**Function**: Event modifiers are scriptable effects that can change game conditions. Examples include:
- Economic modifiers (tariff efficiency, research bonuses)
- Military effects (mobilization size, unit experience)
- Social changes (militancy, consciousness)
- Political impacts (ruling party support)

These modifiers are displayed with icons and can have duration limits or be permanent.

### triggered_modifiers.txt
**Purpose**: Defines conditional modifiers that are checked monthly.

**Function**: Triggered modifiers automatically apply when their conditions are met. They represent advantages or disadvantages based on:
- Geographic position (canal ownership)
- Political status (vassalage)
- Economic conditions
- Size and development level

These provide dynamic bonuses without requiring event intervention.

### on_actions.txt
**Purpose**: Defines event chains that trigger on specific game occurrences.

**Function**: This file schedules events to fire when particular actions happen, including:
- Time pulses (yearly, quarterly)
- Battle outcomes (won or lost)
- Country status changes (becoming/losing great power status)
- Elections
- Colonial conversions

The system ensures that historical and logical events occur in response to game conditions.

## Technical Notes

### Color Definition Format
Throughout the common files, colors are defined as RGB (Red, Green, Blue) values, typically ranging from 0-255 or expressed as decimal fractions (0.0-1.0).

### File Dependencies
Many files reference each other. For example:
- Countries defined in `countries.txt` must have corresponding definition files
- Production types reference goods defined in `goods.txt`
- POP types reference cultures defined in `cultures.txt`

Adding new content often requires updates across multiple files to maintain consistency.

### Scripting Language
The common files use Paradox's custom scripting language, which uses:
- Key-value pairs separated by equals signs
- Braces for grouping related data
- Hash marks (#) for comments
- Tab-based hierarchy for nested structures

## Modifying Common Files

When modifying common files:
1. **Backup originals** before making changes
2. **Test thoroughly** as changes affect core game mechanics
3. **Maintain consistency** across related files
4. **Consider balance** as numeric changes have cascading effects
5. **Document changes** for future reference

The common directory is the foundation of the mod; changes here affect nearly every aspect of gameplay and should be made with careful consideration of their systemic impacts.
