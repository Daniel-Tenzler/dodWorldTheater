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
