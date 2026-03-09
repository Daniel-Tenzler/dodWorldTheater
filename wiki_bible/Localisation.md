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
