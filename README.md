TypescriptTool
==============

Quick and _very_ Dirty Python+PySide GUI Tool to create Typescripts for ConTeXt mkII.

## Installation Notes

This program works on Python 2.6+. It hasn't been tested with Python 3+, and I'm quite sure it doesn't work. 
Moreover, you need PySide 1.02+ for your Python version installed. 

## Usage

1. Run `python TypescriptTool.py`.
2. Load a map file from the appropriate directory. Since this program has been built on a Win7 box with W32Tex 
installed, it defaults to `C:\tex\share\texmf-local\fonts\map\pdftex\context`.
3. You can load multiple map files, these will be shown on the listbox in the upperleft corner of the windows
4. When you select a map files the contained fonts will be shown in the "Fonts" list box. 
5. Ok, you've loaded one or more map files. Now let's create typescripts. 
6. Give a global name to the typescript by using the input box near the "Generate Typescript" button.
7. Click on the "Serif" tab. Set the appropriate encoding (ec, texnansi, cork). 
8. Give the serif font a symbolic name in the "synonym name" box. (frex. DWSerif)
8. Map a font to the appropriate symbolic style by selecting the font file and clicking the appropriate button. 
Ie, say that your font list contains "Times Bold.", that is a bold serif font. You must click on the serif tab,
select "Times Bold" from the font list and press the "Bold" button. Repeat this step for every font in your 
chosen family (Regular, Bold, Italic, BoldItalic, Slanted, BoldSlanted, SmallCaps)
9. Repeat this step for "Sans" and "Mono" macrofamilies. Click on the appropriate tab, set the encoding, 
__choose the appropriate macro family value from the combo box__ (yeah, usability bug) and fill the typescript data
10. Press "generate typescript" and go to "TeX result" tab. You'll find a sample ConTeXt  file to test out your
typescript, with all microtypographic features turned on. 