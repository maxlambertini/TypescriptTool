import re
import os.path
import random

'''
Created on 13/dic/2011

@author: massi
'''
class TTFMapLine:
    """
    This class encapsulates a line of a pdfTeX map file. This line contains info
    pertaining physical font file, its encoding and its font name

    - encoding: the font encoding
    - virtual_font_file: the virtual font file
    - symbolic_name: the human-readable font file name
    """
    def __init__(self,map_line):
        if (map_line is None or map_line == ""):
            raise Exception("Line must not be null")
        items2 = re.split('\\s|\\<', map_line)
        self.items = []
        for l in items2:
            if l <> '':
                self.items.append(l)

        vff_items = re.split ('\-',self.items[0])
        self.encoding = vff_items[0]
        self.virtual_font_file = self.items[0].replace ("raw-","")
        if self.virtual_font_file.endswith("--base"):
            self.virtual_font_file = self.virtual_font_file.replace("--base","")

        if (self.items[1].lower() != "unknown"):
            self.symbolic_name = self.items[1]
        else:
            self.symbolic_name = self.virtual_font_file.replace(self.encoding+"-","")
        self.symbolic_name = self.symbolic_name.replace("-"," ")
        self.family = self.symbolic_name.lower() \
            .replace(" ","").replace("oblique","").replace("narrow","") \
            .replace("condensed","").replace("book","").replace("regular","") \
            .replace("bold","").replace("italic","").replace("black","") \
            .replace("ultra","").replace("extra","").replace("light","").replace("heavy","") \
            .replace("medium","")

        self.isBodyFont = True
        self.isTitleFont = False

        sym_lower = self.symbolic_name.lower()
        if sym_lower.find("bold") > -1 or sym_lower.find("black") > -1 or sym_lower.find("heavy") > -1 or sym_lower.find("ultra") > -1 :
            self.isTitleFont = True
            self.isBodyFont = False
        if sym_lower.find("condensed") > -1 or sym_lower.find("italic") > -1 or sym_lower.find("slanted") > -1 or sym_lower.find("oblique") > -1 or sym_lower.find("narrow") > -1 :
            self.isTitleFont = False
            self.isBodyFont = False



    def __str__(self):
        rv = "Family: %s, Body: %s, Title: %s, File: %s, Encoding: %s, SymName: %s" %  (self.family, self.isBodyFont, self.isTitleFont, self.virtual_font_file, self.encoding, self.symbolic_name)
        return rv

class TTFMapFile:
    """
    This class encapsulate a pdfTeX map file. It exposes three properties:


    - map_path: the path file
    - map_file: the file name
    - map_lines: a list of TTFMapLine instances
    """
    def __init__(self,path):
        self.map_path = path
        self.map_file = os.path.basename(path)
        self.map_lines = []
        self.dict_lines={}
        self.dict_families={}
        self.body_fonts = []
        self.title_fonts=[]
        mf = open(path,"r")
        lines = mf.readlines()
        mf.close()
        for line in lines:
            line = line.replace("\n","").replace("\r","")
            if (line != '' and not line.startswith('%')):
                try:
                    mf = TTFMapLine(line)
                    self.map_lines.append(mf)
                    self.dict_lines[mf.symbolic_name] = mf
                    if mf.isBodyFont:
                        self.body_fonts.append(mf)
                    if mf.isTitleFont:
                        self.title_fonts.append(mf)
                    if not mf.family in self.dict_families:
                        lst_font = []
                        lst_font.append(mf)
                        self.dict_families[mf.family] = lst_font
                    else:
                        self.dict_families[mf.family].append(mf)
                except Exception as exc:
                    print "Error:  ", exc
                    pass

    def __str__ (self):
        rs = "Map File: %s\nMap Path: %s\nFile lines:\n" % (self.map_file, self.map_path)
        for l in self.map_lines:
            rs += str(l) +"\n"
        for l in self.dict_lines.keys():
            rs += "%s: %s\n" % (l, str(self.dict_lines[l]))
        k = self.dict_families.keys()
        k.sort()
        rs += "Families: "+ str(k) + "\n"
        return rs

    def create_typescript_list(self):
        result = []
        x,y=0,0
        for title_font in self.title_fonts:
            x+=1
            for body_font in self.body_fonts:
                y+=1
                ti = TypescriptItem()
                ti.symbolic_name = "font-%d-%d" % (x,y)
                ti.macro_family = "serif"
                ti.encoding = body_font.encoding
                ti.mass_add(body_font, title_font, None, None, None, None, None)
                result.append(ti)
        return result



class TypescriptItem:
    def __init__(self):
        self.symbolic_name = ""
        self.encoding = "texnansi"
        self.macro_family = "serif"
        self.typeface = None
        self.bold = None
        self.italic = None
        self.bold_italic = None
        self.slanted = None
        self.bold_slanted = None
        self.small_caps = None

    def mass_add(self,tf,bf,it,bi,sl,bs,sc):
        (self.typeface, self.bold, self.italic, self.bold_italic, self.slanted, self.bold_slanted, self.small_caps) = (tf,bf,it,bi,sl,bs,sc)

    def physical_typescript_line(self, weight, ttf_line):
        if (ttf_line != None):
            weight = weight.capitalize()
            name = self.symbolic_name.capitalize()
            mf = self.macro_family.capitalize()
            res = "\t\\definefontsynonym[%s%s%s][%s][encoding=%s]\n" % (name,mf,weight,ttf_line.virtual_font_file,self.encoding)
            return res
        else:
            return ""

    def physical_typescript(self):
        s = "\\starttypescript[%s][%s-%s][%s]\n" % (self.macro_family.lower(), self.symbolic_name.lower(), self.macro_family, self.encoding)
        s += self.physical_typescript_line("Regular", self.typeface)
        s += self.physical_typescript_line("Bold", self.bold)
        s += self.physical_typescript_line("BoldItalic", self.bold_italic)
        s += self.physical_typescript_line("Italic", self.italic)
        s += self.physical_typescript_line("Slanted", self.slanted)
        s += self.physical_typescript_line("Boldslanted", self.bold_slanted)
        s += self.physical_typescript_line("Caps", self.small_caps)
        s += "\t\\stoptypescript\n\n"
        return s

    def fallback_typescript_line(self, weight, ttf_line):
        if (ttf_line != None):
            mw = weight
            if (mw == "Regular"):
                mw = ""
            name = self.symbolic_name.capitalize()
            mf = self.macro_family.capitalize()
            res = "\t\\definefontsynonym[%s%s][%s%s%s]\n" % (mf,mw,name,mf, weight.capitalize())
            return res
        else:
            return ""

    def fallback_typescript(self):
        s = "\\starttypescript[%s][%s-%s][name]\n" % (self.macro_family.lower(), self.symbolic_name.lower(), self.macro_family)
        s+= "\t\\usetypescript[%s,fallback]\n" %(self.macro_family.lower())
        s += self.fallback_typescript_line("Regular", self.typeface)
        s += self.fallback_typescript_line("Bold", self.bold)
        s += self.fallback_typescript_line("BoldItalic", self.bold_italic)
        s += self.fallback_typescript_line("Italic", self.italic)
        s += self.fallback_typescript_line("Slanted", self.slanted)
        s += self.fallback_typescript_line("BoldSlanted", self.bold_slanted)
        s += self.fallback_typescript_line("Caps", self.small_caps)
        s += "\\stoptypescript\n\n"
        return s

    def typescript(self):
        return self.physical_typescript()+"\n"+self.fallback_typescript()

    def complete_typescript(self):
        s  = self.typescript()
        s += "\n\n\\starttypescript[ts-%s]\n" % (self.symbolic_name.lower())
        s+= "\t\\definetypeface[ts-%s][tt][%s][%s-%s][default][encoding=%s]\n" % \
            (self.symbolic_name.lower(), self.macro_family.lower(),
             self.symbolic_name.lower(),
             self.macro_family.lower(), self.encoding)
        s += "\\stoptypescript\n\n"
        return s

        pass

class Typescript:
    def __init__(self):
        self.typescript_name = ""
        self.serif = None
        self.sans = None
        self.mono = None

    def typescript(self):
        s = ""
        if (self.serif != None) :
            s += self.serif.typescript()
        if (self.sans != None) :
            s += self.sans.typescript()
        if (self.mono != None) :
            s += self.mono.typescript()
        s += "\n\n\\starttypescript[%s]\n" % (self.typescript_name)
        if (self.mono != None):
            s+= "\t\\definetypeface[%s][tt][mono][%s-%s][default][encoding=%s]\n" % \
                (self.typescript_name, self.mono.symbolic_name.lower(),
                 self.mono.macro_family.lower(), self.mono.encoding)
        if (self.sans != None):
            s+= "\t\\definetypeface[%s][ss][sans][%s-%s][default][encoding=%s]\n" % \
                (self.typescript_name, self.sans.symbolic_name.lower(),
                 self.sans.macro_family.lower(), self.sans.encoding)
        if (self.serif != None):
            s+= "\t\\definetypeface[%s][rm][serif][%s-%s][default][encoding=%s]\n" % \
                (self.typescript_name, self.serif.symbolic_name.lower(),
                 self.serif.macro_family.lower(), self.serif.encoding)
        s += "\\stoptypescript\n\n"
        return s

if __name__ == '__main__':
    c = TTFMapFile("C:/tex/share/texmf-local/fonts/map/pdftex/context/ec-softmaker-ttf-s.map")
    for ti in  c.create_typescript_list():
        print ti.complete_typescript()
