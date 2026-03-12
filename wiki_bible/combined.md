# Victoria 2 Modding Bible (Combined)

> All scraped wiki documentation in one file. See [MODDING_OVERVIEW.md](../MODDING_OVERVIEW.md) for an index.

---

---
title: Alliance modding
category: guide
tags: [diplomacy]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Alliance_modding
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


---

---
title: Bookmark modding
category: guide
tags: [utility]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Bookmark_modding
---

This page documents the formatting and creation of bookmarks.

What does a bookmark look like?

Bookmarks are found within bookmarks.txt.

bookmark =
{
	name = "(bookmark)_NAME"    #defined in localization
	desc = "(bookmark)_DESC"    #defined in localization
	date = (yyyy.m.d)
	cameraX = (x)               #Starting camera distance, in pixels, from left side of provinces.bmp
	cameraY = (y)               #Starting camera distance, in pixels, from top side of provinces.bmp
}


example, from vanilla:

bookmark =
{
	name = "GC_NAME"    
	desc = "GC_DESC"    
	date = 1836.1.1     
	cameraX = 2950      
	cameraY = 1550      
}


This creates a bookmark on January 1, 1836 that has the camera centered on Europe.

Creating a new bookmark

There are a number of steps required when creating a new bookmark to ensure it works properly:

It must be defined in bookmarks.txt
Its date must be within the range of "start_date" and "end_date" in defines.lua
There must be a corresponding pops folder defining the population for that date
If the bookmark is the earliest date, all undated province and history data will belong to it by default. You will have to manually change those to the later dates
If the bookmark is a later date, the default province and history data will be used as well. You must manually define the data for later dates


---

---
title: Building modding
category: guide
tags: [economy]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Building_modding
---

Buildings (forts, naval bases, railroads and factories) are defined in this file. Factories act fundamentally different than the three others, since they are build at state level, while the other is build on province level.[1]

Syntax
fort = {      
	type = fort
	goods_cost =
	{
		lumber = 100
		cement = 100
		explosives = 50
		small_arms = 50
		artillery = 40
	}
	time = 1080 
	visibility = yes
	onmap = yes
	max_level = 6
	province = yes
	fort_level = 1
}
naval_base = {    
	type = naval_base
	cost = 15000
	goods_cost =
	{
		timber = 50
		lumber = 50
		cement = 100
		steel = 100
		machine_parts = 1
	}
	time = 1080
	naval_capacity = 1
	capital = yes
	onmap = yes
	port = yes
	visibility = yes
	max_level = 6
	colonial_points = { 30 50 70 90 110 130 } #points at levels 1-6
	province = yes
	one_per_state = yes
	colonial_range = 50
	local_ship_build = -0.10
}

Cost and goods cost

The goods_cost field determines what goods the state must buy to build this building. These values are static. The cost field for buildings defines an extra money cost that will be applied on top of the money cost calculated based on the goods the building costs. Interestingly, this extra cost scales with level so if cost = 1500, level 1 will cost 1500, level 2 will cost 3000 and so on. In the base game, only the naval base makes use of this field.

Time

Time defines how long it takes to build said building.

Pop build factory

The Pop_build_factory = (yes/no) determines if capitalists can build said building via investment.

Max level

Max level determines how many levels of a building can be build. The default is 6 for province buildings and 99 for factories. These can be changed by the modder easily, as the effects and costs would just scale.

Specific for Province buildings

The province = (yes/no) defines if the building can be build once per state (like naval bases) or once pr province.

Province buildings can generally have any modifier effect that an event modifier can possess, but there is a significant limitation: for most of them, the building may only have one (the last defined one being the one that counts). Another issue is that although the modifier effects do work for the province buildings, and they do show up properly in the tooltips of the province itself, they do not show up in other tooltips where they should.

Specific for factories

The actual goods the factory produces is defined by the production_type = (production_type) Production types are defined in production_types.txt, which defines production formulae for both factories and artisans.

fabric_factory = {
	type = factory
	on_completion = factory
	completion_size = 0.2
	max_level = 99
	goods_cost =
	{
		machine_parts = 20
		iron = 200
		cement = 200
	}
	time = 365
	visibility = yes
	onmap = no

	production_type = fabric_factory
	pop_build_factory = yes
}

Limitations and requirements
not_if_x_exists

The not_if_x_exists field determines which other buildings impede this one from being constructed. It has been confirmed to work for province buildings, but it is unknown if it works for factories. It is not actually used in the base game.

Syntax:

not_if_x_exists = { n }

where n is the name of the province building to be incompatible with this one

Note that although this works correctly, the interface tooltip will have an issue. It will display the name of the building to be constructed itself, rather than the one blocking it. It is possible to alter the localisation tag (BUILDING_BLOCKED_BY) to refer to a particular building, however.

prerequisites

The prerequisites field is almost the mirror opposite to not_if_x_exists. It defines which other buildings any necessary in the province before this one can be constructed. The field has been tested and confirmed to work for province buildings; whether it works for factories is unknown. It is not actually used in the base game.

Syntax:

prerequisites = { n }

where n is the name of the province building to be required

Note that although the requirement works correctly, the displayed text does not. For example, if you create a university building and make it require a school, the displayed text will nevertheless be "Must have University", rather than "Must have School". No way is currently known to fix this, as in the relevant localisation tag (BUILDING_MUST_HAVE), the "$OTHER$" is interpreted by the game as referring to the name of the building to be constructed itself, rather than the prerequisite. It is possible to change that localisation tag to directly refer to the name of a particular building, however.

Misc

It is possible to create new types province buildings in addition to the three in the game, but it is trickier than modding the existing three. This is because it also requires modding the interface. Otherwise the game would crash when you click on a province.

Another issue is that the AI will not build new province buildings by itself, so you will need to create special events or decisions for it to construct the new buildings.

Notes

While Naval bases can only be build once pr state, they are still build in one specific province and have province specific effects, which makes them a province building.


---

---
title: Casus belli modding
category: guide
tags: [diplomacy, war]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Casus_belli_modding
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


---

---
title: Countries
category: other
tags: [country, reference]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Countries
---

Please help create and format strategy guides according to the National strategy guides. Note that nations marked with (1861–P) are able to be played at the beginning of 1861, (1861–R) are able to be released at the beginning of the 1861 start date, (V2) are specific to the original Victoria 2 game, (AHD) is specific to the A House Divided expansion, and (HOD) is specific to the Heart of Darkness expansion. Jan Mayen, besides the colonial dominions, is the only new country in Heart of Darkness. Behind the country name is its TAG used for modding and console commands.

Maps
The political situation of The Grand Campaign bookmark, January 1st, 1836.
The political situation of the A House Divided bookmark, July 1st, 1861.


Great powers
 United Kingdom (ENG)
 France (FRA)
 Prussia (PRU)
 Russia (RUS)
 Austria (AUS)
 United States of America (USA)
 Ottoman Empire (TUR)
 Spain (SPA)
Secondary powers
 Belgium (BEL)
 Brazil (BRZ)
 Denmark (DEN)
 Mexico (MEX)
 Netherlands (NET)
 Portugal (POR)
 Sardinia-Piedmont (SAR)
 Sweden (SWE)
Minor civilized powers
Europe
 Greece (GRE)
 Ionian Islands (ION)
 Krakow (KRA)
 Luxembourg (LUX)
 Moldavia (MOL)
 Montenegro (MON)
 Serbia (SER)
 Switzerland (SWI)
 Wallachia (WAL)
Germany
 Anhalt (ANH)
 Baden (BAD)
 Bavaria (BAV)
 Braunschweig (BRA)
 Bremen (BRE)
 Frankfurt am Main (FRM)
 Hamburg (HAM)
 Hannover (HAN)
 Hesse-Darmstadt (HES)
 Hesse-Kassel (HEK)
 Holstein (HOL)
 Lippe-Detmold (LIP)
 Lübeck (LUB)
 Mecklenburg (MEC)
 Nassau (NAS)
 Oldenburg (OLD)
 Saxe-Coburg-Gotha (COB)
 Saxe-Meiningen (MEI)
 Saxe-Weimar (WEI)
 Saxony (SAX)
 Württemberg (WUR)
Italy
 Lucca (LUC)
 Modena (MOD)
 The Papal States (PAP)
 Two Sicilies (SIC)
 Parma (PAR)
 Tuscany (TUS)
North America
 Haiti (HAI)
 Texas (TEX)
 United States of Central America (UCA)
South America
 Argentina (ARG)
 Bolivia (BOL)
 Chile (CHL)
 Colombia (CLM)
 Ecuador (ECU)
 Paraguay (PRG)
 Peru (PEU)
 Uruguay (URU)
 Venezuela (VNZ)
Africa
 Oranje (ORA)
 South African Republic/Transvaal (TRN)
Releasable or formable civilized nations
Europe
Releasable
 Albania (ALB)
 Armenia (ARM)
 Azerbaijan (AZB)
 Belarus (BYE)
 Bosnia-Herzegovina (BOS)
 Bohemia-Moravia (BOH)
 Bulgaria (BUL)
 Catalonia (CAT)
 Crete (CRE)
 Croatia (CRO)
 Danzig (DZG)
 Estonia (EST)
 Finland (FIN)
 Flanders (FLA)
 Georgia (GEO)
 Hungary (HUN)
 Iceland (ICL)
 Ireland (IRE)
 Jan Mayen (JAN) HOD
 Latvia (LAT)
 Lithuania (LIT)
 Lombardia (LOM)
 Norway (NOR)
 Ruthenia (RUT)
 Schleswig (SCH)
 Scotland (SCO)
 Siebenbürgen (SIE)
 Slovakia (SLV)
 Slovenia (SLO)
 Trieste (TRE)
 Ukraine (UKR)
 Wallonia (WLL)
 Venice (VEN)
Formable countries (some are releasable as well)
 Austria-Hungary (KUK)
 Byzantine Empire (BYZ)
 Czechoslovakia (CZH)
 Germany (GER)
 Italy (ITA)
 Poland (POL)
 Poland-Lithuania (PLC) (1861–R)
 Romania (ROM)
 Scandinavia (SCA)
 South German Federation (SGF)
 United Baltic Nations (UBD)
 Yugoslavia (YUG)
North America
 Californian Republic (CAL)
 Canada (CAN)
 Columbia (COL)
 Confederate States of America (CSA)
 Costa Rica (COS)
 Cuba (CUB)
 Deseret (DES)
 Dominican Republic (DOM) (1861–P)
 El Salvador (ELS) (1861–P)
 Guatemala (GUA) (1861–P)
 Honduras (HON) (1861–P)
 Manhattan Commune (MAN)
 Metis Confederacy (MTC) (1861–R)
 New England (NEN)
 Newfoundland (NEW)
 Nicaragua (NIC) (1861–P)
 Quebec (QUE)
South America
Releasable
 Panama (PNM)
Formable countries (some are releasable as well)
 Gran Colombia (GCO) AHD
Africa
 South Africa (SAF)
 Southern Rhodesia (RHO)
Asia
Releasable
 Cyprus (CYP)
 Israel (ISR)
 Philippines (PHI)
Formable countries (some are releasable as well)
 Arabia (ARA)
 Babylon (BAB)
 India (HND)
Oceania
 Australia (AST)
 New Zealand (NZL)
Uncivilized nations
North America
 Hawaii (HAW)
Africa
 Aldjazair (ALD) V2
 Algeria (ALD) AHD
 Egypt (EGY)
 Ethiopia (ETH)
 Liberia (LIB)
 Madagascar (MAD)
 Morocco (MOR)
 Sokoto (SOK)
 Tripoli (TRI)
 Tunis (TUN)
 Zulu (ZUL)
Asia
 Abu Dhabi (ABU)
 Afghanistan (AFG)
 Atjeh (ATJ)
 Bali (BAL)
 Bhutan (BHU)
 Brunei (BRU)
 Bukkhara (BUK)
 Burma (BUR)
 Cambodia (CAM)
 China (CHI)
 Dai Nam (DAI)
 Hedjaz (HDJ)
 Japan (JAP)
 Johore (JOH)
 Kalat (KAL)
 Khiva (KHI)
 Kokand (KOK)
 Korea (KOR)
 Luang Prabang (LUA)
 Makran (MAK)
 Nejd (NEJ)
 Nepal (NEP)
 Oman (OMA)
 Persia (PER)
 Siam (SIA)
 Sikkim (SIK)
 Tibet (TIB)
 Yemen (YEM)
India
 Awadh (AWA)
 Bastar (BAS)
 Beroda (BER)
 Bikaner (BIK)
 Bhopal (BHO)
 Bundelkhand (BUN)
 Gwalior (GWA)
 Hyderabad (HYD)
 Indore (IND)
 Jaisalmer (JAS)
 Jaipur (JAI)
 Jodhpur (JOD)
 Kutch (KUT)
 Mewar (MEW)
 Mysore (MYS)
 Nagpur (NAG)
 Orissa (ORI)
 Panjab (PAN)
 Sindh (SIN)
 Travancore (TRA)
Chinese substates
 Guangxi (GXI) AHD
 Manchuria (MCK) AHD
 Mongolia (MGL)
 Qinghai (XBI) AHD
 Xinjiang (XIN) AHD
 Yunnan (YNN) AHD
Releasable uncivilized nations
Europe
 Crimea (CRI)
North America
 Cherokee (CHE)
Africa
 Congo (or Congo Free State) (CNG)
 Natalia (NAL)
 Zanzibar (ZAN)
Asia
 Heavenly Kingdom (TPG)
 Iraq (IRQ)
 Java (JAV)
 Kashmir (KAS) (1861–P)
 Ladakh (LAD)
 Mughalistan (MUG)
 Shimla (SHI)
 Wiang Chhan (WIA)
China (only Vanilla)
 Guangxi Clique (GXI) V2
 Manchukuo (MCK) V2
 Shanxi Clique (SXI) V2
 Xibei San Ma (XBI) V2
 Xinjiang Clique (XIN) V2
 Yunnan Clique (YNN) V2


---

---
title: Country modding
category: guide
tags: [country]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Country_modding
---

This guide will direct you through the process of creating a new country. The guide assumes that the culture of said nation already exists. If you want to create a whole new culture, check out culture modding. The guide contains information for both countries that will be on the map upon starting a new game and countries who can be released by their current owner or formed through another country waging war on the owner with the wargoal "Free ____ in ____" This guide will make Byelorus a playable nation as an example.

Finding the Files

The first step is to find the files you will be editing. They are in the Victoria 2 folder. Go to My Computer and access your C: Drive. Open up program files (or program files x86) If the game is bought on steam, it is under Steam --> steamapps --> Common --> Victoria 2 if you downloaded the game off of Steam, but if not it will be under the Paradox Interactive folder. It is strongly recommended that you make a back-up somewhere on you computer. Let's choose to edit the files in the Victoria 2 folder in program files. Rename the one on your desktop something that will let you know it is a backup. Open up the folder in the Paradox Interactive/Steamapps folder and begin.

Summary

Minimum required to add country and ensure no crashes when loading the game:

Victoria 2\common\countries.txt --#list of country tags to load into game
Victoria 2\common\countries\country name.txt --#country parties and common names
Victoria 2\history\countries\TAG - Country Name.txt --#country culture, govt, policies, techs
Victoria 2\gfx\flags\TAG.tga --#don't forget TAG_monarchy, TAG_fascist, TAG_communist, and TAG_republic versions of your flag
Victoria 2\history\provinces --#edit province txt files you want to own, console command "provid" can show province ID in game or Provinces

Additional changes:

Victoria 2\history\units\TAG_oob.txt --#starting units
Victoria 2\gfx\flags\flagfiles.txt --#also edit flagfiles_monarchy.txt, flagfiles_fascist.txt, flagfiles_communist.txt, and flagfiles_republic.txt
Victoria 2\localisation\text.csv #localization file, use notepad to edit; if you use open office or notepad++, make sure you open and save it in ANSI encoding (also called Windows-1252)
Creating the Country
Defining the tag

The country tag is a three letter acronym that the game uses to refer to a specific country. It is used in everything from national events to cores to the starting location of units. The convention is to use an acronym to easily remember it, but it can technically be anything.

In the Victoria 2 folder, find the folder named "common" and open it. First open the .txt file (NOT THE FOLDER) named "countries". It is advised to either find the category that the country you are trying to make best fits into or to create an entire new category just for your own nations. The placement of the line does not make a difference for the game files. It is only for your sake.

For Byelorus, let's go with # Eastern Europe. Create a new line somewhere in the block and type a three letter tag. The tag must be three upper case letters. It cannot be taken by another country (For example "Belarus" can't use BEL as that is already taken by [Belgium]).[1] Ctrl-F and type in the tag you chose to verify that your tag is not already taken. The tag "BYE" is not. Then hit the tab key twice and type following the format of the lines above: = "countries/Byelorus.txt" Save and close this document. This makes the game now that the information of the tag BYE is defined is the byelorus.txt file.

The country file

Now go back and find the folder named countries. Inside will be .txt files of every playable country in the game. It is possible to create the file from the bottom but for your first attempt it is suggested to simply copy the country most similar to the one you aim to make and work from there. For Byelorus - let's go with Russia.

The colour

The first line is the country's color - what shows up on the political map.

color = { 47 91 18 }

It's in RGB format, if you are familiar with it. If not, the first number is red, the second green, and the third blue. The numbers are a scale of 0 to 255; 0 being devoid of that color, 255 being the highest amount. Play around until you find what you want, or copy the numbers from a "custom color selection" in MS Paint.

Graphical culture

The second line is the Graphic culture. This defines the pictures and troops models used.

graphical_culture = RussianGC
Political parties

The third section defines the political parties which will exist in the country. If they are not listed here, they will not exist.

party = {
	name = "RUS_conservative"
	start_date = 1830.1.1
	end_date = 1905.1.1

	ideology = conservative

	economic_policy = interventionism
	trade_policy = protectionism
	religious_policy = moralism
	citizenship_policy = residency
	war_policy = jingoism
}

The name refers to a line in the localisation files. The name can be changed alternatively be changed by editing the names directly in the countries.txt file.

name = "Belarussian Nationalist Party"

Lastly it is actually also possible to refer to the name of another country's party by choosing a tag and adobt that nations parties. E.g. one can adopt Chiles parties if one makes a Spanish nation. This only adopts the name, they are still two separate entities.

If you want more parties with the same ideology they are commonly called "RUS_liberal_2"

The country's history file

Now go into the "history" folder and find the files named TAG - Name e.g. RUS - Russia. These files deals with the conditions for the country at the start of the game. By default they are used for the 1836 scenario. If you want a specific thing to be different in the 1861 scenario, this has to be specified. When not specifiec, the conditions are inherited from the 1836 scenario. Again you can build your own or copy of another one and rename it to BYE - Byelorus.

Capital

The first line defines the capital.

capital = 994

The number refers to a file in the history - provinces map. The information on any province can be found in the victoria2/history/province folder. Each province is saved as a file under the corresponding province number.

Look up the province number for the province you want to be the capital of your country. For Byelorus we can use Minsk, which is 718.

Cultures
primary_culture = russian
culture = byelorussian
culture = ukrainian


Next section defines the primary and secondary cultures. The words are always lowercase and refers to the entities in the cultures.txt file. There must be one and only one primary culture, but you can have as many or as few accepted cultures as your want. If you want no additional accepted cultures, the line can be omitted. One can also add by writing culture = [name]. Let's go with byelorussian as primary and Russian as secondary.

Religion
religion = orthodox

This defines the national religion. The text must be lower case. It refers to one of the 14 religions defined in the religion.txt document.

Government form
See Also: Governments.txt
government = absolute_monarchy

This defines the starting government form. This has little to no effect, if the country doesn't start the game as independent.

Plurality
plurality = 25

This defines the starting plurality of the country. The scale goes from 0 to 100.

National Value
See also: National value modding
nationalvalue = nv_order

This defines which of the three national values the country will have; Liberty, Order or Equality as they are defined in the nationalvalues.txt file. Simply put in the one you find most fitting.

Literacy

Under national value you will find literacy.

literacy = 0.10
non_state_culture_literacy = 0.03

This is a scale from 0.01 to 1.0 interpreted as a percentage. It can be a little tricky to mess with, because it overlaps with information from the provinces files as well as other countries. Non state culture literacy refers to the literacy of non-accepted Pops. It is not required, if you do not want it to be different from the main culture.

Rank, prestige and status

There can potentially be a line defining status and/or if the country is civilized or not.

civilized = yes

If omitted it will default to no.

prestige = 80

This defines the starting prestige of the country. There are no upper limit, and it has no effect if the country doesn't exist at the start of the game. If you are in doubt about which value to put, you can compare with a similar country. For Belarus we can match Denmark as an example and go with 5.

Reforms
Political and Social Reforms

The next block defines the starting reforms of the country. This also has effect when the country is released peacefully. If ommitted it will default to the most regressive type of reform.

slavery = no_slavery
upper_house_composition = appointed
vote_franschise = none_voting
public_meetings = yes_meeting
press_rights = state_press
trade_unions = no_trade_unions
voting_system = first_past_the_post
political_parties = underground_parties

wage_reform = no_minimum_wage
work_hours = no_work_hour_limit
safety_regulations = no_safety
health_care = no_health_care
unemployment_subsidies = no_subsidies
pensions = no_pensions 
school_reforms = no_schools


It is important to get the spelling and underscores absolutely correct. If you want to change it, it is advised to copy a line or two from another country which has the reforms, you want. The titles '# political reforms' and '# social reforms' are only comments and does not strictly have an effect. It is suggested to keep them though for your own overview's sake.

Westernization reforms

Westernization reforms can also be added for uncivilized nations.

foreign_training = yes_foreign_training
foreign_weapons = yes_foreign_weapons
land_reform = yes_land_reform


As it defaults to no reform, if you do not want your country to start with a certain reform, you do not have to add anything. For already westernized countries these lines will have no effect.

Starting political situation
ruling_party = RUS_conservative
upper_house = {
	fascist = 0
	liberal = 19
	conservative = 60
	reactionary = 21
	anarcho_liberal = 0
	socialist = 0
	communist = 0
}

The first line defines which party is in power at the start of the game. It refers to the parties, you have already created in the country file.

The second line sets the starting upper house. The scale is a percentage from 0.0 to 100. Make sure to only use integers (numbers without decimals) and that it adds up to 100.

Technologies and inventions

The next block can look overwhelming, but it actually fairly simple.

post_napoleonic_thought = 1
flintlock_rifles = 1
bronze_muzzle_loaded_artillery = 1
military_staff_system = 1
army_command_principle = 1
post_nelsonian_thought = 1
clipper_design = 1
naval_design_bureaus = 1
alphabetic_flag_signaling = 1
the_command_principle = 1
classicism_n_early_romanticism = 1
late_enlightenment_philosophy = 1
malthusian_thought = 1
enlightenment_thought = 1
introspectionism = 1
private_banks = 1
no_standard = 1
early_classical_theory_and_critique = 1
guild_based_production = 1
water_wheel_power = 1
publishing_industry = 1
mechanized_mining = 1
basic_chemistry = 1

#Inventions
#corvettes = yes
commerce_raiders = yes


Both inventions and technologies is a boolean value. Meaning it has to be either 0 or 1 and yes or no. You can simply see '1' as a yes and '0' as a no. Each line refer to either a technology or an invention. If the value is either 1 or yes, the country will start with said tech/invention. If you don't want a certain tech to be researched you don't have to put anything, as the boolean value defaults to 0/no.

This does not have any effect, if the country doesn't exists at game start.[2]

Consciousness
consciousness = 3
nonstate_consciousness = 1

This defines the starting consciousness. First line is in all integrated states and the second line is in colonies.

Tech School
schools = culture_tech_school

This defines the starting tech school. If the country is not independent at the start of the game, it has no effect and can be omitted.

OOB

The OOB (Order of Battle) defines the placement of troops, relations, influence among other things. The actual values we will get to later. Here we will simply refer to the correct file.

oob = "RUS_oob.txt"
1861.1.1 = {
	oob = "/1861/RUS_oob.txt"

There are one for each of the two start dates in the game. If the country is not independent at the start of the game, it has no effect and can be omitted. Change the RUS to BYE. If you don't Byelorus will start with the same amount of troops in the same places as Russia! Save and close this document.

Bringing your Country into Existence

Now comes the fun part. Making your country exist! Go into the history folder again and open up the province folder. Find the category your country falls in, Byelorus would be in Soviet. The search bar works well if you want a specific province e.g. Minsk. It is recommended that you keep a list of Province ID's nearby for this. A complete list can be found here: Provinces.

The provinces files
Main article: province history modding

Find any province that you want Byelorus to control at the start of the game or potentially own upon being released by Russia or have cores for. (Byelorus' modern day borders are 936 to 939 - but you can modify them however you like. Let's go with 936 - Grodno.

owner = RUS
controller = RUS
add_core = RUS
add_core = POL
add_core = PLC
add_core = BYE


Owner defines who owns the province at the start of the game. Controller defines who has occupied it. If the two tags are the same, the province will start unoccupied. This is only really relevant if you want to start with your country at war or fighting rebels. The "add_core =" adds the specified tag as a core. For Belarus we can add "add_core = BYE". Byelorus now has a core in Grodno. If you want Byelorus to be simply releasable by Russia, this is enough. If you want it to exist on the starting map of the grand campaign, then change the owner and controller from RUS to BYE. Save and close the document and move to the next one. Repeat. Congrats, using this information you should now be able to modify borders at the game start and add cores to provinces! Woo!

The controller, owner and cores can be set completely independently of each other - you can own a province you don't have a core on and vice versa.

Unfortunately each province is stored as a separate file, so for especially large countries this can take a while. Luckily, provinces that border each other tend to have numbers next to each other. So a good bet is that all the provinces you are looking for are the same place.

Like with the country history file, if you want the cores or ownership to be different in the 1861 scenario, this has to be specified. When not specified, the conditions are inherited from the 1836 scenario.

OOB
Sphere of Influence and relations
Main article: Sphere modding

If you want your country to start with certain relations with another nations, a level of influence or in a sphere it has to be editted in the OOB-file. Liek previously mentioned, you have in the country - history file created the link to a certain file, you will have to create.

SWE = {

	value = 125
	level = 3 	
	influence_value = 40


This example is Russias starting relations with Sweden

The TAG is of course the country being sphered (the sphere leader is defined by the file it self). Value refers to the relation. It can be set to any value between -200 and 200. Level refers to the 6 different levels of influence (In Sphere, Friendly, Cordial, Neutral, Opposed, Hostile). 5 is in a sphere while 0 is hostile. Influence_value refers to any additional influence. It goes on a scale from 0 to 100. If you do not put any values for a country it will default to 0 relation, 0 influence and neutral influence level.

If you want your new country to start in the sphere of influence of another country, you will have to found their particular oob.file. Maybe you find it realistic, that Byelorus is in the sphere of influence of Russia at the start of the game. To do this, go in the history folder again and then in the folder units. Find the file named RUS_oob.txt. In this file you can find all starting influence of a country.

Leaders

The next section defines which/if the country starts with any leaders. Each seperate block is a single leader

leader = {
	name = "Prince Vasilchikov"
	date = 1801.1.1
	type = land
	personality = competent
	background = powerful_friends
	prestige = 0.4
}


type (land/sea) defines the leader as a general or admiral. Personality and background refers to the values defined in the traits.txt document.

If you want your country to start without any leaders, simply do not have this section.

Starting troops

If you want, you also can create starting troops for Byelorus. To create them, copy the RUS_oob.txt file and rename it to BYE_oob.txt.

regiment = {
		name= "2.1-ya Gvardeiskaya Pekhotnaya Diviziya"
		type = infantry
		home = 946
	}

	regiment = {
		name= "3.1-ya Gvardeiskaya Pekhotnaya Diviziya"
		type = infantry
		home = 1006
	}

	regiment = {
		name= "1.2-ya Gvardeiskaya Pekhotnaya Diviziya"
		type = infantry
		home = 1008
	}

	regiment = {
		name= "2.2-ya Gvardeiskaya Pekhotnaya Diviziya"
		type = infantry
		home = 343
	}

	regiment = {
		name= "3.2-ya Gvardeiskaya Pekhotnaya Diviziya"
		type = artillery
		home = 718
	}

	regiment = {
		name= "1.3-ya Gvardeiskaya Pekhotnaya Diviziya"
		type = infantry
		home = 360
	}

	regiment = {
		name= "2.3-ya Gvardeiskaya Pekhotnaya Diviziya"
		type = infantry
		home = 994
	}

	regiment = {
		name= "3.3-ya Gvardeiskaya Pekhotnaya Diviziya"
		type = infantry
		home = 1012
	}

}


"army" (or "navy") means, that the following troops form an army. Any army have a name and a starting location.[3] Then follow a lot of regiments (every regiment means a troop) with a name, a type and a home. Home is which province the soldiers has been recruited from(remember: To recruite a unit, you need soldiers POPs).

Getting a Flag
Main article: Flag modding

Flags are in the folder "flags" which is in the "gfx" folder. The maximum flag dimensions that the Victoria 2 engine can cache and render is 128x64. The flag must also be saved in .tga format. You need a program to do this, I recommend paint.net. Install the program and create a new document with the dimensions above. Now pick out a flag for Byelorus, I went with the white red white horizontal tricolor. Find an image on the internet and copy paste it into the program. Resize the image so it entirely fits in the canvas, do not resize the canvas to match the image. Now save it as a .tga with the name BYE. If you want to make different flags for different government types, you can! For the communist Byelorus, why not pick out the flag of the Byelorussian SSR and use that? Simply save it as BYE_communist with the correct dimensions and format! Move the .tga files to the flags folder and just leave them there.

One has to make one BYE, one BYE_communist, one BYE_fascist, one BYE_republic and one BYE_monarchy. No more no less. If one forgets one, the game will fail to load.

Making your Country... Presentable
See also: Localisation

If you were to load up Victoria 2 right now, your country would be fully accessible. However, the name of your country would be whatever you made the tag. If it was releasable, you do have the option to release Byelorus, however the name will be BYE. Also, look at the region of Brest or Lida. Because it is split between Russian Brest and BYE_ADJ Brest.

Localisation

Search the localisation folder for a file named "text.csv" and open it. It's comma delimited so make sure to maintain all formatting.

Ctrl-F and type in any tag you know to find the section where country names are defined. Insert a new line and copy/paste another so you don't have to meticulously type in semicolon formatting. The format (in Notepad) is as follows:

tag;name(English);name(French);name(German);;name(Spanish);;;;;;;;;x;

Let's enter in:

BYE;Byelorus;Byelorussie;Weissrusland;;Bielorrusia;;;;;;;;;x;

If you are lazy and know that you will not ever use the game in French, German or Spanish one can just let the names stay, from the country you copied from. You don't have to get the foreign names correct.

Now Ctrl-F again to find where you see the list of countries names with _ADJ following them. This is where the adjective for countries shows up. Follow the instructions listed above to modify a line for Byelorussian. And once you save this file, the game is completely playable without looking ugly. There is more you can do, but that is beyond this guide. tag_ADJ;name(English);name(French);name(German);;name(Spanish);;;;;;;;;x;

Flavour

Now the country is actually finished. Congratulations. There can still be added flavour with either event modding or decision modding. Or various diplomatic pacts could be added in the history files.

Bug-fixing
If your game fails to load

Pay attention to when to game stops loading and the error message.

If the game stops while loading flags, you are missing a flag file. Every single country needs exactly 5 flag files: one [TAG], one [TAG]_communist, one [TAG]_fascist, one [TAG]_republic and one [TAG]_monarchy. No more no less. If just one of them for any country is missing, the game will fail to load.

If the game stop loading and gives an error box saying "failed to load line 528 "common/countries/[name ... ... ENG" you have made a mistake in the countries.txt file. Usually one of the " " marks is missing and the game files thinks the next country's tag is a part of the name. Example:

ENG		= "countries/United Kingdom.txt
If the in-game text is messed up

If the in-game text is wrongly placed, you may have made a misclick in the localisation files (the one with all the country names and country adjectives). Find a backup and replace with the original. It is way faster than looking for your mistake, as the file is huge.

If the game becomes unplayable, and there is not an easy fix or backup, you can always reinstall the game.

Notes

A tag can also not be a special word used in the game's code base, for example: AND, LOG, NOT, GUI, etc.

If you look at e.g. Irelands file, you will notice the information simply isn't there.

Navies do not have home as they are not recruited from Soldier Pops.


---

---
title: Crime modding
category: guide
tags: [rebels]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Crime_modding
---


This page documents the how to edit to effects of crime effects and how to add new ones. The documents needed is crimes.txt found in the Victoria 2 -> Common folder.

Editing and creating Crime modifiers

This part details how you create a new national type of crime or edit an existing one.

The units in crime.txt document should look like this:

anarchic_bomb_throwers = {
	pop_consciousness_modifier = 0.05
	icon = 1	
	
	trigger = {
	}	
}

citizen_guard = {
	life_rating = -0.02
	local_rgo_output = -0.1
	icon = 2	
	
	trigger = {
	}		
}


This is an example of some of the existing types of crime modifiers. In total there should be 8 different types of crime modifiers. To create a new one, another at the bottom and put in the effects, you want.

Icons

The icon mentioned in to a file in the GFX folder.


---

---
title: Culture modding
category: guide
tags: [culture]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Culture_modding
---

This guide will direct you through the process of creating a new culture or to edit an already existing culture.

Finding the Files

The first step is to find the files you will be editing. They are in the Victoria 2 folder. Go to My Computer and access your C: Drive. Open up program files (or program files x86) If the game is bought on steam, it is under Steam --> steamapps --> Common --> Victoria 2 --> Common if you downloaded the game off of Steam, but if not it will be under the Paradox Interactive folder. It is strongly recommended that you make a back-up somewhere on you computer. Let's choose to edit the files in the Victoria 2 folder in program files. Rename the one on your desktop something that will let you know it is a backup. Open up the folder in the Paradox Interactive/Steamapps folder and begin.

Here you need the cultures.txt file.

The cultures.txt file

Each culture is arranged in culture groups. For example North German, South German and Aszhkenazi is in the Germanic group. They have a few things in common like the nation formed by decisions and some graphical features. Example:

germanic = {
	leader = european
	unit = EuropeanGC
    union = GER


The two first lines determine the pictures used for leaders and the units sprites on the map. Union defines which formable country is the correct if applicable. This is mainly used when a country is formed by rebels.[1]

Here is the default list of possible leader portraits:

european
southamerican
russian
arab
asian
indian
african
polar_bear[2]

Here is the default list of possible unit models:

EuropeanGC
BritishGC
ItalianGC
SpanishGC
FrenchGC
AustriaHungaryGC
RussianGC
MiddleEasternGC
IndianGC
AsianGC
ChineseGC
AfricanGC
ZuluGC

Within each culture group there are blocks for each separate culture. Example:

north_german = { 
		color = { 90 60 60 }
		first_names = { Adelbert Adolf Albrecht Alexander Alfred August Bernhard Burkhard Dieter }
		
		last_names = { Behncke Brommy Cordemann Dreyer Droste Groener "Herwarth von Bittenfeld" Heppendorf Hoffmann Krohn }
	}


[3]

The color determines which colour is used in pie charts and such. It is in RGB format, if you are familiar with it. If not, the first number is red, the second green, and the third blue. The numbers are a scale of 0 to 255; 0 being devoid of that color, 255 being the highest amount. Play around until you find what you want, or copy the numbers from a "custom color selection" in MS Paint.

First names and last names determines the names that leaders can take. There has to be at least 1 example in each, but there can be as many as you like. Most cultures have around 50 first names and 50 last names.

Finishing steps
Main article: Population modding

This is strictly speaking all that is needed to create a culture. To create a nation for your new culture look at Creating a country. To add your culture to the map go to the folder Victoria2 --> history --> Pops. Here is defined the sizes and types of each POP at the start of the game. Each file is a country and it can be a little tricky to find exactly which province is in which file.

The files look like this:

1470 = {
	aristocrats = {
		culture = beifaren
		religion = mahayana
		size = 22000
	}

	bureaucrats = {
		culture = beifaren
		religion = mahayana
		size = 10750
	}


[4]

1470 determines the province, Anqing in this example. For each province, the pops are aranged by pop types. Size is the amount of Pops. Culture determines the culture, and it is here you should put your new culture. Religion of course determines the religion of said pop.

Here you have to add all the POPs you want to have with your new culture. If you are doing this for the first time, it might be a good idea to find a comparable example to have an idea of an appropriate scale.

Remember to also edit the 1861 bookmark, if you ever want use it.


Notes

The union line is typically placed under each of the individual culture blocks, but it is still part of the culture group statements.

Only used by Jan Mayen and considered an Easter Egg.

Most names have been removed for ease of reading.

Most POPs has been removed for ease of reading.


---

---
title: Decision modding
category: guide
tags: [events, scripting]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Decision_modding
---

Unlike events, which are usually outside the player's control, decisions can be taken directly by the player (and any AI country). They can have a variety of effects, from adding or removing modifiers for single provinces to unifying countries and changing international politics. This article is an introduction into the basics of decision modding.

Basics

Before creating an event you should familiarize yourself with scopes, conditions and effects.

A decision typically has these blocks:

potential: The conditions for the decisions being visible.
allow: The conditions for taking the decision.
effect: What the decision does.
ai_will_do: Instructions for the AI.

In each of these blocks scopes, conditions and effects are then used to define the decision.

Example from the Game
One of the most famous decisions in Victoria 2 is probably the German unification decision "Three Hurrahs For Germany!" (expand on the right):

To better understand the decision, it can be broken down into smaller parts:

Start
form_germany = {
	news = yes
	news_desc_long = "form_germany_NEWS_LONG"
	news_desc_medium = "form_germany_NEWS_MEDIUM"
	news_desc_short = "form_germany_NEWS_SHORT"

This names the decision and in this case also gives information for generating a newspaper article, since this is an internationally important decision.

Potential
	potential = {
		is_culture_group = germanic
		NOT = {
			exists = GER
			tag = ISR
		}
	}

The decision is visible in the menu when:

The country's primary culture is in the Germanic group (which includes North German, South German and Ashkenazi).
Germany doesn't already exist, and the country isn't Israel (thus Ashkenazi is excluded).
Allow
	allow = {
		is_greater_power = yes
		prestige = 45
		war = no
		GER = {
			all_core = {
				OR = {
					owned_by = THIS
					owner = {
						in_sphere = THIS
					}
				}
			}
		}
	}

If the potential check is successful, a country can take the decision under the following conditions:

It is a Great Power.
It has at least 45 prestige.
It isn't at war.
For the country with tag GER (Germany):
All core provinces of GER are either
owned by the country taking the decision (THIS) OR
the owner is in the sphere of THIS
Effect
	effect = {
		prestige = 20
		change_tag = GER
		add_accepted_culture = north_german
		add_accepted_culture = south_german
		any_country = {
			limit = {
				is_culture_group = germanic
				in_sphere = THIS
			}
			country_event = { id=11101 days=0 }
		}
	}

If THIS now takes the decision the following happens:

It gains 20 prestige.
Its tag changes to Germany.
North German and South German are added as accepted cultures.
Any country that
the following conditions are true for:
The primary culture is in the Germanic group.
It is in the sphere of THIS.
instantly (0 days after the decision) gets the event with ID 11101, which gives a choice between being peacefully annexed by THIS and refusing annexation (AI countries will always choose annexation).
Creating a Custom Decision

For this example we will make custom decision to annex Tibet as China.

First we should think about what this decision is about and how we could achieve that. It should

annex Tibet
give China cores on Tibet
give China some Infamy
give China a small amount of prestige
anger any Tibetans in China

We should also consider the conditions for the decision:

Visible when
The country is China
China is Westernized
Tibet still exists
Can be taken when
China is a Great Power
China isn't at war
Tibet is a vassal of China
Start

The decision should have a unique name, ideally with some sort of ID in it to prevent confusion with other mods or the base game:

XZ_annex_tibet = {

More experienced modders can also add news information here, but that is optional.

potential

The above conditions put into code:

	potential = {
		tag = CHI				#The tag of the taker is CHI.
		civilized = yes				#The taker has westernized/is a civilized nation.
		exists = TIB				#The country with the tag TIB exists.
	}
allow
	allow = {
		is_greater_power = yes			#The taker is a Great Power.
		war = no				#The taker isn't at war.
		TIB = { vassal_of = THIS }		#The country with the tag TIB is a vassal of the taker.
	}
effect
	effect = {
		badboy = 4				#The taker gains 4 infamy.
		prestige = 10				#The taker gains 10 prestige.
		inherit = TIB				#The taker annexes Tibet.
		any_owned = {				#Any province owned by the taker
			limit = {			#for which the following is true:
				is_core = TIB		#It is a core of Tibet
				NOT = { is_core = CHI }	#It isn't a core of China
			}
			add_core = CHI			#China gains a core on.
		}
		any_pop = {				#Any pop living within the takers borders
			limit = { culture = tibetan }	#Which is Tibetan
			militancy = 7			#Add seven Militancy
			consciousness = 3		#Add 3 Consciousness
		}
		set_country_flag = XZ_annexed_tibet	#Give the taker a country flag (if a check for this decision being taken later needs to be done)
	}

AI instructions
	ai_will_do = {					#Adding this block means that the AI will take this decision as soon as all conditions are met.
		factor = 1
	}
}							#Close the entire decision block.


Implementation

Finally the decision needs to be put into the game. For that three things are necessary:

The file containing it has to be in the appropriate folder.
It has to be localized, otherwise it will appear in the game as XZ_annex_tibet_title with the description XZ_annex_tibet_desc.
A mod file needs to be created so the engine can properly read the files.
File & Folder
First the decision needs to be enclosed in a political_decisions block so the engine knows it is a decision. Expand the final file on the right:

This is now saved as a normal .TXT file in the new mod's decision folder, for example: C:\Program Files\Steam\SteamApps\common\Victoria 2\mod\AnnexTibet\decisions.

Localization

Localizing decisions in Victoria 2 is quite simple, the necessary file has the following structure:

decision_id_title;English;French;German;Polish;Spanish;Italian;Swedish;Czech;Hungarian;Dutch;Portugese;Russian;Finnish;
decision_id_desc;English;French;German;Polish;Spanish;Italian;Swedish;Czech;Hungarian;Dutch;Portugese;Russian;Finnish;

In case of the Tibetan annexation the localization could look something like this:

XZ_annex_tibet_title;Annex Tibet;;;;;;;;;;;;;
XZ_annex_tibet_desc;Tibet has been part of the Empire in all but name since 1720, now it will be officially annexed.;;;;;;;;;;;;;

In this case there are only English localizations.

This file is now saved as a .CSV file in the localisation folder of the mod, for example: C:\Program Files\Steam\SteamApps\common\Victoria 2\mod\AnnexTibet\localisation.

Mod File

A mod file for such a small mod only neeeds two lines: name for the name that will be displayed in the launcher, and path to tell the engine which files to load.

name = "Annex Tibet"
path = "mod/AnnexTibet"

This is saved as a .MOD file in e.g. C:\Program Files\Steam\SteamApps\common\Victoria 2\mod

If all these steps are done the mod is complete and should be available for selection in the game launcher.


---

---
title: Defaultmap
category: other
tags: [map]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Defaultmap
---

This file pertains to a lot of the settings for the map. When it changes, the map information must be reloaded on game start-up. Note: These default values might be wrong because I changed them and forgot what the original values were, so feel free to update them.

Parameter Name	Explanation	Possible Values (Victoria2 v3.03 setting)
max_provinces	Defines the number of provinces in the map. This is usually determined by the number of unique colours in the provinces.bmp file, found in the same directory. Often this number is agreed upon before a mod begins because this number is used 'a lot' throughout.	(3249)
sea_starts	The province ID number of the first ocean province.	( 2703 2704 2705 2706 2707 2708 2709 2710 2711 2712 2713 2714 2715 2716 2717 2718 2719 2720 2721 2722 2723 2724 2725 2726 2727 2728 2729 2730 2731

2732 2733 2734 2735 2736 2737 2738 2739 2740 2741 2742 2743 2744 2745 2746 2747 2748 2749 2750 2751 2752 2753 2754 2755 2756 2757 2758 2759 2760 2761 2762 2763 2764 2765 2766 2767 2768 2769 2770 2771 2772 2773 2774 2775 2776 2777 2778 2779 2780 2781 2782 2783 2784 2785 2786 2787 2788 2789 2790 2791 2792 2793 2794 2795 2796 2797 2798 2799 2800 2800 2801 2802 2803 2804 2805 2806 2807 2808 2809 2810 2811 2812 2813 2814 2815 2816 2817 2818 2819 2820 2821 2822 2823 2824 2825 2826 2827 2828 2829 2830 2831 2832 2833 2834 2835 2836 2837 2838 2839 2840 2841 2842 2843 2844 2845 2846 2847 2848 2849 2850 2851 2852 2853 2854 2855 2856 2857 2858 2859 2860 2861 2862 2863 2864 2865 2866 2867 2868 2869 2870 2871 2872 2873 2874 2875 2876 2877 2878 2879 2880 2881 2882 2883 2884 2885 2886 2887 2888 2889 2890 2891 2892 2893 2894 2895 2896 2897 2898 2899 2900 2901 2902 2903 2904 2905 2906 2907 2908 2909 2910 2911 2912 2913 2914 2915 2916 2917 2918 2919 2920 2921 2922 2923 2924 2925 2926 2927 2928 2929 2930 2931 2932 2933 2934 2935 2936 2937 2938 2939 2940 2941 2942 2943 2944 2945 2946 2947 2948 2949 2950 2951 2952 2953 2954 2955 2956 2957 2958 2959 2960 2961 2962 2963 2964 2965 2966 2967 2968 2969 2970 2971 2972 2973 2974 2975 2976 2977 2978 2979 2980 2981 2982 2983 2984 2985 2986 2987 2988 2989 2990 2991 2992 2993 2994 2995 2996 2997 2998 2999 3000 3001 3002 3003 3004 3005 3006 3007 3008 3009 3010 3011 3012 3013 3014 3015 3016 3017 3018 3019 3020 3021 3022 3023 3024 3025 3026 3027 3028 3029 3030 3031 3032 3033 3034 3035 3036 3037 3038 3039 3040 3041 3042 3043 3044 3045 3046 3047 3048 3049 3050 3051 3052 3053 3054 3055 3056 3057 3058 3059 3060 3061 3062 3063 3064 3065 3066 3067 3068 3069 3070 3071 3072 3073 3074 3075 3076 3077 3078 3079 3080 3081 3082 3083 3084 3085 3086 3087 3088 3089 3090 3091 3092 3093 3094 3095 3096 3097 3098 3099 3100 3101 3102 3103 3104 3105 3106 3107 3108 3109 3110 3111 3112 3113 3114 3115 3116 3117 3118 3119 3120 3121 3122 3123 3124 3125 3126 3127 3128 3129 3130 3131 3132 3133 3134 3135 3136 3137 3138 3139 3140 3141 3142 3143 3144 3145 3146 3147 3148 3149 3150 3151 3152 3153 3154 3155 3156 3157 3158 3159 3160 3161 3162 3163 3164 3165 3166 3167 3168 3169 3170 3171 3172 3173 3174 3175 3176 3177 3178 3179 3180 3181 3182 3183 3184 3185 3186 3187 3188 3189 3190 3191 3192 3193 3194 3195 3196 3197 3198 3199 3200 3201 3202 3203 3204 3205 3206 3207 3208 3209 3210 3211 3212 3213 3214 3215 3216 3217 3218 3219 3220 3221 3222 3223 3224 3225 3226 3227 3228 3229 3230 3231 3232 3233 3234 3235 3236 3237 3238 3239 3240 3241 3242 3243 3244 3245 3247 3248)


definitions	Each province is defined by a unique RGB color value that is defined in this file. Either create one yourself, or use one of the numerous extras provided by Paradox at the end of the file. This is also the final file that contains province numbers, so alter them as you did in text.csv and the history/provinces files.	("definition.csv")
provinces	Defines the shape of each province. Each unique colour denotes a province in this .bmp file, as defined in definitions, above. Note that this image is flipped vertically from how it appears in the game. The game scans this file and attempts to create a province for each color it encounters, so even a subtle error here can make your map refuse to load, since it will think a stray pixel is a new province.	("provinces.bmp")
positions	This annoying file will, depending on how much of a perfectionist you are (and how small your provinces are), take a long time to get straight. It determines where cities, ports, units, etc., show up on the game map. You can get a rough idea as to what values to use by opening provinces.bmp and clicking on the info tab next on top of the navigator window in the upper right of Photoshop. Click on the left of the X Y Coordinates box that appears and choose points as a measurement unit. That box will now display the coordinates currently being pointed at by the mouse. In theory, that works fine. In practice, you'll have to load up EU3, take screenshots of the map in-game to see how it looks, then alter positions.txt appropriately. The reason I suggested skipping topology.bmp earlier is because it can be easier to place things when everything is flat. Oh, and you can't flip and rotate provinces.bmp while you're doing this because it screws with the coordinates. And everytime you make a change EU3 will recalculate all the paths when loading. So all this can be very time-consuming.

One last note on positions.txt. The port_rotation and text_rotation entries in the file determine the direction of ports and province names in game. The value these entries take is the angle as measured in radians from due west. No problem, right? Using the ruler tool in Photoshop we can just determine what angle we want to use, right? Not quite. From what I've been able to determine on-line, there's no way to make Photoshop report angles in radians. Also, Photoshop measures angles from due east (not due west like EU3) and has a maximum value of 180 degrees before switching to negative numbers, whereas radians work on the full 360.

So here's the formula you'll want to use to convert the degrees Photoshop gives you to the value you put into positions.txt:

radians = (-1 * (degrees - 180)) * 0.0174533

The radians used for text_rotation are flipped along the x axis (so a line of text running from NW to SE on the map uses the value you'd expect for one running SW to NE), so take that into account.

Or as a shortcut just use these values:

port_rotation=0.000000 = W port_rotation=0.785398 = NW port_rotation=1.570796 = N port_rotation=2.356194 = NE port_rotation=3.141593 = E port_rotation=3.926991 = SE port_rotation=4.712389 = S port_rotation=5.497787 = SW

text_rotation=0.785398 = from SW text_rotation=0.392699 = from WSW text_rotation=0.000000 = from W text_rotation=5.890486 = from WNW text_rotation=5.497787 = from NW

I should probably also mention that province names are centered (not begun) on the value that you enter for text_position.

	("positions.txt")
terrain	Defines the terrain of each pixel in the world. The terrain of each color is defined/explained in terrain_definition, below, so take a look at that if need be. Generally, purple is mountains, gray is permafrost. Since it uses the same engine, I'm linking to the EU3 equivalent: Mod Guide: Altering the Map	("terrain.bmp")
rivers	Defines the shape of the rivers in the world. A river can have a variety of blues, with darkest meaning the widest river and light blue being relatively narrow (i.e. headwaters)	("rivers.bmp")
terrain_definition	Matches the different terrains to a specified colour, and then adds various gameplay bonuses and maluses to them.	("terrain.txt")
continent	Associates provinces with continents, which determines such things as which advisors you have access to. Enter any new provinces appropriately.	("continent.txt")
border_heights	The values here define what the height of the camera (i.e. zoom level) will be, below which borders will be displayed.
The first value indicates province borders
The second value indicates region borders\
The third value indicates probably country borders
	(500 850 1100)
terrain_sheet_heights	The values here indicate the threshold zoom of the map, below which the terrain will be displayed.	(500)
tree	The threshold zoom of the map, below which individual 3D trees will be rendered.	(350)
border_cutoff	The threshold zoom, below which country borders will be drawn	(1100.0)


---

---
title: Dynamic localisation
category: guide
tags: [localization]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Dynamic_localisation
---

Localisation for events and decisions is usually static, outside of some specific localisation keys. However, through abuse of the change_region_name effect, one can write text with any arbitrary content that changes dependent on in-game dynamic conditions.

## Guide

The Underground Railroad random event has its impact in American New England

Events and decisions can have effects that impact on regions, and these region names appear in the mouse over of the options to choose in an event or the tick to accept a decision. We can use the change_region_name effect to change the name of the region to anything we want it to be, based on whatever conditions we want, and then show the result back to the player.

Firstly, set up a region in region.txt. Note that provinces can be in multiple regions at the same time, there does not appear to be any limit - so long as your dynamic localisation region appears after the actual state you want the province to be in, there is no impact. You can also arbitrarily assign a sea province to a region.

```
dynamic_localisation_region = { 3248 }
```

Then in the effect scope of an event or decision you can summon the arbitrary text to appear on mouseover by simply calling the region scope with nothing in it:

```
political_decisions = {
    show_dynamic_localisation = {
        potential = {
            ...
        }
        effect = {
            dynamic_localisation_region = {}
        }
    }
}
```

To change the text being shown, in an effect block use the change_region_name effect. Note that you must secede the province to the country doing the changing of the region name - calling secede_province with an empty tag as demonstrated will revert to no owner, which is useful when using dynamic localisation on sea province regions. Note the region scope can also take a limit block, a form of IF Emulation, meaning the text can be dynamically set based on conditions.

```
political_decisions = {
    change_dynamic_localisation = {
        potential = {
            3248 = { secede_province = THIS }
        }
        dynamic_localisation_region = {
            state_scope = { change_region_name = "My text is now this!" }
            3248 = { secede_province = --- }
        }
        effect = {
            dynamic_localisation_region = {}
        }
    }
}
```

Dynamic localisation is similar to the concept of metaregions.


---

---
title: Event modding
category: guide
tags: [events]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Event_modding
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


---

---
title: Event picture modding
category: guide
tags: [events, graphics]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Event_picture_modding
---

This is a method for creating quick and dirty event pictures using the free utility, Paint.NET that look reasonably good next to the Paradox pictures. (If you own a more advanced graphics program you'll be able to create even better pictures, with nice airbrushing and fading effects that Paint.NET doesn't feature.)

## Finding an Appropriate Picture

Naturally, a good source of pictures for both PI and modders is Wikipedia and its sister site Wikimedia Commons.

### Good Places to Find Pictures

**Archival sites:**
- U.S. National Archives
- British National Archives
- Archives Canada
- National Archives of Australia
- School library websites

Other student resources - schools and universities also often have access to digital archive services where you can find pictures.

### Tips for Choosing a Picture

- Generally Paradox Interactive seems to prefer line drawings, cartoons and paintings to photographs
- Look for long and thin landscape pictures wherever possible, and go for the highest resolution you can find (they're easier to resize). All event pictures are sized 521 pixels by 203 pixels. If your picture is too small you may have to copy in another image to fill in the space
- If your picture has a plain white background, such as a poster or other document, try overlaying it over the image `gfx\interface\event_country_background.dds` (which is the parchment-like background texture of the event screen)
- Choose something appropriate to the pre-1936 period of course
- If you have mad photoshop skills, you can get creative with tricks such as adding text next to a person's portrait which PI used for some of the author events, see e.g. Emerson.tga and Tocqueville.tga in the `Victoria 2\gfx\pictures\events` folder

This tutorial will be using Henry Arthur McArdle's painting, The Battle of San Jacinto.

## Get Your Pic into Paint.NET and Recolor It

Save the picture and open it in Paint.NET.

If you keep the event picture the same colour as the original source, it'll stick out like a sore thumb next to the sepia-toned vanilla pictures. A neat trick here is to find your game folder (for example, `C:\Program Files\Paradox Interactive\Victoria 2\`) and browse to the `gfx\pictures\events` folder. Open one of the images in Paint.NET, which supports TGA files. Find the Color Picker tool (the eyedropper icon, shortcut: K) and choose a fairly dark brown portion of the image.

Next, use these menu options to re-colour your image:
- `Adjustments > Black and White` (shortcut Ctrl+Shift+G): this is so the color is washed out
- `Effects > Color > Color Filter`: Click the box with the active foreground color, to the left of the color wheel, and the settings will be automatically applied

Now you have a nice sepia-toned picture. If you're doing many pictures at once, you can use the Ctrl+F shortcut or 'Repeat Color Filter' under the Effects menu to speed the process up.

## Resize Your Picture to 521x203

Try changing the size to 521 pixels wide (`Image > Resize` or Ctrl+R), then use Rectangle Select (the dotted square tool, shortcut S) to measure out a box that is 203 pixels tall - the size of the rectangle is indicated in the status bar. You can then use the Move Selection tools or drag the mouse to adjust the selection. Finally, go to `Image > Crop to Selection` (Ctrl+Shift+X). Voila, a 521x203 image!

## Add the Border as a New Layer

A blank frame template for event pictures is available. Save the PNG file somewhere on your computer where you can drag it straight into Paint.NET over your source image. A Drag and Drop dialog box will appear. Choose "Add layer".

As you will see, the border isn't pretty and the edges need extra retouching. Try using `Filters > Blurs > True Blur` to soften the sharp edges of the frame. Since the BlankEventFrame layer should still be selected by default, only the border will blur; if it doesn't, look in the Layers window to ensure that "Background" is not the active layer.

## Save Your Image

Event pictures go in the `Victoria 2\gfx\pictures\events` directory. Save the image as a TGA file (use the dropdown in the Save box) - the default format settings are OK. You'll be prompted to "flatten" the image from two layers to one: go ahead and do it. Now you're done!

## Use Your Image in an Event

It couldn't be easier to use your new image: when writing events, use the line `picture = "xxx"` where xxx is the filename of your TGA file. For example:

```
picture = "SanJacinto"
```

## Making Event Pictures: A Gallery

The tutorial shows the step-by-step process from source image to finished product:
1. Source image selection
2. Paint.NET editing with color picker
3. Color filter application
4. Resizing before cropping
5. Adding the border layer
6. Edge retouching
7. The finished product


---

---
title: Flag modding
category: guide
tags: [graphics]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Flag_modding
---

This page documents the formatting and creation of flags.

What does a flag look like?

Flags are found within gfx\flags.

Flags are saved in the ".tga" file format at a size of 93 x 64.

In vanilla, there are five flag slots:

Default
Communist
Fascist
Monarchy
Republic

These slots correspond to the "flagType" entries referenced in governments.txt. Note that the game will not run, if there is not a defined flag for each country in the countries.txt-file for each government type.

Creating a new flag

Typically, new flags are only added to the files when a new flag type is created for a new or existing government, or when a new country is added.

When a new flag type is added, all countries must have a flag of that new type added. Otherwise the game will crash.

When a new country is added, a flag must be added for each flag slot. Otherwise the game will crash.

All countries must have as many flags as there are flag slots.


---

---
title: FolderFile Overview
category: other
tags: [structure]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/FolderFile_overview
---

Overview

This is a list of what the files and folders inside the main Victoria 2 folder mean, knowing what files go where, and where to make changes is the most important part of modding, as something in the wrong place can easily lead to a fatal crash.

Note that Victoria II's files need to be saved with ANSI encoding in order to work properly in the game. Additionally, some files seem to be encoded in a weird manner (such as some of the province history files), resulting in the game reading their contents as a single line. This can be fixed by creating a new .txt file with ANSI encoding with Notepad++ and copying the contents of the old file to it, deleting the old one and replacing it with the new.


The Files
File/Folder	What it contains
Victoria II\battleplans	Settings for battle plan editor
Victoria II\common\	General information

bookmarks.txt
buildings.txt
cb_types.txt
countries.txt
country_colors.txt
crime.txt
cultures.txt
defines.lua
event_modifiers.txt
goods.txt
governments.txt
ideologies.txt
issues.txt
national_focus.txt
nationalvalues.txt
on_actions.txt
pop_types.txt
production_types.txt
rebel_types.txt
religion.txt
static_modifiers.txt
technology.txt
traits.txt
triggered_modifiers.txt
country\.txt
	
Defines scenarios/start dates
Building statistics
Casus belli attributes and types
Which tag is linked to which .txt in common\countries
RGB code for each country
All crimes and effects
Culture groups, names and colors along with cultural unions
POP, general, diplomatic, economic and military variables
All event and province modifiers and their effects
All goods with their starting price and color
All government types with their ideology and effects
All ideologies and their views on reforms
All reforms (political, social and civilizing) and party issues and their effects
All national focusses and their effects
All national values and the effects
Specially triggered effects
Mean Time To Happen (MTTH) for POP actions (promotion, assimilation etc.)
Production statistics
All rebel types, their goals and chances for rebelling
All religions, their icons and colors
All difficulty, rank and standard modifiers
Technology data
Traits of leaders and their effects
Empty by default
Color, political parties and ship names

Victoria II\decision\	Decisions folder, all decisions are stored here
Victoria II\events\	Events folder, all event files are kept here
Victoria II\gfx\	Graphics
Victoria II\history\	Data on each province, diplomatic relations, country, units and POPs
Victoria II\interface\	Interface Graphics
Victoria II\inventions\	All inventions together with requirements, invention chances and effects
Victoria II\launcher\	Launcher graphics and configuration
Victoria II\localisation\	All text data for things like country names and event description, has options for other languages
Victoria II\map\	Map settings, province shapes, continents, regions etc.
Victoria II\mod\	Folder for storing mods and .mod files
Victoria II\movies\	Game intro movie
Victoria II\music\	Music used by the game
Victoria II\news\	All news stories
Victoria II\poptypes\	All POP data for each specific POP type
Victoria II\script\	All scripts
Victoria II\sound\	All sounds except music
Victoria II\technologies\	Technologies with their effects and attributes
Victoria II\tutorial\	Tutorial configuration
Victoria II\units\	All military unit attributes, for each specific unit

Pop files note: Issue and Ideology modifiers are multipliers, all other seem to be additions.


---

---
title: Full list of effects
category: reference
tags: [scripting]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Full_list_of_effects
---

This article lists all possible event effects. Add any that are missing.

Syntax and terminology

Many event options are of the form

X = {
	limit = {
		A = B
	}
	Y = Z
}

What this means is that when the event triggers, and this outcome is selected, then for all X such that A = B, Y = Z happens to X. X is the target of the command, and may be a group of pops, a group of provinces or states, a country, or other things; A = B is the condition, and may be limiting the pops to only those of certain cultures, limiting the states to only those that are slave states, or other things; Y is the effect, and Z is the argument that tells the effect what to do. This is a general pattern, and may not hold for specific examples.

These may also be nested; for instance,

any_state = {
	limit = {
		is_slave = yes
	}
	any_pop = {
		limit = {
			has_pop_culture = dixie
		}
		consciousness = 0.5
	}
}

says that in all states (any_state) that are slave states (limit = {is_slave = yes}), all pops (any_pop) that are of the Dixie culture will have a CON increase of 0.5

Targets
Pops

An effect that applies to pops can target pops in these classes:

target	what it means
any_pop	targets all pops

aristocrats
artisans
bureaucrats
capitalists
clergymen
clerks
craftsmen
farmers
labourers
officers
slaves
soldiers
	the type of pop specified

poor_strata
middle_strata
rich_strata
	all pops in a certain wealth level

This target can be limited by:

has_pop_culture = (culture)
has_pop_religion = (religion)
is_state_religion = (yes/no)
type (type = slaves or NOT = { type = slaves}, for example)
is_primary_culture = (yes/no)
is_accepted_culture = (yes/no)
consciousness = n (all pops where CON is at least n)
militancy = n
Province

An effect that targets provinces can target these classes:

target	what it means
any_owned	all provinces; can be nested within a state or country target to give all provinces within the state, states, or country selected.
(a province ID)	the province referenced by the ID
capital_scope	for a country event, this targets the country's capital province.

For a province event, if no target is given the effect will target the province for which the event fired.

This target can be limited by:

is_core = (tag) (to specify provinces that have certain cores on them)
province_id = n (to exclude specific provinces from a larger group)
has_province_modifier = (modifier)
has_province_flag = (flag name) (only provinces that have that flag will be targeted)
(ideology) = n (only provinces where (ideology) has more than n% representation)
average_militancy = n (all provinces with average MIL over n)
average_consciousness = n
State

An effect that targets states can target these classes:

target	what it means
random_state	any one state, randomly chosen
(a state name, e.g. USA_1)	the state referenced by that name
state_scope	For a province event, state_scope is the state containing the province

This target can be limited by:

is_slave = (yes/no)
is_colonial = (yes/no)
average_militancy = n (all states with average MIL over n)
average_consciousness = n
has_pop_type = (type)
(issue) = n (all states where (issue) is the primary issue for n% of the population)
Country

An effect that targets a country as a whole can use these targets

target	what it means
no target given	For a country event, the default target is the country that fired the event
(a tag)	the country referenced by the tag
any_country	all countries (the current country not included)
any_greater_power	randomly choose one of the eight great powers
FROM	for a triggered event, FROM is the country that fired the triggering event.
THIS	the country that fires a country-scope event.
owner	for a province event, owner is the country that owns the province that fired the event
sphere_owner	If the country that fired an event is in a sphere, sphere_owner is the nation controlling that sphere


This target can be limited by:

has_country_flag = (flag name) (only countries that have that flag will be targeted)
civilized = (yes/no)
in_culture_group = (group)
(reform_class) = (reform_level) (only countries that have a certain level of political or social reform, ex. press_rights = free_press)
prestige = n (limits to countries with n prestige or more)
tag = (tag) or, more importantly, NOT = {tag = (tag)} (limits to the country with (or the countries without) the given tag
Population Effects
Name	Target	Syntax	Effect	Notes


assimilate

	Province	
assimilate = yes/no
	Changes every pop whose province is currently in scope to the country's primary culture.	Only works in the province scope. Example:
any_owned = { assimilate = yes }
Changes all pops in the country to the primary culture.


consciousness

	POPs	
consciousness = n
	Change the CON of the targeted pop or pops by the given value	Example:
poor_strata = {
	consciousness = 1.5
}


militancy

	POPs	
militancy = n
	Change the MIL of the targeted pop or pops by the given value.	Similar in all aspects to consciousness, as described above.


dominant_issue

	POPs	
dominant_issue = {
	value = (issue)
	factor = n
}
	Changes the dominant issue of a portion of the targeted pop to the given issue.	Works the same way as upper_house.


ideology

	POPs	
ideology = {
	factor = n
	value = (name)
}
	Change the proportion of the targeted pop that follows the specified ideology.	Works the same way as upper_house.


literacy

	POPs	
literacy = n
	Changes the literacy of the targeted pop by the specified amount.	Example:
any_pop = { literacy = -0.10 }
Reduces literacy by 10%.


money

	POPs	
money = n
	Changes the target pop's savings by the specified amount.	


move_issue_percentage

	POPs	
move_issue_percentage = { 
	from = (issue) 
	to = (issue)
	value = n
}
	Makes a certain percentage of people supporting issue A, switch to issue B. This effect is used in the adding of CB, where people switch from jingoism to pro military.	


move_pop

	POPs	
move_pop = (province ID)
	Moves the targeted pop to the specified province.	When a pop moves to a province where another pop of the same type and religion already exists, he will get merged with the latter regardless of culture - sometimes even if another pop of the same type, religion and culture also exists. What culture a POP turns into when they are moved appears to be based on the order POPs are placed in within the game files. Use with caution.


pop_type

	POPs	
pop_type = (type)
	Changes the type of the targeted pop.	


reduce_pop

	POPs	
reduce_pop = n
	Changes the targeted pop to the given proportion of its current value. Increases POP size if n>1.	Example:
any_pop = { reduce_pop = 0.95 }
Reduces every pop by 5%.


scaled_consciousness

	POPs	Example:
scaled_consciousness = {
	factor = n
	ideology or issue = (name)
}
	Changes the consciousness of the targeted pops by the given value multiplied by the proportion of the pop that is of the given ideology or issue.	E.g. if a pop has 40% support for pro-military, and n = 0.5, then the CON increase would be 0.4 * 0.5 = 0.2.


scaled_militancy

	POPs		see scaled_consciousness	
Provincial Effects
Name	Target	Syntax	Effect	Notes


add_core

	Province	
add_core = [TAG/THIS/FROM]
	Adds a core of the given country to the targeted province	


add_province_modifier

	Province	
add_province_modifier = {
	name = (modifiername)
	duration = n
}
	Adds the specified modifier to the targeted province. n in days.	


change_controller

	Province	
change_controller = [TAG]
	Changes the controller (not owner) of the target province.	


change_province_name

		
change_province_name = "name"
	Changes the province's name to the one specified.	


change_region_name

	State	
change_region_name = "name"
	Changes the region (state) name to the one specified.	Example:
1 = { state_scope = { change_region_name = "name" } }
Don't include ANY other effects in the same province scope as this one, else the event will cause a crash.


flashpoint_tension

	State	
flashpoint_tension = n
	Increases the flashpoint tension of the state by n.	HoD only. Example:
state_scope = {
	flashpoint_tension = 10 }


fort

	Province	
 fort = n 
	Changes the target province's fortification level by n.	


infrastructure

	Province	
 infrastructure  = n 
	Changes the target province's infrastructure level by n.	


life_rating

	Province	
life_rating = n
	Changes the target province's life rating by n.	


naval_base

	Province	
naval_base = n 
	Changes the target province's naval base level by n.	


remove_core

	Province	
remove_core = [TAG/THIS]
	Removes a core of the given country to the targeted province.	FROM does not work.


remove_province_modifier

	Province	
remove_province_modifier = [modifier name]
	Removes the specified modifier from the targeted province.	If the modifier does not currently exist in the province, this command won't appear in the tooltip.


RGO_size

	Province	
 RGO_size = n
	Changes the target province's RGO size by n.	


secede_province

	Province	
secede_province = [tag/THIS/FROM]
	Transfers the province in scope from the targeted nation to another.	


sub_unit

	Province	
sub_unit = { 
	type = [unit type] 
	value = current 
}
	Spawns a unit.	Unknown what the value parameter does. In all known examples, it is current.


trade_goods

	Province	
trade_goods = [type]
	Changes the good produced by the target province to the one specified.	
National Effects
Name	Target	Syntax	Effect	Notes


activate_technology

	Country	
activate_technology = [technology]
	Adds the specified technology to the country, whether it is the next level or not.	AHD only


add_accepted_culture

	Country	
add_accepted_culture = [culture]
	Makes the specified culture accepted by the targeted country.	


remove_accepted_culture

	Country	
remove_accepted_culture = (culture)
	Removes the specified culture as accepted by the targeted country.	


add_country_modifier

	Country	
add_country_modifier = {
	name = [modifier]
	duration = n
}
	Adds the specified modifier to the targeted country. n is in days.	Won't replace or extend an already existing modifier.


add_crisis_interest

	Country	
add_crisis_interest = [yes/no]
	Involves the country in scope to the current crisis.	HoD only


add_crisis_temperature

		
add_crisis_temperature = n
	Increases the temperature of the current crisis by n.	


badboy

	Country	
badboy = n
	Change the target country's infamy by n.	


build_factory_in_capital_state

	Country	
build_factory_in_capital_state = [factory type]
	Starts construction of the given factory type in the capital state of the country.	Works as with the westernization reform. Tested in HoD v3.04


capital

	Country	
capital = [province]
	Change the capital of the country to the specified province id.	


civilized

	Country	
civilized = [yes/no]
	Changes the civilized/uncivilized status of the country.	


kill_leader

		
kill_leader = [ID]
	Kills the specified army/navy leader.	The ID can be found in the save file. Unclear if the ID is always the same for leaders created using define_general.


define_general

		
define_general = {
	name = [name]
	personality = [trait]
	background = [trait]
}
	Creates a new general with the specified parameters.	name: see kill_leader


nationalvalue

	Country	
nationalvalue = [value]
	Changes the national value of the current country to the value specified.	value from common\nationalvalues.txt


plurality

	Country	
plurality = n
	Change the plurality of the targeted country by n.	


prestige

	Country	
prestige = n
	Change the prestige of the targeted country by n.	


prestige_factor

	Country	
prestige_factor = n
	Changes the prestige of the targeted country by the current prestige multiplied with n. Change cannot be less than ±1.	


primary_culture

	Country	
primary_culture = [culture]/[TAG/THIS/FROM]
	Changes the target country's primary culture.	This may be used on non-existing countries.


religion

	Country	
religion = (religion)
	Changes the scoped country's state religion to the specified one.	State religion is only visible in save files.


remove_country_modifier

		
remove_country_modifier = [modifier]
	Removes a country modifier.	If the country modifier does not exist, the command won't appear in the tooltip.


research_points

	Country	
research_points = n
	Grants n RPs to the target country's current research project.	


war_exhaustion

	Country	
war_exhaustion = n
	Changes the target country's war exhaustion by n.	


years_of_research

	Country	
years_of_research = n
	Grants a number of RP that would have been accumulated over n years.	


nationalize

	Country	
nationalize = [yes/no]
	Turns all factories invested by foreign powers your own.	
Political Effects
Name	Target	Syntax	Effect	Notes


economic_reform

	Country	
economic_reform = [reform]
	Adds the specified economic reform to the uncivilized nation.	AHD only


election

	Country	
election = yes
	Starts the election process ahead of schedule.	


enable_ideology

		
enable_ideology = [ideology]
	Globally enables the specified ideology.	


government

	Country	
government = [government]
	Changes the target country's government to the specified type.	Does not change any of the country's reforms.


is_slave

	State	
is_slave = (yes/no)
	Sets the slave state / free state status of a state.	Appears in a triggered-only event, syntax doesn't fit the normal model.


military_reform

	Country	
military_reform = [reform]
	Adds the specified military reform to the uncivilized nation.	AHD only


political_reform

	Country	
political_reform = [reform]
	Changes the target country to the specified political reform.	


ruling_party_ideology

	Country	
ruling_party_ideology = [ideology]
	Changes the current ideology of the country's ruling party.	If there is more than one party for that ideology, the first party listed in the country file is chosen.


social_reform

	Country	
social_reform = [reform]
	Changes the target country to the specified social reform.	

upper_house
	Country	
upper_house = {
	ideology = [ideology]
	value = [n]
}
	Changes the proportion of the upper house that follows the specified ideology.	The amount gained (U) is calculated by the following formula: U=1-1/(1+N)

The other values will be multiplied by 1-U.

Example:

Upperhouse starts with 10% (0.1) liberals and 90% (0.9) conservatives.


U=1-1/(1+N)=1-1/(1+0.25)=1-0.8=0.2

1-U=0.8

liberals = 0.1*0.8+.2 = 0.28 = 28%

conservatives = 0.9*0.8 = 0.72 = 72%

N = -1-1/(U-1)


Diplomatic Effects
Name	Target	Syntax	Effect	Notes


add_casus_belli

	Country	
add_casus_belli = {
	target = [TAG/FROM/THIS]
	type = [casus belli]
	months = n
}
	Gives the target a casus belli against the country in scope for n months. Optional fields include state_province_id for when the casus belli targets a specific state, such as with acquire state, and country for when the casus belli targets another country tag, such as with free peoples.	


annex_to

	Country	
annex_to = [TAG/THIS/FROM]
	Annexes the targeted country to the country in the current scope.	


casus_belli

	Country	
casus_belli = {
	target = [TAG/FROM/THIS]
	type = [casus belli]
	months = n
}
	Grants the scoped country a casus belli against the target country for n months. Optional fields include state_province_id for when the casus belli targets a specific state, such as with acquire state, and country for when the casus belli targets another country tag, such as with free peoples.	


create_alliance

	Country	
create_alliance = [TAG]
	Creates an alliance between target country and the scoped country.	


create_vassal

	Country	
create_vassal = [TAG]
	Makes the specified country a vassal of the scoped country, even if they are already a vassal.	


diplomatic_influence

	Country	
diplomatic_influence = {
	who = [TAG/FROM/THIS]
	value = n
}
	Changes the influence that the targeted country has on the specified country by n.	


end_military_access

	Country	
end_military_access = [TAG/THIS/FROM]
	Ends the military access granted by the specified country to the current country.	


end_war

	Country	
end_war = [TAG]
	Ends any war between the target country and the specified country.	Does not create a truce, and there are no penalties for the cancelled CBs. Will not cancel the war with allies or vassals.


inherit

	Country	
inherit = [TAG/FROM/THIS]
	Adds all provinces of the specified country to the targeted country.	


leave_alliance

	Country	
leave_alliance = [TAG/FROM/THIS]
	Remove the current country from an alliance with the specified country.	


military_access

	Country	
military_access = [TAG/THIS/FROM]
	Gives the target country military access to the specified country.	


neutrality

	Country	
neutrality = [yes/no]
	Dissolves all alliances a nation has and set all satellites free.	


relation

	Country	
relation = {
	who = [TAG/FROM/THIS]
	value = n
}
	Changes the relation between the targeted country and the specified country by n.	


release

	Country	
release = [TAG]
	Allows the target country to release the specified country and thereby create a new independent nation.	


release_vassal

	Country	
release_vassal = [TAG/FROM/THIS]
	If this targets a vassal nation (or substate), the vassal is freed. If this targets a non-existing nation, it is released as a vassal of the current country.	If the capital of the released country is not owned, the country is simply freed outright and not as a vassal (check with is_possible_vassal).


war

	Country	
 war = [TAG]
war = {
	target = [TAG]
	attacker_goal = { casus_belli = [casus belli] }
	defender_goal = { casus_belli = [casus belli] }
	call_ally = [yes/no]
}

	Starts a war between the country for whom the event fired and the given country.	See casus belli for info on its options.
Economic Effects
Name	Target	Syntax	Effect	Notes


add_tax_relative_income

	Country	
add_tax_relative_income = n
	Used to remove or add money relative to country's income with maximum taxation.	E.g. if n=0.1, 10% of what income would be if all taxes were maxed out is added.


[resource name]

	Country	
[resource name] = n
	Changes the national stockpile of the resource named by n.	


treasury

	Country	
treasury = n
	Change the amount of cash in the treasury by n.	The maximum amount of money you can add to a country's treasury through this effect is 2147483, or 2^31/100. Values greater than this will overflow.
Function Effects
Name	Target	Syntax	Effect	Notes


change_tag

	Country	
change_tag = [TAG]
	Switches the nation in scope to the specified country tag. No cores will change.	change_tag = culture changes to the union tag for the currently scope country.

The previous example has no effect on cultures with no union tag.


change_tag_no_core_switch

		
change_tag_no_core_switch = [TAG]
	Switches the player nation from the current one to the specified one.	


change_variable

		
change_variable = {
	which = [variable]
	value = n
}
	Increases or decreases the value of an existing variable.	


clr_province_flag

	Province	
clr_province_flag = [flag]
	Removes the specified province flag.	


clr_country_flag

	Country	
clr_country_flag = [flag]
	Removes the specified country flag.	


clr_global_flag

	Global	
clr_global_flag = [flag]
	Removes the specified global flag.	


country_event

		
country_event = [event]
country_event = {
	id = [event]
	days = n
}
	Fires the specified country event for the targeted country.	Second syntax is AHD only.


province_event

		
province_event = { id = [event] }
	Fires the specified province event for the targeted province.	Event can only fire for the owner of the province, and does not work on empty provinces. It will however work if you secede_province at the same time.


random

		
random = {
	chance = n
	[effects]
}
	Specifies the probability n that the effects specified will occur.	


random_list

		
random_list = {
	E1 = { [effect1] }
	E2 = { [effect2] }
	...
	En = { [effectn] }
}
	Causes one of two or more possible effects to happen and specifies the probability for each. Probability of any effect Ex occurring is Ex/(E1+E2+...+En).	Due to the game using a random number seed, the output for this effect will be the same every time it's used in the same event.


set_province_flag

	Province	
set_province_flag = [flag]
	Sets the specified flag for the current province.	


set_country_flag

	Country	
set_country_flag = [flag]
	Sets the specified flag on the current country.	


set_global_flag

	Global	
set_global_flag = [flag]
	Sets the specified flag globally (meaning every tag, existing or not, gets the flag)	


set_variable

		
set_variable = {
	which = [name]
	value = n
}
	Creates a new variable and assigns it the value n. If the variable exist，it's value will be set by n.


---

---
title: Full list of scopes
category: reference
tags: [scripting]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Full_list_of_scopes
---

This is a full list of scopes for scripting event triggers, decision prerequisites, and limits.

Scopes are used to change what an event, decision, or limit is looking at. For example, if you have a provincial event, and wish to look at a population within that province, you use a scope.

Country Scope: Triggers
all_core

Syntax:

all_core = { triggers... }

Scope:
Switches scope to all core provinces of the current country in scope - the triggers must be true for all core provinces for this to return true.

any_core

Syntax:

any_core = { triggers... }

Scope:
Switches scope to all core provinces of the current country in scope - the triggers must be true for one or more core provinces for this to return true.

any_greater_power

Syntax:

any_greater_power = { triggers... }

Scope:
Switches scope to any country which is currently a greater power.

any_neighbor_country

Syntax:

any_neighbor_country = { triggers… }

Scope:
Any country neighboring the current country.

any_owned_province

Syntax:

any_owned_province = { triggers… }

Scope:
Any owned province.

any_pop

Syntax:

any_pop = { triggers… }

Scope:
Any pop in the current country.

any_sphere_member

Syntax:

any_sphere_member = { triggers… }

Scope:
Changes the current scope to any country in your sphere. Localisation is missing from vanilla.

any_state

Syntax:

any_state = { triggers… }

Scope:
Changes the current scope to any owned region.

any_substate

Syntax:

any_substate = { triggers… }

Scope:
Changes the current scope to any substate (not vassal).


capital_scope

Syntax:

capital_scope = { triggers… }

Scope:
Changes the current scope to the country’s capital (thus changing it to province scope).

[country tag]

Syntax:

[tag] = { triggers… }

Scope:
Changes the current scope to the specified country.

cultural_union

Syntax:

cultural_union = { effects… }

Scope:
Changes the current scope to the cultural union of the nation in the previous scope.

overlord

Syntax:

overlord = { triggers...}

Scope:
Changes the scope for a vassal to its overlord country.

[region name]

Syntax:

[region name] = { triggers… }

Scope:
Changes the current scope to the specified region (the ones listed in map\regions.txt).

sphere_owner

Syntax:

sphere_owner = { triggers... }

Scope:
Changes the current scope to the sphere owner of the country.

war_countries

Syntax:

war_countries = { triggers...}

Scope:
Changes scope to all countries at war with the previously scoped country.

Province Scope: Triggers
any_core

Syntax:

any_core = { triggers... }

Scope:
Switches to the country scope of any cores inside the target province. So if the province has cores for Austria and Bohemia, then both those countries would now be in scope (whether they exist or not).

any_neighbor_province

Syntax:

any_neighbor_province = { triggers… }

Scope:
Any land province neighboring the current province. Note that this does not include empty provinces.

any_pop

Syntax:

any_pop = { triggers… }

Scope:
Any pop in the current province.

controller

Syntax:

controller = { triggers … }

Scope:
Changes the current scope to the province controller.

owner

Syntax:

owner = { triggers … }

Scope:
Changes the current scope to the owner of the province.

sea_zone

Syntax:

sea_zone = { triggers … }

Scope:
Changes the current scope to every neighbouring sea provinces.

state_scope

Syntax:

state_scope = { triggers … }

Scope:
Changes the current scope to the state which the province is in.

Pop Scope: Triggers
location

Syntax:

location = { triggers … }

Scope:
Changes the current scope to the province which the pop is in.

country

Syntax:

country = { effects… }

Scope:
Changes the current scope to the country this pop is part of.

cultural_union

Syntax:

cultural_union = { effects… }

Scope:
Changes the current scope to the cultural union of the nation in the previous scope.

Country Scope: Effects
all_core

Syntax:

all_core = { effects... }

Scope:
Changes the current scope to all provinces that are core to the current country (whether the country exists or not).

any_country

Syntax:

any_country = { effects… }

Scope:
Changes the current scope to all the currently available countries.

NOTE: This scope works differently in decisions and events. In decisions, it automatically refers to any existing countries (in fact, it cannot be used to target non-existing countries) and does not target the current country in scope. In events, it automatically refers to all country tags whether they currently exist or not (and would need a limit to specify otherwise), as well as the current country in scope.

any_greater_power

Syntax:

any_greater_power = { effects... }

Scope:
Changes the current scope to all countries which are currently greater powers.

NOTE: For the tooltip, this handily does not display the text of the scope and its conditions but rather lists every greater power individually which would be affected. So, rather than printing "Any greater power that is... NOT.. etc. etc." it would list "Russia: {effect}", "Austria: {effect}" and so forth, whoever is covered by the scope. If you'd prefer to have the tooltip display all the conditions, you should use any_country instead and just include "is_greater_power = yes" in the triggers.

any_owned

Syntax:

any_owned = { effects… }

Scope:
Changes the current scope to every owned province.

any_neighbor_country

Syntax:

any_neighbor_country = { effects… }

Scope:
Changes the current scope to all the neighboring countries.

NOTE: For the tooltip, this handily does not display the text of the scope and its conditions but rather lists every country that would be affected. So, rather than printing "Any neighbor country that is... NOT.. etc. etc." it would list "Russia: {effect}", "Austria: {effect}" and so forth, whoever is covered by the scope. If you'd prefer to have the tooltip display all the conditions, you should use any_country instead and just include "neighbour = THIS" in the triggers.

any_state

Syntax:

any_state = { effects… }

Scope:
Changes the current scope to every owned state.

capital_scope

Syntax:

capital_scope = { effects… }

Scope:
Changes the current scope to the country’s capital.

[country tag]

Syntax:

[tag] = { effects… }

Scope:
Changes the current scope to the specified country.

cultural_union

Syntax:

cultural_union = { effects… }

Scope:
Changes the current scope to the cultural union of the nation in the previous scope.

from

Syntax:

from = { effects… }

Scope:
Changes the scope to the country that triggered the current event.

overlord

Syntax:

overlord = { triggers...}

Scope:
Changes the scope for a vassal to its overlord country.

random_country

Syntax:

random_country = { effects... }

Scope:
Changes the current scope to a random existing country.

random_owned

Syntax:

random_owned = { effects… }

Scope:
Changes the current scope to a random owned province.

random_pop

Syntax:

random_pop = { triggers … }

Scope:
Changes the current scope to a random pop in the country. Can be limited by location.

[region name]

Syntax:

[region name] = { effects… }

Scope:
Changes the current scope to the specified region.

sphere_owner

Syntax:

sphere_owner = { triggers... }

Scope:
Changes the current scope to the sphere owner of the country.

Province Scope: Effects
any_neighbor_province

Syntax:

any_neighbor_province = { effects… }

Scope:
Changes the current scope to every neighbouring land province.

country

Syntax:

country = { effects… }

Scope:
Changes the current scope to the country to which this province belongs.

cultural_union

Syntax:

cultural_union = { effects… }

Scope:
Changes the current scope to the cultural union of the nation in the previous scope.

owner

Syntax:

owner = { effects… }

Scope:
Changes the current scope to the country to which this province belongs. Same as country scope from a province but more consistent with its corresponding trigger.

[province ID]

Syntax:

[province id] = { effects… }

Scope:
Changes the current scope to the specified province.

random_neighbor_province

Syntax:

random_neighbor_province = { effects… }

Scope:
Changes the current scope to a random neighbour province.

random_empty_neighbor_province

Syntax:

random_empty_neighbor_province = { effects… }

Scope:
Changes the current scope to random, empty neighbour province.

sea_zone

Syntax:

sea_zone = { effects … }

Scope:
Changes the current scope to every neighbouring sea provinces.


---

---
title: Government modding
category: guide
tags: [government, politics]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Government_modding
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


---

---
title: IF Emulation
category: guide
tags: [compatibility]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/IF_Emulation
---

In modern Paradox games (CK2 and later) and in any actual programming language, a mod developer can use if statements to enact effects if and only if a certain condition is met. In other words: if [condition] then [effect]. Victoria 2 and all older Paradox games do not have a dedicated if keyword, but the impact of an if statement can still be emulated.

## Goal

Modern Paradox games have if scopes that look like this:

```
if = {
    limit = {
        # conditions
    }
    # effects
}
else_if = {
    limit = {
        # conditions
    }
    # effects
}
else = {
    # effects
}
```

The above code does not work in Victoria 2 because if, else_if, and else are not valid. Instead, Victoria 2 modders must get creative with the options available in the game to emulate such logical behaviour.

## Workaround

The workaround for emulating if statements in Victoria 2 involves using scopes with a limit clause to ensure that only certain effects are applied if certain conditions are met.

Let's suppose you want an event that has two different possible effects, one if the country is free trade, the other if the country is protectionist. Without if emulation, you would have to write two different events, one for protectionist nations and the other for free trade nations, but with if emulation you need only write a single event. The option for the event would look something like this:

```
option = {
    name = "If free trade, lose prestige, if protectionist, gain prestige"
    random_owned = {
        limit = {
            owner = {
                trade_policy = free_trade
            }
        }
        owner = {
            prestige = -10
        }
    }
    random_owned = {
        limit = {
            owner = {
                trade_policy = protectionism
            }
        }
        owner = {
            prestige = 10
        }
    }
}
```

Note that the code above contains two if statements, not an if else statement.

## See Also

See https://eu3.paradoxwikis.com/IF_Emulation for further examples of code emulating if, though note the differences between EU3 and Victoria 2 code.


---

---
title: List of conditions
category: reference
tags: [scripting]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/List_of_conditions
---

This is a full list of conditions usable in event and decision scripting.

Conditions are pieces of script that ask simple logical questions, and return a yes/no answer. These are used in various situations, usually to determine whether or not the prerequisites are met for a certain action to occur.

For example:

trigger = {
	is_greater_power = yes
}


This example displays a trigger for an event. Events can fire only when their trigger requirements are met. This hypothetical event has a very simple trigger, it asks only one thing: is the country in question a great power? If it returns true (i.e. the country is in fact a great power) then they trigger is satisfied and the event may fire. Using Boolean commands and some clever scripting, commands can be used to create very complex sets of requirements. They are used in several different parts of event and decision scripting.

Commands are used for:

The "potential" and "allow" sections of decision scripting to determine when they may be presented to the player as an option
The "trigger" and "MTTH" (Mean Time to Happen) sections of event scripting to determine when they are eligible to fire and the chances of this happening
The "limit" section of effect (within either events or decisions) scripting to determine what the limits of an effect's reach are

Not all commands are useful in all situations. Commands are usually relevant to specific situations.

For example, the command:

religion = protestant

This command is applicable only when a pop is in question, and it therefore non-functional when applied to province, state, national level scripts. Keep the limits of commands in mind when scripting.

The list below is a comprehensive collection of these commands. Enjoy, and get to modding!

Boolean Operators

These are boolean operators. There are only three of them in Victoria 2, but they are extremely useful. Like any command, they can return true or false, but they are special in that they consist entirely of other commands. This makes them highly versatile. Expect to use these more than any other commands.

AND

This operator returns true only when every included statement returns true.

AND = {
	ai = no
	civilized = yes
}

This "and" operator will return true only if the country in question is not controlled by the ai (that is, it is player controlled), and it is civilized.

OR

This operator returns true when any of the included commands returns true.

OR = {
	government = democracy
	prestige = 50
}

This "or" operator will return true if the country in question is either a democracy or has 50 (or more) prestige.

NOT

This command is a little more tricky. It will return true if the included variable is false.

NOT = {
	slavery = yes
}

This "not" operator will return true if the country in question does not allow slavery. This may seem useless, because the scripter could simply use "slavery = no" to achieve the same thing. However, not all commands are so cut and dry as the "slavery" command. Consider the following:

NOT = { 
	num_of_allies = 3
}

This "not" operator will be satisfied only if the country does not have 3 or more allies; or, in more plain terms, if the country has 2 allies or less. Thus we can see that the "not" command is very useful in combination with any numerically-based command.

NOTE: If you include multiple statements within the same NOT operator, it returns true if ALL of the statements evaluate to false, and it returns false if just ONE or more statements evaluates to true. It is essentially the same as an AND operator, only the logic works with false statements instead of true statements.

Broad Commands
year

Syntax:

year = x

Use:
Returns true if x is the current year or a later year.

Range:
This command is usable in any circumstance.

month

Syntax:

month = x

Use:
Returns true if x is the current month or an earlier month.

Range:
This command is usable in any circumstance.

allow_multiple_instances

Syntax:

allow_multiple_instances = [yes/no]

Use:
This will allow multiple instances of the same event to fire to one country.

Range:
Usable for event triggers only.

fire_only_once

Syntax:

fire_only_once = [yes/no]

Use:
The event will fire only once in a game. Normal events will fire whenever their conditions are met, this event will only fire once under any circumstance.

Range:
Usable for event triggers only.

is_triggered_only

Syntax:

is_triggered_only = [yes/no]

Use:
This prevents the event from being put into the event stack in the code and makes it so it may only be triggered by another trigger, decision, or through the game's programming.
(NB: This also means you shouldn't include a trigger = { ... } parameter to your event, as it will be ignored. The only exception is with events triggered by the game's native-code, such as on-action election events.)

Range:
Usable for event triggers only.

major

Syntax:

major = yes

Use:
The event appears with a special window (with the country's flags by the title bar, and without a picture). This also means the event appears on the notifications, similar to how decisions do, with the prefix "Major Event".

Range:
Usable for events only.

immediate

Syntax:

immediate = { (effects) }


Use:
Before the option section, it makes the specified effects in its section happen the moment the event is fired and independent of any option.

Range:
Usable for events only.

check_variable

Syntax:

check_variable = {
which = [name of variable]
value = x
}


Use:
Returns true if the “variable name” has been set at an earlier stage and its value is greater than or equal to x. Note: Doesn't seem to work within the province scope.

has_global_flag

Syntax:

has_global_flag = [name of flag]

Use:
Returns true if the game has the specified global flag defined.

is_canal_enabled

Syntax:

is_canal_enabled = [1,2,3]

Use:
Returns true if the specified canal has been constructed. 1 = Kiel Canal, 2 = Suez Canal, 3 = Panama Canal.

Country Scope

These commands are useful at the country scope. They are applicable whenever the script is referring to a country.

administration_spending

Syntax:

administration_spending = x

Use:
Returns true if the current country invest x% or more in administration.

ai

Syntax:

ai = [yes / no]

Use:
Determines if the country in question is computer or human/player-controlled.

alliance_with

Syntax:

alliance_with = [tag/THIS/FROM]

Use:
Returns true if the country is allied with the specified country.

average_consciousness

Syntax:

average_consciousness = X

Use:
Returns true if the country overall has a consciousness average at or above X.

average_militancy

Syntax:

average_militancy = X

Use:
Returns true if the country overall has a militancy average at or above X.

badboy

Syntax:

badboy = X

Use:
Returns true if the country has an infamy of X. NOTE: Unlike with the effect, X in this case is not a straight integer. It's a percentage of 25 (the "infamy limit"). So 20 infamy is 0.8, and 50 infamy is 2.0.

big_producer (needs clarification)

Syntax:

big_producer = [name of trade good]

Use:
Returns true if the country is a big producer of the specified trade good (may mean this good is in the top 3 exported for the nation or may mean the nation is a top exporter of this good vs all other nations).

blockade

Syntax:

blockade = x

Use:
Returns true if the blockade percentage is equal to x or more.

brigades_compare

Syntax:

brigades_compare = X

Use:
Returns true if the current country has X or more in multiples of army brigades than the country in scope. Example: "brigades_compare = 2" inside an "any_country" scope, would return true for any country that had double the brigades or more than the current country

can_build_factory_in_capital_state

Syntax:

can_build_factory_in_capital_state = [name of factory]

Use:
Returns true if the capital state can build the specified factory. Real factory names can be found in common/buildings.txt (example: can_build_factory_in_capital_state = artillery_factory)

crime_higher_than_education

Syntax:

crime_higher_than_education = [yes/no]

Use:
Returns true if the administration spending slider is higher than the education spending slider.

can_nationalize

Syntax:

can_nationalize = [yes/no]

Use:
Returns true if the current country can nationalize their industry.

can_create_vassals

Syntax:

can_create_vassals = [yes/no]

Use:
Returns true if the current country can create a puppet state.

capital

Syntax:

capital = [province id]

Use:
Returns true if the specified capital is the current country’s capital.

casus_belli

Syntax:

casus_belli = [tag/THIS/FROM]

Use:
Returns true if the country in scope has any active casus belli against the target.

citizenship_policy

Syntax:

citizenship_policy = [policy]

Use:
Returns true if the country has the specified citizenship policy (from common\issues.txt) (example: "citizenship_policy = residency")

civilization_progress

Syntax:

civilization_progress = X

Use:
Returns true if the uncivilized country has progressed to X% of civilization reforms, with X being expressed as a decimal (between 0 and 1). NOTE: While this command displays on tooltips, the value of it does not. Be wary of using this in "allow" fields of decisions.

civilized

Syntax:

civilized = [yes/no]

Use:
Returns true if the current country is civilized.

colonial_nation

Syntax:

colonial_nation = [yes/no]

Use:
Returns true if the current country has colonies anywhere in the world.

constructing_cb_progress

Syntax:

constructing_cb_progress = X

Use:
Returns true if the country CB construction has progressed to X% or more, with X being expressed as a decimal (between 0 and 1).

constructing_cb_type

Syntax:

constructing_cb_type = (name of CB)

Use:
Returns true if the country is constructing the specified CB.

controls

Syntax:

controls = [province id]

Use:
Returns true if the current country controls the specified province.

crime_fighting

Syntax:

crime_fighting = x

Use:
Returns true if the current country invest x% or more in crime fighting.

crisis_exist *HOD ONLY*

Syntax:

crisis_exist = [yes/no]

Use:
Returns true if there is an active crisis somewhere in the world.

culture_has_union_tag

Syntax:

culture_has_union_tag = [yes/no]

Use:
Returns true if the scoped country's primary culture group has a defined cultural union tag/country.

diplomatic_influence

Syntax:

diplomatic_influence = {
	who = [THIS/FROM/TAG]
	value = x
}

Use:
Returns true if country has more than x diplomatic influence in the country in scope.

economic_policy

Syntax:

economic_policy = [policy]

Use:
Returns true if the country has the specified economic policy (from common\issues.txt) (example: "economic_policy = laissez_faire")

economic_reform

Syntax:

economic_reform_name = level
See common/issues.txt for list of uncivilized economic reforms and their levels
Example : land_reform = yes_land_reform means the uncivilized country has researched the Land Reform reform

Use:
Returns true if the country has a specific economic reform at a specific level

education_spending

Syntax:

education_spending = x

Use:
Returns true if the current country invest x% or more in education.

election

Syntax:

election = [yes/no]

Use:
Returns true if there is an ongoing election in the country.

exists

Syntax:

exists = [tag]

Use:
Returns true if the specified country exists. May also be used with [yes/no] to determine if the country in scope actually exists.

government

Syntax:

government = [government type]

Use:
Returns true if the country has the specified government type.

great_wars_enabled

Syntax:

great_wars_enabled = [yes/no]

Use:
Returns true if great wars are enabled.


have_core_in

Syntax:

have_core_in = [country tag]

Use:
Returns true if the country in scope has cores on any provinces of the specified nation.

has_country_flag

Syntax:

has_country_flag = [name of flag]

Use:
Returns true if the country in scope has the specified country flag.

has_country_modifier

Syntax:

has_country_modifier = [name of modifer]

Use:
Returns true if the current country has the specified modifier.

has_cultural_sphere *HOD ONLY*

Syntax:

has_cultural_sphere = [yes/no]

Use:
Returns true if the country in scope has any nations of our culture in their SOI.

has_leader

Syntax:

has_leader = [name of leader]

Use:
Returns true if the specified leader belongs to the current country.

has_recently_lost_war

Syntax:

has_recently_lost_war = [yes/no]

Use:
Returns true if the country in scope has recently lost a war within 5 years.

has_unclaimed_cores

Syntax:

has_unclaimed_cores = [yes/no]

Use:
Returns true if the country in scope has cores that are not owned by them.

[ideology]

Syntax:

[ideology] = x

Use:
Returns true if at least x% of the country’s population follows the specified ideology.
E.g. liberal = 10 will return true if population, NOT voter, support for liberal ideology is at least 10%. This is the same information as that displayed on the pop ideology pie charts in the politics and population screens.

ideology

Syntax:

ideology = [ideology type]

Use:
Returns true if the country’s ruling party belongs to the specified ideology.

industrial_score

Syntax:

industrial_score = x

Use:
Returns true if the country’s industrial score is equal to x or higher.

in_sphere

Syntax:

in_sphere = [tag/FROM/THIS]

Use:
Returns true if the country in scope is in the sphere of the target.

in_default

Syntax:

in_default = [yes/no]

Use:
Returns true if the country in scope has defaulted on debts.

invention

Syntax:

invention = [name of invention]

Use:
Returns true if the country knows the specified invention.

involved_in_crisis *HOD ONLY*

Syntax:

involved_in_crisis = [yes/no]

Use:
Returns true if the country in scope is participating in the current crisis (being "on-the-fence" counts).

is_claim_crisis *HOD ONLY*

Syntax:

is_claim_crisis = [yes/no]

Use:
Returns true if the current crisis is over claims on territory.

is_colonial_crisis

Syntax:

is_colonial_crisis = [yes/no]

Use:
Returns true if the current crisis is over uncolonized land.

is_core

Syntax:

is_core = [province id]

Use:
Returns true if the specified province is a core of the current country.

is_cultural_union

Syntax:

is_cultural_union = [tag/FROM/THIS]

Or

is_cultural_union = [yes/no]

Use:
Returns true if the country in scope is a cultural union country, like Germany, Romania and Italy.

is_culture_group

Syntax:

is_culture_group = [culture/tag/FROM/THIS]

Use:
Returns true if the country in scope has a primary culture of the specified culture group, or if a country is provided, equal to the culture group of the primary culture of that country.

is_disarmed

Syntax:

is_disarmed = [yes/no]

Use:
Returns true if the current country has been disarmed (via the Cut Down to Size casus belli).

is_greater_power

Syntax:

is_greater_power = [yes/no]

Use:
Returns true if the current country is a greater power.

is_ideology_enabled

Syntax:

is_ideology_enabled = ideology
Example : is_ideology_enabled = socialism means socialism is active in the country

Use:
Returns true if the ideology is active in the nation

is_independant

Syntax:

is_independant = [yes/no]

Use:
Determines whether the country is puppet or not. Difference to is_vassal is unknown. Independent is supposed to be spelled wrong: independent

is_liberation_crisis *HOD ONLY*

Syntax:

is_liberation_crisis = [yes/no]

Use:
Returns true if the current crisis a liberation crisis to liberate an entire nation.

is_mobilised

Syntax:

is_mobilised = [yes/no]

Use:
Determines whether the country has mobilised or not.

is_next_reform

Syntax:

is_next_reform = [reform type]

Use:
Returns true if the next reform is the specified reform (if healthcare is no healthcare, then the next reform would be trinket healthcare).

is_our_vassal

Syntax:

is_our_vassal = [tag/THIS/FROM]

Use:
Returns true if the specified country is a vassal of the country in scope.

is_possible_vassal

Syntax:

is_possible_vassal = (tag)

Use:
Returns true if the specified country can be released as a puppet state (meaning do they own the target's capital?).

is_secondary_power

Syntax:

is_secondary_power = [yes/no]

Use:
Returns true if the current country is a secondary power.

is_sphere_leader_of

Syntax:

is_sphere_leader_of = [tag/FROM/THIS]

Returns true if the country in scope is the sphere owner of the target.

is_vassal

Syntax:

is_vassal = [yes/no]

Use:
Returns true if the current country is a puppet.


is_substate

Syntax:

is_substate = [yes/no]

Use:
Returns true if the current country is a substate.

literacy

Syntax:

literacy = x

Use:
Returns true if the average literacy of the country is greater than or equal to the specified amount.

lost_national

Syntax:

lost_national = x

Use:
Returns true if the number of core provinces that a country has lost is equal to x or more.

middle_strata_everyday_needs

Syntax:

middle_strata_everyday_needs = X

Use:
Returns true if the country's middle strata are getting X% of their everyday needs, with X being a value between 0 and 1.

middle_strata_life_needs

Syntax:

middle_strata_life_needs = X

Use:
Returns true if the country's middle strata are getting X% of their life needs, with X being a value between 0 and 1.

middle_strata_luxury_needs

Syntax:

middle_strata_luxury_needs = X

Use:
Returns true if the country's middle strata are getting X% of their luxury needs, with X being a value between 0 and 1.

middle_tax

Syntax:

middle_tax = x

Use:
Returns true if percentage of tax paid by the middle strata is equal to x% or more.

military_access

Syntax:

military_access = [tag/THIS/FROM]

Use:
Returns true if the target country has military access to the scoped country.

military_reform

Syntax:

military_reform_name = level
See common/issues.txt for list of uncivilized military reforms and their levels
Example : foreign_training = yes_foreign_training means the uncivilized country has researched the Foreign Training reform

Use:
Returns true if the country has a specific military reform at a specific level

military_score

Syntax:

military_score = x

OR

military_score = [tag/THIS/FROM]

Use:
Returns true if the country’s military score is equal to x or higher.

military_spending

Syntax:

military_spending = x

Use:
Returns true if the current country invest x% or more in the military.

money

Syntax:

money = x

Use:
Returns true if the amount of money a country has in their treasury is equal to x or more.

nationalvalue

Syntax:

nationalvalue = [national value]

Use:
Returns true if the current country’s national value is equal to the national value specified (using the value in the nationalvalues.txt file... so Liberty would be "nv_liberty".

national_provinces_occupied

Syntax:

national_provinces_occupied = x

Use:
Returns true if a foreign power occupies x% or more of the current country’s provinces.

neighbour

Syntax:

neighbour = [tag/FROM/THIS]

Use:
Returns true if the current country is a neighbour to the specified country.

num_of_allies

Syntax:

num_of_allies = x

Use:
Returns true if the country has x or more allies.

num_of_cities

Syntax:

num_of_cities = x

Use:
Returns true if the country has x or more cities (aka provinces – inherited from EU3).

num_of_ports

Syntax:

num_of_ports = x

Use:
Returns true if the country has x or more ports.

num_of_revolts

Syntax:

num_of_revolts = x

Use:
Returns true if there are x or more revolts in the country (x being the number of states under rebel control).

number_of_states

Syntax:

number_of_states = x

Use:
Returns true if the number of states a country has is equal to x or more.

num_of_substates

Syntax:

num_of_substates = x

Use:
Returns true if the number of substates a country has is equal to x or more.

num_of_vassals

Syntax:

num_of_vassals = x

Use:
Returns true if the number of puppets a country has is equal to x or more.

num_of_vassals_no_substates

Syntax:

num_of_vassals_no_substates = x

Use:
Returns true if the number of puppets that are not substates a country has is equal to x or more.

owns

Syntax:

owns = [province id]

Use:
Returns true if the country owns the specified province.

part_of_sphere

Syntax:

part_of_sphere = [yes/no]

Use:
Determines whether the country in scope is part of ANY great power's sphere.


[party_issue]

Syntax:

[party_issue] = x

Use:
Returns true if total population support for the party issue is at least x%.
(E.g. moralism = 10 will return true if population, NOT voter, support for moralism is at least 10%).

political_movement_strength

Syntax:

political_movement_strength = x

Use:
Checks if there is any political movement with x or more support. The support is calculated by dividing the supporters by the total amount of POPs and then multiplying by MOVEMENT_SUPPRT_UH_FACTOR in defines.lua (default is 3). So for a country with 150000 POPs and a political movement with 5000 supporters, the political_movement_strength would be 3 * 5000 / 150000 = 10% (0.10).

political_reform

Syntax:

political_reform_name = level
See common/issues.txt for list of social reforms and their levels
Example : vote_franchise = wealth_weighted_voting means the country currently has its voting rights set at weighted wealth voting

Use:
Returns true if the country has a specific political reform at a specific level

political_reform_want

Syntax:

political_reform_want = 0.xx

Use:
Returns true if x% or more of the population wants a social reform, x being a value between 0.00 and 1.00

poor_strata_everyday_needs

Syntax:

poor_strata_everyday_needs = X

Use:
Returns true if the country's poor strata are getting X% of their everyday needs, with X being a value between 0 and 1.

poor_strata_life_needs

Syntax:

poor_strata_life_needs = X

Use:
Returns true if the country's poor strata are getting X% of their life needs, with X being a value between 0 and 1.

poor_strata_luxury_needs

Syntax:

poor_strata_luxury_needs = X

Use:
Returns true if the country's poor strata are getting X% of their luxury needs, with X being a value between 0 and 1.

poor_tax

Syntax:

poor_tax = x

Use:
Returns true if percentage of tax paid by the poor strata is equal to x% or more.

pop_majority_culture

Syntax:

pop_majority_culture = (culture)

Use:
Returns true if the majority of a nation's population is of the specified culture.

pop_majority_ideology

Syntax:

pop_majority_ideology = (ideology)

Use:
Returns true if the majority of a nation's population has the specified ideology.

pop_majority_religion

Syntax:

pop_majority_religion = (religion)

Use:
Returns true if the majority of a nation's population has the specified religion.

pop_militancy

Syntax:

pop_militancy = x

Use:
Returns true if any pop in the province has a militancy value equal to x or higher.

[poptype]

Syntax:

[poptype] = x

Use: Returns true if the specified poptype has x% of the total population in the country (x expressed as a value between 0 and 1). Example: "soldiers = 0.05" would return true if soldiers made up 5% or more of the country's population.

prestige

Syntax:

prestige = x

Use:
Returns true if the country has a prestige value equal to x or higher.

primary_culture

Syntax:

primary_culture = [culture]

Use:
Returns true if the country has the specified culture as its primary culture.

accepted_culture

Syntax:

accepted_culture = [culture]

Use:
Returns true if the country has the specified culture as its accepted culture.

plurality

Syntax:

plurality = x

Use:
Returns true if the country has plurality value equal to x or higher.

produces

Syntax:

produces = nameofgood

Use:
Returns true if the country produces the specified industrial or RGO good

rank

Syntax:

rank = x

Use:
Returns true if the country's rank is equal to x or greater

rebel_power_fraction

Syntax:

rebel_power_fraction = x

Use:
Returns true if any rebel has a power (muscle flexing icon, not revolt risk, which has the rebel flag) of at least x%. Would not recommend going too high as pops tend to rebel before their power gets high (revolt risk tends to climb faster than power).

recruited_percentage

Syntax:

recruited_percentage = x

Use:
Returns true if the percentage of recruited regiments is at least x%.

relation

Syntax:

relation = { who = [tag/this/from] value = x }

Use:
Returns true if the specified country has a relation value equal to x or higher with the specified country.

religious_policy

Syntax:

religious_policy = [policy]

Use:
Returns true if the country has the specified religious policy (from common\issues.txt) (example: "religious_policy = moralism")

revolt_percentage

Syntax:

revolt_percentage = x

Use:
Returns true if the percentage of revolts in the country is equal to x or higher.

rich_strata_everyday_needs

Syntax:

rich_strata_everyday_needs = X

Use:
Returns true if the country's rich strata are getting X% of their everyday needs, with X being a value between 0 and 1.

rich_strata_life_needs

Syntax:

rich_strata_life_needs = X

Use:
Returns true if the country's rich strata are getting X% of their life needs, with X being a value between 0 and 1.

rich_strata_luxury_needs

Syntax:

rich_strata_luxury_needs = X

Use:
Returns true if the country's rich strata are getting X% of their luxury needs, with X being a value between 0 and 1.

rich_tax

Syntax:

rich_tax = x

Use:
Returns true if percentage of tax paid by the rich strata is equal to x% or more.

rich_tax_above_poor

Syntax:

rich_tax_above_poor = [yes/no]

Use:
Returns true if percentage of tax paid by the rich strata is greater than the percentage of tax paid by the poor strata.

ruling_party

Syntax:

ruling_party = [tag]

Use:
Returns true if the ruling party is equal to tag.

ruling_party_ideology

Syntax:

ruling_party_ideology = [ideology]

Use:
Returns true if the ruling party of the current country belongs to the specified ideology. This is not a valid condition for ideologies.txt.

slavery

Syntax:

slavery = yes_slavery/no_slavery

Use:
Returns true if the current country allows slavery or not.

social_movement_strength

Syntax:

social_movement_strength= 0.xx

Use:
See political_movement_strength

social_reform

Syntax:

social_reform_name = level
See common/issues.txt for list of social reforms and their levels
Example : wage_reform = trinket_wage means the country currently has its wage level set at trikets

Use:
Returns true if the country has a specific social reform at a specific level

social_reform_want

Syntax:

social_reform_want = 0.xx

Use:
Returns true if x% or more of the population wants a social reform, x being a value between 0.00 and 1.00

social_spending

Syntax:

social_spending = x

Use:
Returns true if the current country is investing x% or more in social issues.

stronger_army_than

Syntax:

stronger_army_than = [tag/this/from]

Use:
Returns true if the current country has a stronger army than the specified country.


substate_of

Syntax:

substate_of = [tag/this/from]

Use:
Returns true if the current country is a substate of the specified country.

tag

Syntax:

tag = [country tag]

Use:
Returns true if the current country has a country tag that matches the specified tag.

[technology]

Syntax:

[technology name] = 1

Use:
Is a boolean that returns true if the country has researched the specified technology (example: "state_n_government = 1")

this_culture_union *HOD ONLY*

Syntax:

this_culture_union = [country tag] / THIS / FROM / this_union

Use:
Returns true if the nation specified has the same cultural union as the country in scope.

total_amount_of_divisions

Syntax:

total_amount_of_divisions = x

Use:
Returns true if the number of divisions belonging to a country is equal to x or more. Note: An army needs at least 2 brigades to count as a division.

total_amount_of_ships

Syntax:

total_amount_of_ships = x

Use:
Returns true if the number of ships belonging to a country is equal to x or more.

total_defensives

Syntax:

total_defensives = x

Use:
Returns true if the current country is currently involved in x or more defensive battles.

total_num_of_ports

Syntax:

total_num_of_ports = x

Use:
Returns true if the current country controls x or more ports.

total_offensives

Syntax:

total_offensives = x

Use:
Returns true if the current country is currently involved in x or more offensive battles.

total_of_ours_sunk

Syntax:

total_of_ours_sunk = x

Use:
Returns true if the number of sunken ships belonging to the current country is equal to x or more.

total_pops

syntax:

TAG = { total_pops = N }

use:
Returns true if the tag has equal or more pops than N.

total_sea_battles

Syntax:

total_sea_battles = x

Use:
Returns true if the number of sea battles currently undertaken is equal to x or more.

total_sunk_by_us

Syntax:

total_sunk_by_us = x

Use:
Returns true if the total number of ships sunk by the current country is equal to x or more.

trade_policy

Syntax:

trade_policy = [policy]

Use:
Returns true if the country has the specified trade policy (from common\issues.txt) (example: "trade_policy = free_trade")

truce_with

Syntax:

truce_with = [tag/this/from]

Use:
Returns true if the current country has a truce with the specified country.

unemployment

Syntax:

unemployment = x

Use:
Returns true if the unemployment percentage is equal to x or higher.

unit_has_leader

Syntax:

unit_has_leader = [yes/no]

Use:
Returns true if any unit in the current country has a leader.

unit_in_battle

Syntax:

unit_in_battle = [yes/no]

Use:
Returns true if the country has any unit that is fighting a battle.

upper_house

Syntax:

upper_house = {
                                          ideology = name
                                          value = 0.x  
			}
where value is a fraction 0.0 to 1.0, so value 0.4 = 40% has that ideology

Use:
Returns true if the country's upper house has the required characteristics

vassal_of

Syntax:

vassal_of = [tag/this/from]

Use:
Returns true if the current country is a puppet state to the specified country.

war

Syntax:

war = [yes/no]

Use:
Returns true if the current country is at war.

war_exhaustion

Syntax:

war_exhaustion = x

Use:
Returns true if the country’s war exhaustion is equal to x or above.

war_policy

Syntax:

war_policy = [policy]

Use:
Returns true if the country has the specified war policy. E.g. Pacifism.

war_score

Syntax:

war_score = x

Use:
Returns true if any war score a country is involved in is at least x%.

war_with

Syntax:

war_with = [tag/FROM/THIS]

Use:
Returns true if the current country is at war with the specified country.

Province Scope
average_consciousness

Syntax:

average_consciousness = X

Use:
Returns true if the province has a consciousness average at or above X.

average_militancy

Syntax:

average_militancy = X

Use:
Returns true if the province has a militancy average at or above X.

can_build_factory

Syntax:

can_build_factory = [yes/no]

Use:
Returns true if the province in scope can construct a factory if the owner has the capability to do so.
(The tooltip displays "can not build factory". This is probably a mistake in the text.csv localization file.)

continent

Syntax:

continent = [name of continent]

Use:
Returns true if the current province belongs to the specified continent.

controlled_by

Syntax:

controlled_by = [tag/FROM/THIS]

Use:
Returns true if the specified country controls the current province.

controlled_by_rebels

Syntax:

controlled_by_rebels = [yes/no]

Use:
Determines whether the province is currently under rebel control (you may also use "controlled_by = REB").

country_units_in_province

Syntax:

country_units_in_province = [tag/FROM/THIS]

Use:
Returns true if the specified country has any units in the current province.

country_units_in_state

Syntax:

country_units_in_state = [tag/FROM/THIS]

Use:
Returns true if the specified country has any units in the current state. Localisation for the state may be broken.

crime_fighting

Syntax:

crime_fighting = x

Use:
Returns true if the current country invest x% or more in crime fighting.

education_spending

Syntax:

education_spending = x

Use:
Returns true if the current country invest x% or more in education.

empty

Syntax:

empty = [yes/no]

Use:
Returns true if the current province is empty (uncolonized).

flashpoint_tension *HOD ONLY*

Syntax:

flashpoint_tension = x

Use:
Returns true if the flashpoint tension in the province is greater than or equal to the specified amount.

has_building

Syntax:

has_building = [building type]

Use:
Returns true if the current province has the specified building.

has_crime

Syntax:

has_crime = [crime type]

Use:
Returns true if the province has the specified crime.

has_culture_core (needs clarification)

Syntax:

has_culture_core = [yes/no]

Use:
Returns true if the pop in scope has the same culture as one of the core nations in the province. IE Mexican culture in California will receive a -20 factor to assimilation in American owned California until USA removes the Mexican cores.

has_empty_adjacent_province

Syntax:

has_empty_adjacent_province = [yes/no]

Use:
Returns true if the current province has an empty adjacent province.

has_empty_adjacent_state

Syntax:

has_empty_adjacent_state = [yes/no]

Use:
Returns true if the current province has an empty adjacent state.

has_factories

Syntax:

has_factories = [yes/no]

Use:
Returns true if the province in scope has any factories.

has_flashpoint

Syntax:

has_flashpoint = [yes/no]

Use:
Returns true if the province has flashpoint tension.

has_national_minority

Syntax:

has_national_minority = [yes/no]

Use:
Returns true if there are pops of different cultures in the province.

has_pop_type

Syntax:

has_pop_type = [pop type]

Use:
Returns true if the current province has any pops of the specified type.

has_province_flag

Syntax:

has_province_flag = [name of flag]

Use:
Returns true if the province in scope has the specified province flag. Note: Doesn't seem to work correctly, usually returning true even if the province doesn't have the flag.

has_province_modifier

Syntax:

has_province_modifier = [name of modifier]

Use:
Returns true if the current province has the specified modifier. This is not a valid condition for the POP files.

has_recent_imigration

Syntax:

has_recent_imigration = X 

Use:
Returns true if the current province has received any immigrants in the past X days.

[ideology]

Syntax:

[ideology] = x

Use:
Returns true if at least x% of the province’s population follows the specified ideology.
E.g. liberal = 10 will return true if population, NOT voter, support for liberal ideology is at least 10%. This is the same information as that displayed on the pop ideology pie chart in the population screen for that province.

is_accepted_culture

Syntax:

is_accepted_culture = [yes/no]

Use:
Returns true if the province's majority culture is the same as the owning country's accepted culture(s).
NB: You can also specify a country tag to the command (including THIS/FROM) and it will return true if the majority culture is the same as the specified country's accepted culture(s).

is_blockaded

Syntax:

is_blockaded = [yes/no]

Use:
Returns true if the province is blockaded.

is_capital

Syntax:

is_capital = [yes/no]

Use:
Returns true if the current province is a capital.

is_coastal

Syntax:

is_coastal = [yes/no]

Use:
Determines whether the province is on a coast (note this means any body of water, even an inland lake—if you want to determine if it's a province that could build a port, use the port command).

is_colonial

Syntax:

is_colonial = [yes/no]

Use:
Returns true if the current province is a colonial province or not

is_core

Syntax:

is_core = [tag/THIS/FROM]

Use:
Returns true is the current province is has a core belonging to the specified country.

is_ideology_enabled

Syntax:

is_ideology_enabled = [ideology type]

Use:
Returns true if the specified ideology has been enabled.

is_overseas

Syntax:

is_overseas = [yes/no]

Use:
Returns true if the specified province is overseas (defined by the game as being on a different continent and not contiguous with the country's non-overseas provinces).

is_primary_culture

Syntax:

is_primary_culture = [yes/no]

Use:
Returns true if the province's majority culture is the same as the owning country's primary culture.
NB: You can also specify a country tag to the command (including THIS/FROM) and it will return true if the majority culture is the same as the specified country's primary culture.

is_state_capital

Syntax:

is_state_capital = [yes/no]

Use:
Returns true if the province in is the state (the region) capital.

is_state_religion (needs clarification)

Syntax:

is_state_religion = [yes/no]

Use:
Likely returns true if the state which the province resides has a religious majority of the primary religion of the nation that owns it.

life_rating

Syntax:

life_rating = x

Use:
Returns true if the life rating in the province is greater than or equal to the specified amount.

literacy

Syntax:

literacy = x

Use:
Returns true if the average literacy in the province is greater than or equal to the specified amount.

military_spending

Syntax:

military_spending = x

Use:
Returns true if the current country are investing x% or more in the military.

minorities

Syntax:

minorities = [yes/no]

Use:
Returns true if there are pops of a non-accepted culture in the province.

owned_by

Syntax:

owned_by = [tag/FROM/THIS]

Use:
Returns true if the specified country owns the current province.

pop_militancy

Syntax:

pop_militancy = x

Use:
Returns true if any pop in the province has a militancy value equal to x or higher.

port

Syntax:

port = [yes/no]

Use:
Returns true if the current province has a port (even if it's level 0). Note that the main use for this, as opposed to is_coastal, is that it specifically returns true for provinces that COULD build a port, as opposed to provinces that border a body of water even if it's an inland lake.

province_control_days

Syntax:

province_control_days = X

Use:
Returns true if the province has been controlled for X number of days by someone other than the owner.

province_id

Syntax:

province_id = [province id]

Use:
Returns true if current province has the specified ID.

region

Syntax:

region = [name of region]

Use:
Returns true if the province belongs to the specified region. Note: In regions.txt provinces can be assigned to multiple regions, which can be used here. Only the first assigned region will be used for normal ingame activites. A region is more commonly referred to as a state.

state_id

Syntax:

state_id = [province id]

Use:
Returns true if the specified province belongs to the same state as the province in the current scope.

terrain

Syntax:

terrain = [terrain type]

Use:
Returns true if the province in scope has the specified terrain type (from map\terrain.txt).

trade_goods

Syntax:

trade_goods= [type]

Use:
Returns true if the trade good in the province matches “type”.

total_pops

syntax:

total_pops = [number]

use:
Returns true if the total pops in provinces match the specified number.

unemployment

Syntax:

unemployment = 0.xx 

Use:
Returns true if there is x% or more unemployment in the province, valued between 0.00 and 1.00

unemployment_by_type

Syntax:

unemployment_by_type = {
	type = [poptype]
	value = x
}


Use:
Returns true if there is x% unemployment for pops of that poptype (with x between 0 and 1).

Example:

unemployment_by_type = {
	type = farmers
	value = 0.5 
}


This would return true if farmers in the province were more than 50% unemployed.

units_in_province

Syntax:

units_in_province = x

Use:
Returns true if there are x or more units in the current province.

work_available

Syntax:

work_available = {
			worker = [type]
}

Use:
Returns true if there is any work available for the specified pop type—meaning specifically is it possible for that pop type to be employed, not whether they would actually find work there or whether there's any unemployment in the province. If a province has factories, this command will always return true for craftsmen and clerks. If the province produces coal, this command will always return true for labourers and false for farmers.

Pop Scope
agree_with_ruling_party

Syntax:

agree_with_ruling_party = X

Use:
Returns true if the POP agrees with at least X percentage (a range of 0.0 to 1.0) of their ruling party's platform issues.

cash_reserves

Syntax:

cash_reserves = x

Use:
Returns true if any pop in the province has a cash reserve equal to the cost of x percentage of their daily needs.

consciousness

Syntax:

consciousness = x

Use:
Returns true if the consciousness value is equal to x or higher.

culture

Syntax:

culture = [culture name]

Use:
Province Scope Effects: Returns true if there is a majority of the specified culture in the specified province.
POP Scope Effects: Warning! Only returns true if there is a majority of the specified culture in the POP's province. To check if the POP itself has the culture, use "has_pop_culture" instead.

everyday_needs

Syntax:

everyday_needs = x

Use:
Returns true if any pop in the province has everyday needs equal to x or more.

has_pop_culture

syntax:

has_pop_culture = [culture] [THIS]

Use:
Returns true if any pop in scope has the specified culture.

has_pop_religion

Syntax:

has_pop_religion = [religion] [THIS]

Use:
Returns true if any pop in scope has the specified religion.

is_primary_culture

Syntax:

is_primary_culture = [yes/no]

Use:
Returns true if culture of the pop in scope is the same as the primary culture of the nation they reside in.
NB: You can also specify a country tag to the command (including THIS/FROM) and it will return true if the culture of the pop in scope matches the primary culture of the country specified.

is_accepted_culture

Syntax:

is_accepted_culture = [yes/no]

Use:
Returns true if culture of the pop in scope is the same as the accepted culture(s) of the nation they reside in.
NB: You can also specify a country tag to the command (including THIS/FROM) and it will return true if the culture of the pop in scope matches the accepted culture(s) of the country specified.

is_culture_group

Syntax:

is_culture_group = [culture/tag/FROM/THIS]

Use:
Returns true if the pop in scope is of the specified culture group, or if a country is specified, equal to the culture group of the primary culture of that country.

is_state_religion

Syntax:

is_state_religion = [yes/no]

Use:
Returns true if the pop in question has the same religion as the state religion.

life_needs

Syntax:

life_needs = x

Use:
Returns true if any pop in the province life needs equal to x or more.

literacy

Syntax:

literacy = x

Use:
Returns true if the literacy value is equal to x or higher.

luxury_needs

Syntax:

luxury_needs = x

Use:
Returns true if any pop in the province has a luxury need equal to x or more.

militancy

Syntax:

militancy = x

Use:
Returns true if the militancy value is equal to x or higher.

money

Syntax:

money = x

Use:
Returns true if any pop in the province has a cash reserve equal to x or higher. Note: Though this condition displays properly in tooltips, it doesn't seem to actually work.

political_movement

Syntax:

political_movement= [yes/no]

Use:
Returns true if the pop is currently part of any political movement.

political_reform_want

Syntax:

political_reform_want = x

Use:
Returns true if the pop in scope has a political reform want percentage greater than or equal to the specified amount.

pop_majority_culture

Syntax:

pop_majority_culture = (culture)

Use:
Returns true if the majority of the pop(s) are of the specified culture.

pop_majority_ideology

Syntax:

pop_majority_ideology = (ideology)

Use:
Returns true if the majority of the pop(s) have the specified ideology.

pop_majority_issue

Syntax:

pop_majority_issue = (issue type)

Use:
Returns true if the majority of a nation's population/if the majority of the pop(s) have the specified majority issue.

pop_majority_religion

Syntax:

pop_majority_religion = (religion)

Use:
Haven't tested, but presumably returns true if the majority of the pop(s) have the specified religion.

religion

Syntax:

religion = [religion name]

Use:
Returns true if the pop's cultural government has the specified state religion. See cultural union in common\cultures.txt

social_movement

Syntax:

social_movement = [yes/no]

Use:
Returns true if the pop is currently part of any social movement.

social_reform_want

Syntax:

social_reform_want = x

Use:
Returns true if the pop in scope has a social reform want percentage greater than or equal to the specified amount.

strata

Syntax:

strata = [poor/middle/rich]

Use:
Returns true if the pop is of the specified strata.

type

Syntax:

type= [type]

Use:
Returns true if there are any pop types of the specified “type”.

unemployment

Syntax:

unemployment = x

Use:
Returns true if the unemployment percentage is equal to x or higher.


---

---
title: Localisation
category: other
tags: [localization]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Localisation
---

Localisation is an important part of Victoria 2's modding system. It connects the variable 'keys' used in the game's internal code and external scripting system with readable text, and also allows translation into multiple languages. Thus it controls the naming of everything from countries to parties to tech in Victoria 2.

The localisation files

In the Victoria 2 folder, you can find the localisation folder. In here is a long list of documents in csv format. The csv format can be edited in excel or similar software.

The files can be quite chaotic to navigate. They are named after the patch in which the name was first defined. Each 'type' of name is generally stored together (names of countries together, event texts together etc.), but not always. All the possible names for e.g. California is stored across 3 different files. You will have to use the search function a lot.

Note that many concepts multiple related texts-blurbs e.g. both a proper name and an adjective or the text for multiple buttons. They are usually stored next to each other or at least in the same section.

Basics

A localisation looks like this (only English, French and German are officially supported and only the default English localisation is generally correct):

key;English;French;German;Polish;Spanish;Italian;Swedish;Czech;Hungarian;Dutch;Portugese;Russian;Finnish;

For example, this is the localisation for the single player button in the main menu:

FE_SINGLE_PLAYER;Single Player;Solo;Einzelspieler;Gra pojedyncza;Un jugador;Giocatore singolo;Egyjátékos mód;Hra pro jednoho hráèe;;;;;;x;;;;

Some commands in Paradox Script create localisation keys.

Events

Events are localised through these three script commands: title, desc, name (the latter in an option code block).
The commands assign keys like this: command = "key". The quotation marks are optional, but it is standard practice to include them.

country_event = {
    id = 100
    title = "EVTNAME100"
    desc = "EVTDESC100"

    option = {
        name = "EVTOPTA100"
    }

    option = {
        name = "EVTOPTB100"
    }
}


The assigned keys can be any arbitrary string, but should follow the above standard: "EVTNAME[ID]" for the title, "EVTDESC[ID]" for the description, and "EVTOPT[A-F][ID]" for options.

The subtitles of election events are localised by adding _sub to the event's title key.

Decisions

Decisions are automatically localised using the name of the decision as defined through the script with the extensions _title and _desc.

Countries

Countries has both a proper name under TAG and it's adjective under TAG_ADJ.

Countries can change names depending on government type. Example:

tag_absolute_monarchy;name(English);name(French);name(German);;name(Spanish);;;;;;;;;x;

CAL_absolute_monarchy;Kingdom of California;Royaim de California;Kingdom of California;;Reino de California;;;;;;;;;x;'


Normally, events and deceisions can only have one localisation - or in other words, one specific event or decision has only one specific localisation key associated with it with is associated with only one piece of text. However, the change_region_name effect can be abused to write decisions, events, or tooltips with localisation that changes depending on in-game circumstances. For more information, see Dynamic localisation.


---

---
title: Map modding
category: guide
tags: [map]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Map_modding
---


This page contains information on the map files.


Province map
map\provinces.bmp
Terrain map
map\terrain.bmp
River map
map\rivers.bmp

Rivers run from a source, indicated by a green pixel, to the ocean. Rivers can combine with other rivers using red pixels. Rivers are drawn with a spectrum of blue colours which indicate the river's length at that position - darker blues resulting in wider rivers, cyan blues resulting in thinner rivers.

Editing the river map is best done with GIMP, which allows you finer controls when exporting the resulting .bmp file. Ensure you have the compatibility option "Do not write color space information" ticked.

Map elements
Adjacencies
Climate
Continent
Positions
States
Terrain types


---

---
title: .mod file
category: other
tags: [structure]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/mod_file
---

The .mod file is the file that tells the game what a mod is called and where to find it. The file should be located in the mod subfolder of the game directory, alongside the mod's file folder.

Structure

The following lines are mandatory and should be arranged as follows:

name = "modName"
path = "mod/modDirectory"
user_dir = "modDirectory"


Optionally, you can declare that your mod is a dependency of another mod. In this case, the base mod is loaded before the secondary mod. Dependencies still require .mod files themselves but do not need to redefine the user_dir.

dependencies = { "baseMod" }


Optionally, you can add additional lines to direct the game to treat the mod files how you wish them to be treated. For example, the replace_path label indicates that none of the base game files in a given directory will be loaded for the mod. If that label is not given, the base game files will be loaded by default.

replace_path = "events"


---

---
title: Modifier effects
category: reference
tags: [scripting]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Modifier_effects
---

List of the variables that modifiers can affect. It is mainly used in modding or to understand the files, if you want to read the exact effects of decisions, events and so forth.

Country Modifiers
administrative_efficiency_modifier

Increases or reduces the country's administrative efficiency modifier. Affects states as well as the country wide admin efficiency.

Syntax:

administrative_efficiency_modifier = n

where n = -0.1 is -0.1 admin efficiency or, in other words, -10% admin efficiency.

badboy

Fixed increase or decrease in infamy at the start of every month.

Syntax:

 badboy = n

where n = -0.1 is -0.1 infamy

cb_generation_speed_modifier

Percentage increase/decrease in the rate at which CB's are justified by a country.

Syntax:

cb_generation_speed_modifier = n

where n = 0.1 is a 10% increase in the speed.

core_pop_(trait)_modifer

Monthly increase or decrease in (trait) for all pops in core provinces (can be consciousness or militancy).

Syntax:

core_pop_militancy_modifier = n

where n = 1 would add 1 MIL each month.

diplomatic_points_modifier

Percentage change in the monthly diplomatic points given to the country.

Syntax:

diplomatic_points_modifier = n

where n = 0.1 would be a 10% increase in diplomatic points.

education_efficiency_modifier *AHD ONLY*

Percentage change in the country's education efficiency.

Syntax:

education_efficiency_modifier = n

where n = 0.1 would be a 10% increase in efficiency.

factory_cost

Percentage increase/decrease in the cost of factories for the country.

Syntax:

factory_cost = n

where n = 0.1 is a 10% increase in factory cost.

factory_input

Percentage change in the input of all factories in the country.

Syntax:

factory_input = n

where n = 0.1 is a 10% increase in input.

factory_output

Percentage change in the output of all factories in the country.

Syntax:

factory_output = n

where n = 0.1 is a 10% increase in output.

factory_owner_cost

Percentage increase/decrease in the cost of factories for the country.

Syntax:

factory_owner_cost = n

where n = 0.1 is a 10% increase in factory cost.

factory_throughput

Percentage change in the throughput of all factories in the country.

Syntax:

factory_throughput = n

where n = 0.1 is a 10% increase in throughput.

global_assimilation_rate

Percentage change in the assimiliation rate of foreign culture pops in a country.

Syntax:

global_assimilation_rate = n

where n = 0.1 would be a 10% increase.

global_immigrant_attract

Increases or decreases the attractiveness of the country to prospective immigrants.

Syntax:

global_immigrant_attract = n

where n = 1 would be a 100% increase.

global_pop_(trait)_modifier

Monthly increase or decrease in (trait) for all pops (can be consciousness or militancy).

Syntax:

global_pop_militancy_modifier = n

where n = 1 would add 1 MIL each month.

global_population_growth

Percentage increase or decrease in the natural growth of pops in the entire country.

Syntax:

global_population_growth = n

where n = 0.1 would be a 10% increase in the growth rate.

import_cost

The amount in percentage that an extra cost is imposed on imported goods.

Syntax:

import_cost = n

where n = 0.1 would make imported goods 10% more expensive.

influence_modifier

Percentage change in the base influence points the country generates.

Syntax:

influence_modifier = n

where n = 0.1 would be a 10% increase in base influence gain.

issue_change_speed

Percentage increase in the rate at which pops change their issue interest.

Syntax:

issue_change_speed = n

where n = 0.1 would be a 10% increase to the speed.

land_organisation

Percentage increase in the organization levels for a country's armies.

Syntax:

land_organisation = n

where n = 0.1 would be a 10% increase to organization.

land_unit_start_experience

Fixed percentage point change in the starting experience of new land units.

Syntax:

land_unit_start_experience = n

where n = 15 would start new land units with 15% (out of 100%) experience, ceteris paribus.

leadership_modifier

Percentage increase or decrease in the rate of Leadership generation.

Syntax:

 leadership_modifier = n 

where n = 1 would double the production (+100%)

loan_interest

Change in the interest applied to foreign loans

Syntax:

loan_interest = n

where n = 0.1 is an increase of 10% interest.

For more Information about interest click here.

max_loan_modifier

Percentage increase or decrease in the maximum loan the country can take.

Syntax:

max_loan_modifier = n

where n = 0.1 is an increase of 10% in maximum loan size.

max_military_spending

Change in the maximum military spending threshold.

Syntax:

max_military_spending = n

where n = 0.1 increases the maximum military spending threshold by 10%

Note: The max military spending you can limit a nation to is 1% (max_military_spending = 0.99). At 100% (max_military_spending = 1) this modifier doesn't work.

max_social_spending

Change in the maximum social spending threshold.

Syntax:

max_social_spending = n

where n = 0.1 increases the maximum social spending threshold by 10%

Note: The max social spending you can limit a nation to is 1% (max_social_spending = 0.99). At 100% (max_social_spending = 1) this modifier doesn't work.

max_tariff

Change in the maximum permissible tariff.

Syntax:

max_tariff = n

where n = 0.1 increases the maximum tariff threshold by 10%.

max_tax

Change in themaximum permissible tax.

Syntax:

max_tax = n

where n = 0.1 increases the maximum tax threshold by 10%

min_military_spending

Change in the minimum military spending threshold.

Syntax:

min_military_spending = n

where n = 0.1 increases the minimum military spending threshold by 10%

min_social_spending

Change in the minimum social spending threshold.

Syntax:

min_social_spending = n

where n = 0.1 increases the minimum social spending threshold by 10%


min_tariff

Change in the minimum permissible tariff.

Syntax:

min_tariff = n

where n = 0.1 increases the minimum tariff threshold by a flat 10%.
Example:

min_tariff = 0.25

will yield a minimum tariff rate of 25% if the base value was 0%.

min_tax

Change in themaximum permissible tax.

Syntax:

min_tax = n

where n = 0.1 increases the min tax threshold by 10% Example:

min_tax = 0.25

will yield a minimum tax rate of 25% if the base value was 0%.

mobilisation_economy_impact

Percentage increase/decrease in the economic impact of a country mobilizing its population.

Syntax:

mobilisation_economy_impact = n

where n = -0.25 would indicate a 25% reduction in the impact.

mobilization_impact

Percentage increase/decrease in the mobilization impact of a country.

Syntax:

mobilization_impact = n

where n = -0.25 would indicate a 25% reduction in the impact.

mobilisation_size

Percentage increase/decrease in the mobilization level for the country.

Syntax:

mobilisation_size = n

where n = 0.05 increases mobilization by 5%.

naval_organisation

Percentage increase in the organization levels for a country's ships.

Syntax:

naval_organisation = n

where n = 0.1 would be a 10% increase to organization.

naval_unit_start_experience

Percentage increase in the starting experience of new ships.

Syntax:

naval_unit_start_experience = n

where n = 15 would start new ships with 15% (out of 100%) experience, ceteris paribus.

non_accepted_pop_consciousness_modifier

Monthly change in consciousness (CON) for all POPs of non-accepted cultures.

Syntax:

non_accepted_pop_consciousness_modifier = n

where n = 2 would add 2 CON/month to POPs of non-accepted cultures.


non_accepted_pop_militancy_modifier

Monthly change in militancy (MIL) for all POPs of non-accepted cultures.

Syntax:

non_accepted_pop_militancy_modifier = n

where n = 2 would add 2 MIL/month to POPs of non-accepted cultures.

org_regain

Percentage change of the rate of organization regeneration for a country's units.

Syntax:

org_regain = n

where n = 0.1 is an increase of 10% organization/month.

political_reform_desire

Percentage change in the desire of all pops within the country for political reforms.

Syntax:

political_reform_desire = n

where n = 0.1 is an increase of 10%.

prestige

Flat change in prestige per month

Syntax:

prestige = n

where n = 0.02 yields +0.02 prestige/month.

research_points

Flat change in research points per day.

Syntax:

research_points = n

where n = 0.01 is +0.01 research points per day.

research_points_modifier

Percentage change in the rate of research points (RP) generation. Applied after any research_points base modifier.

Syntax:

research_points_modifier = n

where n = -0.5 would halve research point gain from any source, ceteris paribus.

research_points_on_conquer

Percentage modifier on the number of research points an uncivilized nation gains when they conquer lands.

Syntax:

research_points_on_conquer = n

where n = 0.25 will increase the number of research points gained via conquest by +25%.

rgo_output

Percentage change in the output of all the country's RGO's. Note the modifier name is case-insensitive (RGO_output and rgo_output both work).

Syntax:

RGO_output = n

where n = 0.1 would be a 10% increase in output.

rgo_throughput

Percentage change in the throughput of all of a country's RGO's. Note the modifier name is case-insensitive (RGO_throughput and rgo_throughput both work).

Syntax:

RGO_throughput = n

where n = 0.1 would be a 10% increase in throughput.

ruling_party_support

Percentage change in voter support for the current ruling party throughout the country.

Syntax:

ruling_party_support = n

where n = 0.1 would be a 10% increase in voter support.

social_reform_desire

Percentage change in the desire of all pops within the country for social reforms.

Syntax:

social_reform_desire = n

where n = 0.1 is an increase of 10%.

suppression_points_modifier

Percentage change in the gain of suppression points.

Syntax:

suppression_points_modifier = n

where n = 0.1 is an increase of 10%.

supply_consumption

Percentage increase/decrease in the amount of resources needed to supply units.

Syntax:

supply_consumption = n

where n = 0.1 would be an increase of 10%.

(strata)_vote

Percentage increase or decrease in the weighting of the strata's vote.

Syntax:

poor_vote = 0.1

is a 10% increase in the weight of all poor pops' votes.

tax_efficiency

Percentage change in the efficiency of tax collection for the entire country

Syntax:

tax_efficiency = n 

where n = 0.1 is an increase of 10%.

(category)_tech_research_bonus

Percentage cost change of the category's technologies.

Syntax:

industry_tech_research_bonus = n

where n = 0.1 decreases the cost of industry technologies by 10%

unit_start_experience

Fixed percentage point change in the starting experience of all new units.

Syntax:

unit_start_experience = n

where n = 15 would start new land units with 15% (out of 100%) experience, ceteris paribus.

war_exhaustion

Monthly change in a country's war exhaustion.

Syntax:

war_exhaustion = n

where n = 1 would add 1 WE each month.

Province Modifiers
assimilation_rate

Percentage change in the assimiliation rate of foreign culture pops in a province.

Syntax:

assimilation_rate = n

where n = 0.1 would be a 10% increase.

immigrant_attract

Increases or decreases the attractiveness of a province to prospective immigrants.

Syntax:

immigrant_attract = n

where n = 1 would be a 100% increase.

immigrant_push

Increases or decreases the amount emigrating from the province in scope.

Syntax:

immigrant_push = n

where n = 1 would be a 100% increase.

NB: While this does not increase the emigration rate, it does increase the emigration amount. Every month, the emigration chance tick hits, and if it hits a threshold (threshold percentage factors are in ..\common\pop_types.txt), this modifier will increase the amount that would emigrate from a certain pop. For example, if there is a non-accepted pop at 7 militancy and in a province that is not their core, they will most certainly hit the emigration threshold. Normally, only a few thousand at most per month would leave, however, if immigrant_push was set to, say, 100, it would increase the amount emigrating by a factor of 10,000. This would increase the emigration amount from the usual thousand or so, into the hundreds of thousands.

life_rating

Percentage change in the life rating of a province.

Syntax:

life_rating = n

where n = 1 would be an increase of 100%.

local_artisan_output

Percentage change in the output of a province's artisans.

Syntax:

local_artisan_output = n

where n = 0.1 would be a 10% increase in output.

local_factory_input

Percentage change of the input of factories in the province's state.

Syntax:

local_factory_input = n

where n = 0.1 would be a (10% / number of provinces in the state) increase in input.

local_factory_output

Percentage change of the output of factories in the province's state.

Syntax:

local_factory_output = n

where n = 0.1 would be a (10% / number of provinces in the state) increase in output.

local_factory_throughput

Percentage change of the throughput of factories in the province's state.

Syntax:

local_factory_throughput = n

where n = 0.1 would be a (10% / number of provinces in the state) increase in throughput.

local_repair

Percentage change of the repair rate for ships in a province.

Syntax:

local_repair = n

where n = 0.1 is an increase of 10% additional strength repaired per month.

local_RGO_output

Percentage change in the output of a province's RGO.

Syntax:

local_RGO_output = n

where n = 0.1 would be a 10% increase in output.

local_RGO_throughput

Percentage change in the throughput of a province's RGO.

Syntax:

local_RGO_throughput = n

where n = 0.1 would be a 10% increase in throughput.

local_ruling_party_support

Percentage change in voter support for the current ruling party in the province.

Syntax:

local_ruling_party_support = n

where n = 0.1 would be a 10% increase in voter support.

local_ship_build

Percentage change of the time to build naval units in this province.

Syntax:

local_ship_build = n

where n = 0.1 is a 10% increase.

pop_(trait)_modifier

Monthly increase or decrease in (trait; either consciousness or militancy) for all pops in a province.

Syntax:

pop_consciousness_modifier = n 

where n = 1 would add 1 CON each month.

population_growth

Percentage increase or decrease in the natural growth of pops in a province.

Syntax:

population_growth = n

where n = 0.1 would be a 10% increase in the growth rate.

(type)_rgo_eff

Percentage change in the efficiency of a province's RGO. The (type) can be farm or mine.

Syntax:

farm_rgo_eff = n

where n = 0.1 would be a 10% increase in efficiency.

(type)_rgo_size

Percentage change in the size of a province's RGO. The (type) can be farm or mine.

Syntax:

farm_rgo_size = n

where n = 0.1 would be a 10% increase in RGO size.

Country & Province Modifiers
goods_demand

Percentage increase or decrease in the demand for all goods of pops in the country or province specified.

Syntax:

goods_demand = n

where n = 0.1 would be a 10% increase in the demand.

(strata)_income_modifier

Percentage increase or decrease in the income of pops in the specified strata. This modifier appears not to be working, if you did manage to get the effect working, remove this text.

Syntax:

 rich_income_modifier = n

, n = 0.1 is a 10% increase in income.

(strata)_(level)_needs

Strata can be poor, middle, or rich; level can be life, everyday, or luxury. After checks on the HoD v3.04 it appears that this modifier works for the social reforms listed in issues.txt but has no effect* when used in event_modifiers.txt.

*in event_modifiers.txt effects for middle strata and rich strata are swapped.

Syntax:

 poor_life_needs = n

, -1 < n < 1. Not sure what the specific effect of the value of n is, might be percentage increase ex. n = 0.1 means that strata's life needs increase by 10%.


In the event_modifiers.txt file, you'll see that every modifier has an icon it displays—for country modifiers, this is the icon that appears in the diplomacy screen (the one over which you hover to get the description and modifiers text). For province modifiers, this is the icon that appears in the province detail screen. The number of the icon corresponds to the "placement" of the modifier in the modifiers.dds file (in the gfx\interface folder). So you could, conceivably, go to that file and count along the strip to see the number of the icon you want.

The thing to note, however, is that province modifiers and country modifiers actually work a bit differently. The country modifiers "skip" the first two icons on the strip (the gavels—you can't get either to appear as country modifier icons) and "icon = 1" for a country modifier is actually the green pie chart icon (and thus you can only go up to 18 rather than 20). The picture below displays this (using the icons form vanilla), with the first row being province modifiers and the second row being country modifiers:


---

---
title: National focus modding
category: guide
tags: [politics]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/National_focus_modding
---

This page documents the how to edit to effects of the various National focus, how to add new ones. The documents needed are national_focus.txt found in the Victoria 2 -> Common folder and the icon files found in Victoria 2 -> History -> GFX. Lastly you will need the localisation files to edit the name and description of the national focus.

Editing and creating National Values

This part details how you edit the effects of an existing national focus.

The national_focus.txt document should look like this:

rail_focus =
{
	encourage_rail = 
	{
		railroads = 0.5 #Capitalists 50% more likeley to choose railroads
		icon = 2
	}
}

immigration_focus = 
{
	immigration =
	{
		immigrant_attract = 0.2 #increases attactiveness to immigrants by 20 %
		icon = 3
		limit = { 
			#OR = { 
				#continent = north_america
				#continent = south_america
				#is_overseas = yes
			#}  
		}
	}
}

diplomatic_focus =
{
	increase_tension =
	{
		icon = 4
		has_flashpoint = yes
		own_provinces = no

		flashpoint_tension = 0.15

		limit = {
			is_core = THIS
			THIS = {
				is_greater_power = no
			}
		}
	}
}

promotion_focus =
{
	promote_aristocrats =
	{
		aristocrats = 0.20 #20% more likeley to become artisans
		icon = 5
		outliner_show_as_percent = yes
	}

	promote_artisans =
	{
		artisans = 0.20 #20% more likeley to become this type
		icon = 6
		outliner_show_as_percent = yes
	}

	promote_bureaucrats =
	{
		bureaucrats = 0.20 #20% more likeley to become this type
		icon = 7
		outliner_show_as_percent = yes
	}

	promote_capitalists =
	{
		capitalists = 0.20 #20% more likeley to become this type
		icon = 8
		outliner_show_as_percent = yes
		limit = { 
			civilized = yes
		}

	}
	
	promote_clergymen =
	{
		clergymen = 0.20 #20% more likeley to become this type
		icon = 9
		outliner_show_as_percent = yes
	}

	promote_clerks =
	{
		clerks = 0.20 #20% more likeley to become this type
		icon = 10
		outliner_show_as_percent = yes
		limit = { 
			civilized = yes
		}
	}

	promote_craftsmen =
	{
		craftsmen = 0.20 #20% more likeley to become this type
		icon = 11
		outliner_show_as_percent = yes
		limit = { 
			civilized = yes
		}
	}

	promote_farmers =
	{
		farmers = 0.20 #20% more likeley to become this type
		icon = 12
		outliner_show_as_percent = yes
	}
	
	promote_labourers =
	{
		labourers = 0.20 #20% more likeley to become this type
		icon = 13
		outliner_show_as_percent = yes
	}

	promote_officers =
	{
		officers = 0.20 #20% more likeley to become this type
		icon = 14
		outliner_show_as_percent = yes
	}

	promote_soldiers =
	{
		soldiers = 0.20 #20% more likeley to become this type
		icon = 15
		outliner_show_as_percent = yes
	}
}

production_focus =
{
	automation_focus =
	{
		aeroplanes = 18.3
		barrels = 18.3
		automobiles = 18.3
		icon = 16
		limit = { year = 1880 }
	}

	electrical_focus =
	{
		radio = 18.3
		telephones = 18.3
		electric_gear = 18.3
		icon = 17
		limit = { year = 1880 }
	}

	chemical_focus =
	{
		fuel = 18.3
		oil = 18.3
		icon = 18
		limit = { year = 1880 }
	}

	shipping_focus =
	{
		steamer_convoy = 18.3
		clipper_convoy = 18.3
		icon = 19
		limit = { 
			#civilized = yes
			state_scope = { any_owned_province = { port = yes } }
		}
	}

	textile_focus =
	{
		luxury_clothes = 18.3
		regular_clothes = 18.3
		fabric = 0.3
		dye = 0.3
		icon = 20
		#limit = { 
		#	civilized = yes
		#}
	}

	wood_focus = 
	{
		paper = 18.3
		luxury_furniture = 18.3
		furniture = 18.3
		lumber = 18.3
		icon = 21
		#limit = { 
		#	civilized = yes
		#}
	}

	basic_industry_focus =
	{
		steel = 18.3
		machine_parts = 25.3
		cement = 18.3
		icon = 22
		#limit = { 
		#	civilized = yes
		#}
	}

	armaments_focus = 
	{
		artillery = 18.3
		small_arms = 18.3
		ammunition = 18.3
		canned_food = 18.3  
		explosives = 18.3
		fertilizer = 18.3
		icon = 23
		#limit = { 
		#	civilized = yes
		#}
	}

	consumer_focus = 
	{
		liquor = 18.3
		wine = 18.3
		glass = 18.3
		icon = 24
		#limit = { 
		#	civilized = yes
		#}
	}
}

party_loyalty_focus =
{
	fascist_focus =
	{
		ideology = fascist
		loyalty_value = 0.001 # By that much pops will be more loyal
		icon = 25
	}
	
	reactionary_focus =
	{
		ideology = reactionary
		loyalty_value = 0.001 # By that much pops will be more loyal
		icon = 26
	}
	
	conservative_focus =
	{
		ideology = conservative
		loyalty_value = 0.001 # By that much pops will be more loyal
		icon = 27
	}
	
	socialist_focus =
	{
		ideology = socialist
		loyalty_value = 0.001 # By that much pops will be more loyal
		icon = 28
	}
	
	communist_focus =
	{
		ideology = communist
		loyalty_value = 0.001 # By that much pops will be more loyal
		icon = 29
	}
	
	liberal_focus =
	{
		ideology = liberal
		loyalty_value = 0.001 # By that much pops will be more loyal
		icon = 30
	}
	
	anarcho_liberal_focus =
	{
		ideology = anarcho_liberal
		loyalty_value = 0.001 # By that much pops will be more loyal
		icon = 31
	}
}

Explanation

Overall category: Coming Soon

Limit: Here you can change when the national focus should be usable. The ones in use are status, in-game year, ownership status and cores. But it could potentially also be certain technologies, wether the country is at war or not or any other condition.

Values The values of the effects are assumed to be percentages. They are confusingly listed in two different formats. So "regular_clothes = 18.3; fabric = 0.3" means that the capitalists' tendency to build said factory/building is increased by 18.3% and 30% respectively.

Icon The icon number refers to a file in the GFX folder. When simply changing the effects of an already existing national focus, you don't need to do anything about this. Coming soon

Encourage industries The name of the scope references an instance in the buildings.txt file.

Party Loyalty The name refers to an ideology in the ideologies.txt file.

The defines.lua file

How the amount of primary culture population relates to the amount of NFs is defined in Victoria II/common/defines.lua. Inside the file there is NATIONAL_FOCUS_DIVIDER, which is 400000.0 in an unmodded game.

Creating a new national focus

Creating a new type of national foxus is a little more elaborate than simply editing an already existing one. First and foremost you will need to add a new icon that can be refered.


---

---
title: National value modding
category: guide
tags: [politics]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/National_value_modding
---

This page documents the how to edit to effects of National values, how to add new ones, and how the change the national value of each specific country. The documents needed are nationalvalues.txt found in the Victoria 2 -> Common folder and country files found in Victoria 2 -> History -> Countries

Editing and creating National Values

This part details how you create a new national value or edit an existing one.

The nationalvalues.txt document should look like this:

nv_order = {
	mobilisation_size = 0.04
	mobilisation_economy_impact = 1.0
}

nv_liberty = {
	mobilisation_size = 0.02
	mobilisation_economy_impact = 0.75
}

nv_equality = {
	mobilisation_size = 0.06
	mobilisation_economy_impact = 1.25
}


It mentions the existing national values; Order, Liberty and Equality and there effects on mobilization. To create a new one, simply at a fourth and put in the effects, you want. Only country modifiers are used. Note that in addition to the effects found in this file, national values affect other things, for example POPs' ideologies.

Setting the national value of a specific country

To actually use a national value, you have to go to Victoria 2 -> History -> Countries and find the country, you want to edit the national value of.

Each country is called its three letter acronym and its name. For example 'BAD - Baden.txt'.

In this file you find the line nationalvalue = nv_order. It should be in line 6. Simply change the nv_order part to the one you want.


---

---
title: Population modding
category: guide
tags: [population]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Population_modding
---

Population modding can be used to change the population of a country. The files needed are in history/pops/. In vanilla Victoria 2 there are two folders: 1836.1.1 and 1861.4.14, they determine in what bookmarks the content of these folders are used.

In these folders there are files, based on modern borders. These files contain the information needed for the population in-game. For example, the file Estonia.txt contains:

#Estonia Region (436000) 
#under the rule of Russia in 1836  
#Tallinn/Reval (160000/40000 POPS)  
349 = {
	clergymen = {
		culture = estonian
		religion = protestant
		size = 325
	}
        etc...
}
#Narva (184000/46000 POPS)  
350 = {
	clergymen = {
		culture = estonian
		religion = protestant
		size = 425
	}
        etc...
}
etc...

Setup

As shown, the population uses the following setup:

[Province ID] = {
	[Population type] = {
		culture = [culture]
		religion = [religion]
		size = [quantity]
	}
}

Example

Editing existing population easy, since you only have to change some variables, or copy-paste a bit.

Let's say you made a new province with the code '3249', and you want to add the population.

A new file needs an unique name, like Newprovinces.txt and has to be a '.txt' file, which is nothing else than a normal text file, and most programs, like Notepad++, use this as standard format. I suggest making a new file, since it's easier to use when you have to upgrade it to the 1861 folder. It also needs to be in history/pops/1836.1.1.

This is what you need to fill in if you want the population to be to be mostly farmers, a large amount of soldiers, and a small amount of clergymen, aristocrats, labourers and artisans, the culture to be about 75% Dutch, 12.5% Flemish and 12.5% Wallonian, and the religion to be 75% Protestant and 25% Catholic, and have a total size of 20,000:

3249 = {
    farmers = {
        culture = dutch
        religion = protestant
        size = 8000
    }
    farmers = {
        culture = wallonian
        religion = catholic
        size = 1000
    }
    farmers = {
        culture = flemish
        religion = catholic
        size = 1000
    }
    soldiers = {
        culture = dutch
        religion = protestant
        size = 3700
    }
    soldiers = {
        culture = wallonian
        religion = catholic
        size = 650
    }
    soldiers = {
        culture = flemish
        religion = catholic
        size = 650
    }
    clergymen = {
        culture = dutch
        religion = protestant
        size = 100
    }
    artisans = {
        culture = dutch
        religion = protestant
        size = 1000
    }
    artisans = {
        culture = wallonian
        religion = catholic
        size = 500
    }
    artisans = {
        culture = flemish
        religion = catholic
        size = 500
    }
    aristocrats = {
        culture = dutch
        religion = protestant
        size = 150
    }
    labourers = {
        culture = dutch
        religion = protestant
        size = 2000
    }
    labourers = {
        culture = wallonian
        religion = catholic
        size = 450
    }
    labourers = {
        culture = flemish
        religion = catholic
        size = 300
    }
}


The total size of all the pops is now 20,000. The balance between Protestants and Catholics is 14,950/5,050 (74.75%/25.25%). The balance between Dutch, Wallonian and Flemish is 14,950/2,600/2,450 (74.75%/13%/12.25%).

Upgrading to 1861

You also have to use a file for the 1861.4.14 folder. To do this simply copy-paste the file you used to the 1861.4.14 folder in the history/pops/ folders, there is no need to change the name. You can then decide to keep it the same, but usually population grows. Most of the time population grows with about 3% between the 1836 and 1861 files. You can simply increase all the quantities by 3% in the 1861 file, sometimes this will end up giving you numbers with decimals, don't worry, you can either round it up or down, or fill in the number including the decimals, since the game will round it up or down itself.

When everything is done, you will have a fully functional province population.


---

---
title: Province history modding
category: guide
tags: [province]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Province_history_modding
---

This page documents the formatting and creation of province history files.


What does a province history file look like?

Province history files are found within history\provinces. From there they divided into various regions. Each province in the game has a seperate file named province number - province name. Example: 256 - Belfast.

Required info

At the bare minimum, most provinces files will look like this:

owner = TAG           #Tag of owner country
controller = TAG      #Tag of controller country
add_core = TAG        #Tag of core country
add_core = TAG        #A second core country's tag. 
trade_goods = (good)  #Resource in province
life_rating = x       #Life rating of province


The controller of a province determines if it is occupied at the start of the game. Unless we are talking about rebels (which is a tag; REB), this is really only used if the country starts at war. If owner and controller is the same tag, the province is unoccupied. Otherwise it is occupied. There can only be one controller and one owner, but there is no limit to the number of cores a province can have.

Additional info

Many provinces will have much more in their history files. Since all values defaults to either 0 (for numeric values) or no (for boolean values), if something is not wanted, there does not need to be any code.

example of London, from vanilla:

owner = ENG
controller = ENG
add_core = ENG
trade_goods = grain
life_rating = 45
fort = 1
party_loyalty = {
	ideology = liberal
	loyalty_value = 10.5
}
state_building = {
	level = 1
	building = furniture_factory
	upgrade = yes
}
state_building = {
	level = 1
	building = paper_mill
	upgrade = yes
}
state_building = {
	level = 1
	building = ammunition_factory
	upgrade = yes
}
state_building = {
	level = 1
	building = small_arms_factory
	upgrade = yes
}
state_building = {
	level = 2
	building = clipper_shipyard
	upgrade = yes
}
1861.1.1 = {
	state_building = {
		level = 1
		building = luxury_clothes_factory
		upgrade = yes
	}
	state_building = {
		level = 1
		building = luxury_furniture_factory
		upgrade = yes
	}
}
1861.1.1 = { railroad = 3 }


There is a lot to break down here, but let's start small.

owner = ENG
controller = ENG
add_core = ENG
trade_goods = grain
life_rating = 45


This says that London is owned, controlled, and cored by the ENG tag, or the United Kingdom. It's resource is grain, and the life rating is high at 45.

Now, for the new stuff:

fort = 1


London also has a level 1 fort present.

party_loyalty = { ideology = liberal loyalty_value = 10.5 }

This says that London has a significant loyalty towards the liberal ideology.

state_building = {
	level = 1
	building = furniture_factory
	upgrade = yes
}
state_building = {
	level = 1
	building = paper_mill
	upgrade = yes
}


This says that the state London is in owns two level one factories, a furniture factory and a paper mill.

1861.1.1 = {
	state_building = {
		level = 1
		building = luxury_clothes_factory
		upgrade = yes
	}
	state_building = {
		level = 1
		building = luxury_furniture_factory
		upgrade = yes
	}
}
1861.1.1 = { railroad = 3 }


This says that in the 1861 bookmark, London owns these two new factories and a level three railroad.

Editing province history files
Party loyalty
party_loyalty = {
	ideology = (ideology)    #same as in ideologies.txt
	loyalty_value = x
}

Buildings
Factories
state_building = {
	level = x
	building = (building)    #same as in buildings.txt
	upgrade = yes
}

Forts and railroads
fort = x
railroad = x


X here of course refers to the level of each building. It goes from 0 to 6. If you leave it out, it will default to 0 (no building).

Different bookmarks

Any of the above entries can be enclosed in date brackets so that they do not appear until later bookmarks.

1861.1.1 = { 
owner = PRU
controller = PRU
add_core = PRU
remove_core = AUS
}


This will make it so that in the ACW bookmark, the province will change hands from Austria to Prussia.

Bugfixing

If a certain province looks to have a core with the rebel flag, it is likely because you have added a core to a country that does not exist (meaning they have not been defined in the common/countries.txt file). It is likely because you have written the three letter acronym wrong.


---

---
title: Provinces
category: data
tags: [province]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Provinces
---

Map with all province IDs

Provinces are the smallest type of geographic entity. The provinces are permanent and cannot be altered. They are grouped together in States, which is again grouped in continents.

The following table lists all provinces and their properties.

Tip: Use Ctrl+F to open a search panel, so you can find the province you want.

ID	Province Name	Owner	Cores	Resource	Life Rating	Region	Continent
1	Sitka	 Russia	 Russia	 Timber	20	Alaska	North America
2	Yakutat	 Russia	 Russia	 Fish	20	Alaska	North America
3	Kenai	 Russia	 Russia	 Fish	20	Alaska	North America
4	Dutch Harbor	 Russia	 Russia	 Fish	20	Alaska	North America
5	Bethel	 Russia	 Russia	 Fish	20	Alaska	North America
6	Whitehorse	uncolonized	 Canada	 Fish	15	Yukon Territory	North America
7	Dawson	uncolonized	 Canada	 Fish	15	Yukon Territory	North America
8	Ross River	uncolonized	 Canada	 Grain	15	Yukon Territory	North America
9	Fort Simpson	uncolonized	 Canada	 Timber	15	Northwest Territories	North America
10	Inuvik	uncolonized	 Canada	 Grain	15	Northwest Territories	North America
11	Echo Bay	uncolonized	 Canada	 Fish	15	Northwest Territories	North America
12	Reliance	uncolonized	 Canada	 Fish	15	Northwest Territories	North America
13	Vancouver	 United Kingdom	 Canada  Columbia	 Timber	35	British Columbia	North America
14	Vancouver Island	 United Kingdom	 Canada  Columbia	 Fish	35	British Columbia	North America
15	Prince Rupert	 United Kingdom	 Canada  Columbia	 Timber	35	British Columbia	North America
16	Glenora	 United Kingdom	 Canada  Columbia	 Timber	30	British Columbia	North America
17	Atlin	 United Kingdom	 Canada  Columbia	 Timber	30	British Columbia	North America
18	Fort Saint John	uncolonized	 Canada  Columbia	 Timber	30	British Columbia	North America
19	Prince George	 United Kingdom	 Canada  Columbia	 Timber	35	British Columbia	North America
20	Kelowna	uncolonized	 Canada  Columbia	 Grain	35	British Columbia	North America
21	Vernon	uncolonized	 Canada  Columbia	 Timber	35	British Columbia	North America
22	Edmonton	uncolonized	 Canada	 Grain	30	Alberta	North America
23	Athabaska Landing	uncolonized	 Canada	 Cattle	30	Alberta	North America
24	Jasper	uncolonized	 Canada	 Timber	30	Alberta	North America
25	Banff	uncolonized	 Canada	 Coal	35	Alberta	North America
26	Calgary	uncolonized	 Canada	 Grain	35	Alberta	North America
27	Denwood	uncolonized	 Canada	 Timber	30	Alberta	North America
28	Fort MacLeod	 United Kingdom	 Canada	 Iron	35	Alberta	North America
29	Medicine Hat	 United Kingdom	 Canada	 Fruit	35	Alberta	North America
30	Regina	 United Kingdom	 Canada	 Grain	35	Saskatchewan
31	Stanley	uncolonized	 Canada	 Timber	30	Saskatchewan
32	Prince Albert	uncolonized	 Canada  Metis Confederacy	 Grain	30	Saskatchewan
33	Asquith	uncolonized	 Canada	 Grain	30	Saskatchewan
34	Saskatoon	uncolonized	 Canada	 Grain	30	Saskatchewan
35	Maple Creek	 United Kingdom	 Canada	 Grain	35	Saskatchewan
36	Winnipeg	 United Kingdom	 Canada  Metis Confederacy	 Grain	35	Manitoba
37	Churchill	 United Kingdom	 Canada  Metis Confederacy	 Fish	35	Manitoba
38	Indian Lakes	uncolonized	 Canada  Metis Confederacy	 Timber	30	Manitoba
39	Norway House	uncolonized	 Canada  Metis Confederacy	 Timber	30	Manitoba
40	Dauphin	uncolonized	 Canada  Metis Confederacy	 Cattle	30	Manitoba
41	Brandon	 United Kingdom	 Canada  Metis Confederacy	 Grain	35	Manitoba
42	Pembina	 United Kingdom	 Canada  Metis Confederacy	 Grain	35	Manitoba
43	Arviat	 United Kingdom	 Canada	 Fish	25	Nunavut
44	Coral Harbour	 United Kingdom	 Canada	 Iron	35	Nunavut
45	Baffin Island	 United Kingdom	 Canada	 Fish	25	Nunavut
46	Toronto	 United Kingdom	 Canada	 Grain	35	Ontario
47	Fort Severn	 United Kingdom	 Canada	 Fish	35	Ontario
48	Fort Albany	 United Kingdom	 Canada	 Fish	35	Ontario
49	Dryden	 United Kingdom	 Canada	 Timber	35	Ontario
50	Thunder Bay	 United Kingdom	 Canada	 Cattle	35	Ontario
51	Sault Ste Marie	 United Kingdom	 Canada	 Cattle	35	Ontario
52	Sudbury	 United Kingdom	 Canada	 Cattle	35	Ontario
53	Barrie	 United Kingdom	 Canada	 Grain	35	Ontario
54	Windsor	 United Kingdom	 Canada	 Grain	35	Ontario
55	Hamilton	 United Kingdom	 Canada	 Fish	35	Ontario
56	Kingston	 United Kingdom	 Canada	 Grain	35	Ontario
57	Ottawa	 United Kingdom	 Canada	 Grain	35	Ontario
58	Montreal	 United Kingdom	 Canada  Quebec	 Cattle	35	Quebec
59	Nitchequon	 United Kingdom	 Canada  Quebec	 Fish	35	Quebec
60	Fort Rupert	 United Kingdom	 Canada  Quebec	 Fish	35	Quebec
61	Chicoutimi	 United Kingdom	 Canada  Quebec	 Grain	35	Quebec
62	Sept-Îles	 United Kingdom	 Canada  Quebec	 Fish	35	Quebec
63	Temiscaming	 United Kingdom	 Canada  Quebec	 Cattle	35	Quebec
64	Trois-Rivières	 United Kingdom	 Canada  Quebec	 Grain	35	Quebec
65	Quebec City	 United Kingdom	 Canada  Quebec	 Grain	35	Quebec
66	Sherbrooke	 United Kingdom	 Canada  Quebec	 Grain	35	Quebec
67	Rimouski	 United Kingdom	 Canada  Quebec	 Grain	35	Quebec
68	Fredericton	 United Kingdom	 Canada	 Timber	35	New Brunswick
69	Bathurst	 United Kingdom	 Canada	 Cattle	35	New Brunswick
70	Prince Edward Island	 United Kingdom	 Canada	 Fish	35	New Brunswick
71	Halifax	 United Kingdom	 Canada	 Fish	35	New Brunswick
72	Truro	 United Kingdom	 Canada	 Timber	35	New Brunswick
73	Cape Breton Island	 United Kingdom	 Canada	 Timber	35	New Brunswick
74	Saint Johns	 United Kingdom	 Canada  Newfoundland	 Fish	35	Newfoundland
75	Millertown	 United Kingdom	 Canada  Newfoundland	 Iron	35	Newfoundland
76	Hopedale	 United Kingdom	 Canada  Newfoundland  Quebec	 Fish	35	Newfoundland
77	St Pierre & Miquelon	 France		 Fish	35	Saint Pierre and Miquelon
78	Seattle	uncolonized		 Timber	35	Washington
79	Spokane	uncolonized		 Timber	35	Washington
80	Walla Walla	uncolonized		 Timber	35	Washington
81	Portland	uncolonized		 Timber	35	Oregon
82	Baker City	uncolonized		 Timber	35	Oregon
83	Klamath Falls	uncolonized		 Fish	35	Oregon
84	San Francisco	 Mexico	 Californian Republic	 Fruit	40	California
85	Eureka	 Mexico	 Californian Republic	 Fish	40	California
86	Sacramento	 Mexico	 Californian Republic	 Fruit	35	California
87	Monterey	 Mexico	 Californian Republic  Mexico	 Fruit	40	California
88	Mariposa	 Mexico	 Californian Republic  Deseret	 Fruit	35	California
89	Los Angeles	 Mexico	 Californian Republic  Deseret  Mexico	 Grain	40	California
90	San Diego	 Mexico	 Californian Republic	 Grain	40	California
91	Boise	uncolonized		 Wool	35	Nevada-Utah
92	Coeur D'Alene	 United States of America	 United States of America	 Timber	35	Nevada-Utah
93	Pocatello	uncolonized		 Cattle	35	Nevada-Utah
94	Carson City	 Mexico	 Deseret	 Iron	35	Nevada-Utah
95	Elko	 Mexico	 Deseret	 Iron	35	Nevada-Utah
96	Las Vegas	 Mexico	 Deseret	 Iron	35	Nevada-Utah
97	Salt Lake City	 Mexico	 Mexico  Deseret	 Coal	35	Nevada-Utah
98	Loa	 Mexico	 Mexico  Deseret	 Grain	35	Nevada-Utah
99	Moab	 Mexico	 Mexico  Deseret	 Grain	35	Nevada-Utah
100	Phoenix	 Mexico	 Deseret	 Iron	35	Arizona
101	Flagstaff	 Mexico	 Deseret  Mexico	 Cattle	35	Arizona
102	Tucson	 Mexico		 Cattle	35	Arizona
103	Santa Fe	 Mexico	 Mexico	 Fruit	35	New Mexico
104	Albuquerque	 Mexico		 Cattle	35	New Mexico
105	Las Cruces	 Mexico	 Mexico	 Cattle	35	New Mexico
106	Denver	uncolonized		 Cattle	35	Colorado
107	Grand Junction	uncolonized		 Cattle	35	Colorado
108	Alamosa	uncolonized		 Cattle	35	Colorado
109	Pueblo	uncolonized		 Cattle	35	Colorado
110	Cheyenne	 United States of America	 United States of America	 Grain	35	Wyoming
111	Cody	 United States of America	 United States of America	 Coal	35	Wyoming
112	Casper	 United States of America	 United States of America	 Grain	35	Wyoming
113	Bozeman	 United States of America	 United States of America	 Cattle	35	Montana
114	Missoula	 United States of America	 United States of America	 Cattle	35	Montana
115	Great Falls	 United States of America	 United States of America	 Cattle	35	Montana
116	Billings	 United States of America	 United States of America	 Cattle	35	Montana
117	Bismarck	 United States of America		 Coal	35	North Dakota
118	Minot	 United States of America	 United States of America	 Coal	35	North Dakota
119	Dickinson	 United States of America	 United States of America	 Cattle	35	North Dakota
120	Sioux Falls	 United States of America	 United States of America	 Grain	35	South Dakota
121	Dupree	 United States of America	 United States of America	 Coal	35	South Dakota
122	Rapid City	 United States of America	 United States of America	 Grain	35	South Dakota
123	Omaha	 United States of America	 United States of America	 Fruit	35	Nebraska
124	Alliance	 United States of America	 United States of America	 Grain	35	Nebraska
125	North Platte	 United States of America	 United States of America	 Grain	35	Nebraska
126	Topeka	 United States of America		 Grain	35	Kansas
127	Goodland	 United States of America		 Fruit	35	Kansas
128	Wichita	 United States of America		 Grain	35	Kansas
129	Oklahoma City	uncolonized		 Grain	35	Oklahoma
130	Tahlequah	uncolonized		 Grain	35	Oklahoma
131	Okmulgee	uncolonized		 Grain	35	Oklahoma
132	Houston	 Texas	 Texas	 Cattle	35	Texas
133	Austin	 Texas	 Mexico  Texas	 Cattle	35	Texas
134	Dallas	 Texas	 Mexico  Texas	 Cattle	35	Texas
135	Lubbock	 Texas	 Mexico  Texas	 Sulphur	35	Texas
136	El Paso	 Mexico		 Cattle	35	Texas
137	San Antonio	 Texas	 Mexico  Texas	 Cattle	35	Texas
138	Laredo	 Mexico	 Mexico  Texas	 Cattle	35	Texas
139	New Orleans	 United States of America	 United States of America	 Grain	35	Louisiana
140	Baton Rouge	 United States of America	 United States of America	 Cotton	35	Louisiana
141	Lake Charles	 United States of America	 United States of America	 Sulphur	35	Louisiana
142	Shreveport	 United States of America		 Sulphur	35	Louisiana
143	Little Rock	 United States of America	 Cherokee	 Grain	35	Arkansas
144	Hot Springs	 United States of America	 United States of America	 Grain	35	Arkansas
145	Fayetteville	 United States of America	 Cherokee  United States of America	 Timber	35	Arkansas
146	St Louis	 United States of America	 United States of America	 Cattle	35	Missouri
147	Joplin	 United States of America	 United States of America	 Coal	35	Missouri
148	Malden	 United States of America	 United States of America	 Grain	35	Missouri
149	Jefferson City	 United States of America	 United States of America	 Coal	35	Missouri
150	Kansas City	 United States of America	 United States of America	 Coal	35	Missouri
151	Des Moines	 United States of America	 United States of America	 Grain	35	Iowa
152	Oskaloosa	 United States of America	 United States of America	 Grain	35	Iowa
153	Cedar Rapids	 United States of America	 United States of America	 Cattle	35	Iowa
154	Sioux City	 United States of America	 United States of America	 Grain	35	Iowa
155	Minneapolis	 United States of America	 United States of America	 Timber	35	Minnesota
156	Granite Falls	 United States of America	 United States of America	 Coal	35	Minnesota
157	Moorhead	 United States of America	 United States of America	 Timber	35	Minnesota
158	Duluth	 United States of America	 United States of America	 Iron	35	Minnesota
159	Milwaukee	 United States of America	 United States of America	 Timber	35	Wisconsin
160	Eau Claire	 United States of America	 United States of America	 Grain	35	Wisconsin
161	Green Bay	 United States of America	 United States of America	 Timber	35	Wisconsin
162	Madison	 United States of America	 United States of America	 Coal	35	Wisconsin
163	Chicago	 United States of America	 United States of America	 Coal	35	Illinois
164	Rockford	 United States of America	 United States of America	 Coal	35	Illinois
165	Champaign	 United States of America	 United States of America	 Coal	35	Illinois
166	Peoria	 United States of America	 United States of America	 Cattle	35	Illinois
167	Springfield	 United States of America	 United States of America	 Cattle	35	Illinois
168	Carbondale	 United States of America	 United States of America	 Cattle	35	Illinois
169	Indianapolis	 United States of America	 United States of America	 Grain	35	Indiana
170	Evansville	 United States of America	 United States of America	 Grain	35	Indiana
171	South Bend	 United States of America	 United States of America	 Timber	35	Indiana
172	Fort Wayne	 United States of America	 United States of America	 Timber	35	Indiana
173	Detroit	 United States of America	 United States of America	 Timber	35	Michigan
174	Grand Rapids	 United States of America	 United States of America	 Timber	35	Michigan
175	Saginaw	 United States of America	 United States of America	 Timber	35	Michigan
176	Traverse City	 United States of America	 United States of America	 Timber	35	Michigan
177	Marquette	 United States of America	 United States of America	 Iron	35	Michigan
178	Cleveland	 United States of America	 United States of America	 Coal	35	Ohio
179	Columbus	 United States of America	 United States of America	 Grain	35	Ohio
180	Sandusky	 United States of America	 United States of America	 Timber	35	Ohio
181	Dayton	 United States of America	 United States of America	 Grain	35	Ohio
182	Cincinnati	 United States of America	 United States of America	 Grain	35	Ohio
183	Marietta	 United States of America	 United States of America	 Cotton	35	Ohio
184	Louisville	 United States of America	 United States of America	 Tobacco	35	Kentucky
185	Lexington	 United States of America	 United States of America	 Coal	35	Kentucky
186	Bowling Green	 United States of America	 United States of America	 Cattle	35	Kentucky
187	Paducah	 United States of America	 United States of America	 Cattle	35	Kentucky
188	Nashville	 United States of America	 United States of America	 Grain	35	Tennessee
189	Memphis	 United States of America	 United States of America	 Cotton	35	Tennessee
190	Knoxville	 United States of America	 United States of America	 Coal	35	Tennessee
191	Chattanooga	 United States of America	 United States of America	 Coal	35	Tennessee
192	Jackson	 United States of America	 United States of America	 Cotton	35	Mississippi
193	Vicksburg	 United States of America	 United States of America	 Grain	35	Mississippi
194	Biloxi	 United States of America	 United States of America	 Cotton	35	Mississippi
195	Montgomery	 United States of America	 United States of America	 Cotton	35	Alabama
196	Tuscaloosa	 United States of America	 United States of America	 Iron	35	Alabama
197	Mobile	 United States of America	 United States of America	 Cotton	35	Alabama
198	Tallahassee	 United States of America	 United States of America	 Cotton	35	Florida
199	St Augustine	 United States of America	 United States of America	 Cotton	35	Florida
200	Tampa	 United States of America	 United States of America	 Fruit	25	Florida
201	Atlanta	 United States of America		 Cotton	35	Georgia - US
202	Valdosta	 United States of America	 United States of America	 Cotton	35	Georgia - US
203	Bermuda	 United Kingdom		 Fish	35	Caribbean Islands
204	Savannah	 United States of America		 Cotton	35	Georgia - US
205	Charleston	 United States of America		 Coal	35	Georgia - US
206	Columbia	 United States of America	 United States of America	 Cotton	35	Georgia - US
207	Greenville	 United States of America		 Tobacco	35	Virginia
208	Raleigh	 United States of America		 Tobacco	35	Virginia
209	Charlotte	 United States of America		 Tobacco	35	Virginia
210	WIlmington	 United States of America		 Cotton	35	Virginia
211	Richmond	 United States of America	 United States of America	 Tobacco	35	Virginia
212	Manassas	 United States of America		 Tobacco	35	Virginia
213	Fredericksburg	 United States of America	 United States of America	 Tobacco	35	Virginia
214	Norfolk	 United States of America		 Tobacco	35	Virginia
215	Staunton	 United States of America		 Grain	35	Virginia
216	Roanoke	 United States of America		 Tobacco	35	Virginia
217	Wheeling	 United States of America		 Coal	35	West Virginia
218	Huntington	 United States of America		 Coal	35	West Virginia
219	Baltimore	 United States of America	 United States of America	 Timber	35	Maryland
220	Washington	 United States of America		 Grain	35	District of Columbia
221	Hagerstown	 United States of America		 Tobacco	35	Maryland
222	Dover	 United States of America	 United States of America	 Grain	35	Maryland
223	Philadelphia	 United States of America		 Iron	40	Pennsylvania
224	Scranton	 United States of America		 Grain	35	Pennsylvania
225	Williamsport	 United States of America	 United States of America	 Coal	35	Pennsylvania
226	Harrisburg	 United States of America		 Tobacco	35	Pennsylvania
227	Pittsburgh	 United States of America		 Coal	35	Pennsylvania
228	Erie	 United States of America		 Timber	35	Pennsylvania
229	Newark	 United States of America		 Fish	35	New Jersey
230	Trenton	 United States of America		 Cattle	30	New Jersey
231	Atlantic City	 United States of America	 United States of America	 Fish	35	New Jersey
232	New York	 United States of America	 Manhattan Commune	 Grain	50	New York
233	Long Island	 United States of America	 United States of America	 Grain	35	New York
234	Albany	 United States of America	 United States of America	 Iron	35	New York
235	Binghamton	 United States of America		 Grain	35	New York
236	Buffalo	 United States of America	 United States of America	 Timber	35	New York
237	Rochester	 United States of America		 Grain	35	New York
238	Syracuse	 United States of America	 United States of America	 Grain	35	New York
239	Watertown	 United States of America		 Iron	35	New York
240	Plattsburgh	 United States of America		 Timber	35	New York
241	Hartford	 United States of America	 New England  United States of America	 Fish	35	Massachussets
242	Providence	 United States of America	 New England	 Grain	25	Massachussets
243	Boston	 United States of America	 New England	 Grain	40	Massachussets
244	New Bedford	 United States of America	 New England	 Grain	35	Massachussets
245	Pittsfield	 United States of America	 New England	 Iron	35	Massachussets
246	Burlington	 United States of America	 New England	 Timber	35	New England
247	Concord	 United States of America	 New England	 Timber	35	New England
248	Lewiston	 United States of America	 New England  United States of America	 Timber	35	New England
249	Bangor	 United States of America	 Canada  New England  United States of America	 Timber	35	New England
250	Caribou	 United Kingdom	 Canada  New England	 Timber	35	New England
251	Godthab	 Denmark	 Denmark  Scandinavia	 Fish	35	Iceland & Greenland
252	Iceland	 Denmark	 Denmark  Scandinavia	 Fish	35	Iceland & Greenland
253	Faroe Islands	 Denmark	 Denmark  Scandinavia	 Fish	35	Iceland & Greenland
254	Belfast	 United Kingdom	 Ireland  United Kingdom	 Cattle	35	Ulster
255	Londonderry	 United Kingdom	 Ireland  United Kingdom	 Cattle	35	Ulster
256	Armagh	 United Kingdom	 Ireland  United Kingdom	 Cattle	35	Ulster
257	Donegal	 United Kingdom	 Ireland  United Kingdom	 Cattle	35	Ulster
258	Galway	 United Kingdom	 Ireland  United Kingdom	 Cattle	35	Leinster-Connacht
259	Sligo	 United Kingdom	 Ireland  United Kingdom	 Cattle	35	Leinster-Connacht
260	Cork	 United Kingdom	 Ireland  United Kingdom	 Fish	35	Munster
261	Limerick	 United Kingdom	 Ireland  United Kingdom	 Fish	35	Munster
262	Waterford	 United Kingdom	 Ireland  United Kingdom	 Fish	35	Munster
263	Dublin	 United Kingdom	 Ireland  United Kingdom	 Grain	35	Leinster-Connacht
264	Kildare	 United Kingdom	 Ireland  United Kingdom	 Cattle	35	Leinster-Connacht
265	Wexford	 United Kingdom	 Ireland  United Kingdom	 Fish	35	Leinster-Connacht
266	Aberdeen	 United Kingdom	 Scotland  United Kingdom	 Wool	35	Highlands
267	Inverness	 United Kingdom	 Scotland  United Kingdom	 Sulphur	35	Highlands
268	Dundee	 United Kingdom	 Scotland  United Kingdom	 Fish	35	Highlands
269	Edinburgh	 United Kingdom	 Scotland  United Kingdom	 Coal	35	Lowlands
270	Stirling	 United Kingdom	 Scotland  United Kingdom	 Coal	35	Lowlands
271	Glasgow	 United Kingdom	 Scotland  United Kingdom	 Coal	35	Lowlands
272	Dumfries	 United Kingdom	 Scotland  United Kingdom	 Coal	35	Lowlands
273	Cardiff	 United Kingdom	 United Kingdom	 Coal	35	Wales
274	Cardigan	 United Kingdom	 United Kingdom	 Fish	35	Wales
275	Llandrindod	 United Kingdom	 United Kingdom	 Sulphur	35	Wales
276	Holyhead	 United Kingdom	 United Kingdom	 Fish	35	Wales
277	Liverpool	 United Kingdom	 United Kingdom	 Fish	40	North West England
278	Manchester	 United Kingdom	 United Kingdom	 Coal	40	North West England
279	Carlisle	 United Kingdom	 United Kingdom	 Grain	35	North West England
280	Newcastle upon Tyne	 United Kingdom	 United Kingdom	 Coal	35	North East England
281	Hull	 United Kingdom	 United Kingdom	 Fish	35	North East England
282	Leeds	 United Kingdom	 United Kingdom	 Coal	35	North East England
283	Sheffield	 United Kingdom	 United Kingdom	 Coal	35	North East England
284	Birmingham	 United Kingdom	 United Kingdom	 Coal	35	Midlands
285	Chester	 United Kingdom	 United Kingdom	 Fish	35	North West England
286	Shrewsbury	 United Kingdom	 United Kingdom	 Iron	35	Midlands
287	Coventry	 United Kingdom	 United Kingdom	 Grain	35	Midlands
288	Nottingham	 United Kingdom	 United Kingdom	 Coal	35	Midlands
289	Leicester	 United Kingdom	 United Kingdom	 Grain	35	Midlands
290	Lincoln	 United Kingdom	 United Kingdom	 Iron	35	Midlands
291	Cambridge	 United Kingdom	 United Kingdom	 Grain	35	Eastern Counties
292	Ipswich	 United Kingdom	 United Kingdom	 Grain	35	Eastern Counties
293	Chelmsford	 United Kingdom	 United Kingdom	 Coal	35	Eastern Counties
294	Oxford	 United Kingdom	 United Kingdom	 Grain	35	South East England
295	St Albans	 United Kingdom	 United Kingdom	 Grain	35	Eastern Counties
296	Bristol	 United Kingdom	 United Kingdom	 Iron	35	South West England
297	Salisbury	 United Kingdom	 United Kingdom	 Grain	35	South West England
298	Bath	 United Kingdom	 United Kingdom	 Grain	35	South West England
299	Plymouth	 United Kingdom	 United Kingdom	 Fish	35	South West England
300	London	 United Kingdom	 United Kingdom	 Grain	45	South East England
301	Canterbury	 United Kingdom	 United Kingdom	 Coal	35	South East England
302	Brighton	 United Kingdom	 United Kingdom	 Fish	35	South East England
303	Southampton	 United Kingdom	 United Kingdom	 Fish	35	South East England
304	Isle of Man	 United Kingdom	 United Kingdom	 Fish	35	North West England
305	Trondheim	 Sweden	 Norway  Sweden  Scandinavia	 Timber	35	Nordnorge
306	Bodo	 Sweden	 Norway  Sweden  Scandinavia	 Fish	35	Nordnorge
307	Hammerfest	 Sweden	 Norway  Sweden  Scandinavia	 Timber	35	Nordnorge
308	Alesund	 Sweden	 Norway  Sweden  Scandinavia	 Fish	35	Nordnorge
309	Bergen	 Sweden	 Norway  Sweden  Scandinavia	 Fish	35	Vestlandet
310	Christiansand	 Sweden	 Norway  Sweden  Scandinavia	 Fish	35	Vestlandet
311	Skien	 Sweden	 Norway  Sweden  Scandinavia	 Timber	35	Vestlandet
312	Drammen	 Sweden	 Norway  Sweden  Scandinavia	 Grain	35	Vestlandet
313	Christiania	 Sweden	 Norway  Sweden  Scandinavia	 Fish	35	Ostlandet
314	Hamar	 Sweden	 Norway  Sweden  Scandinavia	 Grain	35	Ostlandet
315	Lillehammer	 Sweden	 Norway  Sweden  Scandinavia	 Timber	35	Ostlandet
316	Frederiksstad	 Sweden	 Norway  Sweden  Scandinavia	 Grain	35	Ostlandet
317	Gävle	 Sweden	 Sweden  Scandinavia	 Timber	35	Norrland
318	Sundsvall	 Sweden	 Sweden  Scandinavia	 Timber	35	Norrland
319	Östersund	 Sweden	 Sweden  Scandinavia	 Timber	35	Norrland
320	Umeå	 Sweden	 Sweden  Scandinavia	 Timber	35	Norrland
321	Luleå	 Sweden	 Sweden  Scandinavia	 Iron	35	Norrland
322	Stockholm	 Sweden	 Sweden  Scandinavia	 Coal	35	Svealand
323	Falun	 Sweden	 Sweden  Scandinavia	 Iron	35	Svealand
324	Uppsala	 Sweden	 Sweden  Scandinavia	 Timber	35	Svealand
325	Norrköping	 Sweden	 Sweden  Scandinavia	 Grain	35	Svealand
326	Västerås	 Sweden	 Sweden  Scandinavia	 Iron	35	Svealand
327	Örebro	 Sweden	 Sweden  Scandinavia	 Timber	35	Svealand
328	Karlstad	 Sweden	 Sweden  Scandinavia	 Timber	35	Svealand
329	Göteborg	 Sweden	 Sweden  Scandinavia	 Fish	35	Götaland
330	Borås	 Sweden	 Sweden  Scandinavia	 Fish	35	Götaland
331	Gotland	 Sweden	 Sweden  Scandinavia	 Grain	35	Götaland
332	Kalmar	 Sweden	 Sweden  Scandinavia	 Timber	35	Götaland
333	Växjö	 Sweden	 Sweden  Scandinavia	 Grain	35	Götaland
334	Malmö	 Sweden	 Sweden  Scandinavia	 Grain	35	Götaland
335	Karlskrona	 Sweden	 Sweden  Scandinavia	 Fish	35	Götaland
336	Oulu	 Russia	 Finland  Sweden  Russia	 Timber	35	Northern Finland
337	Kajaani	 Russia	 Finland  Sweden  Russia	 Timber	35	Northern Finland
338	Tornio	 Russia	 Finland  Sweden  Russia	 Iron	35	Northern Finland
339	Viipuri	 Russia	 Finland  Russia	 Timber	35	Southern Finland
340	Kotka	 Russia	 Finland  Sweden  Russia	 Timber	35	Southern Finland
341	Mikkeli	 Russia	 Finland  Sweden  Russia	 Timber	35	Northern Finland
342	Kuopio	 Russia	 Finland  Sweden  Russia	 Iron	35	Northern Finland
343	Helsinki	 Russia	 Finland  Sweden  Russia	 Grain	35	Southern Finland
344	Hämeenlinna	 Russia	 Finland  Sweden  Russia	 Timber	35	Southern Finland
345	Turku	 Russia	 Finland  Sweden  Russia	 Fish	35	Southern Finland
346	Vaasa	 Russia	 Finland  Sweden  Russia	 Timber	35	Southern Finland
347	Tampere	 Russia	 Finland  Sweden  Russia	 Timber	35	Southern Finland
348	Åland Islands	 Russia	 Finland  Sweden  Russia	 Fish	35	Southern Finland
349	Reval	 Russia	 Estonia  Russia	 Grain	35	Estonia
350	Narva	 Russia	 Estonia  Russia	 Cattle	35	Estonia
351	Pärnu	 Russia	 Estonia  Russia	 Grain	35	Estonia
352	Dorpat	 Russia	 Estonia  Russia	 Cattle	35	Estonia
353	Ösel	 Russia	 Estonia  Russia	 Grain	35	Estonia
354	Riga	 Russia	 Latvia  Russia	 Fish	35	Latvia
355	Valmeira	 Russia	 Latvia  Russia	 Cattle	35	Latvia
356	Daugavpils	 Russia	 Latvia  Russia	 Grain	35	Latvia
357	Jelgava	 Russia	 Latvia  Russia	 Cattle	35	Latvia
358	Ventspils	 Russia	 Latvia  Russia	 Fish	35	Latvia
359	Liepaja	 Russia	 Latvia  Russia	 Grain	35	Latvia
360	Vilnius	 Russia	 Lithuania  Poland  Russia	 Grain	35	Lietuva
361	Kaunas	 Russia	 Lithuania  Russia	 Grain	35	Lietuva
362	Marijampole	 Russia	 Lithuania  Russia	 Grain	35	Lietuva
363	Panevezys	 Russia	 Lithuania  Russia	 Grain	35	Lietuva
364	Siauliai	 Russia	 Lithuania  Russia	 Cattle	35	Lietuva
365	Palanga	 Russia	 Lithuania  Russia	 Grain	35	Lietuva
366	Aarhus	 Denmark	 Denmark  Scandinavia	 Grain	35	Jylland
367	Aalborg	 Denmark	 Denmark  Scandinavia	 Fish	35	Jylland
368	Ribe	 Denmark	 Denmark  Scandinavia	 Cattle	35	Jylland
369	Kiel	 Holstein	 Germany  Holstein	 Cattle	35	Schleswig-Holstein
370	Flensburg	 Denmark	 Denmark  Germany  Schleswig	 Cattle	35	Schleswig-Holstein
371	Aabenraa	 Denmark	 Denmark  Germany  Schleswig	 Cattle	35	Schleswig-Holstein
372	Copenhagen	 Denmark	 Denmark  Scandinavia	 Grain	35	Sjaelland
373	Odense	 Denmark	 Denmark  Scandinavia	 Grain	35	Sjaelland
374	Bornholm	 Denmark	 Denmark  Scandinavia	 Fish	35	Sjaelland
375	Amsterdam	 Netherlands	 Netherlands	 Cattle	35	Holland
376	Rotterdam	 Netherlands	 Netherlands	 Fish	35	Holland
377	Utrecht	 Netherlands	 Netherlands	 Grain	35	Holland
378	Middelburg	 Netherlands	 Netherlands	 Fish	35	Holland
379	Eindhoven	 Netherlands	 Netherlands	 Coal	35	Gelderland
380	Breda	 Netherlands	 Netherlands	 Cattle	35	Gelderland
381	Maastricht	 Netherlands	 Netherlands	 Coal	35	Gelderland
382	Arnhem	 Netherlands	 Netherlands	 Cattle	35	Gelderland
383	Groningen	 Netherlands	 Netherlands	 Grain	35	Friesland
384	Zwolle	 Netherlands	 Netherlands	 Fish	35	Friesland
385	Leeuwarden	 Netherlands	 Netherlands	 Cattle	35	Friesland
386	Assen	 Netherlands	 Netherlands	 Wool	35	Friesland
387	Brussels	 Belgium	 Belgium  Flanders  Netherlands	 Sulphur	35	Vlaanderen
388	Bruges	 Belgium	 Belgium  Flanders  Netherlands	 Grain	35	Vlaanderen
389	Ghent	 Belgium	 Belgium  Flanders  Netherlands	 Wool	35	Vlaanderen
390	Antwerp	 Belgium	 Belgium  Flanders  Netherlands	 Cattle	35	Vlaanderen
391	Hasselt	 Belgium	 Belgium  Flanders  Netherlands	 Coal	35	Vlaanderen
392	Namur	 Belgium	 Belgium  Netherlands  Wallonia	 Iron	35	Wallonie
393	Tournai	 Belgium	 Belgium  Netherlands  Wallonia	 Coal	35	Wallonie
394	Charleroi	 Belgium	 Belgium  Netherlands  Wallonia	 Coal	35	Wallonie
395	Liège	 Belgium	 Belgium  Netherlands  Wallonia	 Iron	35	Wallonie
396	Spa	 Belgium	 Belgium  Netherlands  Wallonia	 Coal	35	Wallonie
397	Luxembourg	 Luxembourg	 Luxembourg	 Iron	35	Wallonie
398	Arlon	 Belgium	 Belgium  Netherlands  Wallonia	 Timber	35	Wallonie
399	Lille	 France	 France	 Iron	35	Picardie
400	Dunkirk	 France	 France	 Fish	35	Picardie
401	Arras	 France	 France	 Coal	35	Picardie
402	Amiens	 France	 France	 Fish	35	Picardie
403	Laon	 France	 France	 Grain	35	Champagne
404	Cambrai	 France	 France	 Coal	35	Champagne
405	Charleville	 France	 France	 Coal	35	Champagne
406	Troyes	 France	 France	 Timber	35	Champagne
407	Chaumont	 France	 France	 Iron	35	Franche-Comté
408	Chalons	 France	 France	 Fruit	35	Champagne
409	Strasbourg	 France	 France  Germany	 Grain	35	Alsace-Lorraine
410	Colmar	 France	 France  Germany	 Sulphur	35	Alsace-Lorraine
411	Nancy	 France	 France	 Iron	35	Franche-Comté
412	Metz	 France	 France  Germany	 Precious metal	35	Alsace-Lorraine
413	Verdun	 France	 France	 Coal	35	Franche-Comté
414	Épinal	 France	 France	 Sulphur	35	Franche-Comté
415	Rouen	 France	 France	 Cotton	35	Normandie
416	Évreux	 France	 France	 Grain	35	Normandie
417	Alençon	 France	 France	 Cotton	35	Normandie
418	Caen	 France	 France	 Cotton	35	Normandie
419	Channel Islands	 United Kingdom	 United Kingdom	 Fish	35	South West England
420	Brest	 France	 France	 Grain	35	Bretagne
421	St Brieuc	 France	 France	 Grain	35	Bretagne
422	Vannes	 France	 France	 Fish	35	Bretagne
423	Nantes	 France	 France	 Coal	35	Bretagne
424	Rennes	 France	 France	 Grain	35	Bretagne
425	Paris	 France	 France	 Grain	40	Ile de France
426	Chartres	 France	 France	 Grain	35	Ile de France
427	Melun	 France	 France	 Grain	35	Ile de France
428	Dijon	 France	 France	 Fruit	35	Bourgogne
429	Auxerre	 France	 France	 Iron	35	Bourgogne
430	Moulins	 France	 France	 Coal	35	Bourgogne
431	Macon	 France	 France	 Coal	35	Bourgogne
432	Besançon	 France	 France	 Coal	35	Bourgogne
433	Lons	 France	 France	 Grain	35	Bourgogne
434	Angers	 France	 France	 Coal	35	Loire
435	Laval	 France	 France	 Coal	35	Loire
436	Le Mans	 France	 France	 Grain	35	Region Centre
437	La Roche	 France	 France	 Grain	35	Loire
438	Orléans	 France	 France	 Timber	35	Region Centre
439	Bourges	 France	 France	 Timber	35	Region Centre
440	Blois	 France	 France	 Grain	35	Region Centre
441	Tours	 France	 France	 Grain	35	Region Centre
442	La Rochelle	 France	 France	 Fish	35	Poitou
443	Poitiers	 France	 France	 Grain	35	Poitou
444	Angoulême	 France	 France	 Cattle	35	Poitou
445	Limoges	 France	 France	 Cattle	35	Limousin
446	Châteauroux	 France	 France	 Grain	35	Limousin
447	Tulle	 France	 France	 Coal	35	Limousin
448	Clermont-Ferrand	 France	 France	 Coal	35	Auvergne
449	Aurillac	 France	 France	 Coal	35	Auvergne
450	Cahors	 France	 France	 Timber	35	Auvergne
451	Lyon	 France	 France	 Grain	35	Rhone
452	St Étienne	 France	 France	 Sulphur	35	Rhone
453	Valence	 France	 France	 Coal	35	Rhone
454	Grenoble	 France	 France	 Tobacco	35	Rhone
455	Toulouse	 France	 France	 Grain	35	Le Midi
456	Montauban	 France	 France	 Tobacco	35	Le Midi
457	Foix	 France	 France	 Grain	35	Le Midi
458	Bordeaux	 France	 France	 Fruit	35	Aquitaine
459	Mont de Marsan	 France	 France	 Grain	35	Aquitaine
460	Pau	 France	 France	 Grain	35	Aquitaine
461	Montpellier	 France	 France	 Cattle	35	Languedoc
462	Rodez	 France	 France	 Coal	35	Languedoc
463	Carcassone	 France	 France	 Grain	35	Languedoc
464	Perpignan	 France	 Catalonia  France	 Grain	35	Languedoc
465	Annecy	 Sardinia-Piedmont	 Italy  Sardinia-Piedmont	 Coal	35	Savoie
466	Chambéry	 Sardinia-Piedmont	 Italy  Sardinia-Piedmont	 Grain	35	Savoie
467	Marseilles	 France	 France	 Coal	35	Provence
468	Avignon	 France	 France	 Sulphur	35	Provence
469	Digne	 France	 France	 Silk	35	Provence
470	Toulon	 France	 France	 Silk	35	Provence
471	Frejus	 France	 France	 Silk	35	Provence
472	Nice	 Sardinia-Piedmont	 Italy  Sardinia-Piedmont	 Grain	35	Provence
473	Corsica	 France	 France	 Fish	35	Provence
474	La Coruña	 Spain	 Spain	 Fish	35	Galicia
475	Oviedo	 Spain	 Spain	 Coal	35	Galicia
476	Vigo	 Spain	 Spain	 Fish	35	Galicia
477	León	 Spain	 Spain	 Coal	35	León-Castilla
478	Santander	 Spain	 Spain	 Fish	35	Galicia
479	Burgos	 Spain	 Spain	 Iron	35	León-Castilla
480	Valladolid	 Spain	 Spain	 Cattle	35	León-Castilla
481	Soria	 Spain	 Spain	 Grain	35	León-Castilla
482	Salamanca	 Spain	 Spain	 Grain	35	León-Castilla
483	Ávila	 Spain	 Spain	 Grain	35	León-Castilla
484	Badajoz	 Spain	 Spain	 Wool	35	Extremadura
485	Almendralejo	 Spain	 Spain	 Wool	35	Extremadura
486	Cáceres	 Spain	 Spain	 Iron	35	Extremadura
487	Madrid	 Spain	 Spain	 Cattle	40	Castilla la Nueva
488	Sigüenza	 Spain	 Spain	 Grain	35	Castilla la Nueva
489	Toledo	 Spain	 Spain	 Iron	35	Castilla la Nueva
490	Cuenca	 Spain	 Spain	 Grain	35	Castilla la Nueva
491	Ciudad Real	 Spain	 Spain	 Grain	35	Castilla la Nueva
492	Bilbao	 Spain	 Spain	 Iron	35	Vasconia-Aragón
493	Pamplona	 Spain	 Spain	 Fruit	35	Vasconia-Aragón
494	Logroño	 Spain	 Spain	 Iron	35	Vasconia-Aragón
495	Zaragoza	 Spain	 Spain	 Grain	35	Vasconia-Aragón
496	Huesca	 Spain	 Spain	 Wool	35	Vasconia-Aragón
497	Teruel	 Spain	 Spain	 Grain	35	Vasconia-Aragón
498	Barcelona	 Spain	 Catalonia  Spain	 Cattle	35	Catalonia
499	Gerona	 Spain	 Catalonia  Spain	 Fruit	35	Catalonia
500	Lérida	 Spain	 Catalonia  Spain	 Fruit	35	Catalonia
501	Tarragona	 Spain	 Catalonia  Spain	 Grain	35	Catalonia
502	Balearic Islands	 Spain	 Spain	 Cattle	35	Catalonia
503	Valencia	 Spain	 Spain	 Fruit	35	Valencia
504	Castellón	 Spain	 Spain	 Fruit	35	Valencia
505	Alicante	 Spain	 Spain	 Fruit	35	Valencia
506	Cartagena	 Spain	 Spain	 Iron	35	Valencia
507	Murcia	 Spain	 Spain	 Iron	35	Valencia
508	Albacete	 Spain	 Spain	 Fruit	35	Valencia
509	Seville	 Spain	 Spain	 Grain	35	Andalucía
510	Córdoba	 Spain	 Spain	 Grain	35	Andalucía
511	Huelva	 Spain	 Spain	 Grain	35	Andalucía
512	Cádiz	 Spain	 Spain	 Fish	35	Andalucía
513	Granada	 Spain	 Spain	 Iron	35	Granada
514	Málaga	 Spain	 Spain	 Coal	35	Granada
515	Almería	 Spain	 Spain	 Iron	35	Granada
516	Jaén	 Spain	 Spain	 Grain	35	Granada
517	Gibraltar	 United Kingdom	 United Kingdom	 Fish	35	Gibraltar
518	Oporto	 Portugal	 Portugal	 Fruit	35	Douro
519	Vila Real	 Portugal	 Portugal	 Fruit	35	Douro
520	Covilhã	 Portugal	 Portugal	 Wool	35	Douro
521	Lisbon	 Portugal	 Portugal	 Grain	35	Estremadura
522	Coimbra	 Portugal	 Portugal	 Fruit	35	Estremadura
523	Abrantes	 Portugal	 Portugal	 Grain	35	Estremadura
524	Setubal	 Portugal	 Portugal	 Grain	35	Estremadura
525	Évora	 Portugal	 Portugal	 Grain	35	Alentejo
526	Beja	 Portugal	 Portugal	 Iron	35	Alentejo
527	Faro	 Portugal	 Portugal	 Fruit	35	Alentejo
528	Hamburg	 Hamburg	 Germany  Hamburg	 Fruit	35	Osthannover
529	Lauenburg	 Holstein	 Germany  Holstein	 Grain	35	Schlewsig-Holstein
530	Lübeck	 Lübeck	 Germany  Lübeck	 Fish	35	Schlewsig-Holstein
531	Stade	 Hannover	 Germany  Hannover	 Cattle	35	Osthannover
532	Lüneburg	 Hannover	 Germany  Hannover	 Cattle	35	Osthannover
533	Heligoland	 United Kingdom	 United Kingdom	 Fish	35	Osthannover
534	Hanover	 Hannover	 Germany  Hannover	 Fruit	35	Hannover
535	Nienburg	 Hannover	 Germany  Hannover	 Grain	35	Hannover
536	Brunswick	 Braunschweig	 Braunschweig  Germany	 Fruit	35	Hessen
537	Göttingen	 Hannover	 Germany  Hannover	 Grain	35	Hessen
538	Osnabrück	 Hannover	 Germany  Hannover	 Grain	35	Hannover
539	Bremen	 Bremen	 Bremen  Germany	 Fish	35	Osthannover
540	Oldenburg	 Oldenburg	 Germany  Oldenburg	 Fish	35	Hannover
541	Cloppenburg	 Oldenburg	 Germany  Oldenburg	 Coal	35	Hannover
542	Lingen	 Hannover	 Germany  Hannover	 Cattle	35	Hannover
543	Emden	 Hannover	 Germany  Hannover	 Fish	35	Hannover
544	Schwerin	 Mecklenburg	 Germany  Mecklenburg	 Grain	35	Pommern
545	Neustrelitz	 Mecklenburg	 Germany  Mecklenburg	 Grain	35	Pommern
546	Stettin	 Prussia	 Germany  Prussia	 Fish	35	Pommern
547	Swinemünde	 Prussia	 Germany  Prussia	 Fruit	35	Pommern
548	Stralsund	 Prussia	 Germany  Prussia	 Fish	35	Pommern
549	Berlin	 Prussia	 Germany  Prussia	 Fruit	40	Brandenburg
550	Prenzlau	 Prussia	 Germany  Prussia	 Cattle	35	Brandenburg
551	Pritzwalk	 Prussia	 Germany  Prussia	 Cattle	35	Brandenburg
552	Cottbus	 Prussia	 Germany  Prussia	 Fruit	35	Brandenburg
553	Magdeburg	 Prussia	 Germany  Prussia	 Cattle	35	Magdeburg
554	Erfurt	 Prussia	 Germany  Prussia	 Iron	35	Magdeburg
555	Dessau	 Anhalt	 Anhalt  Germany	 Fruit	35	Magdeburg
556	Halle	 Prussia	 Germany  Prussia	 Fruit	35	Magdeburg
557	Stendal	 Prussia	 Germany  Prussia	 Grain	35	Magdeburg
558	Dresden	 Saxony	 Germany  Saxony	 Coal	35	Sachsen
559	Leipzig	 Saxony	 Germany  Saxony	 Coal	35	Sachsen
560	Chemnitz	 Saxony	 Germany  Saxony	 Iron	35	Sachsen
561	Weimar	 Saxe-Weimar	 Germany  Saxe-Weimar	 Grain	35	Sachsen
562	Gotha	 Saxe-Coburg-Gotha	 Germany  Saxe-Coburg-Gotha	 Iron	35	Sachsen
563	Meiningen	 Saxe-Meiningen	 Germany  Saxe-Meiningen	 Iron	35	Sachsen
564	Frankfurt	 Frankfurt am Main	 Frankfurt am Main  Germany	 Fruit	35	Hesse-Nassau
565	Wiesbaden	 Nassau	 Germany  Nassau	 Fruit	35	Hesse-Nassau
566	Kassel	 Hesse-Kassel	 Germany  Hesse-Kassel	 Grain	35	Hessen
567	Giessen	 Hesse-Darmstadt	 Germany  Hesse-Darmstadt	 Cattle	35	Hesse-Nassau
568	Fulda	 Hesse-Kassel	 Germany  Hesse-Kassel	 Grain	35	Hessen
569	Mannheim	 Baden	 Baden  Germany	 Grain	35	Baden
570	Mainz	 Hesse-Darmstadt	 Germany  Hesse-Darmstadt	 Sulphur	35	Rhineland
571	Kaiserlautern	 Bavaria	 Bavaria  Germany	 Fruit	35	Rhineland
572	Trier	 Prussia	 Germany  Prussia	 Fruit	35	Rhineland
573	Saarbrücken	 Prussia	 Germany  Prussia	 Coal	35	Rhineland
574	Kreuznach	 Prussia	 Germany  Prussia	 Grain	35	Rhineland
575	Cologne	 Prussia	 Germany  Prussia	 Coal	35	Nordrhein
576	Aachen	 Prussia	 Germany  Prussia	 Coal	35	Nordrhein
577	Cleves	 Prussia	 Germany  Prussia	 Coal	35	Nordrhein
578	Düsseldorf	 Prussia	 Germany  Prussia	 Coal	35	Nordrhein
579	Koblenz	 Prussia	 Germany  Prussia	 Timber	35	Nordrhein
580	Dortmund	 Prussia	 Germany  Prussia	 Coal	35	Westfalen
581	Münster	 Prussia	 Germany  Prussia	 Coal	35	Westfalen
582	Minden	 Prussia	 Germany  Prussia	 Cattle	35	Westfalen
583	Siegen	 Prussia	 Germany  Prussia	 Cattle	35	Westfalen
584	Korbach	 Prussia	 Germany  Prussia	 Timber	35	Westfalen
585	Detmold	 Lippe-Detmold	 Germany  Lippe-Detmold	 Coal	35	Westfalen
586	Karlsruhe	 Baden	 Baden  Germany	 Fruit	35	Baden
587	Freiburg	 Baden	 Baden  Germany	 Fruit	35	Baden
588	Konstanz	 Baden	 Baden  Germany	 Timber	35	Baden
589	Stuttgart	 Württemberg	 Germany  Württemberg	 Fruit	35	Württemberg
590	Heilbronn	 Württemberg	 Germany  Württemberg	 Fruit	35	Württemberg
591	Tübingen	 Württemberg	 Germany  Württemberg	 Grain	35	Württemberg
592	Augsburg	 Bavaria	 Bavaria  Germany	 Cattle	35	Bayern
593	Ulm	 Württemberg	 Germany  Württemberg	 Grain	35	Württemberg
594	Sigmaringen	 Prussia	 Germany  Prussia	 Grain	35	Württemberg
595	Nuremberg	 Bavaria	 Bavaria  Germany	 Grain	35	Franken
596	Aschaffenburg	 Bavaria	 Bavaria  Germany	 Grain	35	Franken
597	Würzburg	 Bavaria	 Bavaria  Germany	 Fruit	35	Franken
598	Bayreuth	 Bavaria	 Bavaria  Germany	 Timber	35	Franken
599	Munich	 Bavaria	 Bavaria  Germany	 Cattle	35	Bayern
600	Landshut	 Bavaria	 Bavaria  Germany	 Cattle	35	Bayern
601	Ingolstadt	 Bavaria	 Bavaria  Germany	 Grain	35	Bayern
602	Regensburg	 Bavaria	 Bavaria  Germany	 Grain	35	Bayern
603	Zurich	 Switzerland	 Switzerland	 Cattle	35	East Switzerland
604	Basel	 Switzerland	 Switzerland	 Fruit	35	West Switzerland
605	Bern	 Switzerland	 Switzerland	 Iron	35	West Switzerland
606	Lucerne	 Switzerland	 Switzerland	 Timber	35	East Switzerland
607	Geneva	 Switzerland	 Switzerland	 Grain	35	West Switzerland
608	Neuchâtel	 Switzerland	 Prussia  Switzerland	 Coal	35	West Switzerland
609	Sitten	 Switzerland	 Switzerland	 Coal	35	West Switzerland
610	Ponape	uncolonized		 Fish	15	Micronesia
611	Chur	 Switzerland	 Switzerland	 Cattle	35	East Switzerland
612	Innsbruck	 Austria	 Austria	 Timber	35	Tirol
613	Salzburg	 Austria	 Austria	 Grain	35	Tirol
614	Bregenz	 Austria	 Austria	 Timber	35	Tirol
615	Lienz	 Austria	 Austria	 Timber	35	Tirol
616	Graz	 Austria	 Austria	 Iron	35	Kärnten-Steiermark
617	Judenburg	 Austria	 Austria	 Iron	35	Kärnten-Steiermark
618	Klagenfurt	 Austria	 Austria	 Coal	35	Kärnten-Steiermark
619	Vienna	 Austria	 Austria	 Grain	35	Österreich
620	Sankt Pölten	 Austria	 Austria	 Coal	35	Österreich
621	Krems	 Austria	 Austria	 Grain	35	Österreich
622	Linz	 Austria	 Austria	 Sulphur	35	Österreich
623	Sopron	 Austria	 Austria  Hungary	 Fruit	35	Transdanubia
624	Eisenstadt	 Austria	 Austria  Hungary	 Grain	35	Österreich
625	Prague	 Austria	 Austria  Bohemia-Moravia  Czechoslovakia	 Iron	35	Bohemia
626	Hradec Králové	 Austria	 Austria  Bohemia-Moravia  Czechoslovakia	 Coal	35	Bohemia
627	Karlsbad	 Austria	 Austria  Bohemia-Moravia  Czechoslovakia	 Iron	35	Bohemia
628	Aussig	 Austria	 Austria  Bohemia-Moravia  Czechoslovakia	 Coal	35	Bohemia
629	Plzen	 Austria	 Austria  Bohemia-Moravia  Czechoslovakia	 Coal	35	Bohemia
630	Budejovice	 Austria	 Austria  Bohemia-Moravia  Czechoslovakia	 Coal	35	Bohemia
631	Brno	 Austria	 Austria  Bohemia-Moravia  Czechoslovakia	 Coal	35	Moravia
632	Olomouc	 Austria	 Austria  Bohemia-Moravia  Czechoslovakia	 Coal	35	Moravia
633	Bratislava	 Austria	 Austria  Czechoslovakia  Hungary  Slovakia	 Cattle	35	Slovakia
634	Trencín	 Austria	 Austria  Czechoslovakia  Hungary  Slovakia	 Grain	35	Slovakia
635	Nitra	 Austria	 Austria  Czechoslovakia  Hungary  Slovakia	 Grain	35	Slovakia
636	Banská Bystrica	 Austria	 Austria  Czechoslovakia  Hungary  Slovakia	 Grain	35	Slovakia
637	Koice	 Austria	 Austria  Czechoslovakia  Hungary  Slovakia	 Coal	35	Slovakia
638	Ronava	 Austria	 Austria  Czechoslovakia  Hungary  Slovakia	 Coal	35	Slovakia
639	Zalaegerszeg	 Austria	 Austria  Hungary	 Cattle	35	Transdanubia
640	Pécs	 Austria	 Austria  Hungary	 Cattle	35	Transdanubia
641	Budapest	 Austria	 Austria  Hungary	 Cattle	35	Central Hungary
642	Gyor	 Austria	 Austria  Hungary	 Cattle	35	Transdanubia
643	Székesfehévár	 Austria	 Austria  Hungary	 Grain	35	Transdanubia
644	Kaposvár	 Austria	 Austria  Hungary	 Cattle	35	Transdanubia
645	Kecskemét	 Austria	 Austria  Hungary	 Grain	35	Transdanubia
646	Miskolc	 Austria	 Austria  Hungary	 Fruit	35	Transdanubia
647	Oradea	 Austria	 Austria  Hungary  Romania  Siebenbürgen	 Wool	35	Alföld
648	Debrecen	 Austria	 Austria  Hungary  Romania	 Fruit	35	Transdanubia
649	Szeged	 Austria	 Austria  Hungary	 Fruit	35	Transdanubia
650	Békéscsab	 Austria	 Austria  Hungary  Romania	 Fruit	35	Transdanubia
651	Szatmár	 Austria	 Austria  Hungary  Romania  Siebenbürgen	 Fruit	35	Alföld
652	Temesvar	 Austria	 Austria  Hungary  Romania  Siebenbürgen	 Grain	35	Alföld
653	Resicabánya	 Austria	 Austria  Hungary  Romania  Siebenbürgen	 Grain	35	Alföld
654	Cluj	 Austria	 Austria  Hungary  Romania  Siebenbürgen	 Grain	35	Western Siebenbürgen
655	Gyulafehervar	 Austria	 Austria  Hungary  Romania  Siebenbürgen	 Grain	35	Western Siebenbürgen
656	Deva	 Austria	 Austria  Hungary  Romania  Siebenbürgen	 Grain	35	Western Siebenbürgen
657	Nagyszeben	 Austria	 Austria  Hungary  Romania  Siebenbürgen	 Cattle	35	Eastern Siebenbürgen
658	Hawaii	 Hawaii	 Hawaii	 Fish	35	Hawaiian Islands
659	Brasso	 Austria	 Austria  Hungary  Romania  Siebenbürgen	 Wool	35	Eastern Siebenbürgen
660	Udvarhely	 Austria	 Austria  Hungary  Romania  Siebenbürgen	 Wool	35	Eastern Siebenbürgen
661	Beszterce	 Austria	 Austria  Hungary  Romania  Siebenbürgen	 Grain	35	Western Siebenbürgen
662	Cernauti	 Austria	 Austria  Moldavia  Romania  Ruthenia  Ukraine	 Fruit	35	Moldavia
663	Suceava	 Austria	 Austria  Moldavia  Romania  Ruthenia  Ukraine	 Cattle	35	Moldavia
664	Bucharest	 Wallachia	 Romania  Wallachia	 Grain	35	Wallachia
665	Tirgu Jiu	 Wallachia	 Romania  Wallachia	 Grain	35	Wallachia
666	Craiova	 Wallachia	 Romania  Wallachia	 Coal	35	Wallachia
667	Tirgoviste	 Wallachia	 Romania  Wallachia	 Wool	35	Wallachia
668	Braila	 Wallachia	 Romania  Wallachia	 Coal	35	Wallachia
669	Calarasi	 Wallachia	 Romania  Wallachia	 Coal	35	Wallachia
670	Iasi	 Moldavia	 Moldavia  Romania	 Fruit	35	Moldavia
671	Botosani	 Moldavia	 Moldavia  Romania	 Fruit	35	Moldavia
672	Bacau	 Moldavia	 Moldavia  Romania	 Grain	35	Moldavia
673	Galati	 Moldavia	 Moldavia  Romania	 Grain	35	Moldavia
674	Constanta	 Ottoman Empire	 Bulgaria  Ottoman Empire  Romania  Wallachia	 Grain	35	Dobrudja
675	Tulcea	 Ottoman Empire	 Ottoman Empire  Romania  Wallachia	 Coal	35	Dobrudja
676	Chisinau	 Russia	 Moldavia  Romania  Russia	 Fruit	35	Budjak
677	Balti	 Russia	 Moldavia  Romania  Russia	 Fruit	35	Budjak
678	Izmail	 Russia	 Moldavia  Romania  Russia	 Fish	35	Budjak
679	Kolberg	 Prussia	 Germany  Poland  Prussia	 Grain	35	Pommern
680	Köslin	 Prussia	 Germany  Poland  Prussia	 Grain	35	Pommern
681	Küstrin	 Prussia	 Germany  Prussia	 Grain	35	Brandenburg
682	Breslau	 Prussia	 Germany  Poland  Prussia	 Grain	35	Schlesien
683	Liegnitz	 Prussia	 Germany  Poland  Prussia	 Fruit	35	Schlesien
684	Oppeln	 Prussia	 Germany  Poland  Prussia	 Coal	35	Schlesien
685	Kattowitz	 Prussia	 Germany  Poland  Prussia	 Coal	35	Schlesien
686	Line Islands	uncolonized		 Fish	15	Kiribati
687	Görlitz	 Prussia	 Germany  Prussia	 Coal	35	Sachsen
688	Troppau	 Austria	 Austria  Bohemia-Moravia  Czechoslovakia	 Coal	35	Moravia
689	Tesin	 Austria	 Austria  Bohemia-Moravia  Czechoslovakia	 Coal	35	Moravia
690	Danzig	 Prussia	 Danzig  Germany  Poland  Prussia	 Fish	35	Westpreußen
691	Tuchel	 Prussia	 Germany  Poland  Prussia	 Cattle	35	Posen
692	Deutsch Krone	 Prussia	 Germany  Poland  Prussia	 Grain	35	Posen
693	Elbing	 Prussia	 Germany  Poland  Prussia	 Cattle	35	Westpreußen
694	Torun	 Prussia	 Germany  Poland  Prussia	 Grain	35	Westpreußen
695	Königsberg	 Prussia	 Germany  Prussia	 Cattle	35	Ostpreußen
696	Allenstein	 Prussia	 Germany  Poland  Prussia	 Cattle	35	Westpreußen
697	Gumbinnen	 Prussia	 Germany  Prussia	 Grain	35	Ostpreußen
698	Memel	 Prussia	 Germany  Lithuania  Prussia	 Fish	35	Ostpreußen
699	Posen	 Prussia	 Germany  Poland  Prussia	 Grain	35	Posen
700	Bromberg	 Prussia	 Germany  Poland  Prussia	 Grain	35	Posen
701	Gniezno	 Prussia	 Germany  Poland  Prussia	 Grain	35	Posen
702	Lvov	 Austria	 Austria  Poland  Ruthenia  Ukraine	 Coal	35	East Galicia
703	Krakow	 Krakow	 Krakow  Poland	 Coal	35	West Galicia
704	Novy Sacz	 Austria	 Austria  Poland	 Grain	35	West Galicia
705	Przemysl	 Austria	 Austria  Poland	 Coal	35	West Galicia
706	Warsaw	 Russia	 Poland  Russia	 Cattle	35	Mazowieckie
707	Suwalki	 Russia	 Poland  Russia	 Grain	35	Mazowieckie
708	Plock	 Russia	 Poland  Russia	 Fruit	35	Mazowieckie
709	Lomza	 Russia	 Poland  Russia	 Grain	35	Mazowieckie
710	Skierniewice	 Russia	 Poland  Russia	 Fruit	35	Wielkopolskie
711	Siedlice	 Russia	 Poland  Russia	 Cattle	35	Mazowieckie
712	Lodz	 Russia	 Poland  Russia	 Cattle	35	Wielkopolskie
713	Radom	 Russia	 Poland  Russia	 Coal	35	Wielkopolskie
714	Tarnow	 Austria	 Austria  Poland	 Grain	35	West Galicia
715	Lublin	 Russia	 Poland  Russia	 Grain	35	Mazowieckie
716	Kielce	 Russia	 Poland  Russia	 Wool	35	Wielkopolskie
717	Kalisz	 Russia	 Poland  Russia	 Grain	35	Wielkopolskie
718	Minsk	 Russia	 Russia	 Timber	35	Minsk
719	Bialystock	 Russia	 Poland  Russia	 Grain	35	Brėst
720	Turin	 Sardinia-Piedmont	 Italy  Sardinia-Piedmont	 Fruit	35	Piemonte
721	Aosta	 Sardinia-Piedmont	 Italy  Sardinia-Piedmont	 Wool	35	Piemonte
722	Novara	 Sardinia-Piedmont	 Italy  Sardinia-Piedmont	 Cattle	35	Piemonte
723	Alessandria	 Sardinia-Piedmont	 Italy  Sardinia-Piedmont	 Fruit	35	Piemonte
724	Genoa	 Sardinia-Piedmont	 Italy  Sardinia-Piedmont	 Fruit	35	Piemonte
725	Savona	 Sardinia-Piedmont	 Italy  Sardinia-Piedmont	 Fish	35	Piemonte
726	Milan	 Austria	 Austria  Italy  Lombardia	 Iron	35	Lombardia
727	Bergamo	 Austria	 Austria  Italy  Lombardia	 Cattle	35	Lombardia
728	Brescia	 Austria	 Austria  Italy  Lombardia	 Silk	35	Lombardia
729	Venice	 Austria	 Austria  Venice	 Fish	35	Venezia
730	Verona	 Austria	 Austria  Venice	 Silk	35	Venezia
731	Padua	 Austria	 Austria  Venice	 Fruit	35	Venezia
732	Treviso	 Austria	 Austria  Venice	 Iron	35	Venezia
733	Udine	 Austria	 Austria  Venice	 Fish	35	Venezia
734	Trent	 Austria	 Austria	 Grain	35	South Tirol
735	Bozen	 Austria	 Austria	 Grain	35	South Tirol
736	Trieste	 Austria	 Austria  Trieste  Yugoslavia	 Grain	35	Istria
737	Gorizia	 Austria	 Austria  Slovenia  Venice  Yugoslavia	 Grain	35	Istria
738	Parma	 Parma	 Italy  Parma	 Iron	35	Emilia
739	Modena	 Modena	 Italy  Modena	 Iron	35	Emilia
740	Massa	 Modena	 Italy  Modena	 Timber	35	Emilia
741	Bologna	 Papal States	 Italy  Papal States	 Timber	35	Romagna
742	Ferrara	 Papal States	 Italy  Papal States	 Grain	35	Romagna
743	Ravenna	 Papal States	 Italy  Papal States	 Wool	35	Romagna
744	Florence	 Tuscany	 Italy  Tuscany	 Fruit	35	Toscana
745	Leghorn	 Tuscany	 Italy  Tuscany	 Fish	35	Toscana
746	Lucca	 Lucca	 Italy  Lucca	 Grain	35	Emilia
747	Siena	 Tuscany	 Italy  Tuscany	 Grain	35	Toscana
748	Grosetto	 Tuscany	 Italy  Tuscany	 Cattle	35	Toscana
749	Rome	 Papal States	 Italy  Papal States	 Fruit	35	Lazio
750	Viterbo	 Papal States	 Italy  Papal States	 Fruit	35	Lazio
751	Perugia	 Papal States	 Italy  Papal States	 Fruit	35	Lazio
752	Ancona	 Papal States	 Italy  Papal States	 Fruit	35	Lazio
753	Aquila	 Two Sicilies	 Italy  Two Sicilies	 Wool	35	Puglia
754	Naples	 Two Sicilies	 Italy  Two Sicilies	 Fish	35	Campania
755	Salerno	 Two Sicilies	 Italy  Two Sicilies	 Fruit	35	Campania
756	Bari	 Two Sicilies	 Italy  Two Sicilies	 Grain	35	Puglia
757	Foggia	 Two Sicilies	 Italy  Two Sicilies	 Fish	35	Puglia
758	Brindisi	 Two Sicilies	 Italy  Two Sicilies	 Fish	35	Puglia
759	Reggio di Calabria	 Two Sicilies	 Italy  Two Sicilies	 Fish	35	Campania
760	Catanzaro	 Two Sicilies	 Italy  Two Sicilies	 Fish	35	Campania
761	Potenza	 Two Sicilies	 Italy  Two Sicilies	 Fruit	35	Campania
762	Palermo	 Two Sicilies	 Italy  Two Sicilies	 Fish	35	Sicily
763	Messina	 Two Sicilies	 Italy  Two Sicilies	 Sulphur	35	Sicily
764	Catania	 Two Sicilies	 Italy  Two Sicilies	 Sulphur	35	Sicily
765	Cagliari	 Sardinia-Piedmont	 Italy  Sardinia-Piedmont	 Sulphur	35	Sardegna
766	Sassari	 Sardinia-Piedmont	 Italy  Sardinia-Piedmont	 Grain	35	Sardegna
767	Maribor	 Austria	 Austria  Slovenia  Yugoslavia	 Timber	35	Slovenia
768	Ljubljana	 Austria	 Austria  Slovenia  Yugoslavia	 Cotton	35	Slovenia
769	Postojna	 Austria	 Austria  Slovenia  Yugoslavia	 Grain	35	Istria
770	Pola	 Austria	 Austria  Croatia  Yugoslavia	 Grain	35	Istria
771	Zagreb	 Austria	 Austria  Croatia  Hungary  Yugoslavia	 Timber	35	Croatia
772	Sisak	 Austria	 Austria  Croatia  Hungary  Yugoslavia	 Cattle	35	Croatia
773	Karlovac	 Austria	 Austria  Croatia  Hungary  Yugoslavia	 Fruit	35	Croatia
774	Senj	 Austria	 Austria  Croatia  Hungary  Yugoslavia	 Iron	35	Croatia
775	Varaždin	 Austria	 Austria  Croatia  Hungary  Yugoslavia	 Wool	35	Croatia
776	Bjelovar	 Austria	 Austria  Croatia  Hungary  Yugoslavia	 Grain	35	Croatia
777	Požega	 Austria	 Austria  Croatia  Hungary  Yugoslavia	 Fruit	35	Croatia
778	Fiume	 Austria	 Austria  Croatia  Yugoslavia	 Fruit	35	Istria
779	Osijek	 Austria	 Austria  Croatia  Hungary  Yugoslavia	 Cattle	35	Croatia
780	Split	 Austria	 Austria  Croatia  Yugoslavia	 Fish	35	Dalmatia
781	Zadar	 Austria	 Austria  Croatia  Yugoslavia	 Fruit	35	Dalmatia
782	Dubrovnik	 Austria	 Austria  Croatia  Yugoslavia	 Fish	35	Dalmatia
783	Sarajevo	 Ottoman Empire	 Bosnia-Herzegovina  Ottoman Empire  Yugoslavia	 Fruit	35	Bosnia
784	Bihac	 Ottoman Empire	 Bosnia-Herzegovina  Ottoman Empire  Yugoslavia	 Grain	35	Bosnia
785	Banja Luka	 Ottoman Empire	 Bosnia-Herzegovina  Ottoman Empire  Yugoslavia	 Fish	35	Bosnia
786	Tuzla	 Ottoman Empire	 Bosnia-Herzegovina  Ottoman Empire  Yugoslavia	 Grain	35	Bosnia
787	Foca	 Ottoman Empire	 Bosnia-Herzegovina  Ottoman Empire  Yugoslavia	 Coal	35	Bosnia
788	Mostar	 Ottoman Empire	 Bosnia-Herzegovina  Ottoman Empire  Yugoslavia	 Grain	35	Bosnia
789	Livno	 Ottoman Empire	 Bosnia-Herzegovina  Ottoman Empire  Yugoslavia	 Grain	35	Bosnia
790	Kitwe	uncolonized		 Tobacco	25	Zambia
791	Mitrovica	 Austria	 Austria  Hungary  Serbia  Yugoslavia	 Timber	35	Slavonia
792	Pancevo	 Austria	 Austria  Hungary  Serbia  Yugoslavia	 Grain	35	Slavonia
793	Vukovar	 Austria	 Austria  Croatia  Hungary  Yugoslavia	 Cattle	35	Croatia
794	Belgrade	 Serbia	 Serbia  Yugoslavia	 Grain	35	Northern Serbia
795	Bor	 Serbia	 Serbia  Yugoslavia	 Grain	35	Northern Serbia
796	Kragujevac	 Serbia	 Serbia  Yugoslavia	 Coal	35	Northern Serbia
797	Užice	 Serbia	 Serbia  Yugoslavia	 Grain	35	Northern Serbia
798	Niš	 Ottoman Empire	 Ottoman Empire  Serbia  Yugoslavia	 Timber	35	Southern Serbia
799	Leskovac	 Ottoman Empire	 Ottoman Empire  Serbia  Yugoslavia	 Timber	35	Southern Serbia
800	Ulcinj	 Ottoman Empire	 Montenegro  Ottoman Empire  Yugoslavia	 Grain	35	Montenegro
801	Tahiti	uncolonized		 Fish	15	New Caledonia
802	Pristina	 Ottoman Empire	 Ottoman Empire  Serbia  Yugoslavia	 Timber	35	Southern Serbia
803	Prizren	 Ottoman Empire	 Ottoman Empire  Serbia  Yugoslavia	 Timber	35	Southern Serbia
804	Novi Pazar	 Ottoman Empire	 Ottoman Empire  Serbia  Yugoslavia	 Iron	35	Southern Serbia
805	Salonika	 Ottoman Empire	 Greece  Ottoman Empire	 Tobacco	35	East Macedonia
806	Skopje	 Ottoman Empire	 Bulgaria  Ottoman Empire  Serbia  Yugoslavia	 Timber	35	North Macedonia
807	Bitola	 Ottoman Empire	 Bulgaria  Ottoman Empire  Serbia  Yugoslavia	 Timber	35	North Macedonia
808	Petrich	 Ottoman Empire	 Bulgaria  Ottoman Empire	 Wool	35	Rumelia
809	Sofia	 Ottoman Empire	 Bulgaria  Ottoman Empire	 Timber	35	Rumelia
810	Vidin	 Ottoman Empire	 Bulgaria  Ottoman Empire	 Grain	35	Bulgaria
811	Ruse	 Ottoman Empire	 Bulgaria  Ottoman Empire	 Grain	35	Bulgaria
812	Pleven	 Ottoman Empire	 Bulgaria  Ottoman Empire	 Grain	35	Bulgaria
813	Shumen	 Ottoman Empire	 Bulgaria  Ottoman Empire	 Grain	35	Bulgaria
814	Varna	 Ottoman Empire	 Bulgaria  Ottoman Empire	 Cotton	35	Bulgaria
815	Plovdiv	 Ottoman Empire	 Bulgaria  Ottoman Empire	 Tobacco	35	Rumelia
816	Stara Zagora	 Ottoman Empire	 Bulgaria  Ottoman Empire	 Tobacco	35	Rumelia
817	Burgas	 Ottoman Empire	 Bulgaria  Ottoman Empire	 Grain	35	Rumelia
818	Silistre	 Ottoman Empire	 Bulgaria  Ottoman Empire  Romania	 Grain	35	Dobrudja
819	Florina	 Ottoman Empire	 Greece  Ottoman Empire	 Timber	35	West Macedonia
820	Grevena	 Ottoman Empire	 Greece  Ottoman Empire	 Grain	35	West Macedonia
821	Edessa	 Ottoman Empire	 Greece  Ottoman Empire	 Grain	35	West Macedonia
822	Polygyros	 Ottoman Empire	 Greece  Ottoman Empire	 Tobacco	35	East Macedonia
823	Kavala	 Ottoman Empire	 Bulgaria  Greece  Ottoman Empire	 Tobacco	35	East Macedonia
824	Janina	 Ottoman Empire	 Greece  Ottoman Empire	 Wool	35	Thessaly
825	Arta	 Ottoman Empire	 Greece  Ottoman Empire	 Wool	35	Thessaly
826	Corfu	 Ionian Islands	 Greece  Ionian Islands	 Fish	35	Peloponnese
827	Zante	 Ionian Islands	 Greece  Ionian Islands	 Fish	35	Peloponnese
828	Edirne	 Ottoman Empire	 Ottoman Empire	 Grain	35	Thrace
829	Xanthe	 Ottoman Empire	 Bulgaria  Greece  Ottoman Empire	 Grain	35	East Macedonia
830	Dedeagatch	 Ottoman Empire	 Bulgaria  Greece  Ottoman Empire	 Grain	35	East Macedonia
831	Larisa	 Ottoman Empire	 Greece  Ottoman Empire	 Fruit	35	Thessaly
832	Volos	 Ottoman Empire	 Greece  Ottoman Empire	 Grain	35	Thessaly
833	Trikkala	 Ottoman Empire	 Greece  Ottoman Empire	 Grain	35	Thessaly
834	Athens	 Greece	 Greece	 Fruit	35	Attica
835	Amfissa	 Greece	 Greece	 Cotton	35	Attica
836	Lamia	 Greece	 Greece	 Cotton	35	Attica
837	Missolonghi	 Greece	 Greece	 Grain	35	Attica
838	Khalkis	 Greece	 Greece	 Grain	35	Attica
839	Nafplion	 Greece	 Greece	 Fruit	35	Peloponnese
840	Corinth	 Greece	 Greece	 Fruit	35	Peloponnese
841	Kalamata	 Greece	 Greece	 Fruit	35	Peloponnese
842	Patras	 Greece	 Greece	 Fruit	35	Peloponnese
843	Chios	 Ottoman Empire	 Greece  Ottoman Empire	 Sulphur	35	Aegean Islands
844	Myteline	 Ottoman Empire	 Greece  Ottoman Empire	 Grain	35	Aegean Islands
845	Cyclades	 Greece	 Greece	 Fish	35	Aegean Islands
846	Dodecanese	 Ottoman Empire	 Greece  Ottoman Empire	 Grain	35	Aegean Islands
847	Chania	 Egypt	 Crete  Egypt  Greece	 Fruit	35	Aegean Islands
848	Iraklion	 Egypt	 Crete  Egypt  Greece	 Fruit	35	Aegean Islands
849	Tirana	 Ottoman Empire	 Albania  Ottoman Empire	 Grain	35	Albania
850	Shkoder	 Ottoman Empire	 Albania  Ottoman Empire	 Grain	35	Albania
851	Durres	 Ottoman Empire	 Albania  Ottoman Empire	 Cattle	35	Albania
852	Vlore	 Ottoman Empire	 Albania  Ottoman Empire	 Cattle	35	Albania
853	Gjirokaster	 Ottoman Empire	 Albania  Ottoman Empire	 Cattle	35	Albania
854	Malta	 United Kingdom		 Fish	35	Sicily
855	Nicosia	 Ottoman Empire	 Greece  Cyprus  Ottoman Empire	 Fruit	35	Cyprus
856	Limassol	 Ottoman Empire	 Greece  Cyprus  Ottoman Empire	 Fruit	35	Cyprus
857	Famagusta	 Ottoman Empire	 Greece  Cyprus  Ottoman Empire	 Fruit	35	Cyprus
858	Kirklareli	 Ottoman Empire	 Ottoman Empire	 Grain	35	Thrace
859	Gallipoli	 Ottoman Empire	 Ottoman Empire	 Grain	35	Thrace
860	Istanbul	 Ottoman Empire	 Ottoman Empire	 Fruit	35	Thrace
861	Üsküdar	 Ottoman Empire	 Ottoman Empire	 Grain	35	Thrace
862	Izmit	 Ottoman Empire	 Ottoman Empire	 Fruit	35	Hudavendigar
863	Bursa	 Ottoman Empire	 Ottoman Empire	 Grain	35	Hudavendigar
864	Balikesir	 Ottoman Empire	 Ottoman Empire	 Grain	35	Aydin
865	Canakkale	 Ottoman Empire	 Ottoman Empire	 Fish	35	Aydin
866	Afyon	 Ottoman Empire	 Ottoman Empire	 Opium	35	Hudavendigar
867	Kütahya	 Ottoman Empire	 Ottoman Empire	 Grain	35	Hudavendigar
868	Eskishehir	 Ottoman Empire	 Ottoman Empire	 Wool	35	Hudavendigar
869	Izmir	 Ottoman Empire	 Ottoman Empire	 Fish	35	Aydin
870	Manisa	 Ottoman Empire	 Ottoman Empire	 Grain	35	Aydin
871	Denizli	 Ottoman Empire	 Ottoman Empire	 Wool	35	Aydin
872	Mugla	 Ottoman Empire	 Ottoman Empire	 Coal	35	Aydin
873	Konya	 Ottoman Empire	 Ottoman Empire	 Wool	35	Konya
874	Burdur	 Ottoman Empire	 Ottoman Empire	 Grain	35	Konya
875	Antalya	 Ottoman Empire	 Ottoman Empire	 Grain	35	Konya
876	Ankara	 Ottoman Empire	 Ottoman Empire	 Fruit	35	Ankara and Adana
877	Amasya	 Ottoman Empire	 Ottoman Empire	 Wool	35	Ankara and Adana
878	Kayseri	 Ottoman Empire	 Ottoman Empire	 Wool	35	Ankara and Adana
879	Sivas	 Ottoman Empire	 Ottoman Empire	 Wool	35	Trabzon
880	Kastamonu	 Ottoman Empire	 Ottoman Empire	 Coal	35	Kastamonu
881	Bolu	 Ottoman Empire	 Ottoman Empire	 Coal	35	Kastamonu
882	Trabzon	 Ottoman Empire	 Ottoman Empire	 Cattle	35	Trabzon
883	Sinop	 Ottoman Empire	 Ottoman Empire	 Fish	35	Kastamonu
884	Giresun	 Ottoman Empire	 Ottoman Empire	 Fruit	35	Trabzon
885	Kars	 Ottoman Empire	 Armenia  Ottoman Empire	 Iron	35	Kars
886	Ardahan	 Ottoman Empire	 Armenia  Ottoman Empire	 Wool	35	Kars
887	Erzurum	 Ottoman Empire	 Ottoman Empire	 Cattle	35	Trabzon
888	Erzincan	 Ottoman Empire	 Ottoman Empire	 Iron	35	Trabzon
889	Malatya	 Ottoman Empire	 Ottoman Empire	 Iron	35	Diyarbakir-Van
890	Van	 Ottoman Empire	 Armenia  Ottoman Empire	 Iron	35	Diyarbakir-Van
891	Bitlis	 Ottoman Empire	 Ottoman Empire	 Grain	35	Diyarbakir-Van
892	Hakkari	 Ottoman Empire	 Ottoman Empire	 Fruit	35	Diyarbakir-Van
893	Diyarbakir	 Ottoman Empire	 Ottoman Empire	 Iron	35	Diyarbakir-Van
894	Adana	 Egypt	 Egypt  Ottoman Empire	 Wool	35	Ankara And Adana
895	Mersin	 Ottoman Empire	 Ottoman Empire	 Fish	35	Konya
896	Marash	 Egypt	 Egypt  Ottoman Empire	 Wool	35	Ankara and Adana
897	Aleppo	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Aleppo
898	Antep	 Egypt	 Egypt  Ottoman Empire	 Wool	35	Ankara and Adana
899	Urfa	 Ottoman Empire	 Ottoman Empire	 Grain	35	Diyarbakir-Van
900	Antioch	 Egypt	 Egypt  Ottoman Empire	 Fruit	35	Aleppo
901	Dayr al-Zour	 Ottoman Empire	 Ottoman Empire	 Grain	35	Aleppo
902	Damascus	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Syria
903	Homs	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Syria
904	Hama	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Aleppo
905	Latakia	 Egypt	 Egypt  Ottoman Empire	 Fruit	35	Aleppo
906	Suwayda	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Syria
907	Palmyra	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Syria
908	Amman	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Transjordan
909	Jerash	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Transjordan
910	Ruwayshid	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Transjordan
911	Maan	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Transjordan
912	Baalbeck	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Lebanon
913	Beirut	 Egypt	 Egypt  Ottoman Empire	 Fruit	35	Lebanon
914	Askaleh	 Egypt	 Egypt  Ottoman Empire	 Iron	35	Lebanon
915	Sidon	 Egypt	 Egypt  Ottoman Empire	 Fruit	35	Lebanon
916	Acre	 Egypt	 Egypt  Ottoman Empire	 Fruit	35	Palestine
917	Jerusalem	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Palestine
918	Nablus	 Egypt	 Egypt  Ottoman Empire	 Fruit	35	Palestine
919	Jaffa	 Egypt	 Egypt  Ottoman Empire	 Fruit	35	Palestine
920	Gaza	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Palestine
921	Beersheba	 Egypt	 Egypt  Ottoman Empire	 Grain	35	Palestine
922	Aqaba	 Egypt	 Egypt  Ottoman Empire	 Wool	35	Transjordan
923	Mosul	 Ottoman Empire	 Iraq  Ottoman Empire	 Sulphur	35	Mosul
924	Arbil	 Ottoman Empire	 Iraq  Ottoman Empire	 Wool	35	Mosul
925	Kirkuk	 Ottoman Empire	 Iraq  Ottoman Empire	 Grain	35	Mosul
926	Baghdad	 Ottoman Empire	 Iraq  Ottoman Empire	 Grain	35	Baghdad
927	Samarra	 Ottoman Empire	 Iraq  Ottoman Empire	 Grain	35	Baghdad
928	Mendeli	 Ottoman Empire	 Iraq  Ottoman Empire	 Grain	35	Mosul
929	Karbala	 Ottoman Empire	 Iraq  Ottoman Empire	 Grain	35	Baghdad
930	Kut	 Ottoman Empire	 Iraq  Ottoman Empire	 Grain	35	Basra
931	Rutbah	 Ottoman Empire	 Iraq  Ottoman Empire	 Sulphur	35	Baghdad
932	Basra	 Ottoman Empire	 Iraq  Ottoman Empire	 Fruit	35	Basra
933	Nasiriyya	 Ottoman Empire	 Iraq  Ottoman Empire	 Fruit	35	Basra
934	Najaf	 Ottoman Empire	 Iraq  Ottoman Empire	 Fruit	35	Baghdad
935	Kuwait	 Ottoman Empire	 Iraq  Ottoman Empire	 Fruit	35	Basra
936	Grodno	 Russia	 Poland  Russia	 Grain	35	Brėst
937	Brest-Litovsk	 Russia	 Poland  Russia	 Grain	35	Brėst
938	Lida	 Russia	 Poland  Russia	 Grain	35	Brėst
939	Baranovichi	 Russia	 Poland  Russia	 Grain	35	Brėst
940	Pinsk	 Russia	 Poland  Russia	 Grain	35	Brėst
941	Slutsk	 Russia	 Russia	 Cattle	35	Minsk
942	Mozyr	 Russia	 Russia	 Cattle	35	Minsk
943	Smolensk	 Russia	 Russia	 Cattle	35	Smolensk
944	Orsha	 Russia	 Russia	 Grain	35	Orsha
945	Vitebsk	 Russia	 Russia	 Grain	35	Orsha
946	Polotsk	 Russia	 Russia	 Wool	35	Orsha
947	Pastavy	 Russia	 Russia	 Grain	35	Orsha
948	Mogilev	 Russia	 Russia	 Grain	35	Orsha
949	Gomel	 Russia	 Russia	 Cattle	35	Orsha
950	Uzgorod	 Austria	 Austria  Hungary  Ruthenia  Slovakia	 Coal	35	Slovakia
951	Stryi	 Austria	 Austria  Poland  Ruthenia  Ukraine	 Coal	35	East Galicia
952	Ternopil	 Austria	 Austria  Poland  Ruthenia  Ukraine	 Grain	35	East Galicia
953	Stanislavov	 Austria	 Austria  Poland  Ruthenia  Ukraine	 Grain	35	East Galicia
954	Vinnitsa	 Russia	 Russia  Ukraine	 Cattle	35	Kiev
955	Proskorov	 Russia	 Russia  Ukraine	 Cattle	35	Rovne
956	Rovne	 Russia	 Poland  Russia  Ukraine	 Grain	35	Rovne
957	Kovel	 Russia	 Poland  Russia  Ukraine	 Grain	35	Rovne
958	Kiev	 Russia	 Russia  Ukraine	 Grain	35	Kiev
959	Korosten	 Russia	 Russia  Ukraine	 Grain	35	Kiev
960	Zhitomir	 Russia	 Russia  Ukraine	 Grain	35	Kiev
961	Cherkassy	 Russia	 Russia  Ukraine	 Cattle	35	Kiev
962	Chernigov	 Russia	 Russia  Ukraine	 Grain	35	Kiev
963	Poltava	 Russia	 Russia  Ukraine	 Coal	35	Kiev
964	Simferopol	 Russia	 Crimea  Russia  Ukraine	 Fish	35	Crimea
965	Cherson	 Russia	 Russia  Ukraine	 Fish	35	Cherson
966	Kerch	 Russia	 Crimea  Russia  Ukraine	 Iron	35	Crimea
967	Sevastopol	 Russia	 Crimea  Russia  Ukraine	 Fish	35	Crimea
968	Odessa	 Russia	 Russia  Ukraine	 Fish	35	Cherson
969	Pervomaisk	 Russia	 Russia  Ukraine	 Cattle	35	Cherson
970	Nikolaev	 Russia	 Russia  Ukraine	 Fish	35	Cherson
971	Krivoy Rog	 Russia	 Russia  Ukraine	 Coal	35	Cherson
972	Ekaterinoslav	 Russia	 Russia  Ukraine	 Coal	35	Luhansk
973	Melitopol	 Russia	 Russia  Ukraine	 Coal	35	Luhansk
974	Kramatorsk	 Russia	 Russia  Ukraine	 Coal	35	Luhansk
975	Yuzovka	 Russia	 Russia	 Coal	35	Luhansk
976	Mariupol	 Russia	 Russia  Ukraine	 Coal	35	Luhansk
977	Kursk	 Russia	 Russia	 Grain	35	Kursk
978	Kharkov	 Russia	 Russia  Ukraine	 Coal	35	Luhansk
979	Rostov	 Russia	 Russia	 Coal	35	Rostov
980	Luhansk	 Russia	 Russia  Ukraine	 Cattle	35	Luhansk
981	Archangel	 Russia	 Russia	 Timber	35	Arkhangelsk
982	Petsamo	 Russia	 Finland  Russia  Sweden	 Iron	35	Northern Finland
983	Kandalaksha	 Russia	 Russia	 Sulphur	35	Karelia
984	Kostomushka	 Russia	 Russia	 Timber	35	Karelia
985	Mezen	 Russia	 Russia	 Timber	35	Nenetsia
986	Naryn Mar	 Russia	 Russia	 Timber	15	Nenetsia
987	Ust Sysolsk	 Russia	 Russia	 Timber	35	Galich
988	Povyents	 Russia	 Russia	 Timber	35	Karelia
989	Vologda	 Russia	 Russia	 Timber	35	Tver
990	Kotlas	 Russia	 Russia	 Timber	35	Galich
991	Uglich	 Russia	 Russia	 Timber	35	Galich
992	Belozersk	 Russia	 Russia	 Cattle	35	Tver
993	Vyterga	 Russia	 Russia	 Timber	35	Tver
994	St Petersburg	 Russia	 Russia	 Grain	35	Ingria
995	Petrozavorsk	 Russia	 Russia	 Grain	35	Karelia
996	Luga	 Russia	 Russia	 Grain	35	Ingria
997	Gdov	 Russia	 Russia	 Grain	35	Ingria
998	Tver	 Russia	 Russia	 Timber	35	Tver
999	Rzhev	 Russia	 Russia	 Timber	35	Smolensk
1000	Staritsa	 Russia	 Russia	 Timber	35	Smolensk
1001	Yaroslavl	 Russia	 Russia	 Timber	35	Tver
1002	Manzhouli	 China	 China	 Cattle	35	Manchuria
1003	Novgorod	 Russia	 Russia	 Grain	35	Novgorod
1004	Tikhvin	 Russia	 Russia	 Grain	35	Novgorod
1005	Borovichi	 Russia	 Russia	 Grain	35	Novgorod
1006	Pskov	 Russia	 Russia	 Cattle	35	Ingria
1007	Velikiye Luki	 Russia	 Russia	 Grain	35	Smolensk
1008	Moscow	 Russia	 Russia	 Timber	35	Moscow
1009	Borodino	 Russia	 Russia	 Timber	35	Bryansk
1010	Kaluga	 Russia	 Russia	 Timber	35	Bryansk
1011	Tula	 Russia	 Russia	 Grain	35	Moscow
1012	Ryazan	 Russia	 Russia	 Timber	35	Moscow
1013	Vladimir	 Russia	 Russia	 Timber	35	Moscow
1014	Vyazma	 Russia	 Russia	 Timber	35	Bryansk
1015	Peremyshl	 Russia	 Russia	 Timber	35	Bryansk
1016	Bryansk	 Russia	 Russia	 Cattle	35	Bryansk
1017	Orel	 Russia	 Russia	 Timber	35	Kursk
1018	Belgorod	 Russia	 Russia	 Grain	35	Kursk
1019	Voronets	 Russia	 Russia	 Grain	35	Kursk
1020	Nizhni Novgorod	 Russia	 Russia	 Timber	35	Kazan
1021	Penza	 Russia	 Russia	 Grain	35	Tartaria
1022	Ivanovo	 Russia	 Russia	 Timber	35	Moscow
1023	Kostorma	 Russia	 Russia	 Timber	35	Galich
1024	Galich	 Russia	 Russia	 Timber	35	Galich
1025	Tambov	 Russia	 Russia	 Grain	35	Tartaria
1026	Perm	 Russia	 Russia	 Iron	35	Perm
1027	Vetluga	 Russia	 Russia	 Timber	35	Kazan
1028	Vyatkha	 Russia	 Russia	 Grain	35	Kazan
1029	Glasov	 Russia	 Russia	 Timber	35	Perm
1030	Kazan	 Russia	 Russia	 Grain	35	Kazan
1031	Sarapul	 Russia	 Russia	 Timber	35	Perm
1032	Chistopol	 Russia	 Russia	 Timber	35	Kazan
1033	Simbirsk	 Russia	 Russia	 Cattle	35	Kazan
1034	Samara	 Russia	 Russia	 Grain	35	Samara
1035	Syzran	 Russia	 Russia	 Grain	35	Samara
1036	Astrakhan	 Russia	 Russia	 Wool	35	Astrakhan
1037	Saratov	 Russia	 Russia	 Grain	35	Tartaria
1038	Novo Uzensk	 Russia	 Russia	 Grain	35	Tartaria
1039	Tsaritsyn	 Russia	 Russia	 Cattle	35	Astrakhan
1040	Zarevka	 Russia	 Russia	 Wool	35	Astrakhan
1041	Elitsa	 Russia	 Russia	 Wool	35	Astrakhan
1042	Ufa	 Russia	 Russia	 Iron	35	Samara
1043	Busuluk	 Russia	 Russia	 Cattle	35	Samara
1044	Orenburg	 Russia	 Russia	 Iron	35	Samara
1045	Migolinskaya	 Russia	 Russia	 Cattle	35	Rostov
1046	Chirskaya	 Russia	 Russia	 Coal	35	Rostov
1047	Azov	 Russia	 Russia	 Cattle	35	Rostov
1048	Ekaterinodar	 Russia	 Russia	 Cattle	35	Ekaterinodar
1049	Novorossiysk	 Russia	 Russia	 Grain	35	Ekaterinodar
1050	Stavropol	 Russia	 Russia	 Grain	35	Ekaterinodar
1051	Adygei	 Russia	 Russia	 Grain	35	Ekaterinodar
1052	Derbent	 Russia	 Russia	 Fruit	35	North Caucasia
1053	Gunib	 Russia	 Russia	 Silk	35	North Caucasia
1054	Vladikavkaz	 Russia	 Russia	 Wool	35	North Caucasia
1055	Grozny	 Russia	 Russia	 Wool	35	North Caucasia
1056	Pyatigorsk	 Russia	 Russia	 Grain	35	Ekaterinodar
1057	Kizylyar	 Russia	 Russia	 Silk	35	North Caucasia
1058	Ekaterinburg	 Russia	 Russia	 Coal	35	Ural
1059	Chelyabinsk	 Russia	 Russia	 Iron	35	Ural
1060	Orsk	 Russia	 Russia	 Iron	35	Samara
1061	Tyumen	 Russia	 Russia	 Timber	35	Ural
1062	Berezov	 Russia	 Russia	 Iron	35	Ural
1063	Tomsk	 Russia	 Russia	 Coal	35	Tomsk
1064	Omsk	 Russia	 Russia	 Sulphur	35	Tobolsk
1065	Nizhnevartovsk	 Russia	 Russia	 Timber	15	Ob
1066	Tobolsk	 Russia	 Russia	 Timber	35	Tobolsk
1067	Barnaul	 Russia	 Russia	 Coal	35	Tomsk
1068	Ulala	 Russia	 Russia	 Coal	35	Tomsk
1069	Vilyuysk	 Russia	 Russia	 Cattle	15	West Yakutsk
1070	Bryanka	 Russia	 Russia	 Coal	15	Upper Yeniseysk
1071	Bytantaysk	 Russia	 Russia	 Timber	15	Yakutsk
1072	Okhotsk	 Russia	 Russia	 Grain	35	Okhotsk
1073	Yevensk	 Russia	 Russia	 Grain	20	Kamchatka
1074	Petropavlovsk	 Russia	 Russia	 Fish	20	Kamchatka
1075	Irkutsk	 Russia	 Russia	 Coal	35	Irkutsk
1076	Bratsk	 Russia	 Russia	 Coal	35	Irkutsk
1077	Krasnoyarsk	 Russia	 Russia	 Timber	35	Tomsk
1078	Chita	 Russia	 Russia	 Timber	35	Irkutsk
1079	Nerchinsk	 Russia	 Russia	 Grain	35	Trans-Baikal
1080	Chernomin	 Russia	 Russia	 Cattle	35	Trans-Baikal
1081	Yaksa	 Russia	 Russia	 Grain	35	Trans-Baikal
1082	Haishenwai	 China	 China	 Coal	35	Outer Manchuria
1083	Boli	 China	 China	 Coal	35	Outer Manchuria
1084	Utchan	 China	 China	 Coal	35	Outer Manchuria
1085	Ulusamudan	 China	 China	 Grain	35	Outer Manchuria
1086	Pogobi	uncolonized	 Japan  Russia	 Fish	35	Sakhalin
1087	Ootomari	uncolonized	 Japan  Russia	 Coal	35	Sakhalin
1088	Shumshu	uncolonized	 Japan  Russia	 Coal	20	Hokkaido
1089	Etorofu	uncolonized	 Japan  Russia	 Fish	20	Hokkaido
1090	Tblisi	 Russia	 Georgia  Russia	 Wool	35	Georgia - Russia
1091	Pasanauri	 Russia	 Georgia  Russia	 Wool	35	Georgia - Russia
1092	Kutaisi	 Russia	 Georgia  Russia	 Fruit	35	Georgia - Russia
1093	Akihaltsikle	 Russia	 Georgia  Russia	 Wool	35	Georgia - Russia
1094	Poti	 Russia	 Georgia  Russia	 Tea	35	Georgia - Russia
1095	Sukhumi	 Russia	 Georgia  Russia	 Grain	35	Georgia - Russia
1096	Batum	 Ottoman Empire	 Georgia  Ottoman Empire	 Tea	35	Kars
1097	New Caledonia	uncolonized		 Coffee	15	New Caledonia
1098	Erivan	 Russia	 Armenia  Russia	 Iron	35	Armenia
1099	Gyumri	 Russia	 Armenia  Russia	 Wool	35	Armenia
1100	Kapan	 Russia	 Armenia  Azerbaijan  Russia	 Iron	35	Armenia
1101	Nakhichevan	 Russia	 Armenia  Russia	 Iron	35	Armenia
1102	Baku	 Russia	 Azerbaijan  Russia	 Grain	35	Azerbaijan
1103	Siyazen	 Russia	 Azerbaijan  Russia	 Fruit	35	Azerbaijan
1104	Sheki	 Russia	 Azerbaijan  Russia	 Grain	35	Azerbaijan
1105	Ganja	 Russia	 Azerbaijan  Russia	 Wool	35	Azerbaijan
1106	Agdam	 Russia	 Armenia  Azerbaijan  Russia	 Wool	35	Azerbaijan
1107	Lankaran	 Russia	 Azerbaijan  Russia	 Wool	35	Azerbaijan
1108	Tabriz	 Persia	 Azerbaijan  Persia	 Coal	35	Tabriz
1109	Khvoy	 Persia	 Persia	 Cotton	35	Tabriz
1110	Urumia	 Persia	 Persia	 Wool	35	Tabriz
1111	Mahabad	 Persia	 Persia	 Wool	35	Tabriz
1112	Ardabil	 Persia	 Azerbaijan  Persia	 Timber	35	Tabriz
1113	Rasht	 Persia	 Persia	 Timber	35	Gilan-Mazandaran
1114	Noshehr	 Persia	 Persia	 Timber	35	Gilan-Mazandaran
1115	Sari	 Persia	 Persia	 Wool	35	Gilan-Mazandaran
1116	Gorgan	 Persia	 Persia	 Wool	35	Gilan-Mazandaran
1117	Kermanshah	 Persia	 Persia	 Wool	35	Luristan
1118	Sanandaj	 Persia	 Persia	 Wool	35	Luristan
1119	Ilam	 Persia	 Persia	 Cotton	35	Luristan
1120	Khoramabad	 Persia	 Persia	 Cotton	35	Luristan
1121	Tehran	 Persia	 Persia	 Cotton	35	Irakajemi
1122	Hamadan	 Persia	 Persia	 Fruit	35	Luristan
1123	Zanjan	 Persia	 Persia	 Cattle	35	Tabriz
1124	Qazvin	 Persia	 Persia	 Timber	35	Irakajemi
1125	Qom	 Persia	 Persia	 Grain	35	Irakajemi
1126	Semnan	 Persia	 Persia	 Coal	35	Irakajemi
1127	Isfahan	 Persia	 Persia	 Cotton	35	Isfahan
1128	Arak	 Persia	 Persia	 Iron	35	Isfahan
1129	Kashan	 Persia	 Persia	 Wool	35	Isfahan
1130	Yazd	 Persia	 Persia	 Iron	35	Isfahan
1131	Ahvaz	 Persia	 Persia	 Grain	35	Khuzestan
1132	Abadan	 Persia	 Persia	 Fish	35	Khuzestan
1133	Dezful	 Persia	 Persia	 Cotton	35	Khuzestan
1134	Dehkord	 Persia	 Persia	 Cotton	35	Fars-Kerman
1135	Shiraz	 Persia	 Persia	 Opium	35	Fars-Kerman
1136	Bushire	 Persia	 Persia	 Fish	35	Khuzestan
1137	Yasuj	 Persia	 Persia	 Fruit	35	Fars-Kerman
1138	Kangan	 Persia	 Persia	 Fish	35	Khuzestan
1139	Sirjan	 Persia	 Persia	 Iron	35	Fars-Kerman
1140	Kerman	 Persia	 Persia	 Cotton	35	Fars-Kerman
1141	Lengeh	 Persia	 Persia	 Fish	35	Laristan-Sistan
1142	Bandar Abbas	 Persia	 Persia	 Fruit	35	Laristan-Sistan
1143	Bam	 Persia	 Persia	 Cotton	35	Fars-Kerman
1144	Zahedan	 Persia	 Persia	 Grain	35	Laristan-Sistan
1145	Jask	 Persia	 Persia	 Fruit	35	Laristan-Sistan
1146	Chabahar	 Persia	 Persia	 Fish	35	Laristan-Sistan
1147	Mashhad	 Persia	 Persia	 Coal	35	Khorasan
1148	Birjand	 Persia	 Persia	 Cotton	35	Khorasan
1149	Sabzevan	 Persia	 Persia	 Coal	35	Khorasan
1150	Bojnurd	 Persia	 Persia	 Coal	35	Khorasan
1151	Mecca	 Hedjaz	 Hedjaz	 Grain	35	Hedjaz
1152	Jidda	 Hedjaz	 Hedjaz	 Grain	35	Hedjaz
1153	Medina	 Hedjaz	 Hedjaz	 Grain	35	Hedjaz
1154	Tabuk	 Hedjaz	 Hedjaz	 Wool	35	Hedjaz
1155	Abha	 Hedjaz	 Hedjaz	 Wool	35	Hedjaz
1156	Kaf	 Egypt	 Egypt  Ottoman Empire	 Wool	35	Hail
1157	Riyadh	 Nejd	 Nejd	 Wool	10	Nejd
1158	Rafha	 Nejd	 Nejd	 Wool	10	Hail
1159	Halaban	 Nejd	 Nejd	 Wool	10	Nejd
1160	Hail	 Nejd	 Nejd	 Wool	10	Hail
1161	Sharurah	 Nejd	 Nejd	 Wool	10	Nejd
1162	Bahrain	 Abu Dhabi	 Abu Dhabi	 Grain	35	Abu Dhabi
1163	Qatif	 Nejd	 Nejd	 Grain	35	Hail
1164	Hufuf	 Nejd	 Nejd	 Grain	35	Nejd
1165	Doha	 Abu Dhabi	 Abu Dhabi	 Grain	35	Abu Dhabi
1166	Muscat	 Oman	 Oman	 Opium	35	Oman
1167	Abu Dhabi	 Abu Dhabi	 Abu Dhabi	 Grain	35	Abu Dhabi
1168	Dubai	 Abu Dhabi	 Abu Dhabi	 Grain	35	Abu Dhabi
1169	Sohar	 Oman	 Oman	 Grain	35	Oman
1170	Nizwa	 Oman	 Oman	 Opium	35	Oman
1171	Sur	 Oman	 Oman	 Fruit	35	Oman
1172	Duqm	 Oman	 Oman	 Fish	35	Oman
1173	Mukalla	 Yemen	 Yemen	 Opium	35	Yemen
1174	Salalah	 Oman	 Oman	 Opium	35	Oman
1175	Ghayda	 Yemen	 Yemen	 Opium	35	Yemen
1176	Bayda	 Yemen	 Yemen	 Fish	35	Yemen
1177	Socotra	 Yemen	 Yemen	 Fish	35	Yemen
1178	Sana	 Yemen	 Yemen	 Grain	35	Yemen
1179	Hodeida	 Yemen	 Yemen	 Grain	35	Yemen
1180	Taizz	 Yemen	 Yemen	 Grain	35	Yemen
1181	Qaraganda	uncolonized		 Coal	25	Akmolinsk
1182	Guryev	 Russia	 Russia	 Wool	35	Uralsk
1183	Aqtobe	 Russia	 Russia	 Wool	35	Uralsk
1184	Kokshetau	 Russia	 Russia	 Iron	35	Akmolinsk
1185	Yasi	 Kokand	 Kokand	 Wool	35	Semireche
1186	Alma Ata	 Kokand	 Kokand	 Grain	35	Semireche
1187	Semipalatinsk	 Russia	 Russia	 Timber	35	Semireche
1188	Qaratal	uncolonized		 Fish	25	Semireche
1189	Bishkek	 Kokand	 Kokand	 Wool	35	Kirghizia
1190	Naryn	 Kokand	 Kokand	 Grain	35	Kirghizia
1191	Khiva	 Khiva	 Khiva	 Wool	35	Uzbekia
1192	Nukus	 Khiva	 Khiva	 Opium	35	Uzbekia
1193	Kyzylorda	 Kokand	 Kokand	 Coal	35	Akmolinsk
1194	Aqtau	uncolonized		 Opium	25	Uralsk
1195	Tashkent	 Kokand	 Kokand	 Grain	35	Uzbekia
1196	Dashhowuz	 Khiva		 Wool	35	Turkmenia
1197	Shymkent	 Bukkhara	 Bukkhara	 Grain	35	Uzbekia
1198	Bukhara	 Bukkhara	 Bukkhara	 Wool	35	Uzbekia
1199	Samarkand	 Bukkhara	 Bukkhara	 Grain	35	Uzbekia
1200	Qarshi	 Bukkhara	 Bukkhara	 Wool	35	Uzbekia
1201	Khojand	 Kokand	 Kokand	 Grain	35	Tajikistan
1202	Kokand	 Kokand	 Kokand	 Grain	35	Kirghizia
1203	Osh	 Kokand	 Kokand	 Grain	35	Kirghizia
1204	Ashkhabad	uncolonized		 Opium	35	Turkmenia
1205	Kyzyl Arvat	uncolonized		 Grain	35	Turkmenia
1206	Merv	 Khiva	 Khiva	 Cotton	35	Turkmenia
1207	Kulob	 Bukkhara	 Bukkhara	 Grain	35	Tajikistan
1208	Khorug	 Kokand	 Kokand	 Cattle	35	Tajikistan
1209	Kabul	 Afghanistan	 Afghanistan	 Timber	35	Eastern Afghanistan
1210	Faizabad	 Afghanistan	 Afghanistan	 Wool	35	Eastern Afghanistan
1211	Balkh	 Bukkhara	 Bukkhara	 Grain	35	Western Afghanistan
1212	Herat	 Afghanistan	 Afghanistan	 Fruit	35	Western Afghanistan
1213	Bamyan	 Afghanistan	 Afghanistan	 Grain	35	Western Afghanistan
1214	Farrah	 Afghanistan	 Afghanistan	 Cotton	35	Western Afghanistan
1215	Kandahar	 Afghanistan	 Afghanistan	 Wool	35	Western Afghanistan
1216	Jalalabad	 Afghanistan	 Afghanistan	 Grain	35	Eastern Afghanistan
1217	Ghazni	 Afghanistan	 Afghanistan	 Wool	35	Eastern Afghanistan
1218	Peshawar	 Panjab	 Panjab	 Grain	35	Baluchistan
1219	Quetta	 Kalat	 Kalat	 Wool	35	Baluchistan
1220	Dalbandin	 Kalat	 Kalat	 Wool	35	Baluchistan
1221	Kalat	 Kalat	 India  Kalat	 Wool	35	Baluchistan
1222	Bela	 Makran	 Makran	 Tea	35	Baluchistan
1223	Chitral	 Panjab	 Kashmir  Panjab	 Grain	35	Baluchistan
1224	Srinagar	 Panjab	 Kashmir  India  Panjab	 Grain	35	Kashmir
1225	Gilgit	 Panjab	 Kashmir  Panjab	 Tea	35	Kashmir
1226	Leh	 Panjab	 Kashmir  Ladakh  Panjab	 Wool	35	Kashmir
1227	Lahore	 Panjab	 India  Panjab	 Cotton	35	Punjab
1228	Multan	 Panjab	 India  Panjab	 Tea	35	Punjab
1229	Sialkot	 Panjab	 India  Panjab	 Cotton	35	Punjab
1230	Attock	 Panjab	 India  Panjab	 Wool	35	Punjab
1231	Bahawalpur	 Panjab	 India  Panjab	 Tea	35	Punjab
1232	Shahpur	 Panjab	 India  Panjab	 Tea	35	Punjab
1233	Amritsar	 Panjab	 India  Panjab	 Fruit	35	Punjab
1234	Firozpur	 Panjab	 India  Panjab	 Wool	35	Punjab
1235	Simla	 United Kingdom	 India  Shimla	 Tea	35	Punjab
1236	Delhi	 United Kingdom	 India  Mughalistan	 Tea	35	United Provinces
1237	Panipat	 United Kingdom	 India  Mughalistan	 Cotton	35	United Provinces
1238	Dehra Dun	 United Kingdom	 India  Mughalistan	 Tea	35	United Provinces
1239	Meerut	 United Kingdom	 India  Mughalistan	 Grain	35	United Provinces
1240	Agra	 United Kingdom	 India  Mughalistan	 Grain	35	United Provinces
1241	Cawnpore	 United Kingdom	 India  Mughalistan	 Dye	35	United Provinces
1242	Lucknow	 Awadh	 Awadh  India	 Timber	35	United Provinces
1243	Allahabad	 United Kingdom	 Bundelkhand  India	 Grain	35	United Provinces
1244	Fyzabad	 Awadh	 Awadh  India	 Timber	35	United Provinces
1245	Benares	 United Kingdom	 Bundelkhand  India	 Fruit	35	United Provinces
1246	Gorakhpur	 United Kingdom	 Bundelkhand  India	 Fruit	35	United Provinces
1247	Patna	 United Kingdom	 India	 Opium	35	Bihar
1248	Gaya	 United Kingdom	 India	 Opium	35	Bihar
1249	Kharswari	 United Kingdom	 India	 Grain	35	Bihar
1250	Bhagalpur	 United Kingdom	 India	 Opium	35	Bihar
1251	Calcutta	 United Kingdom	 India	 Dye	35	South Bengal
1252	Darjeeling	 United Kingdom	 India	 Wool	35	North Bengal
1253	Bardwan	 United Kingdom	 India	 Dye	35	North Bengal
1254	Dacca	 United Kingdom	 India	 Grain	35	North Bengal
1255	Rajshahi	 United Kingdom	 India	 Grain	35	North Bengal
1256	Jessore	 United Kingdom	 India	 Dye	35	South Bengal
1257	Chittagong	 United Kingdom	 India	 Dye	35	South Bengal
1258	Gauhati	 United Kingdom	 India	 Tea	35	Assam
1259	Imphal	 United Kingdom	 India	 Tea	35	Assam
1260	Dibrugarh	 United Kingdom	 India	 Tea	35	Assam
1261	Cuttack	 United Kingdom	 India  Orissa	 Grain	35	Orissa
1262	Keunjahr	 Orissa	 India  Orissa	 Grain	35	Orissa
1263	Sambalpur	 Orissa	 India  Orissa	 Grain	35	Orissa
1264	Ajmer	 United Kingdom	 India  Mewar	 Cotton	35	Rajputana
1265	Jaisalmer	 Jaisalmer	 India  Jaisalmer	 Wool	35	Rajputana
1266	Jodhpur	 Jodhpur	 India  Jodhpur	 Tea	35	Rajputana
1267	Bikaner	 Bikaner	 Bikaner  India	 Wool	35	Rajputana
1268	Jaipur	 Jaipur	 India  Jaipur	 Timber	35	Rajputana
1269	Udaipur	 Mewar	 India  Mewar	 Cotton	35	Rajputana
1270	Gwalior	 Gwalior	 Gwalior  India	 Dye	35	Central India
1271	Indore	 Indore	 India  Indore	 Cotton	35	Central India
1272	Bhopal	 Bhopal	 Bhopal  India	 Dye	35	Central India
1273	Chhatarpur	 Bundelkhand	 Bundelkhand  India	 Dye	35	Central India
1274	Rewa	 Bundelkhand	 Bundelkhand  India	 Tea	35	Central India
1275	Jubulpore	 United Kingdom	 India  Nagpur	 Dye	35	Central India
1276	Hoshangabad	 United Kingdom	 Bhopal  India	 Dye	35	Central India
1277	Nagpur	 Nagpur	 India  Nagpur	 Dye	35	Nagpur
1278	Amarati	 Hyderabad	 Hyderabad  India	 Tea	35	Nagpur
1279	Jagdalpur	 Bastar	 Bastar  India	 Grain	35	Nagpur
1280	Raipur	 Nagpur	 India  Nagpur	 Dye	35	Nagpur
1281	Bilaspur	 Nagpur	 India  Nagpur	 Grain	35	Nagpur
1282	Raigarh	 United Kingdom	 India  Nagpur	 Grain	35	Nagpur
1283	Hyderabad	 Hyderabad	 Hyderabad  India	 Cotton	35	Hyderabad
1284	Aurangabad	 Hyderabad	 Hyderabad  India	 Cotton	35	Hyderabad
1285	Nizamabad	 Hyderabad	 Hyderabad  India	 Cotton	35	Hyderabad
1286	Gulbarga	 Hyderabad	 Hyderabad  India	 Cotton	35	Hyderabad
1287	Warangal	 Hyderabad	 Hyderabad  India	 Cotton	35	Hyderabad
1288	Karachi	 Sindh	 Sindh	 Fruit	35	Sind
1289	Sukkur	 Sindh	 Sindh	 Grain	35	Sind
1290	Umarkot	 Sindh	 India  Sindh	 Tea	35	Sind
1291	Ahmedabad	 United Kingdom	 Beroda  India	 Tobacco	35	Gujarat
1292	Rajkot	 Beroda	 Beroda  India	 Cotton	35	Gujarat
1293	Mandvi	 Kutch	 India  Kutch	 Cotton	35	Gujarat
1294	Patan	 Beroda	 Beroda  India	 Cotton	35	Gujarat
1295	Baroda	 Beroda	 Beroda  India	 Cotton	35	Gujarat
1296	Surat	 United Kingdom	 India	 Grain	35	Gujarat
1297	Bombay	 United Kingdom	 India	 Grain	35	Bombay
1298	Nasik	 United Kingdom	 India	 Grain	35	Bombay
1299	Poona	 United Kingdom	 India	 Grain	35	Bombay
1300	Bijapur	 United Kingdom	 India	 Fruit	35	Bombay
1301	Kolhapur	 United Kingdom	 India	 Tea	35	Bombay
1302	Belgaum	 United Kingdom	 India	 Fruit	35	Bombay
1303	Goa	 Portugal	 India	 Fruit	35	Bombay
1304	Madras	 United Kingdom	 Hyderabad  India	 Grain	35	Madras
1305	Vizagapatnam	 United Kingdom	 India  Orissa	 Tobacco	35	Circars
1306	Masulipatnam	 United Kingdom	 Hyderabad  India	 Grain	35	Circars
1307	Nellore	 United Kingdom	 Hyderabad  India	 Grain	35	Circars
1308	Kurnool	 United Kingdom	 Hyderabad  India	 Tea	35	Circars
1309	Tanjore	 United Kingdom	 Hyderabad  India	 Dye	35	Madras
1310	Madurai	 United Kingdom	 Hyderabad  India	 Dye	35	Madras
1311	Coimbatore	 United Kingdom	 Hyderabad  India  Mysore	 Tea	35	Madras
1312	Pondicherry	 France	 Hyderabad  India	 Grain	35	Madras
1313	Bangalore	 Mysore	 India  Mysore	 Wool	35	Mysore
1314	Mysore	 Mysore	 India  Mysore	 Tea	35	Mysore
1315	Chitaldroog	 Mysore	 India  Mysore	 Tea	35	Mysore
1316	Mangalore	 United Kingdom	 India  Mysore	 Fruit	35	Mysore
1317	Calicut	 United Kingdom	 India  Mysore	 Grain	35	Travancore
1318	Cochin	 Travancore	 India  Travancore	 Grain	35	Travancore
1319	Trivandrum	 Travancore	 India  Travancore	 Fruit	35	Travancore
1320	Andaman Islands	 United Kingdom		 Grain	30	South Bengal
1321	Colombo	 United Kingdom	 India	 Fruit	35	Ceylon
1322	Jaffna	 United Kingdom	 India	 Tea	35	Ceylon
1323	Kandy	 United Kingdom	 India	 Tea	35	Ceylon
1324	Trincomalee	 United Kingdom	 India	 Tea	35	Ceylon
1325	Maldives	 United Kingdom	 India	 Fish	35	Ceylon
1326	Katmandu	 Nepal	 Nepal	 Tea	25	Himalayas
1327	Jumla	 Nepal	 Nepal	 Tea	25	Himalayas
1328	Tumlong	 Sikkim	 India  Sikkim	 Wool	25	Himalayas
1329	Thimpu	 Bhutan	 Bhutan	 Wool	25	Himalayas
1330	Rangoon	 Burma	 Burma	 Grain	30	Pegu
1331	Bassein	 United Kingdom	 Burma	 Fish	30	Pegu
1332	Pegu	 Burma	 Burma	 Grain	30	Pegu
1333	Toungoo	 Burma	 Burma	 Opium	30	Pegu
1334	Ava	 Burma	 Burma	 Tropical wood	35	Shan States
1335	Kyaukse	 Burma	 Burma	 Opium	35	Shan States
1336	Magwe	 Burma	 Burma	 Tropical wood	35	Shan States
1337	Prome	 Burma	 Burma	 Grain	30	Shan States
1338	Taunggyi	 Burma	 Burma	 Opium	35	Shan States
1339	Haka	 Burma	 Burma	 Tropical wood	35	Kachin
1340	Lashio	 Burma	 Burma	 Tropical wood	35	Shan States
1341	Putao	 Burma	 Burma	 Timber	35	Kachin
1342	Myitkyina	 Burma	 Burma	 Grain	35	Kachin
1343	Moulmein	 United Kingdom	 Burma	 Grain	30	Tenasserim
1344	Mergui	 United Kingdom	 Burma	 Fish	30	Tenasserim
1345	Sittwe	 United Kingdom	 Burma	 Grain	35	Pegu
1346	Bangkok	 Siam	 Siam	 Grain	30	Bangkok
1347	Lopburi	 Siam	 Siam	 Opium	30	Bangkok
1348	Nakhon Sawan	 Siam	 Siam	 Opium	30	Chiang Mai
1349	Sukothai	 Siam	 Siam	 Opium	30	Chiang Mai
1350	Nakhon Ratchasima	 Siam	 Siam	 Tea	30	Nakhon Ratchasima
1351	Prachinburi	 Siam	 Siam	 Grain	30	Nakhon Ratchasima
1352	Phuket	 Siam	 Siam	 Timber	30	Bangkok
1353	Ratchaburi	 Siam	 Siam	 Iron	30	Bangkok
1354	Nakhon Si Thammarat	 Siam	 Siam	 Timber	30	Bangkok
1355	Chiang Mai	 Siam	 Siam	 Opium	30	Chiang Mai
1356	Luang Prabang	 Luang Prabang	 Luang Prabang	 Tropical wood	30	Laos
1357	Vientiane	 Siam	 Luang Prabang  Siam  Wiang Chhan	 Grain	30	Laos
1358	Udon Thani	 Siam	 Siam	 Fruit	30	Nakhon Ratchasima
1359	Sisaket	 Siam	 Siam	 Tea	30	Nakhon Ratchasima
1360	Xiangabouli	 Siam	 Luang Prabang  Siam  Wiang Chhan	 Tropical wood	30	Laos
1361	Savannakhet	 Siam	 Luang Prabang  Siam	 Grain	30	Laos
1362	Salavan	 Luang Prabang	 Luang Prabang	 Tobacco	30	Laos
1363	Pakche	 Siam	 Siam	 Grain	30	Laos
1364	Oudong	 Cambodia	 Cambodia	 Tropical wood	30	Cambodia
1365	Chanthaburi	 Siam	 Cambodia  Siam	 Grain	30	Nakhon Ratchasima
1366	Battambang	 Siam	 Cambodia  Siam	 Grain	30	Cambodia
1367	Kampot	 Cambodia	 Cambodia	 Tropical wood	30	Cambodia
1368	Stongtreng	 Cambodia	 Cambodia	 Grain	30	Cambodia
1369	Hanoi	 Dai Nam	 Dai Nam	 Grain	30	Tonkin
1370	Hai Phong	 Dai Nam	 Dai Nam	 Grain	30	Tonkin
1371	Cao Bang	 Dai Nam	 Dai Nam	 Grain	30	Tonkin
1372	Son La	 Dai Nam	 Dai Nam	 Tropical wood	30	Tonkin
1373	Lang Son	 Dai Nam	 Dai Nam	 Grain	30	Tonkin
1374	Thanh Hoa	 Dai Nam	 Dai Nam	 Grain	30	Annam
1375	Hue	 Dai Nam	 Dai Nam	 Grain	30	Annam
1376	Vinh	 Dai Nam	 Dai Nam	 Grain	30	Annam
1377	Tourane	 Dai Nam	 Dai Nam	 Tobacco	30	Annam
1378	Pleiku	 Dai Nam	 Dai Nam	 Tobacco	30	Cochin China
1379	Qui Nhon	 Dai Nam	 Dai Nam	 Tobacco	30	Cochin China
1380	Saigon	 Dai Nam	 Dai Nam	 Grain	30	Cochin China
1381	Dong Quai	 Dai Nam	 Dai Nam	 Cotton	30	Cochin China
1382	Hatien	 Dai Nam	 Dai Nam	 Tropical wood	30	Cochin China
1383	Vinhlong	 Dai Nam	 Dai Nam	 Grain	30	Cochin China
1384	Singapore	 United Kingdom	 Johore	 Tropical wood	30	Malaya
1385	Johor Bahru	 Johore	 Johore	 Tropical wood	30	Malaya
1386	Malacca	 United Kingdom	 Johore	 Tropical wood	30	Malaya
1387	Kuala Lumpur	 Johore	 Johore	 Timber	30	Malaya
1388	Penang	 United Kingdom	 Johore	 Timber	30	Malaya
1389	Alor Setar	 Siam	 Johore  Siam	 Timber	30	Malaya
1390	Kuantan	 Johore	 Johore	 Timber	30	Malaya
1391	Kota Bahru	 Siam	 Siam	 Tropical wood	30	Malaya
1392	Pattani	 Siam	 Siam	 Tropical wood	30	Bangkok
1393	Brunei	 Brunei	 Brunei	 Timber	30	North Borneo
1394	Kuching	 Brunei	 Brunei	 Coffee	30	North Borneo
1395	Bintulu	 Brunei	 Brunei	 Timber	30	North Borneo
1396	Api	 Brunei	 Brunei	 Grain	15	North Borneo
1397	Sandakan	uncolonized		 Grain	15	North Borneo
1398	Jambi	 Netherlands		 Grain	30	Sumatra
1399	Palembang	 Netherlands		 Grain	30	Sumatra
1400	Inderagiri	 Netherlands		 Grain	30	Sumatra
1401	Siak	 Netherlands		 Grain	30	Sumatra
1402	Tanjungpinang	 Netherlands		 Timber	30	Sumatra
1403	Lampung	 Netherlands		 Timber	30	Sumatra
1404	Palak Pinang	 Netherlands		 Timber	30	Sumatra
1405	Banda Aceh	 Atjeh	 Atjeh	 Grain	30	Aceh
1406	Medan	 Atjeh	 Atjeh	 Tobacco	30	Aceh
1407	Tapaktuan	 Atjeh	 Atjeh	 Tea	30	Aceh
1408	Padang	 Netherlands		 Tobacco	30	Sumatra
1409	Sibolga	 Atjeh	 Atjeh	 Coffee	30	Aceh
1410	Bencoolen	 Netherlands		 Tobacco	30	Sumatra
1411	Gunungsitoli	 Netherlands		 Fish	30	Sumatra
1412	Aden	 Yemen	 Yemen	 Fish	35	Yemen
1413	Batavia	 Netherlands	 Java	 Coffee	30	Java
1414	Bogor	 Netherlands	 Java	 Coffee	30	Java
1415	Cirebon	 Netherlands	 Java	 Coffee	30	Java
1416	Yogyakarta	 Netherlands	 Java	 Fruit	30	Java
1417	Semarang	 Netherlands	 Java	 Fruit	30	Java
1418	Surabaya	 Netherlands	 Java	 Sulphur	30	Java
1419	Surakarta	 Netherlands	 Java	 Fruit	30	Java
1420	Probolinggo	 Netherlands	 Java	 Sulphur	30	Java
1421	Madura	 Netherlands		 Sulphur	30	Java
1422	Muraleve	uncolonized		 Grain	15	Borneo
1423	Banjarmasin	 Netherlands		 Sulphur	30	Borneo
1424	Pasir	 Netherlands		 Sulphur	30	Borneo
1425	Tarakan	uncolonized		 Timber	15	Borneo
1426	Pontianak	uncolonized		 Grain	15	Borneo
1427	Kota Waringin	 Netherlands		 Grain	30	Borneo
1428	Sintang	uncolonized		 Coffee	15	Borneo
1429	Samarinda	uncolonized		 Sulphur	15	Borneo
1430	Makassar	 Netherlands		 Timber	30	Moluccas
1431	Bone	 Netherlands		 Timber	30	Moluccas
1432	Mamuju	 Netherlands		 Grain	30	Moluccas
1433	Menado	 Netherlands		 Dye	30	Moluccas
1434	Luwuk	 Netherlands		 Timber	30	Moluccas
1435	Palu	 Netherlands		 Timber	30	Moluccas
1436	Kendari	 Netherlands		 Dye	30	Moluccas
1437	Bulon	 Netherlands		 Fish	30	Moluccas
1438	Bali	 Bali	 Bali	 Fish	30	Sunda Islands
1439	Flores	 Netherlands		 Timber	30	Sunda Islands
1440	Sumbawa	 Netherlands		 Timber	30	Sunda Islands
1441	Sumba	 Netherlands		 Timber	30	Sunda Islands
1442	Lombok	 Bali	 Bali	 Timber	30	Sunda Islands
1443	Roti	 Netherlands		 Timber	30	Sunda Islands
1444	Alor	uncolonized		 Tropical wood	30	Sunda Islands
1445	Kaupeng	 Netherlands		 Timber	30	Sunda Islands
1446	Dili	 Portugal	 Portugal	 Timber	30	Sunda Islands
1447	Ternate	 Netherlands		 Fish	30	Moluccas
1448	Jilolo	 Netherlands		 Fish	30	Moluccas
1449	Ambon	 Netherlands		 Grain	30	Moluccas
1450	Ceram	 Netherlands		 Grain	30	Moluccas
1451	Aru	 Netherlands		 Fish	30	Moluccas
1452	Biak	 Netherlands		 Fish	30	Western New Guinea
1453	Sorong	 Netherlands		 Fish	30	Western New Guinea
1454	Merah	 Netherlands		 Fish	30	Western New Guinea
1455	Manila	 Spain	 Philippines	 Fruit	30	Luzón
1456	Vigan	 Spain	 Philippines	 Grain	30	Luzón
1457	Legazpi	 Spain	 Philippines	 Fruit	30	Luzón
1458	Mindoro	 Spain	 Philippines	 Fish	30	Luzón
1459	Palawan	 Spain	 Philippines	 Tropical wood	30	Visayas
1460	Iloilo	 Spain	 Philippines	 Fish	30	Visayas
1461	Tacloban	 Spain	 Philippines	 Grain	30	Visayas
1462	Zamboanga	 Spain	 Philippines	 Iron	30	Mindanao
1463	Davao	 Spain	 Philippines	 Iron	30	Mindanao
1464	Sulu	 Spain	 Philippines	 Fish	30	Mindanao
1465	Urga	 China	 China  Mongolia	 Cattle	35	Mongolia
1466	Dalandzadgad	 China	 China  Mongolia	 Timber	35	Mongolia
1467	Bayan Tumen	 China	 China  Mongolia	 Cattle	35	Mongolia
1468	Uliastai	 China	 China  Mongolia	 Grain	35	Mongolia
1469	Kyzyl	 China	 China	 Coal	35	Tomsk
1470	Anqing	 China	 China	 Tea	35	Southern Anhui
1471	Chizhou	 China	 China	 Tea	35	Southern Anhui
1472	Fengyang	 China	 China	 Tea	35	Northern Anhui
1473	Huizhou	 China	 China	 Tea	35	Southern Anhui
1474	Luzhou	 China	 China	 Tea	35	Southern Anhui
1475	Ningguo	 China	 China	 Timber	35	Southern Anhui
1476	Sizhou	 China	 China	 Tea	35	Jiangsu
1477	Taiping	 China	 China	 Silk	35	Jiangsu
1478	Yingzhou	 China	 China	 Tea	35	Northern Anhui
1479	Mukden	 China	 China  Manchuria	 Timber	35	Manchuria
1480	Jinzhou	 China	 China  Manchuria	 Timber	35	Manchuria
1481	Port Arthur	 China	 China	 Timber	35	Manchuria
1482	Fuzhou	 China	 China	 Tea	35	Fujian
1483	Jianning	 China	 China	 Tea	35	Fujian
1484	Quanzhou	 China	 China	 Tea	35	Fujian
1485	Taibei	 China	 China	 Tea	35	Formosa
1486	Tingzhou	 China	 China	 Tea	35	Fujian
1487	Zhangzhou	 China	 China	 Tea	35	Fujian
1488	Jiayuguan	 China	 China  Xibei San Ma	 Cotton	35	Gansu
1489	Gongchang	 China	 China  Xibei San Ma	 Timber	35	Gansu
1490	Lanzhou	 China	 China  Xibei San Ma	 Coal	35	Gansu
1491	Ningxia	 China	 China  Xibei San Ma	 Grain	35	Gansu
1492	Pingliang	 China	 China  Xibei San Ma	 Grain	35	Gansu
1493	Canton	 China	 China  Guangxi	 Timber	35	Guangdong
1494	Chaozhou	 China	 China	 Silk	35	Shaozhou
1495	Gauzhou	 China	 China  Guangxi	 Silk	35	Guangdong
1496	Hong Kong	 China	 China	 Tea	35	Hong Kong & Macao
1497	Huizhou	 China	 China	 Silk	35	Shaozhou
1498	Macao	 Portugal	 Portugal	 Tea	35	Hong Kong & Macao
1499	Hainan	 China	 China	 Timber	35	Guangdong
1500	Shaozhou	 China	 China	 Tropical wood	35	Shaozhou
1501	Zhaoqing	 China	 China  Guangxi	 Timber	35	Guangdong
1502	Nanning	 China	 China  Guangxi	 Cotton	35	Guangxi
1503	Guilin	 China	 China  Guangxi	 Cotton	35	Guangxi
1504	Pingle	 China	 China  Guangxi	 Cotton	35	Guangxi
1505	Guiyang	 China	 China  Yunnan	 Tea	35	Yunnan
1506	Anshun	 China	 China  Yunnan	 Tea	35	Yunnan
1507	Zhenyuan	 China	 China  Yunnan	 Tea	35	Yunnan
1508	Kaifeng	 China	 China	 Grain	35	Henan
1509	Guide	 China	 China	 Tea	35	Northern Anhui
1510	Luoyang	 China	 China	 Timber	35	Henan
1511	Zhengzhou	 China	 China	 Tea	35	Henan
1512	Chenzhou	 China	 China	 Tea	35	Northern Anhui
1513	Nanyang	 China	 China	 Grain	35	Henan
1514	Runing	 China	 China	 Tea	35	Henan
1515	Weihui	 China	 China	 Iron	35	Henan
1516	Hanyang	 China	 China	 Tea	35	Eastern Hubei
1517	Dean	 China	 China	 Tea	35	Eastern Hubei
1518	Huangzhou	 China	 China	 Tea	35	Eastern Hubei
1519	Anlu	 China	 China	 Tea	35	Western Hubei
1520	Jingzhou	 China	 China	 Tea	35	Western Hubei
1521	Shinan	 China	 China	 Silk	35	Western Hubei
1522	Wuchang	 China	 China	 Iron	35	Eastern Hubei
1523	Xiangyang	 China	 China	 Grain	35	Western Hubei
1524	Changsha	 China	 China  Guangxi	 Tea	35	Hunan
1525	Changde	 China	 China  Guangxi	 Silk	35	Hunan
1526	Baoqing	 China	 China  Guangxi	 Timber	35	Hunan
1527	Hengzhou	 China	 China  Guangxi	 Tea	35	Guangxi
1528	Yuezhou	 China	 China  Guangxi	 Iron	35	Hunan
1529	Yongshun	 China	 China  Guangxi	 Silk	35	Hunan
1530	Yongzhou	 China	 China  Guangxi	 Silk	35	Guangxi
1531	New Ireland	uncolonized		 Tropical wood	15	Northern New Guinea
1532	Guihua Tumed	 China	 China	 Coal	35	Inner Mongolia
1533	Jirim Chuulgan	 China	 China	 Timber	35	Manchuria
1534	Ulaan Chab Chuulghan	 China	 China	 Timber	35	Inner Mongolia
1535	Yeke Juu Chuulghan	 China	 China	 Timber	35	Inner Mongolia
1536	Huaian	 China	 China	 Silk	35	Jiangsu
1537	Changzhou	 China	 China	 Tea	35	Suzhou
1538	Shanghai	 China	 China	 Tea	35	Suzhou
1539	Suzhou	 China	 China	 Silk	35	Suzhou
1540	Taicangzhou	 China	 China	 Tea	35	Suzhou
1541	Tongzhou	 China	 China	 Tea	35	Suzhou
1542	Xuzhou	 China	 China	 Silk	35	Jiangsu
1543	Yangzhou	 China	 China	 Silk	35	Jiangsu
1544	Zhenjiang	 China	 China	 Silk	35	Suzhou
1545	Nanchang	 China	 China	 Timber	35	Jiangxi
1546	Guangxin	 China	 China	 Tea	35	Jiangxi
1547	Jian	 China	 China	 Tea	35	Jiangxi
1548	Jianchang	 China	 China	 Tea	35	Jiangxi
1549	Jiujiang	 China	 China	 Timber	35	Jiangxi
1550	Ganzhou	 China	 China	 Coal	35	Jiangxi
1551	Raozhou	 China	 China	 Timber	35	Jiangxi
1552	Qiqihar	 China	 China  Manchuria	 Coal	35	Manchuria
1553	Aigun	 China	 China  Manchuria	 Coal	35	Manchuria
1554	Ninguta	 China	 China  Manchuria	 Coal	35	Manchuria
1555	Jilin	 China	 China  Manchuria	 Iron	35	Manchuria
1556	Makhai	 China	 China  Xibei San Ma	 Grain	35	Qinghai
1557	Balekungomi	 China	 China  Xibei San Ma	 Coal	35	Qinghai
1558	Kegudo	 China	 China  Xibei San Ma	 Grain	35	Qinghai
1559	Xian	 China	 China  Xibei San Ma	 Coal	35	Ningxia
1560	Merauke	 Netherlands		 Fish	30	Western New Guinea
1561	Yenan	 China	 China  Xibei San Ma	 Coal	35	Ningxia
1562	Hanzhong	 China	 China  Xibei San Ma	 Coal	35	Ningxia
1563	Jinan	 China	 China	 Cotton	35	Southern Zhili
1564	Caozhou	 China	 China	 Grain	35	Southern Zhili
1565	Laizhou	 China	 China	 Cotton	35	Shandong
1566	Qingdao	 China	 China	 Fruit	35	Shandong
1567	Qingzhou	 China	 China	 Grain	35	Shandong
1568	Taian	 China	 China	 Grain	35	Southern Zhili
1569	Weihaiwei	 China	 China	 Grain	35	Shandong
1570	Wuding	 China	 China	 Grain	35	Southern Zhili
1571	Yizhou	 China	 China	 Grain	35	Shandong
1572	Taiyuan	 China	 China  Shanxi Clique	 Coal	35	Shanxi
1573	Fenzhou	 China	 China  Shanxi Clique	 Coal	35	Shanxi
1574	Luan	 China	 China  Shanxi Clique	 Coal	35	Shanxi
1575	Pingyang	 China	 China  Shanxi Clique	 Coal	35	Shanxi
1576	Datong	 China	 China  Shanxi Clique	 Timber	35	Shanxi
1577	Chongqing	 China	 China	 Tea	35	Chongqing
1578	Chengdu	 China	 China	 Tea	35	Sichuan
1579	Baotung	 China	 China	 Fruit	35	Chongqing
1580	Jiading	 China	 China	 Fruit	35	Sichuan
1581	Kuizhou	 China	 China	 Tea	35	Chongqing
1582	Longan	 China	 China	 Coal	35	Sichuan
1583	Shunqing	 China	 China	 Tea	35	Chongqing
1584	Tongchuan	 China	 China	 Fruit	35	Chongqing
1585	Yibin	 China	 China	 Tea	35	Sichuan
1586	Yazhou	 China	 China	 Timber	35	Sichuan
1587	Lhasa	 Tibet	 Tibet	 Cattle	30	Tibet
1588	Chamdo	 Tibet	 Tibet	 Cattle	30	Tibet
1589	Shigatse	 Tibet	 Tibet	 Cattle	30	Tibet
1590	Lhodrak	 Tibet	 Tibet	 Cattle	25	Tibet
1591	Changtang	 Tibet	 Tibet	 Cattle	30	Tibet
1592	Ngari	 Tibet	 Tibet	 Cattle	30	Tibet
1593	Tawang	 Tibet	 India  Tibet	 Cattle	30	Tibet
1594	Kashgar	 China	 China  Xinjiang	 Cotton	35	Xinjiang
1595	Ili	 China	 China  Xinjiang	 Sulphur	35	Xinjiang
1596	Tulta	 China	 China  Xinjiang	 Cotton	35	Xinjiang
1597	Aksu	 China	 China  Xinjiang	 Sulphur	35	Xinjiang
1598	Khotan	 China	 China  Xinjiang	 Grain	35	Xinjiang
1599	Kumul	 China	 China  Xinjiang	 Grain	35	Xinjiang
1600	Díhuà	 China	 China  Xinjiang	 Cotton	35	Xinjiang
1601	Kunming	 China	 China  Yunnan	 Silk	35	Yunnan
1602	Dali	 China	 China  Yunnan	 Timber	35	Yunnan
1603	Puer	 China	 China  Yunnan	 Tea	35	Yunnan
1604	Hangzhou	 China	 China	 Silk	35	Zhejiang
1605	Huzhou	 China	 China	 Silk	35	Zhejiang
1606	Jiaxing	 China	 China	 Silk	35	Zhejiang
1607	Jinhua	 China	 China	 Timber	35	Zhejiang
1608	Ningbo	 China	 China	 Timber	35	Zhejiang
1609	Shaoxing	 China	 China	 Timber	35	Zhejiang
1610	Taizhou	 China	 China	 Tea	35	Zhejiang
1611	Wenzhou	 China	 China	 Tea	35	Zhejiang
1612	Beijing	 China	 China	 Tea	35	Northern Zhili
1613	Chengde	 China	 China	 Iron	35	Northern Zhili
1614	Daming	 China	 China	 Grain	35	Southern Zhili
1615	Jizhou	 China	 China	 Silk	35	Northern Zhili
1616	Shuntian	 China	 China	 Tea	35	Northern Zhili
1617	Tianjin	 China	 China	 Silk	35	Northern Zhili
1618	Zhongding	 China	 China	 Silk	35	Northern Zhili
1619	Pyongyang	 Korea	 Korea	 Coal	35	Pyongyang
1620	Chonchon	 Korea	 Korea	 Iron	35	Pyongyang
1621	Hamhung	 Korea	 Korea	 Iron	35	Pyongyang
1622	Chongjin	 Korea	 Korea	 Coal	35	Pyongyang
1623	Kimchaek	 Korea	 Korea	 Coal	35	Pyongyang
1624	Seoul	 Korea	 Korea	 Grain	35	Seoul
1625	Kaesong	 Korea	 Korea	 Grain	35	Sariwon
1626	Haeju	 Korea	 Korea	 Iron	35	Sariwon
1627	Sariwon	 Korea	 Korea	 Iron	35	Sariwon
1628	Inchon	 Korea	 Korea	 Grain	35	Seoul
1629	Wonsan	 Korea	 Korea	 Grain	35	Sariwon
1630	Kangnung	 Korea	 Korea	 Grain	35	Seoul
1631	Wonju	 Korea	 Korea	 Timber	35	Seoul
1632	Pusan	 Korea	 Korea	 Grain	35	Busan
1633	Taegu	 Korea	 Korea	 Timber	35	Busan
1634	Pohang	 Korea	 Korea	 Coal	35	Busan
1635	Kwangju	 Korea	 Korea	 Grain	35	Busan
1636	Taejon	 Korea	 Korea	 Fish	35	Seoul
1637	Cheju	 Korea	 Korea	 Grain	35	Busan
1638	Hiroshima	 Japan	 Japan	 Cotton	35	Chugoku-Shikoku
1639	Okayama	 Japan	 Japan	 Timber	35	Chugoku-Shikoku
1640	Yamaguchi	 Japan	 Japan	 Grain	35	Chugoku-Shikoku
1641	Matsue	 Japan	 Japan	 Fish	35	Chugoku-Shikoku
1642	Hakodate	 Japan	 Japan	 Coal	35	Hokkaido
1643	Ishikara	 Japan	 Japan	 Fish	35	Hokkaido
1644	Nemuru	 Japan	 Japan	 Timber	35	Hokkaido
1645	Niigata	 Japan	 Japan	 Grain	35	Chubu
1646	Kanazawa	 Japan	 Japan	 Fish	35	Chubu
1647	Fukui	 Japan	 Japan	 Fish	35	Chubu
1648	Toyama	 Japan	 Japan	 Tea	35	Chubu
1649	Edo	 Japan	 Japan	 Grain	35	Kanto
1650	Chiba	 Japan	 Japan	 Grain	35	Kanto
1651	Yokohama	 Japan	 Japan	 Grain	35	Kanto
1652	Urawa	 Japan	 Japan	 Silk	35	Kanto
1653	Mito	 Japan	 Japan	 Grain	35	Kanto
1654	Bonin	 Japan	 Japan	 Fish	30	Bonin Islands
1655	Osaka	 Japan	 Japan	 Tea	35	Kansai
1656	Wakayama	 Japan	 Japan	 Tea	35	Kansai
1657	Kyoto	 Japan	 Japan	 Tea	35	Kansai
1658	Nara	 Japan	 Japan	 Grain	35	Kansai
1659	Kobe	 Japan	 Japan	 Tea	35	Kansai
1660	Fukuoka	 Japan	 Japan	 Tea	35	Kyushu
1661	Nagasaki	 Japan	 Japan	 Coal	35	Kyushu
1662	Kagoshima	 Japan	 Japan	 Grain	35	Kyushu
1663	Miyazaki	 Japan	 Japan	 Tobacco	35	Kyushu
1664	Kumamoto	 Japan	 Japan	 Coal	35	Kyushu
1665	Kochi	 Japan	 Japan	 Fish	35	Chugoku-Shikoku
1666	Matsuyama	 Japan	 Japan	 Timber	35	Chugoku-Shikoku
1667	Tokushima	 Japan	 Japan	 Tobacco	35	Chugoku-Shikoku
1668	Sendai	 Japan	 Japan	 Grain	35	Tohoku
1669	Fukushima	 Japan	 Japan	 Fish	35	Tohoku
1670	Morioka	 Japan	 Japan	 Sulphur	35	Tohoku
1671	Akita	 Japan	 Japan	 Iron	35	Tohoku
1672	Aomori	 Japan	 Japan	 Iron	35	Tohoku
1673	Yamagata	 Japan	 Japan	 Silk	35	Tohoku
1674	Utsunomiya	 Japan	 Japan	 Tobacco	35	Kanto
1675	Nagoya	 Japan	 Japan	 Silk	35	Chubu
1676	Shizuoka	 Japan	 Japan	 Grain	35	Chubu
1677	Nagano	 Japan	 Japan	 Fish	35	Chubu
1678	Okinawa	 Japan	 Japan	 Grain	35	Kyushu
1679	Amari	 Japan	 Japan	 Iron	35	Kyushu
1680	Fez	 Morocco	 Morocco	 Grain	35	Fez
1681	Wazzan	 Morocco	 Morocco	 Grain	35	Fez
1682	Meknes	 Morocco	 Morocco	 Grain	35	Fez
1683	Taza	 Morocco	 Morocco	 Wool	35	Taza
1684	Wujda	 Morocco	 Morocco	 Grain	35	Taza
1685	Rabat	 Morocco	 Morocco	 Grain	35	Fez
1686	Tangier	 Morocco	 Morocco	 Grain	35	al-Rif
1687	Tetouan	 Morocco	 Morocco	 Grain	35	al-Rif
1688	Ajdir	 Morocco	 Morocco	 Fish	35	al-Rif
1689	Melilla	 Spain	 Spain	 Fish	35	al-Rif
1690	Marrakesh	 Morocco	 Morocco	 Fruit	35	Morocco
1691	Casablanca	 Morocco	 Morocco	 Grain	35	Morocco
1692	Huribka	 Morocco	 Morocco	 Grain	35	Morocco
1693	Sawira	 Morocco	 Morocco	 Grain	35	Morocco
1694	Agadir	 Morocco	 Morocco	 Fish	35	West Morocco
1695	Ifni	 Morocco	 Morocco	 Fish	30	West Morocco
1696	Tarfaya	 Morocco	 Morocco	 Fish	30	West Morocco
1697	Figuig	 Morocco	 Morocco	 Fruit	35	Taza
1698	Rashidia	 Morocco	 Morocco	 Grain	35	Taza
1699	Warzazat	 Morocco	 Morocco	 Fruit	35	Taza
1700	Algiers	 France		 Grain	35	Algiers
1701	Bougie	 France		 Grain	35	Algiers
1702	Setif	 Algeria	 Algeria	 Wool	35	Tlemcen
1703	Medea	 Algeria	 Algeria	 Grain	35	Tlemcen
1704	Oran	 France		 Grain	35	Algiers
1705	Tlemcen	 Algeria	 Algeria	 Iron	35	Tlemcen
1706	Mustaghanim	 France		 Fruit	35	Algiers
1707	Mascara	 Algeria	 Algeria	 Fruit	35	Tlemcen
1708	Constantine	 Algeria	 Algeria	 Iron	35	Constantine
1709	Bone	 France		 Grain	35	Algiers
1710	Biskra	 Algeria	 Algeria	 Iron	35	Constantine
1711	Ouargla	 Algeria	 Algeria	 Wool	35	Constantine
1712	Tuggurt	 Algeria	 Algeria	 Wool	35	Constantine
1713	Laghwat	 Algeria	 Algeria	 Grain	35	Constantine
1714	Bechar	uncolonized		 Wool	10	West Sahara
1715	Naama	 Algeria	 Algeria	 Wool	35	Tlemcen
1716	Tindouf	uncolonized		 Fruit	10	West Sahara
1717	Chenachene	uncolonized		 Grain	10	West Sahara
1718	In Salah	uncolonized		 Grain	10	Sahara
1719	Ilizi	uncolonized		 Wool	10	Sahara
1720	Timimoun	uncolonized		 Fruit	10	West Sahara
1721	In Guezzam	uncolonized		 Grain	10	Sahara
1722	Tin Zawatene	uncolonized		 Fruit	10	Sahara
1723	Balboa	 Colombia	 Colombia  Panama	 Fruit	30	Panama
1724	Tamanrasset	uncolonized		 Wool	10	Sahara
1725	Tunis	 Tunis	 Tunis	 Grain	35	Tunisia
1726	Bizerte	 Tunis	 Tunis	 Grain	35	Tunisia
1727	Gafsa	 Tunis	 Tunis	 Wool	35	Tunisia
1728	Kairouan	 Tunis	 Tunis	 Fruit	35	Tunisia
1729	Tozeur	 Tunis	 Tunis	 Wool	35	Tunisia
1730	Gabes	 Tunis	 Tunis	 Grain	35	Tunisia
1731	Tripoli	 Ottoman Empire	 Ottoman Empire	 Fruit	35	Tripoli
1732	Gharyan	 Tripoli	 Tripoli	 Fruit	35	Tripoli
1733	Misratah	 Ottoman Empire	 Ottoman Empire	 Fruit	35	Libya
1734	Sirt	 Ottoman Empire	 Ottoman Empire	 Wool	35	Libya
1735	Benghazi	 Ottoman Empire	 Ottoman Empire	 Fruit	35	Libya
1736	Darna	 Ottoman Empire	 Ottoman Empire	 Fish	35	Libya
1737	Tobruk	 Ottoman Empire	 Ottoman Empire	 Grain	35	Libya
1738	Jaghbub	uncolonized		 Grain	15	Libyan Desert
1739	Kufra	uncolonized		 Fruit	15	Libyan Desert
1740	Waddan	uncolonized		 Wool	15	Libyan Desert
1741	Murzuk	 Tripoli	 Tripoli	 Fruit	25	Tripoli
1742	Sabha	 Tripoli	 Tripoli	 Wool	25	Tripoli
1743	Ghat	 Tripoli	 Tripoli	 Wool	25	Tripoli
1744	Ghadamis	 Tripoli	 Tripoli	 Fruit	35	Tripoli
1745	Cairo	 Egypt	 Egypt	 Grain	35	Lower Egypt
1746	Dumyat	 Egypt	 Egypt	 Grain	35	Sinai
1747	Tanta	 Egypt	 Egypt	 Cotton	35	Lower Egypt
1748	Mansura	 Egypt	 Egypt	 Fruit	35	Sinai
1749	Ziqaziq	 Egypt	 Egypt	 Cotton	35	Sinai
1750	Giza	 Egypt	 Egypt	 Cotton	35	Lower Egypt
1751	Alexandria	 Egypt	 Egypt	 Cotton	35	Lower Egypt
1752	Matruh	 Egypt	 Egypt	 Fruit	35	Matruh
1753	Sidi Barrani	 Egypt	 Egypt	 Fruit	35	Matruh
1754	Siwa	 Egypt	 Egypt	 Grain	10	Matruh
1755	Suez	 Egypt	 Egypt	 Cotton	35	Sinai
1756	Al Arish	 Egypt	 Egypt	 Fruit	35	Sinai
1757	Sharm al-Shaykh	 Egypt	 Egypt	 Fruit	35	Sinai
1758	Farafra	 Egypt	 Egypt	 Fruit	25	Egyptian Desert
1759	Bawiti	 Egypt	 Egypt	 Grain	35	Matruh
1760	Mut	 Egypt	 Egypt	 Grain	35	Egyptian Desert
1761	Baris	 Egypt	 Egypt	 Fruit	35	Egyptian Desert
1762	Asyut	 Egypt	 Egypt	 Cotton	35	Middle Egypt
1763	Bani Suwayf	 Egypt	 Egypt	 Grain	35	Middle Egypt
1764	Minya	 Egypt	 Egypt	 Cotton	35	Middle Egypt
1765	Fayyum	 Egypt	 Egypt	 Cotton	35	Middle Egypt
1766	Aswan	 Egypt	 Egypt	 Grain	35	Egyptian Desert
1767	Luxor	 Egypt	 Egypt	 Grain	35	Upper Egypt
1768	Idfu	 Egypt	 Egypt	 Cotton	35	Upper Egypt
1769	Qina	 Egypt	 Egypt	 Cotton	35	Upper Egypt
1770	Qusayr	 Egypt	 Egypt	 Grain	35	Upper Egypt
1771	Marsa Alam	 Egypt	 Egypt	 Grain	35	Upper Egypt
1772	Ras Gharib	 Egypt	 Egypt	 Grain	35	Middle Egypt
1773	Aaiun	uncolonized		 Fish	10	West Morocco
1774	Dakhla	uncolonized		 Wool	15	West Morocco
1775	Nouakchott	uncolonized		 Fish	15	Mauritania
1776	Rosso	uncolonized		 Wool	15	Mauritania
1777	Aleg	uncolonized		 Wool	15	Mauritania
1778	Maghama	uncolonized		 Timber	15	Mauritania
1779	Shingit	uncolonized		 Grain	15	Mauritania
1780	Tishit	uncolonized		 Fruit	15	Inner Mauritania
1781	Walata	uncolonized		 Wool	10	Inner Mauritania
1782	Bir Murghayn	uncolonized		 Grain	10	Inner Mauritania
1783	Dakar	uncolonized		 Grain	15	Senegal
1784	Saint-Louis	 France		 Fruit	30	Senegal
1785	Banjul	 United Kingdom		 Fruit	30	Gambia
1786	Linguere	uncolonized		 Grain	15	Senegal
1787	Diourbel	uncolonized		 Grain	15	Senegal
1788	Kaolack	uncolonized		 Grain	15	Gambia
1789	Podor	 France		 Fruit	30	Senegal
1790	Matam	uncolonized		 Fruit	15	Senegal
1791	Bakel	uncolonized		 Cattle	15	Gambia
1792	Ziguinchor	uncolonized		 Grain	15	Gambia
1793	Velingara	uncolonized		 Fish	15	Gambia
1794	Bamako	uncolonized		 Fruit	15	Western Mali
1795	Kayes	uncolonized		 Wool	15	Western Mali
1796	Nioro	uncolonized		 Fruit	15	Western Mali
1797	Kita	uncolonized		 Fruit	15	Western Mali
1798	Bougouni	uncolonized		 Cattle	15	Eastern Mali
1799	Sikasso	uncolonized		 Cotton	15	Eastern Mali
1800	Segu	uncolonized		 Fruit	15	Eastern Mali
1801	Mourdiah	uncolonized		 Grain	15	Western Mali
1802	Jenne	uncolonized		 Grain	15	Eastern Mali
1803	Timbuktu	uncolonized		 Cattle	15	Timbuktu
1804	Bandiagara	uncolonized		 Cattle	15	Eastern Mali
1805	Gao	uncolonized		 Wool	15	Timbuktu
1806	Taoudenni	uncolonized		 Grain	10	Timbuktu
1807	Tessalit	uncolonized		 Grain	10	Timbuktu
1808	Niamey	uncolonized		 Grain	15	Outer Hausaland
1809	Say	uncolonized		 Grain	15	Outer Hausaland
1810	Dosso	uncolonized		 Grain	15	Outer Hausaland
1811	Maradi	uncolonized		 Grain	15	Outer Hausaland
1812	Agades	uncolonized		 Wool	10	Niger
1813	Arlit	uncolonized		 Fruit	10	Niger
1814	Madama	uncolonized		 Wool	10	Niger
1815	Zinder	uncolonized		 Cattle	10	Outer Hausaland
1816	Kufe	uncolonized		 Grain	10	Outer Hausaland
1817	Bilma	uncolonized		 Fruit	10	Niger
1818	Massenya	uncolonized		 Grain	15	Waddai
1819	Moundou	uncolonized		 Cotton	15	Waddai
1820	Bongor	uncolonized		 Grain	15	Waddai
1821	Abeche	uncolonized		 Grain	15	Chad
1822	Am Timan	uncolonized		 Fruit	15	Waddai
1823	Mongo	uncolonized		 Grain	15	Waddai
1824	Mao	uncolonized		 Fish	15	Chad
1825	Zouar	uncolonized		 Fruit	10	Chad
1826	Faya	uncolonized		 Wool	10	Chad
1827	Khartoum	 Egypt	 Egypt	 Tropical wood	30	Sudan
1828	Wad Madani	 Egypt	 Egypt	 Grain	30	Sudan
1829	Kassala	 Egypt	 Egypt	 Tropical wood	30	Sudan
1830	Sennar	 Egypt	 Egypt	 Grain	30	Sudan
1831	Rabak	 Egypt	 Egypt	 Grain	30	Sudan
1832	Fashoda	 Egypt	 Egypt	 Grain	30	Sudan
1833	Suakin	 Egypt	 Egypt	 Tropical wood	10	Dongola
1834	Halaib	 Egypt	 Egypt	 Fruit	35	Dongola
1835	Dongola	 Egypt	 Egypt	 Fruit	30	Dongola
1836	Hayya	 Egypt	 Egypt	 Tropical wood	30	Dongola
1837	Atbara	 Egypt	 Egypt	 Tropical wood	30	Dongola
1838	Obeid	 Egypt	 Egypt	 Wool	30	Kordofan
1839	Nuhud	 Egypt	 Egypt	 Grain	30	Kordofan
1840	Kaduqli	 Egypt	 Egypt	 Wool	30	Kordofan
1841	Fasher	uncolonized		 Wool	30	Darfur
1842	Junayah	uncolonized		 Grain	10	Darfur
1843	Waw	uncolonized		 Grain	15	Equatoria
1844	Bor	uncolonized		 Grain	15	Equatoria
1845	Yambio	uncolonized		 Grain	15	Equatoria
1846	Lado	uncolonized		 Timber	15	Equatoria
1847	Kapoeta	uncolonized		 Wool	15	Equatoria
1848	Asmara	 Egypt	 Egypt	 Fruit	35	Eritrea
1849	Massawa	 Egypt	 Egypt	 Fruit	35	Eritrea
1850	Akordat	 Egypt	 Egypt	 Fruit	30	Eritrea
1851	Assab	 Egypt	 Egypt	 Fruit	35	Eritrea
1852	Gonder	 Ethiopia	 Ethiopia	 Cattle	30	Gonder-Tigray
1853	Debre Tabor	 Ethiopia	 Ethiopia	 Cattle	30	Gonder-Tigray
1854	Matamma	 Ethiopia	 Ethiopia	 Grain	30	Gonder-Tigray
1855	Debre Markos	 Ethiopia	 Ethiopia	 Cattle	30	Gonder-Tigray
1856	Aksum	 Ethiopia	 Ethiopia	 Cattle	30	Gonder-Tigray
1857	Antalo	 Ethiopia	 Ethiopia	 Cattle	30	Gonder-Tigray
1858	Awsa	 Ethiopia	 Ethiopia	 Grain	30	Gonder-Tigray
1859	Ankober	 Ethiopia	 Ethiopia	 Coffee	30	Oromia
1860	Awasa	 Ethiopia	 Ethiopia	 Cattle	30	Amhara
1861	Aselia	 Ethiopia	 Ethiopia	 Grain	30	Oromia
1862	Bonga	 Ethiopia	 Ethiopia	 Grain	30	Amhara
1863	Asosa	 Ethiopia	 Ethiopia	 Cattle	30	Amhara
1864	Negele	uncolonized		 Coffee	30	Amhara
1865	Harer	 Ethiopia	 Ethiopia	 Coffee	30	Oromia
1866	Goba	uncolonized		 Cattle	30	Oromia
1867	Werder	uncolonized		 Grain	30	Oromia
1868	Mogadishu	 Oman	 Oman	 Cattle	35	Somaliland
1869	Baidoa	uncolonized		 Cotton	15	Somaliland
1870	Kismayo	uncolonized		 Cattle	15	Somaliland
1871	Hobye	uncolonized		 Grain	15	Somaliland
1872	Busaso	uncolonized		 Grain	15	Somaliland
1873	Berbera	uncolonized		 Cotton	15	Somaliland
1874	Zeyla	uncolonized		 Grain	15	Somaliland
1875	Djibuti	uncolonized		 Cattle	15	Eritrea
1876	Cape Verde	 Portugal		 Coffee	35	Macaronesia
1877	Bissau	 Portugal		 Grain	35	Gambia
1878	Gabu	uncolonized		 Grain	15	Gambia
1879	Boffa	uncolonized		 Fruit	15	Guinea
1880	Timbo	uncolonized		 Fruit	15	Guinea
1881	Dinguiraye	uncolonized		 Fruit	15	Guinea
1882	Kankan	uncolonized		 Fruit	15	Guinea
1883	Beyla	uncolonized		 Timber	15	Guinea
1884	Freetown	 United Kingdom		 Grain	35	Sierra Leone
1885	Falaba	uncolonized		 Coffee	15	Sierra Leone
1886	Bo	uncolonized		 Grain	15	Sierra Leone
1887	Monrovia	 Liberia	 Liberia	 Coffee	35	Liberia
1888	Harper	 Liberia	 Liberia	 Coffee	30	Liberia
1889	Bopolu	uncolonized		 Coffee	15	Liberia
1890	Gbarnga	uncolonized		 Coffee	15	Liberia
1891	Zwedru	uncolonized		 Tropical wood	15	Liberia
1892	Grand Lahou	uncolonized		 Coffee	15	Ivory Coast
1893	Sassandra	uncolonized		 Cotton	15	Windward Coast
1894	Grand Bassam	 France		 Cattle	35	Ivory Coast
1895	Bouake	uncolonized		 Grain	15	Windward Coast
1896	Man	uncolonized		 Grain	15	Windward Coast
1897	Akoupe	uncolonized		 Coffee	15	Ivory Coast
1898	Kong	uncolonized		 Cattle	15	Ivory Coast
1899	Bondouku	uncolonized		 Coffee	15	Ivory Coast
1900	Odienne	uncolonized		 Cattle	15	Windward Coast
1901	Wagadugu	uncolonized		 Grain	15	Volta
1902	Wahiguya	uncolonized		 Grain	15	Volta
1903	Dori	uncolonized		 Grain	15	Volta
1904	Fada Ngourma	uncolonized		 Grain	15	Volta
1905	Bobo Dioulasso	uncolonized		 Grain	15	Volta
1906	Orodaro	uncolonized		 Grain	15	Volta
1907	Accra	uncolonized		 Cattle	15	Ghana
1908	Cape Coast	 United Kingdom		 Coffee	35	Ghana
1909	Sekondi	 Netherlands	 Netherlands	 Cattle	35	Ghana
1910	Kumasi	uncolonized		 Coffee	15	Ghana
1911	Kintampo	uncolonized		 Cattle	15	Ghana
1912	Wa	uncolonized		 Grain	15	Ghana
1913	Tamale	uncolonized		 Grain	15	Ghana
1914	Lome	uncolonized		 Fish	15	Togo
1915	Ho	uncolonized		 Cattle	15	Togo
1916	Yendi	uncolonized		 Cattle	15	Togo
1917	Atakpame	uncolonized		 Coffee	15	Togo
1918	Sokode	uncolonized		 Grain	15	Togo
1919	Cotonou	uncolonized		 Cattle	15	Dahomey
1920	Abomey	uncolonized		 Grain	15	Dahomey
1921	Nikki	uncolonized		 Grain	15	Dahomey
1922	Jugu	uncolonized		 Grain	15	Dahomey
1923	Lagos	uncolonized		 Tropical wood	15	Yoruba States
1924	Abeokuta	uncolonized		 Grain	15	Yoruba States
1925	Ibadan	uncolonized		 Coffee	15	Yoruba States
1926	Ife	uncolonized		 Tropical wood	15	Yoruba States
1927	Ilorin	 Sokoto	 Sokoto	 Grain	15	Hausaland
1928	Benin	uncolonized		 Cattle	15	Benin
1929	Akure	uncolonized		 Tropical wood	15	Benin
1930	Lokoja	 Sokoto	 Sokoto	 Cattle	35	Benin
1931	Warri	uncolonized		 Tropical wood	15	Niger Delta
1932	Bonny	uncolonized		 Tropical wood	15	Niger Delta
1933	Awka	uncolonized		 Coal	15	Niger Delta
1934	Calabar	uncolonized		 Coal	15	Niger Delta
1935	Aruchukwu	uncolonized		 Fish	15	Niger Delta
1936	Makurdi	 Sokoto	 Sokoto	 Grain	35	Benin
1937	Tukari	 Sokoto	 Sokoto	 Cattle	35	Nigeria
1938	Bussa	uncolonized		 Fruit	15	Hausaland
1939	Zaria	 Sokoto	 Sokoto	 Cattle	35	East Hausaland
1940	Bida	 Sokoto	 Sokoto	 Grain	35	Hausaland
1941	Abuja	 Sokoto	 Sokoto	 Cotton	35	East Hausaland
1942	Bauchi	 Sokoto	 Sokoto	 Grain	35	Nigeria
1943	Jos	 Sokoto	 Sokoto	 Fruit	35	Nigeria
1944	Gombe	 Sokoto	 Sokoto	 Cattle	35	Nigeria
1945	Kano	 Sokoto	 Sokoto	 Fruit	35	East Hausaland
1946	Kebbi	 Sokoto	 Sokoto	 Cattle	35	Hausaland
1947	Katsina	 Sokoto	 Sokoto	 Grain	35	East Hausaland
1948	Sokoto	 Sokoto	 Sokoto	 Cattle	35	Hausaland
1949	Hadejia	 Sokoto	 Sokoto	 Coal	35	East Hausaland
1950	Yola	 Sokoto	 Sokoto	 Grain	35	Nigeria
1951	Kuka	uncolonized		 Cotton	35	Bornu
1952	Nguru	uncolonized		 Cattle	35	Bornu
1953	Dikoa	uncolonized		 Fruit	35	Bornu
1954	São Tomé	 Portugal		 Coffee	35	North Angola
1955	Fernando Pó	 Spain	 Spain	 Wool	35	South Cameroon
1956	Douala	uncolonized		 Grain	15	South Cameroon
1957	Buea	uncolonized		 Timber	15	South Cameroon
1958	Kribi	uncolonized		 Coffee	15	South Cameroon
1959	Yaounde	uncolonized		 Timber	15	South Cameroon
1960	Bafoussam	uncolonized		 Timber	15	North Cameroon
1961	Bamenda	uncolonized		 Timber	15	North Cameroon
1962	Bertoua	uncolonized		 Grain	15	South Cameroon
1963	Ngaoundere	 Sokoto	 Sokoto	 Grain	15	North Cameroon
1964	Maroua	uncolonized		 Fruit	15	North Cameroon
1965	Bangui	uncolonized		 Timber	15	Ubangi-Shari
1966	Nola	uncolonized		 Cattle	15	Ubangi-Shari
1967	Bouar	uncolonized		 Cattle	15	Ubangi-Shari
1968	Bossangoa	uncolonized		 Grain	15	Ubangi-Shari
1969	Zemio	uncolonized		 Cattle	15	Ubangi-Shari
1970	Bangassou	uncolonized		 Timber	15	Ubangi-Shari
1971	Ndele	uncolonized		 Cattle	15	Ubangi-Shari
1972	Libreville	uncolonized		 Timber	15	Gabon
1973	Bata	uncolonized		 Timber	15	Gabon
1974	Mayumbe	uncolonized		 Timber	15	Gabon
1975	Moanda	uncolonized		 Timber	15	Gabon
1976	Makokou	uncolonized		 Iron	15	Gabon
1977	Nkuna	uncolonized		 Fruit	15	Congo
1978	Madingou	uncolonized		 Iron	15	Congo
1979	Biloka	 United Kingdom		 Tropical wood	30	Guayana
1980	Djambala	uncolonized		 Timber	15	Congo
1981	Impfondo	uncolonized		 Timber	15	Congo
1982	Kinshasa	uncolonized		 Fruit	15	Bas-Congo
1983	Boma	uncolonized		 Timber	15	Bas-Congo
1984	Kananga	uncolonized		 Fruit	15	Kasai
1985	Kumbana	uncolonized		 Grain	15	Bas-Congo
1986	Lusambo	uncolonized		 Tropical wood	15	Kasai
1987	Bunkeya	uncolonized		 Grain	15	Katanga
1988	Mussumba	uncolonized		 Tropical wood	15	Katanga
1989	Munza	uncolonized		 Tropical wood	15	Katanga
1990	Nyangwe	uncolonized		 Fruit	15	Congo Orientale
1991	Uvira	uncolonized		 Fruit	15	Congo Orientale
1992	Basoko	uncolonized		 Timber	15	Equateur
1993	Irebu	uncolonized		 Grain	15	Equateur
1994	Nsheng	uncolonized		 Grain	15	Kasai
1995	Gemena	uncolonized		 Cotton	15	Equateur
1996	Kisangani	uncolonized		 Tropical wood	15	Congo Orientale
1997	Mungbane	uncolonized		 Fruit	15	Congo Orientale
1998	Baramo	uncolonized		 Fruit	15	Congo Orientale
1999	Luanda	 Portugal		 Coffee	35	North Angola
2000	Cabinda	uncolonized		 Fruit	15	North Angola
2001	Mbanza	 Portugal		 Fruit	35	North Angola
2002	Quibala	uncolonized		 Coffee	15	East Angola
2003	Benguela	 Portugal		 Grain	35	South Angola
2004	Moçâmedes	 Portugal		 Fish	35	South Angola
2005	Huambo	uncolonized		 Fruit	15	South Angola
2006	Kuito	uncolonized		 Fruit	15	East Angola
2007	Mavinga	uncolonized		 Grain	15	East Angola
2008	Ondjiva	uncolonized		 Iron	15	South Angola
2009	Malanje	uncolonized		 Fruit	15	East Angola
2010	Saurimo	uncolonized		 Cattle	15	East Angola
2011	Kubanda	uncolonized		 Grain	15	East Angola
2012	Lusaka	uncolonized		 Grain	15	Zambia
2013	Mongu	uncolonized		 Cattle	15	Zambia
2014	Kasempa	uncolonized		 Grain	15	Zambia
2015	Monzo	uncolonized		 Grain	15	Zambia
2016	Kazembe	uncolonized		 Grain	15	Kazembe
2017	Kasema	uncolonized		 Cattle	15	Kazembe
2018	Chipata	uncolonized		 Grain	15	Kazembe
2019	Entebbe	uncolonized		 Cotton	15	Uganda
2020	Mbarara	uncolonized		 Cotton	15	Uganda
2021	Masindi	uncolonized		 Coffee	15	Uganda
2022	Kitgum	uncolonized		 Cotton	15	Uganda
2023	Jinja	uncolonized		 Cotton	15	Uganda
2024	Nairobi	uncolonized		 Grain	15	Kenya
2025	Marsabit	uncolonized		 Cattle	15	Kenya
2026	Lodwar	uncolonized		 Tea	15	Rift Valley
2027	Nakuru	uncolonized		 Coffee	15	Rift Valley
2028	Kisumu	uncolonized		 Tea	15	Rift Valley
2029	Mombasa	 Oman	 Oman  Zanzibar	 Fish	35	Zanzibar
2030	Lamu	 Oman	 Oman  Zanzibar	 Cattle	35	Kenya
2031	Wajir	uncolonized		 Coffee	15	Kenya
2032	Garissa	uncolonized		 Coffee	15	Kenya
2033	Voi	uncolonized		 Grain	15	Zanzibar
2034	Kigali	uncolonized		 Coffee	15	Tanganyika
2035	Usumbura	uncolonized		 Cotton	15	Tanganyika
2036	Dar Es Salaam	 Oman	 Oman  Zanzibar	 Fish	35	Zanzibar
2037	Tanga	 Oman	 Oman  Zanzibar	 Grain	35	Zanzibar
2038	Kilwa	 Oman	 Oman  Zanzibar	 Grain	35	Lindi
2039	Lindi	 Oman	 Oman  Zanzibar	 Grain	35	Lindi
2040	Songea	uncolonized		 Grain	15	Lindi
2041	Masasi	uncolonized		 Cattle	15	Lindi
2042	Iringa	uncolonized		 Tobacco	15	Lindi
2043	Tabora	uncolonized		 Tobacco	15	Tanganyika
2044	Mwanza	uncolonized		 Cotton	15	Tanganyika
2045	Morogoro	uncolonized		 Fruit	15	Zanzibar
2046	Ujiji	uncolonized		 Coffee	15	Tanganyika
2047	Arusha	uncolonized		 Grain	15	Tanganyika
2048	Zanzibar	 Oman	 Oman  Zanzibar	 Grain	35	Zanzibar
2049	Lourenço Marques	 Portugal		 Grain	35	Lourenço Marques
2050	Chaimate	 Portugal		 Grain	35	Lourenço Marques
2051	Inhambane	 Portugal		 Grain	35	Lourenço Marques
2052	Massekisse	uncolonized		 Grain	35	Lourenço Marques
2053	Sena	 Portugal		 Grain	35	Zambezia
2054	Tete	uncolonized		 Grain	15	Zambezia
2055	Songo	uncolonized		 Grain	15	Zambezia
2056	Zombo	uncolonized		 Coffee	15	Zambezia
2057	Sofala	 Portugal		 Tobacco	35	Zambezia
2058	Mossurize	uncolonized		 Grain	35	Zambezia
2059	Quelimane	 Portugal		 Grain	35	Zambezia
2060	Moçambique	 Portugal		 Cotton	35	Mocambique
2061	Angoche	 Portugal		 Tobacco	35	Mocambique
2062	Shangzhou	 China	 China  Xibei San Ma	 Coal	35	Ningxia
2063	Ibo	 Portugal		 Grain	35	Mocambique
2064	Nampula	uncolonized		 Grain	35	Mocambique
2065	Milange	 Portugal		 Grain	35	Mocambique
2066	Zomba	uncolonized		 Tobacco	15	Mocambique
2067	Lilongwe	uncolonized		 Cattle	15	Kazembe
2068	Harare	uncolonized		 Coffee	15	Zambezi
2069	Gweru	uncolonized		 Cattle	15	Zambezi
2070	Mutare	uncolonized		 Tobacco	15	Zambezi
2071	Bulawayo	uncolonized		 Iron	15	Zambezi
2072	Hwange	uncolonized		 Cattle	15	Zambezi
2073	Masvingo	uncolonized		 Iron	15	Zambezi
2074	Gaborone	uncolonized		 Wool	15	Botswana
2075	Serowe	uncolonized		 Grain	15	Botswana
2076	Nokaneng	uncolonized		 Fruit	15	Botswana
2077	Tsabong	uncolonized		 Grain	15	Botswana
2078	Windhoek	uncolonized		 Wool	15	Hereroland
2079	Swakopmund	uncolonized		 Fish	15	Hereroland
2080	Tsumeb	uncolonized		 Wool	15	Hereroland
2081	Linyati	uncolonized		 Grain	15	Hereroland
2082	Otjinene	uncolonized		 Grain	15	Hereroland
2083	Walvis Bay	uncolonized		 Wool	15	Namaqualand
2084	Angra Pequena	uncolonized		 Grain	15	Namaqualand
2085	Nu-gouses	uncolonized		 Grain	15	Namaqualand
2086	Karasburg	uncolonized		 Grain	15	Namaqualand
2087	Cape Town	 United Kingdom	 South Africa	 Fruit	35	Cape Colony
2088	Springbok	uncolonized		 Wool	15	Cape Colony
2089	Worcester	 United Kingdom	 South Africa	 Fruit	35	Cape Colony
2090	Swettenham	 United Kingdom	 South Africa	 Wool	35	Cape Colony
2091	Mossel Bay	 United Kingdom	 South Africa	 Fruit	35	Cape Colony
2092	Beaufort	 United Kingdom	 South Africa	 Fruit	35	Northern Cape
2093	Calvinia	 United Kingdom	 South Africa	 Grain	35	Northern Cape
2094	Kimberley	uncolonized		 Cattle	15	Northern Cape
2095	Dikathong	uncolonized		 Grain	15	Northern Cape
2096	Port Elizabeth	 United Kingdom	 South Africa	 Fruit	35	Eastern Cape
2097	Graaf Reinet	 United Kingdom	 South Africa	 Fruit	35	Eastern Cape
2098	Bisho	 United Kingdom	 South Africa	 Wool	35	Eastern Cape
2099	Mathele	 United Kingdom	 South Africa	 Grain	35	Eastern Cape
2100	Umtata	 United Kingdom	 South Africa	 Wool	35	Eastern Cape
2101	Bloemfontein	 Oranje	 Oranje  South Africa	 Wool	35	Vrystaat
2102	Winburg	 Oranje	 Oranje  South Africa	 Coal	35	Vrystaat
2103	Philippolis	 Oranje	 Oranje  South Africa	 Iron	35	Vrystaat
2104	Thaba Bosiu	 United Kingdom	 South Africa	 Coal	35	Natal-Zululand
2105	Pretoria	 Transvaal	 South Africa  Transvaal	 Grain	35	Transvaal
2106	Witwatersrand	 Transvaal	 South Africa  Transvaal	 Wool	35	Transvaal
2107	Klerksdorp	 Transvaal	 South Africa  Transvaal	 Grain	35	Transvaal
2108	Mosega	 Transvaal	 South Africa  Transvaal	 Grain	35	Transvaal
2109	Lydenburg	 Transvaal	 South Africa  Transvaal	 Grain	35	Transvaal
2110	Thohoyandu	 Transvaal	 South Africa  Transvaal	 Grain	35	Transvaal
2111	Durban	 Zulu	 Natalia  South Africa  Zulu	 Wool	35	Natal-Zululand
2112	Ladysmith	 Zulu	 South Africa  Zulu	 Grain	35	Natal-Zululand
2113	Ulundi	 Zulu	 South Africa  Zulu	 Wool	35	Natal-Zululand
2114	Mbabane	 Transvaal	 South Africa  Transvaal	 Grain	35	Transvaal
2115	Tananarive	 Madagascar	 Madagascar	 Tropical wood	35	North Madagascar
2116	Fianarantsoa	 Madagascar	 Madagascar	 Coal	35	South Madagascar
2117	Ampanihy	 Madagascar	 Madagascar	 Grain	35	South Madagascar
2118	Tolanaro	 Madagascar	 Madagascar	 Grain	35	South Madagascar
2119	Toamasina	 Madagascar	 Madagascar	 Fruit	35	North Madagascar
2120	Antsiranana	 Madagascar	 Madagascar	 Timber	35	North Madagascar
2121	Mahajanga	 Madagascar	 Madagascar	 Timber	35	North Madagascar
2122	Toliara	 Madagascar	 Madagascar	 Fruit	35	South Madagascar
2123	Comoros	uncolonized		 Fish	35	South Madagascar
2124	Mayotte	uncolonized		 Grain	35	Indian Ocean Territory
2125	Mauritius	 United Kingdom		 Fruit	35	Indian Ocean Territory
2126	Bourbon	 France		 Fish	35	Indian Ocean Territory
2127	Seychelles	 United Kingdom		 Fruit	35	Indian Ocean Territory
2128	Diego Garcia	 United Kingdom	 India	 Fish	35	Ceylon
2129	Saint Helena	 United Kingdom		 Fish	35	South Atlantic Islands
2130	Ascension	 United Kingdom		 Fish	35	South Atlantic Islands
2131	Falkland Islands	 United Kingdom	 Argentina	 Wool	30	Patagonia Meridional
2132	Tristan da Cunha	 United Kingdom		 Fish	35	South Atlantic Islands
2133	South Georgia	uncolonized		 Fish	30	South Atlantic Islands
2134	Azores	 Portugal	 Portugal	 Fruit	35	Macaronesia
2135	Madeira	 Portugal	 Portugal	 Fruit	35	Macaronesia
2136	Canary Islands	 Spain	 Spain	 Fruit	35	West Morocco
2137	Hermosillo	 Mexico	 Mexico	 Cattle	35	Sonora
2138	Loreto	 Mexico		 Fish	35	Sonora
2139	Rosarito	 Mexico	 Mexico	 Fruit	40	Sonora
2140	Nogales	 Mexico	 Mexico	 Grain	35	Sonora
2141	Guaymas	 Mexico	 Mexico	 Cattle	35	Sonora
2142	Chihuahua	 Mexico	 Mexico	 Iron	35	Chihuahua
2143	Paso del Norte	 Mexico	 Mexico	 Grain	35	Chihuahua
2144	Delicias	 Mexico	 Mexico	 Cattle	35	Chihuahua
2145	Parral	 Mexico	 Mexico	 Cattle	35	Chihuahua
2146	Monterrey	 Mexico		 Grain	35	Nuevo León
2147	Morelos	 Mexico	 Mexico	 Grain	35	Chihuahua
2148	Reynosa	 Mexico	 Mexico	 Fish	35	Nuevo León
2149	Matamoros	 Mexico	 Mexico	 Cattle	35	Nuevo León
2150	Ciudad Victoria	 Mexico	 Mexico	 Cattle	35	Nuevo León
2151	Saltillo	 Mexico	 Mexico	 Dye	35	Durango
2152	Monclova	 Mexico	 Mexico	 Dye	35	Chihuahua
2153	Durango	 Mexico	 Mexico	 Cattle	35	Durango
2154	Santa María del Oro	 Mexico	 Mexico	 Grain	35	Durango
2155	Torreón	 Mexico	 Mexico	 Cattle	35	Durango
2156	Mazatlán	 Mexico	 Mexico	 Cattle	35	Durango
2157	Culiacán	 Mexico	 Mexico	 Cattle	35	Durango
2158	Zacatecas	 Mexico		 Grain	35	Zacatecas
2159	San Luis Potosí	 Mexico	 Mexico	 Grain	35	Zacatecas
2160	Aguascalientes	 Mexico	 Mexico	 Timber	35	Jalisco
2161	Tepic	 Mexico	 Mexico	 Fish	35	Jalisco
2162	Veracruz	 Mexico	 Mexico	 Grain	35	México
2163	Tampico	 Mexico		 Fish	35	Nuevo León
2164	Minatitlán	 Mexico	 Mexico	 Iron	35	México
2165	Villahermosa	 Mexico	 Mexico	 Coffee	30	Yucatán
2166	Guadalajara	 Mexico	 Mexico	 Fish	30	Jalisco
2167	Guanajuato	 Mexico	 Mexico	 Grain	35	Zacatecas
2168	Puerto Vallarta	 Mexico	 Mexico	 Fish	35	Jalisco
2169	Colima	 Mexico		 Iron	35	Jalisco
2170	Morelia	 Mexico	 Mexico	 Wool	35	Morelia
2171	Los Albañiles	 Mexico	 Mexico	 Grain	35	Morelia
2172	Mexico City	 Mexico		 Grain	35	México
2173	Querétaro	 Mexico	 Mexico	 Fruit	35	Zacatecas
2174	Toluca	 Mexico	 Mexico	 Grain	35	Morelia
2175	Tulancingo	 Mexico	 Mexico	 Grain	35	México
2176	Puebla	 Mexico	 Mexico	 Dye	35	México
2177	Oaxaca	 Mexico	 Mexico	 Grain	35	México
2178	Collataro	 Mexico	 Mexico	 Grain	35	Morelia
2179	Acapulco	 Mexico	 Mexico	 Grain	35	Morelia
2180	Chilpancingo	 Mexico	 Mexico	 Cattle	35	Morelia
2181	Tuxtla	 Mexico	 Mexico	 Cotton	30	Yucatán
2182	Tapachula	 Mexico	 Mexico	 Cotton	30	Yucatán
2183	Mérida	 Mexico		 Cotton	30	Yucatán
2184	Campeche	 Mexico		 Timber	30	Yucatán
2185	Bacalar	 Mexico	 Mexico	 Timber	30	Yucatán
2186	Guatemala	 USCA	 Guatemala	 Fruit	30	Guatemala
2187	Quetzaltenango	 USCA	 Guatemala  USCA	 Iron	30	Guatemala
2188	Puerto Barrios	 USCA	 Guatemala  USCA	 Fruit	30	Guatemala
2189	Sayaxche	 USCA	 Guatemala  USCA	 Timber	30	Guatemala
2190	Belize	 United Kingdom		 Fruit	30	Guatemala
2191	San Salvador	 USCA	 El Salvador  USCA	 Coffee	30	Honduras
2192	San Miguel	 USCA	 El Salvador  USCA	 Tropical wood	30	Honduras
2193	Comayagua	 USCA	 USCA	 Fruit	30	Honduras
2194	San Pedro Sula	 USCA	 Honduras  USCA	 Fruit	30	Honduras
2195	La Ceiba	 USCA	 Honduras  USCA	 Fruit	30	Honduras
2196	Puerto Lempira	 USCA	 Honduras  USCA	 Timber	30	Honduras
2197	Managua	 USCA	 Nicaragua	 Coffee	30	Nicaragua
2198	Rivas	 USCA	 Nicaragua	 Fruit	30	Nicaragua
2199	León	 USCA	 Nicaragua  USCA	 Coffee	30	Nicaragua
2200	Bluefields	 USCA	 Nicaragua  USCA	 Cattle	30	Nicaragua
2201	San José	 USCA	 Costa Rica  USCA	 Fruit	30	Costa Rica
2202	Liberia	 USCA	 Costa Rica  USCA	 Fruit	30	Costa Rica
2203	Limón	 USCA	 Costa Rica  USCA	 Coffee	30	Costa Rica
2204	Panama City	 Colombia	 Colombia  Panama	 Fruit	30	Panama
2205	David	 Colombia	 Colombia  Panama	 Coffee	30	Panama
2206	Penonomé	 Colombia	 Colombia  Panama	 Fruit	30	Panama
2207	Sainshand	 China	 China  Mongolia	 Grain	35	Mongolia
2208	Yaviza	 Colombia	 Colombia  Panama	 Fruit	30	Panama
2209	Havana	 Spain	 Cuba	 Tobacco	35	Greater Antilles
2210	Jagua	 Spain	 Cuba	 Tobacco	35	Greater Antilles
2211	Camagüey	 Spain	 Cuba	 Tobacco	35	Greater Antilles
2212	Santiago de Cuba	 Spain	 Cuba	 Tobacco	35	Greater Antilles
2213	Port Au Prince	 Haiti	 Haiti	 Tobacco	35	Hispaniola
2214	Santo Domingo	 Haiti	 Dominican Republic  Haiti	 Tobacco	35	Hispaniola
2215	Cap Haitien	 Haiti	 Haiti	 Tobacco	35	Hispaniola
2216	La Vega	 Haiti	 Dominican Republic  Haiti	 Tobacco	35	Hispaniola
2217	Jamaica	 United Kingdom		 Sulphur	35	Caribbean Islands
2218	Cayman Islands	 United Kingdom		 Fruit	35	Caribbean Islands
2219	Bahamas	 United Kingdom		 Cotton	35	Caribbean Islands
2220	Turks And Caicos	 United Kingdom		 Cotton	35	Caribbean Islands
2221	Nanjing	 China	 China	 Tea	35	Jiangsu
2222	Puerto Rico	 Spain		 Cotton	35	West Indies
2223	Saint Thomas	 Denmark		 Tobacco	35	West Indies
2224	Antigua	 United Kingdom		 Fruit	35	West Indies
2225	Montserrat	 United Kingdom		 Cotton	35	West Indies
2226	Tortola	 United Kingdom		 Tobacco	35	West Indies
2227	Saint Kitts	 United Kingdom		 Cotton	35	West Indies
2228	Martinique	 France		 Cotton	35	Lesser Antilles
2229	Barbados	 United Kingdom		 Tobacco	35	Lesser Antilles
2230	Guadeloupe	 France		 Fruit	35	West Indies
2231	Saint Lucia	 United Kingdom		 Cotton	35	Lesser Antilles
2232	Dominica	 United Kingdom		 Cotton	35	Lesser Antilles
2233	Grenada	 United Kingdom		 Cotton	35	Lesser Antilles
2234	Curacao	 Netherlands		 Tobacco	35	Zulia
2235	Aruba	 Netherlands		 Tobacco	35	Zulia
2236	Saint Martin	 Netherlands		 Tobacco	35	West Indies
2237	Trinidad	 United Kingdom		 Cotton	35	Lesser Antilles
2238	Tobago	 United Kingdom		 Cotton	35	Lesser Antilles
2239	Georgetown	 United Kingdom		 Fruit	30	Guayana
2240	Paramaribo	 Netherlands		 Grain	30	Guayana
2241	Cayenne	 France		 Timber	30	Guayana
2242	Mahdia	 United Kingdom		 Tropical wood	30	Guayana
2243	Essequibo	 United Kingdom		 Fruit	30	Guayana
2244	Christmas Island	uncolonized		 Fish	15	Christmas & Cocos Islands
2245	Apetina	 Netherlands		 Timber	30	Guayana
2246	Maripasoula	 France		 Timber	30	Guayana
2247	Bogotá	 Colombia	 Colombia	 Cattle	30	Cundinamarca
2248	Ibagué	 Colombia	 Colombia	 Grain	30	Cundinamarca
2249	Tunja	 Colombia	 Colombia	 Cattle	30	Cundinamarca
2250	Manizales	 Colombia	 Colombia	 Grain	30	Cundinamarca
2251	Cúcuta	 Colombia	 Colombia	 Coffee	30	Antioquía
2252	Medellín	 Colombia	 Colombia	 Coffee	30	Antioquía
2253	Quibdó	 Colombia	 Colombia	 Coffee	30	Antioquía
2254	Cartagena de Indias	 Colombia	 Colombia	 Coffee	30	Antioquía
2255	Barranquilla	 Colombia	 Colombia	 Coffee	30	Antioquía
2256	Cali	 Colombia	 Colombia	 Grain	30	Cauca
2257	Popayán	 Colombia	 Colombia	 Grain	30	Cauca
2258	Buenaventura	 Colombia	 Colombia	 Fish	30	Cauca
2259	Pasto	 Colombia	 Colombia	 Cattle	30	Cauca
2260	San José del Guaviare	 Colombia	 Colombia	 Cattle	25	Guaviare
2261	Obando	 Colombia	 Colombia	 Timber	25	Guaviare
2262	Casanare	 Colombia	 Colombia	 Timber	25	Guaviare
2263	El Encanto	 Colombia	 Colombia	 Timber	25	Guaviare
2264	Caracas	 Venezuela	 Venezuela	 Fruit	30	Miranda
2265	Guanare	 Venezuela	 Venezuela	 Coffee	30	Miranda
2266	Calabozo	 Venezuela	 Venezuela	 Coffee	30	Miranda
2267	Cumaná	 Venezuela	 Venezuela	 Fruit	30	Miranda
2268	San Felipe	 Venezuela	 Venezuela	 Timber	30	Zulia
2269	Güiria	 Venezuela	 Venezuela	 Fruit	30	Bolívar
2270	Maracaibo	 Venezuela	 Venezuela	 Coffee	30	Zulia
2271	Valera	 Venezuela	 Venezuela	 Cattle	30	Zulia
2272	Coro	 Venezuela	 Venezuela	 Cattle	30	Zulia
2273	Barquisimento	 Venezuela	 Venezuela	 Coffee	30	Zulia
2274	Barinas	 Venezuela	 Venezuela	 Cattle	30	Miranda
2275	Angostura	 Venezuela	 Venezuela	 Wool	30	Bolívar
2276	Curiapo	 Venezuela	 Venezuela	 Coffee	30	Bolívar
2277	El Jobal	 Venezuela	 Venezuela	 Fruit	25	Bolívar
2278	San Fernado de Atabapo	 Venezuela	 Venezuela	 Wool	25	Bolívar
2279	Quito	 Ecuador	 Ecuador	 Fruit	30	Ecuador
2280	Guayaquil	 Ecuador	 Ecuador	 Fruit	35	Ecuador
2281	Esmereldas	 Ecuador	 Ecuador	 Fruit	35	Ecuador
2282	Loja	 Ecuador	 Ecuador	 Cattle	30	Ecuador
2283	Zamora	 Ecuador	 Ecuador	 Grain	30	Ecuador
2284	Tena	 Ecuador	 Ecuador	 Timber	30	Ecuador
2285	Galápagos	 Ecuador	 Ecuador	 Fish	30	Ecuador
2286	Iquitos	 Peru	 Peru	 Timber	30	Pastaza
2287	Yurimaguas	 Ecuador	 Ecuador	 Timber	30	Pastaza
2288	Yuncos	 Ecuador	 Ecuador	 Wool	30	Pastaza
2289	Puca Urco	 Ecuador	 Ecuador	 Timber	30	Pastaza
2290	Cajamarca	 Peru	 Peru	 Wool	30	Cajamarca
2291	Piura	 Peru	 Peru	 Wool	35	Cajamarca
2292	Trujillo	 Peru	 Peru	 Fish	35	Cajamarca
2293	Huánuco	 Peru	 Peru	 Wool	30	Lima
2294	Moyobamba	 Peru	 Peru	 Timber	30	Cajamarca
2295	Lima	 Peru	 Peru	 Cattle	35	Lima
2296	Huancavelica	 Peru	 Peru	 Cattle	30	Lima
2297	Ica	 Peru	 Peru	 Fish	35	Ica
2298	Huaraz	 Peru	 Peru	 Iron	35	Lima
2299	Ayacucho	 Peru	 Peru	 Cattle	30	Ica
2300	Pucallpa	 Peru	 Peru	 Wool	30	Lima
2301	Puerto Maldonado	 Peru	 Peru	 Timber	30	Ica
2302	Cusco	 Peru	 Peru	 Wool	30	Ica
2303	Puno	 Peru	 Peru	 Sulphur	30	Arequipa
2304	Arequipa	 Peru	 Peru	 Sulphur	35	Arequipa
2305	Antofagasta	 Bolivia	 Bolivia  Chile	 Wool	35	Atacama
2306	Sorocaba	 Brazil	 Brazil	 Cattle	35	São Paulo
2307	Iquique	 Peru	 Peru	 Cattle	35	Atacama
2308	Arica	 Peru	 Peru	 Sulphur	35	Atacama
2309	Calama	 Bolivia	 Bolivia  Chile	 Wool	35	Atacama
2310	La Paz	 Bolivia	 Bolivia	 Cattle	30	La Paz
2311	Cochabamba	 Bolivia	 Bolivia	 Fruit	30	La Paz
2312	Oruro	 Bolivia	 Bolivia	 Iron	30	Potosi
2313	Chuquisaca	 Bolivia	 Bolivia	 Wool	30	Santa Cruz
2314	Potosí	 Bolivia	 Bolivia	 Grain	30	Potosi
2315	Tarija	 Bolivia	 Argentina  Bolivia	 Wool	30	Jujuy
2316	Santa Cruz	 Bolivia	 Bolivia	 Fruit	30	Santa Cruz
2317	San Ignacio	 Bolivia	 Bolivia	 Tropical wood	30	Santa Cruz
2318	Roboré	 Bolivia	 Bolivia	 Tropical wood	30	Santa Cruz
2319	Santa Ana	 Bolivia	 Bolivia	 Timber	30	La Paz
2320	Riberalta	 Bolivia	 Bolivia	 Timber	30	La Paz
2321	Cobija	 Bolivia	 Bolivia	 Tropical wood	30	La Paz
2322	Copiapó	 Chile	 Chile	 Iron	35	Santiago
2323	La Serena	 Chile	 Chile	 Grain	35	Santiago
2324	Santiago	 Chile	 Chile	 Grain	35	Santiago
2325	Valparaíso	 Chile	 Chile	 Fruit	35	Santiago
2326	Viña del Mar	 Chile	 Chile	 Fruit	35	Santiago
2327	Talca	 Chile	 Chile	 Grain	35	Los Ríos
2328	Valdivia	 Chile	 Chile	 Grain	35	Los Ríos
2329	Temuco	 Chile	 Chile	 Grain	35	Los Ríos
2330	Cauquenes	 Chile	 Chile	 Iron	35	Los Ríos
2331	Chillán	 Chile	 Chile	 Iron	35	Los Ríos
2332	Osorno	 Chile	 Chile	 Grain	35	Araucania
2333	Puerto Aisén	uncolonized		 Fruit	25	Araucania
2334	Punta Arenas	uncolonized		 Wool	25	Araucania
2335	Porvenir	uncolonized		 Wool	25	Araucania
2336	Easter Island	uncolonized		 Fish	15	Araucania
2337	Fortin Falcon	 Bolivia	 Bolivia  Paraguay	 Tropical wood	30	Alto Paraguay
2338	Puerto Guaraní	 Bolivia	 Bolivia  Paraguay	 Timber	30	Alto Paraguay
2339	Asuncion	 Paraguay	 Paraguay	 Cattle	30	Bajo Paraguay
2340	Pilar	 Paraguay	 Paraguay	 Timber	30	Bajo Paraguay
2341	Encarnación	 Paraguay	 Paraguay	 Cattle	30	Bajo Paraguay
2342	San Pedro	 Paraguay		 Fruit	30	Bajo Paraguay
2343	Concepción	 Paraguay	 Paraguay	 Cattle	30	Bajo Paraguay
2344	Montevideo	 Uruguay	 Uruguay	 Cattle	35	Uruguay
2345	Paysandú	 Uruguay	 Uruguay	 Cattle	35	Uruguay
2346	Tacuarembó	 Uruguay	 Uruguay	 Wool	35	Uruguay
2347	Melo	 Uruguay	 Uruguay	 Cattle	35	Uruguay
2348	Buenos Aires	 Argentina		 Cattle	35	Buenos Aires
2349	Junín	 Argentina	 Argentina	 Cattle	35	Buenos Aires
2350	Azul	 Argentina		 Cattle	35	Buenos Aires
2351	La Plata	 Argentina		 Cattle	35	Buenos Aires
2352	Mar del Plata	 Argentina	 Argentina	 Cattle	35	Buenos Aires
2353	Trenque Lanquen	 Argentina		 Cattle	35	Buenos Aires
2354	Bahía Blanca	 Argentina	 Argentina	 Cattle	35	Buenos Aires
2355	Carmen	 Argentina	 Argentina	 Cattle	35	Buenos Aires
2356	Corrientes	 Argentina	 Argentina	 Cattle	30	Corrientes
2357	Curuzú Cuatiú	 Argentina	 Argentina	 Cattle	35	Corrientes
2358	Santo Tomás	 Argentina	 Argentina	 Fruit	30	Corrientes
2359	Colón	 Argentina	 Argentina	 Fruit	35	Santa Fe
2360	Paraná	 Argentina	 Argentina	 Cattle	35	Santa Fe
2361	Sancti Spiritu	 Argentina	 Argentina	 Grain	35	Santa Fe
2362	Reconquista	 Argentina		 Cattle	35	Santa Fe
2363	Rosario	 Argentina	 Argentina	 Cattle	35	Santa Fe
2364	Resistencia	 Argentina		 Cattle	30	Chaco
2365	Villa Ángela	 Argentina	 Argentina	 Cattle	30	Chaco
2366	Formosa	 Bolivia	 Argentina  Bolivia  Paraguay	 Timber	30	Alto Paraguay
2367	Xolotas	 Bolivia	 Argentina  Bolivia  Paraguay	 Timber	30	Alto Paraguay
2368	Salta	 Argentina		 Wool	35	Jujuy
2369	Jujuy	 Argentina		 Wool	30	Jujuy
2370	Cochinoca	 Bolivia	 Argentina  Bolivia	 Wool	30	Jujuy
2371	Equia	 Argentina	 Argentina	 Timber	30	Jujuy
2372	Rivadavia	 Argentina	 Argentina	 Timber	30	Jujuy
2373	Tucumán	 Argentina		 Fruit	35	Tucumán
2374	Catamarca	 Argentina		 Wool	35	Tucumán
2375	Vinchina	 Argentina	 Argentina	 Iron	35	Tucumán
2376	Santiago del Estero	 Argentina	 Argentina	 Timber	35	Chaco
2377	Añatuya	 Argentina	 Argentina	 Timber	35	Chaco
2378	Mailín	 Argentina	 Argentina	 Timber	35	Chaco
2379	Córdoba de Argentina	 Argentina	 Argentina	 Grain	35	La Pampa
2380	Villa Nueva	 Argentina	 Argentina	 Grain	35	La Pampa
2381	Río Cuarto	 Argentina	 Argentina	 Cattle	35	La Pampa
2382	Renancó	 Argentina	 Argentina	 Wool	35	La Pampa
2383	San Luis	 Argentina	 Argentina	 Grain	35	La Pampa
2384	Mercedes	 Argentina	 Argentina	 Cattle	35	La Pampa
2385	La Rioja	 Argentina		 Wool	35	Tucumán
2386	Santa Rita	 Argentina	 Argentina	 Wool	35	Tucumán
2387	San Juan	 Argentina	 Argentina	 Fruit	35	Tucumán
2388	Calingasta	 Argentina	 Argentina	 Fruit	35	Tucumán
2389	Mendoza	 Argentina	 Argentina	 Fruit	35	Río Negro
2390	San Rafael	 Argentina	 Argentina	 Fruit	35	Río Negro
2391	Neuquén	uncolonized		 Cattle	25	Patagonia Septentrional
2392	Viedma	uncolonized		 Wool	25	Patagonia Septentrional
2393	Telén	 Argentina	 Argentina	 Wool	25	Río Negro
2394	Bariloche	uncolonized		 Wool	25	Patagonia Septentrional
2395	Curacó	 Argentina	 Argentina	 Wool	25	Río Negro
2396	Rawson	uncolonized		 Wool	25	Patagonia Septentrional
2397	Esquel	uncolonized		 Wool	25	Patagonia Septentrional
2398	Puerto Deseado	uncolonized		 Wool	25	Patagonia Meridional
2399	Rio Gallegos	uncolonized		 Wool	25	Patagonia Meridional
2400	Rio Grande	uncolonized		 Wool	25	Patagonia Meridional
2401	Marabitanas	 Colombia	 Colombia	 Tobacco	25	Amazonas
2402	Manaus	 Brazil	 Brazil	 Tropical wood	25	Pará
2403	Cachoeira	 Brazil	 Brazil	 Tobacco	25	Amazonas
2404	Tefe	 Brazil	 Brazil	 Tropical wood	25	Amazonas
2405	Borba	 Brazil	 Brazil	 Tropical wood	25	Amazonas
2406	Cocos Islands	uncolonized		 Fish	15	Christmas & Cocos Islands
2407	Tabatinga	 Brazil	 Brazil	 Timber	25	Amazonas
2408	Oriximina	 Brazil	 Brazil	 Tropical wood	25	Pará
2409	Saint Vincent	 United Kingdom		 Cotton	35	Lesser Antilles
2410	Belém	 Brazil	 Brazil	 Grain	35	Maranhão
2411	Santarém	 Brazil	 Brazil	 Grain	25	Maranhão
2412	Óbidos	 Brazil	 Brazil	 Tropical wood	35	Pará
2413	Marabá	 Brazil	 Brazil	 Grain	25	Maranhão
2414	Amapá	 Brazil	 Brazil	 Tropical wood	35	Pará
2415	Macapá	 Brazil	 Brazil	 Tropical wood	35	Pará
2416	Dourados	 Brazil	 Brazil	 Tropical wood	25	Mato Grosso
2417	Vila Bela	 Brazil	 Brazil	 Tobacco	25	Mato Grosso
2418	Cuiabá	 Brazil	 Brazil	 Fruit	25	Mato Grosso
2419	Corumbá	 Brazil	 Brazil	 Fruit	25	Mato Grosso
2420	Iguatemi	 Paraguay	 Brazil  Paraguay	 Sulphur	25	Mato Grosso
2421	Vila Boa	 Brazil	 Brazil	 Tropical wood	35	Mato Grosso
2422	Aganja	 Brazil	 Brazil	 Fruit	35	Mato Grosso
2423	Palmas	 Brazil	 Brazil	 Fruit	35	Maranhão
2424	São Luís	 Brazil	 Brazil	 Tobacco	35	Maranhão
2425	Chapada	 Brazil	 Brazil	 Cotton	35	Maranhão
2426	Teresina	 Brazil	 Brazil	 Fruit	35	Rio Grande do Norte
2427	Oeiras	 Brazil	 Brazil	 Grain	35	Rio Grande do Norte
2428	Paraíba	 Brazil	 Brazil	 Fruit	35	Pernambuco
2429	Fortaleza	 Brazil	 Brazil	 Fruit	35	Rio Grande do Norte
2430	Crato	 Brazil	 Brazil	 Cotton	35	Rio Grande do Norte
2431	Natal	 Brazil	 Brazil	 Cotton	35	Rio Grande do Norte
2432	Recife	 Brazil	 Brazil	 Coffee	35	Pernambuco
2433	Cabrobo	 Brazil	 Brazil	 Cotton	35	Pernambuco
2434	Maceió	 Brazil	 Brazil	 Tobacco	35	Pernambuco
2435	Aracaju	 Brazil	 Brazil	 Tobacco	35	Pernambuco
2436	Salvador de Bahia	 Brazil	 Brazil	 Tobacco	35	Bahia
2437	Juazeiro	 Brazil	 Brazil	 Tobacco	35	Bahia
2438	Vila do Barra	 Brazil	 Brazil	 Cattle	35	Bahia
2439	Porto Seguro	 Brazil	 Brazil	 Coffee	35	Bahia
2440	Vitória da Conquista	 Brazil	 Brazil	 Coffee	35	Bahia
2441	Ouro Preto	 Brazil	 Brazil	 Coffee	35	Minas Gerais
2442	Sabará	 Brazil	 Brazil	 Coffee	35	Minas Gerais
2443	Januária	 Brazil	 Brazil	 Coffee	35	Minas Gerais
2444	Paracatu	 Brazil	 Brazil	 Cattle	35	Minas Gerais
2445	Uberaba	 Brazil	 Brazil	 Fruit	35	Minas Gerais
2446	São João del Rey	 Brazil	 Brazil	 Tropical wood	35	Minas Gerais
2447	Rio de Janeiro	 Brazil	 Brazil	 Coffee	35	Rio de Janeiro
2448	Campos	 Brazil	 Brazil	 Coffee	35	Rio de Janeiro
2449	Vitória	 Brazil	 Brazil	 Fruit	35	Rio de Janeiro
2450	São Paulo	 Brazil	 Brazil	 Coffee	35	São Paulo
2451	Santos	 Brazil	 Brazil	 Coffee	35	São Paulo
2452	Campinas	 Brazil	 Brazil	 Cattle	35	São Paulo
2453	Assis	 Brazil	 Brazil	 Cattle	35	São Paulo
2454	Fiji	uncolonized		 Fish	15	Fiji
2455	Iguape	 Brazil	 Brazil	 Cattle	35	São Paulo
2456	Araraquara	 Brazil	 Brazil	 Coffee	35	São Paulo
2457	Curitiba	 Brazil	 Brazil	 Fruit	35	Paraná
2458	Garapuava	 Brazil	 Brazil	 Coffee	35	Paraná
2459	Lajes	 Brazil	 Brazil	 Fruit	35	Paraná
2460	Castro	 Brazil	 Brazil	 Grain	35	Paraná
2461	Desterro	 Brazil	 Brazil	 Cattle	35	Paraná
2462	São Miguel	 Brazil	 Brazil	 Tropical wood	35	Paraná
2463	Porto Alegre	 Brazil	 Brazil	 Cattle	35	Rio Grande do Sul
2464	Pelotas	 Brazil	 Brazil	 Cattle	35	Rio Grande do Sul
2465	Passo Fundo	 Brazil	 Brazil	 Tobacco	35	Rio Grande do Sul
2466	Santa Maria	 Brazil	 Brazil	 Timber	35	Rio Grande do Sul
2467	Alegrete	 Brazil	 Brazil	 Cattle	35	Rio Grande do Sul
2468	Sydney	 United Kingdom	 Australia	 Grain	30	New South Wales
2469	Newcastle	 United Kingdom	 Australia	 Coal	30	New South Wales
2470	Port Macquarie	 United Kingdom	 Australia	 Grain	30	New South Wales
2471	Ophir	 United Kingdom	 Australia	 Grain	30	New South Wales
2472	Eden	 United Kingdom	 Australia	 Grain	30	New South Wales
2473	Wagga Wagga	 United Kingdom	 Australia	 Grain	30	New South Wales
2474	Moree	 United Kingdom	 Australia	 Grain	30	New South Wales
2475	Broken Hill	 United Kingdom	 Australia	 Grain	30	New South Wales
2476	Melbourne	 United Kingdom	 Australia	 Wool	30	Victoria
2477	Warmambool	 United Kingdom	 Australia	 Wool	30	Victoria
2478	Ballarat	 United Kingdom	 Australia	 Wool	30	Victoria
2479	Sale	 United Kingdom	 Australia	 Grain	30	Victoria
2480	Beechworth	 United Kingdom	 Australia	 Wool	30	Victoria
2481	Swan Hill	 United Kingdom	 Australia	 Grain	30	Victoria
2482	Tasmania	 United Kingdom	 Australia	 Timber	30	Victoria
2483	Brisbane	 United Kingdom	 Australia	 Cattle	30	Queensland
2484	Gladstone	 United Kingdom	 Australia	 Wool	30	Queensland
2485	Clermont	 United Kingdom	 Australia	 Cattle	30	Queensland
2486	Toowoomba	 United Kingdom	 Australia	 Cattle	30	Queensland
2487	Townsville	 United Kingdom	 Australia	 Cattle	30	Queensland
2488	Cooktown	 United Kingdom	 Australia	 Tropical wood	30	Queensland
2489	Longreach	 United Kingdom	 Australia	 Cattle	30	Queensland
2490	Charleville	uncolonized	 Australia	 Cattle	15	Queensland
2491	Adelaide	 United Kingdom	 Australia	 Wool	30	South Australia
2492	Port Lincolon	 United Kingdom	 Australia	 Wool	30	South Australia
2493	Robe	 United Kingdom	 Australia	 Wool	30	South Australia
2494	Port Augusta	 United Kingdom	 Australia	 Grain	30	South Australia
2495	Oodnadatta	uncolonized	 Australia	 Fruit	15	South Australia
2496	Tarcoola	 United Kingdom	 Australia	 Wool	30	South Australia
2497	Perth	 United Kingdom	 Australia	 Grain	30	Western Australia
2498	Kojonup	 United Kingdom	 Australia	 Grain	30	Western Australia
2499	Geraldton	 United Kingdom	 Australia	 Grain	30	Western Australia
2500	Kalgoorlie	 United Kingdom	 Australia	 Grain	30	Western Australia
2501	Broome	 United Kingdom	 Australia	 Grain	20	Western Australia
2502	Dampier	 United Kingdom	 Australia	 Grain	30	Western Australia
2503	Wiluna	uncolonized	 Australia	 Cattle	15	Western Australia
2504	Esperance	 United Kingdom	 Australia	 Fruit	30	Western Australia
2505	Palmerston	 United Kingdom	 Australia	 Grain	20	Northern Territory
2506	Tennant Creek	 United Kingdom	 Australia	 Cattle	15	Northern Territory
2507	Alice Springs	uncolonized	 Australia	 Cattle	15	Northern Territory
2508	Norfolk Island	 United Kingdom	 Australia	 Fish	30	New South Wales
2509	Auckland	 United Kingdom	 New Zealand	 Cattle	30	North Island
2510	New Plymouth	 United Kingdom	 New Zealand	 Cattle	30	North Island
2511	Napier	uncolonized	 New Zealand	 Cattle	30	North Island
2512	Wellington	 United Kingdom	 New Zealand	 Cattle	30	North Island
2513	Dunedin	uncolonized	 New Zealand	 Wool	30	South Island
2514	Hokitika	uncolonized	 New Zealand	 Wool	30	South Island
2515	Christchurch	uncolonized	 New Zealand	 Wool	30	South Island
2516	Nelson	 United Kingdom	 New Zealand	 Cattle	30	South Island
2517	Guam	 Spain	 Spain	 Fish	30	Micronesia
2518	Palau	 Spain	 Spain	 Fruit	30	Micronesia
2519	Yap	uncolonized		 Fish	15	Micronesia
2520	Taveuni	uncolonized		 Fish	15	Fiji
2521	Saipan	 Spain	 Spain	 Fish	30	Micronesia
2522	Marshall Islands	uncolonized		 Fish	15	Micronesia
2523	Nauru	uncolonized		 Fish	15	Fiji
2524	Wake	uncolonized		 Fish	10	Hawaiian Islands
2525	Marcus	uncolonized		 Fish	10	Bonin Islands
2526	Palmyra	uncolonized		 Fish	20	Hawaiian Islands
2527	Gilbert Islands	uncolonized		 Fish	15	Kiribati
2528	Port Moresby	uncolonized		 Tropical wood	15	Southern New Guinea
2529	Kerema	uncolonized		 Tropical wood	15	Southern New Guinea
2530	Lae	uncolonized		 Tropical wood	15	Northern New Guinea
2531	Madang	uncolonized		 Grain	15	Northern New Guinea
2532	Forte São Joaquim	 Brazil	 Brazil	 Tropical wood	25	Amazonas
2533	Targu Mures	 Austria	 Austria  Hungary  Romania  Siebenbürgen	 Grain	35	Eastern Siebenbürgen
2534	Solomon Islands	uncolonized		 Fruit	15	Southern New Guinea
2535	New Hebrides	uncolonized		 Fish	15	Southern New Guinea
2536	Santa Cruz Islands	uncolonized		 Fish	15	Southern New Guinea
2537	New Britain	uncolonized		 Tropical wood	15	Northern New Guinea
2538	Novi Sad	 Austria	 Austria  Hungary  Serbia  Yugoslavia	 Wool	35	Slavonia
2539	Bougainville	uncolonized		 Tropical wood	15	Northern New Guinea
2540	Tonga	uncolonized		 Fish	15	Tonga
2541	Ellice Islands	uncolonized		 Fish	15	Tonga
2542	Wallis And Futuna	uncolonized		 Fish	15	New Caledonia
2543	Apia	uncolonized		 Fish	15	Tonga
2544	Pago Pago	uncolonized		 Fish	15	Tonga
2545	Rarotonga	uncolonized		 Fish	15	Tonga
2546	Tongareva	uncolonized		 Fish	15	Tonga
2547	Tokelau	uncolonized		 Fish	15	Tonga
2548	Niue	uncolonized		 Fish	15	Fiji
2549	Tarauacá	 Bolivia	 Bolivia  Brazil	 Tropical wood	25	Amazonas
2550	Forte do Principe	 Brazil	 Brazil	 Tropical wood	25	Mato Grosso
2551	Marquesas	uncolonized		 Fish	15	New Caledonia
2552	Pitcairn	uncolonized		 Fish	15	Fiji
2553	Tuamotus	uncolonized		 Fish	15	New Caledonia
2554	Posadas	 Argentina	 Argentina	 Cattle	30	Corrientes
2555	Augusta	 United States of America	 United States of America	 Cotton	35	Georgia - US
2556	Asheville	 United States of America	 United States of America	 Tobacco	35	North Carolina
2557	Esbjerg	 Denmark	 Denmark  Scandinavia	 Cattle	35	Jylland
2558	De Aar	 United Kingdom	 South Africa	 Fruit	35	Northern Cape
2559	Suhaj	 Egypt	 Egypt	 Cotton	35	Middle Egypt
2560	Darmstadt	 Hesse-Darmstadt	 Germany  Hesse-Darmstadt	 Fruit	35	Hesse-Nassau
2561	Siegburg	 Prussia	 Germany  Prussia	 Cattle	35	Nordrhein
2562	Tainan	 China	 China	 Tea	35	Formosa
2563	Safi	 Morocco	 Morocco	 Grain	35	Morocco
2564	Salima	 Egypt	 Egypt	 Cattle	30	Dongola
2565	Cebu	 Spain	 Philippines	 Fish	30	Visayas
2566	Agartala	 United Kingdom	 India	 Grain	35	Assam
2567	Gaeta	 Two Sicilies	 Italy  Two Sicilies	 Fish	35	Campania
2568	Lugano	 Switzerland	 Switzerland	 Wool	35	East Switzerland
2569	Niksic	 Ottoman Empire	 Montenegro  Ottoman Empire  Yugoslavia	 Grain	35	Montenegro
2570	Beauvais	 France	 France	 Grain	35	Picardie
2571	Tauranga	 United Kingdom	 New Zealand	 Cattle	30	North Island
2572	Nan	 Siam	 Siam	 Opium	30	Chiang Mai
2573	Mboul	uncolonized		 Grain	15	Senegal
2574	Mochudi	uncolonized		 Wool	15	Botswana
2575	Ipoh	 Johore	 Johore	 Timber	30	Malaya
2576	Natuna	 Netherlands		 Fish	30	Malaya
2577	Pljevlja	 Ottoman Empire	 Montenegro  Ottoman Empire  Yugoslavia	 Iron	35	Montenegro
2578	Tacna	 Peru	 Peru	 Wool	35	Arequipa
2579	Truk	uncolonized		 Fish	15	Micronesia
2580	Stara Ladoga	 Russia	 Russia	 Grain	35	Novgorod
2581	Mataka	uncolonized		 Grain	15	Mocambique
2582	Kotor	 Austria	 Austria  Croatia  Yugoslavia	 Fish	35	Dalmatia
2583	Cetinje	 Montenegro	 Montenegro  Yugoslavia	 Fish	35	Montenegro
2584	Bielsko	 Austria	 Austria  Poland	 Coal	35	West Galicia
2585	Matan as Sarah	uncolonized		 Wool	15	Libyan Desert
2586	Al-Ahsa	 Nejd	 Nejd	 Grain	10	Nejd
2587	Kola	 Russia	 Russia	 Timber	35	Karelia
2588	Onega	 Russia	 Russia	 Timber	35	Arkhangelsk
2589	Shoyna	 Russia	 Russia	 Timber	35	Nenetsia
2590	Ugolnoye	 Russia	 Russia	 Fish	20	Coastal Chukotka
2591	Holsteinsborg	 Denmark	 Denmark  Scandinavia	 Fish	35	Iceland & Greenland
2592	Ungava	 United Kingdom	 Canada  Quebec	 Cattle	35	Quebec
2593	Fort George	 United Kingdom	 Canada  Quebec	 Timber	35	Quebec
2594	Pickle	 United Kingdom	 Canada	 Timber	35	Ontario
2595	Nunavut	 United Kingdom	 Canada	 Fish	35	Nunavut
2596	Fort Resolution	uncolonized	 Canada	 Fish	15	Northwest Territories
2597	Fort Vermilion	uncolonized	 Canada	 Timber	30	Alberta
2598	Fort Liard	uncolonized	 Canada	 Timber	15	Northwest Territories
2599	Fairbanks	uncolonized		 Fish	15	Alaska
2600	Altamira	 Brazil	 Brazil	 Grain	25	Maranhão
2601	Sandy Desert	uncolonized	 Australia	 Grain	15	Western Australia
2602	Roebourne	 United Kingdom	 Australia	 Grain	30	Western Australia
2603	Tanami	uncolonized	 Australia	 Cattle	15	Northern Territory
2604	Normanton	 United Kingdom	 Australia	 Tropical wood	30	Queensland
2605	Gibson's Desert	uncolonized	 Australia	 Grain	15	Western Australia
2606	Zhambyl	uncolonized	 Russia	 Coal	25	Semireche
2607	Lop Nur	 China	 China  Xinjiang	 Cotton	35	Xinjiang
2608	Khatgal	 China	 China  Mongolia	 Iron	35	Mongolia
2609	Araouane	uncolonized		 Grain	10	Timbuktu
2610	Uralsk	 Russia	 Russia	 Wool	35	Uralsk
2611	Turgay	 Russia	 Russia	 Wool	35	Uralsk
2612	Aktash	uncolonized	 Russia	 Coal	25	Akmolinsk
2613	Nyda	uncolonized	 Russia	 Timber	15	Ob
2614	Mordiyakha	uncolonized	 Russia	 Timber	15	Ob
2615	Krasnoselkup	 Russia	 Russia	 Timber	15	Lower Yeniseysk
2616	Tilichiki	 Russia	 Russia	 Fish	20	Kamchatka
2617	Saghalian Oula	 China	 China	 Coal	35	Outer Manchuria
2618	Talaya	 Russia	 Russia	 Grain	35	Upper Okhotsk
2619	Abiy	uncolonized	 Russia	 Timber	15	North Yakutsk
2620	Syasir	uncolonized	 Russia	 Cattle	15	Upper Okhotsk
2621	Srednekolymsk	uncolonized	 Russia	 Timber	15	Inner Chuktoka
2622	Markovo	uncolonized	 Russia	 Grain	15	Inner Chuktoka
2623	Midway Island	uncolonized		 Fish	10	Hawaiian Islands
2624	Loango	uncolonized		 Timber	15	Congo
2625	Port Hope Simpson	 United Kingdom	 Canada  Newfoundland	 Fish	35	Newfoundland
2626	Port Harrison	 United Kingdom	 Canada  Quebec	 Grain	35	Quebec
2627	Fort Chimo	 United Kingdom	 Canada  Quebec	 Timber	35	Quebec
2628	Attawapiskat	 United Kingdom	 Canada	 Fish	35	Ontario
2629	Beatton River	uncolonized	 Canada	 Timber	30	British Columbia
2630	Cordova	uncolonized		 Fish	15	Alaska
2631	Unalakeet	uncolonized		 Fish	15	Alaska
2632	Ammassalik	 Denmark	 Denmark  Scandinavia	 Fish	35	Iceland & Greenland
2633	Ossora	 Russia	 Russia	 Fish	20	Kamchatka
2634	Rassvet	 Russia	 Russia	 Fish	20	Coastal Chukotka
2635	Kariba	uncolonized		 Grain	25	Zambezi
2636	Egedesminde	 Denmark	 Denmark  Scandinavia	 Fish	35	Iceland & Greenland
2637	Novo Mariinsk	 Russia	 Russia	 Fish	20	Coastal Chukotka
2638	Omsukchan	 Russia	 Russia	 Grain	20	Upper Okhotsk
2639	Susuman	 Russia	 Russia	 Fish	35	Upper Okhotsk
2640	Ziryanka	uncolonized	 Russia	 Cattle	15	Upper Okhotsk
2641	Ayan	 Russia	 Russia	 Grain	35	Okhotsk
2642	Ust Nera	 Russia	 Russia	 Cattle	35	Okhotsk
2643	Honuu	uncolonized	 Russia	 Grain	15	North Yakutsk
2644	Olyekminsk	 Russia	 Russia	 Timber	35	Trans-Baikal
2645	Chilchi	 Russia	 Russia	 Coal	35	Trans-Baikal
2646	Ases Igan	 Russia	 Russia	 Coal	15	Upper Yeniseysk
2647	Yansk	uncolonized	 Russia	 Timber	15	North Yakutsk
2648	Yakutsk	 Russia	 Russia	 Grain	35	Okhotsk
2649	Zhigansk	 Russia	 Russia	 Grain	15	Yakutsk
2650	Nyurba	 Russia	 Russia	 Grain	15	West Yakutsk
2651	Udanchniy	 Russia	 Russia	 Timber	15	West Yakutsk
2652	Kular	uncolonized	 Russia	 Grain	15	Yakutsk
2653	Saskylah	uncolonized	 Russia	 Timber	15	North Siberia
2654	Khatanga	uncolonized	 Russia	 Timber	15	North Siberia
2655	Tura	 Russia	 Russia	 Iron	15	Middle Siberia
2656	Tayimba	 Russia	 Russia	 Coal	35	Middle Siberia
2657	Svetlogorsk	 Russia	 Russia	 Grain	15	Lower Yeniseysk
2658	Kheta	uncolonized	 Russia	 Timber	15	Lower Yeniseysk
2659	Napalkovo	uncolonized	 Russia	 Timber	15	Ob
2660	Bereyezovka	uncolonized	 Russia	 Grain	15	Inner Chukotka
2661	Nizhnekolymsk	uncolonized	 Russia	 Timber	15	Coastal Chukotka
2662	Cherskiy	uncolonized	 Russia	 Timber	15	Inner Chukotka
2663	Kamenskoye	 Russia	 Russia	 Grain	20	Kamchatka
2664	Oyotuni	uncolonized	 Russia	 Grain	15	Inner Chukotka
2665	Chokurdakh	uncolonized	 Russia	 Timber	15	North Yakutsk
2666	Pevek	uncolonized	 Russia	 Grain	15	Coastal Chukotka
2667	Bulun	uncolonized	 Russia	 Timber	15	Yakutsk
2668	Verkhoyansk	 Russia	 Russia	 Grain	15	North Yakutsk
2669	Amga	 Russia	 Russia	 Grain	35	Okhotsk
2670	Tiksi	uncolonized	 Russia	 Timber	15	North Siberia
2671	Zhilinda	 Russia	 Russia	 Cattle	15	West Yakutsk
2672	Pokrovsk	 Russia	 Russia	 Timber	15	Yakutsk
2673	Olenyok	uncolonized	 Russia	 Grain	15	North Siberia
2674	Essey	uncolonized	 Russia	 Timber	15	North Siberia
2675	Yekonda	 Russia	 Russia	 Grain	15	Middle Siberia
2676	Kirensk	 Russia	 Russia	 Grain	35	Irkutsk
2677	Dotkon	 Russia	 Russia	 Coal	35	Irkutsk
2678	Bulgan	 China	 China  Mongolia	 Timber	35	Mongolia
2679	Khovd	 China	 China  Mongolia	 Cotton	35	Mongolia
2680	Dudinka	 Russia	 Russia	 Timber	15	Lower Yeniseysk
2681	Kikkiakki	 Russia	 Russia	 Timber	15	Upper Yeniseysk
2682	Aksarka	 Russia	 Russia	 Timber	15	Ob
2683	Bakchar	 Russia	 Russia	 Coal	35	Tobolsk
2684	Yar Sale	uncolonized	 Russia	 Timber	15	Ob
2685	Muzhi	 Russia	 Russia	 Timber	35	Ural
2686	Ishim	 Russia	 Russia	 Sulphur	35	Tobolsk
2687	Amderma	 Russia	 Russia	 Timber	15	Nenetsia
2688	Inta	 Russia	 Russia	 Fish	15	Nenetsia
2689	Mulda	 Russia	 Russia	 Timber	35	Perm
2690	Verkhniy Ufaley	 Russia	 Russia	 Grain	15	Ob
2691	Vorgovo	 Russia	 Russia	 Grain	15	Upper Yeniseysk
2692	Kostino	 Russia	 Russia	 Timber	15	Upper Yeniseysk
2693	Uchami	 Russia	 Russia	 Timber	15	Lower Yeniseysk
2694	Vanavara	 Russia	 Russia	 Grain	35	Middle Siberia
2695	Mukhtuya	 Russia	 Russia	 Grain	15	West Yakutsk
2696	Aldan	 Russia	 Russia	 Grain	35	Trans-Baikal
2697	Magdagachi	 Russia	 Russia	 Grain	35	Trans-Baikal
2698	Slavgorod	 Russia	 Russia	 Coal	35	Tomsk
2699	Izhma	 Russia	 Russia	 Timber	15	Nenetsia
2700	Usogorsk	 Russia	 Russia	 Timber	35	Perm
2701	Surinda	 Russia	 Russia	 Grain	35	Middle Siberia
2702	Aralsk	 Russia	 Russia	 Wool	35	Uralsk
2703~3245	Sea provinces
3246	Jan Mayen	 Sweden	 Jan Mayen  Norway  Scandinavia  Sweden	 Fish	35	Nordnorge
3247~3248	Sea provinces


---

---
title: Puppet modding
category: guide
tags: [diplomacy]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Puppet_modding
---

This page documents the formatting and creation of puppets.

Creation of new puppet relationships

The files governing puppet relations are found within history\diplomacy. You are looking for the "unions" file and the "puppetstates" file. It does not matter which file you use, as long as it is within the correct folder.

Each relationship is made up of four informations:

first =
second =
start_date =
end_date =

You should note the overlord tag in first = and the puppet in second =. The start date should be before the intented start date. Any date before 1836.1.1 is just for flavour. If you intend the relationship to only be present for the 'American Civil War' scenario, use the start date 1861.1.1 instead. The end date does not have an effect, so just use 1936.1.1.

Example: 

vassal = {
	
first = ENG
	
second = GWA
	
start_date = 1836.1.1
	
end_date = 1949.1.1
}


This case creates the starting puppet relation between United Kingdom and Gwalior.


---

---
title: Religion modding
category: guide
tags: [culture]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Religion_modding
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


---

---
title: Save Game editing
category: other
tags: [utility]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Save-game_editing
---

This is a modding guide for Save-game editing.

Save location

Save files are located in Victoria 2's installation directory (ie C:\Program Files\Steam\SteamApps\Common\Victoria 2\). Unlike more recent Paradox Interactive games, they are not located under Program Files. Note: Editing save games prevent achievements!

Save files are normally compressed and saved as binary. To prevent that, open game in debug mode and save game again. Warning: Save Files will become 10x bigger! To return file size to normal, after editing open game without debug mode and save again.

Editing

The save games are very large, so it is not recommended to use Notepad. Instead use Notepad++ or Sublime Text to edit saves.


---

---
title: Sphere modding
category: guide
tags: [diplomacy]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Sphere_modding
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


---

---
title: War modding
category: guide
tags: [diplomacy]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/War_modding
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


