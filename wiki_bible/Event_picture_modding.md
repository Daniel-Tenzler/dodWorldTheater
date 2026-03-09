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
