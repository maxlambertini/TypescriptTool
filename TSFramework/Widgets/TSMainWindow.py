# -*- coding: utf-8 -*-
from PySide.QtCore import *
from PySide.QtGui import *
from TSFramework.Widgets import *
import TSFramework.Structures
import TSFramework
from TSFramework.Widgets.QTypescriptItemWidget import QTypescriptWidget


TEX_TEMPLATE = u"""
\\setupfontsynonym[Sans][handling=highquality]
\\setupfontsynonym[SansBold][handling=highquality]
\\setupfontsynonym[SansItalic][handling=highquality]
\\setupfontsynonym[SansBoldItalic][handling=highquality]
\\setupfontsynonym[SansSlanted][handling=highquality]
\\setupfontsynonym[SansBoldSlanted][handling=highquality]
\\setupfontsynonym[SansSmallCaps][handling=highquality]
\\setupfontsynonym[Serif][handling=highquality]
\\setupfontsynonym[SerifBold][handling=highquality]
\\setupfontsynonym[SerifItalic][handling=highquality]
\\setupfontsynonym[SerifBoldItalic][handling=highquality]
\\setupfontsynonym[SerifSlanted][handling=highquality]
\\setupfontsynonym[SerifBoldSlanted][handling=highquality]
\\setupfontsynonym[SerifSmallCaps][handling=highquality]
\\setupfontsynonym[Mono][handling=highquality]
\\setupfontsynonym[MonoBold][handling=highquality]
\\setupfontsynonym[MonoItalic][handling=highquality]
\\setupfontsynonym[MonoBoldItalic][handling=highquality]
\\setupfontsynonym[MonoSlanted][handling=highquality]
\\setupfontsynonym[MonoBoldSlanted][handling=highquality]
\\setupfontsynonym[MonoSmallCaps][handling=highquality]

\\setupfonthandling[hz][min=0, max=90, step=5]
\\setupalign[hanging,hz,spacing]
\\setupinterlinespace
[height=.72,
depth=.28,
top=1.0,
bottom=0.4,
line=3ex]


\\setuphead[chapter] % equivalente a H1
[
    align={center,nothyphenated,strict},
    style={\\tfd},
    after={\\blank[4*line]},
    page=yes,
    continue=no
]

\\setuphead[subject] % equivalente a H2
[
    align={flushleft, nothyphenated, verytolerant},
    after={\\blank[6pt]},
    before={\\blank[6pt]},
    style=\\tfc % da notare che uso il font definito con \\font\\eulb pi� sopra.
]


\\setuphead[subsubsubject] % equivalente a H3
[
    align={flushleft, nothyphenated, verytolerant},
    before={\\blank[6pt]},
    after={\\blank[4pt]},
    style=\\tfb
]

%---------------- page size, spacing ------------------------------
\\setuppapersize[a4][a4] % this is default and may be omitted


\\setuplayout
[leftmargin=10mm,
rightmargin=10mm,
leftmargindistance=5mm,
rightmargindistance=5mm,
backspace=20mm,
cutspace=20mm,
header=5mm,
footer=7mm,
height=middle,
topspace=8mm,
bottomspace=10mm,
width=middle]
\\setuppagenumbering[location=right,style=\\tfxx]


\\def\\SpecimenLine#1#2#3#4#5#6
{
\\switchtobodyfont[rm,9pt]
\\setupinterlinespace[line=9pt]
\\vskip 1mm
\\hairline
{\\tt #5 #3}
\\vskip 1mm
\\switchtobodyfont[#1,#2,#3]
\\setupinterlinespace[height=.72,
depth=.28,
top=1.0,
bottom=0.4,
line=3.5em]
#4
#6
\\switchtobodyfont[rm,9pt]
\\setupinterlinespace[line=9pt]
\\tt
\\par
}

\\def\\SpecimenPage#1#2#3#4{\\bgroup
\\SpecimenLine{#1}{#2}{72pt}{#3}{#4}{Watson?}
\\SpecimenLine{#1}{#2}{48pt}{#3}{#4}{you excel yourself!}
\\SpecimenLine{#1}{#2}{36pt}{#3}{#4}{\\& said H\\"olme\\cc  , p\\"u\\${\\.h}in\\.g b\\aa c\\=k  h\\=\\i s 22 chairs}
\\SpecimenLine{#1}{#2}{24pt}{#3}{#4}{and l\\'ight\\`ing \\`a {\\k c}ig{\\d a}re{\\=t}te. -- I am b\\`o\\`und t\\~o s\\^ay that i\\~n all the ac\\cc ounts }
\\SpecimenLine{#1}{#2}{18pt}{#3}{#4}{which you have been so good as to give of my own
small achievements you have habitually underrated your own
abilities. }
\\hairline
\\vskip 3mm
\\startcolumns[n=2]
\\SpecimenLine{#1}{#2}{14pt}{#3}{#4}{It may be that you are not flowing fine, but you
are affably of light. Some people without possessing genius
have a remarkable power of stimulating it.}
\\SpecimenLine{#1}{#2}{12pt}{#3}{#4}{He had never said as much before, and I must admit that his words
gave me keen pleasure, for I had often been piqued by his
indifference to my admiration and to the attempts which I had
made to give publicity to his methods.}
\\SpecimenLine{#1}{#2}{10pt}{#3}{#4}{I was proud, too, to think
that I had so far mastered his system as to apply it in a way
which earned his approval. He now took the stick from my hands
and examined it for a few minutes}
\\stopcolumns
\\hairline
\\switchtobodyfont[#1,#2,9pt]
#3
\\parindent=6pt
\\startcolumns[n=3]
\\baselineskip=12pt
\\setuplayout[grid=yes]
``Ask Jeff'' or `Ask Jeff'. Take the chef d'\\oe uvre! Two of [of] (of) `of' ``of'' of? of! of*. Ydes, Yffignac and Ygrande are in France: so are Ypres, Les W\\"oevres, the F\\^oret de W\\oe vres, the Voire and Vauvise. Yves is in heaven; D'Amboise is in jail. Lyford's in Texas \\& L'Anse-aux-Griffons in Qu\\'ebec; Yriarte, Yciar and Ysa\\"ye are at Yale. Kyoto and Ryotsu are both in Japan, Kwikpak on the Yukon Delta, Kv\\ae ven in Norway, Kyulu in Kenya, not in Rwanda.
\\par
Walton's in West Virginia, but Wren's in Oregon. Tl\\'alpan is near Xochimilco in M\\'exico, the Zygos and Zylophagou are in Cyprus, Zwettl in Austria, F\\ae no in Denmark, V\\ae roy in Norway. Tchula is in Mississippi, the Tittabawassee in Michigan. Twodot is here in Montana, Ywamun in Burma. Yggddrasil and Ymir, Yngvi and V\\'oden, V\\'idrio and Skeggj\\"old and T{\\'y}r are all in the Eddas. Ktipas and Tmolos in Greece, but V\\'azquez is in Argentina. Vdovino in Russia. Is Toussaint L'Ouverture here?
\\stopcolumns
\\setuplayout[grid=no]
\\parindent=0pt
\\page
\\egroup}

\\def\\SpecimenFamily#1#2#3{
    \\SpecimenPage{#1}{#2}{\\tf}{#3 Regular}
    \\SpecimenPage{#1}{#2}{\\bf}{#3 BoldFace}
    \\SpecimenPage{#1}{#2}{\\it}{#3 Italic}
    \\SpecimenPage{#1}{#2}{\\bi}{#3 BoldItalic}
    \\SpecimenPage{#1}{#2}{\\sl}{#3 Slanted}
    \\SpecimenPage{#1}{#2}{\\bs}{#3 BoldSlanted}
    \\SpecimenPage{#1}{#2}{\\sc}{#3 SmallCaps}
}

\\def\\DemoBlockItem#1{
\\startcolumns[n=3]
\\vskip 1em
\\startalignment[flushright]
{#1 The Shape Of The Things To Come}
\\stopalignment
\\blank
``Ask Jeff'' or `Ask Jeff'. Take the chef d'\\oe uvre! Two of [of] (of) `of' ``of'' of? of! of*. Ydes, Yffignac and Ygrande are in France: so are Ypres, Les W\\"oevres, the F\\^oret de W\\oe vres, the Voire and Vauvise. Yves is in heaven; D'Amboise is in jail. Lyford's in Texas \\& L'Anse-aux-Griffons in Qu\\'ebec; Yriarte, Yciar and Ysa\\"ye are at Yale. Kyoto and Ryotsu are both in Japan, Kwikpak on the Yukon Delta, Kv\\ae ven in Norway, Kyulu in Kenya, not in Rwanda.
\\par
Walton's in West Virginia, but Wren's in Oregon. Tl\\'alpan is near Xochimilco in M\\'exico, the Zygos and Zylophagou are in Cyprus, Zwettl in Austria, F\\ae no in Denmark, V\\ae roy in Norway. Tchula is in Mississippi, the Tittabawassee in Michigan. Twodot is here in Montana, Ywamun in Burma. Yggddrasil and Ymir, Yngvi and V\\'oden, V\\'idrio and Skeggj\\"old and T{\\'y}r are all in the Eddas. Ktipas and Tmolos in Greece, but V\\'azquez is in Argentina. Vdovino in Russia. Is Toussaint L'Ouverture here?
\\stopcolumns
\\vskip 2em
}

\\def\\DemoBlockFamily#1{
\\switchtobodyfont[#1,9pt]
\\DemoBlockItem{\\tfd}
\\DemoBlockItem{\\bfd}
\\DemoBlockItem{\\itd}
\\DemoBlockItem{\\bid}
\\DemoBlockItem{\\sld}
\\DemoBlockItem{\\bsd}
\\DemoBlockItem{\\scd}
}


\\starttext

"""

class QTSMainWindow(QMainWindow):

    def __init__(self):
        super(QTSMainWindow, self).__init__()
        self.setupUI()
        self.retranslateUi()
        self.connect_signals_slot()

        self.map_files = {}
        self.current_map_fonts = {}


    def setupUI(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QSplitter(self.splitter_2)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QSize(150, 0))
        self.splitter.setMaximumSize(QSize(400, 16777215))
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lstMapFiles = QListWidget(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstMapFiles.sizePolicy().hasHeightForWidth())
        self.lstMapFiles.setSizePolicy(sizePolicy)
        self.lstMapFiles.setObjectName("lstMapFiles")
        self.verticalLayout.addWidget(self.lstMapFiles)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QLabel(self.widget1)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lstFont = QListWidget(self.widget1)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstFont.sizePolicy().hasHeightForWidth())
        self.lstFont.setSizePolicy(sizePolicy)
        self.lstFont.setObjectName("lstFont")
        self.verticalLayout_2.addWidget(self.lstFont)
        self.widget2 = QWidget(self.splitter_2)
        self.widget2.setObjectName("widget2")
        self.verticalLayout_6 = QVBoxLayout(self.widget2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit = QLineEdit(self.widget2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.btnGenerate = QPushButton(self.widget2)
        self.btnGenerate.setObjectName("btnGenerate")
        self.horizontalLayout.addWidget(self.btnGenerate)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.tabWidget = QTabWidget(self.widget2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.tswSerif = QTypescriptWidget(self.tab)
        self.tswSerif.setObjectName("tswSerif")
        self.verticalLayout_3.addWidget(self.tswSerif)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.tswSans = QTypescriptWidget(self.tab_2)
        self.tswSans.setObjectName("tswSans")
        self.verticalLayout_4.addWidget(self.tswSans)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.tswMono = QTypescriptWidget(self.tab_3)
        self.tswMono.setObjectName("tswMono")
        self.horizontalLayout_2.addWidget(self.tswMono)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_5 = QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.txtTexResult = QTextEdit(self.tab_4)
        self.txtTexResult.setObjectName("txtTexResult")
        self.verticalLayout_5.addWidget(self.txtTexResult)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.horizontalLayout_3.addWidget(self.splitter_2)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.action_Load_Map_File = QAction(self)
        self.action_Load_Map_File.setObjectName("action_Load_Map_File")
        self.actionE_xit = QAction(self)
        self.actionE_xit.setObjectName("actionE_xit")
        self.menu_File.addAction(self.action_Load_Map_File)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionE_xit)
        self.menubar.addAction(self.menu_File.menuAction())
        self.tabWidget.setCurrentIndex(0)


        pass

    def retranslateUi(self):
        self.setWindowTitle(QApplication.translate("TypescriptMainWindow", "MainWindow", None, QApplication.UnicodeUTF8))
        self.label.setText(QApplication.translate("TypescriptMainWindow", "Map Files", None, QApplication.UnicodeUTF8))
        self.label_2.setText(QApplication.translate("TypescriptMainWindow", "Fonts", None, QApplication.UnicodeUTF8))
        self.label_3.setText(QApplication.translate("TypescriptMainWindow", "TextLabel", None, QApplication.UnicodeUTF8))
        self.btnGenerate.setText(QApplication.translate("TypescriptMainWindow", "Generate Typescript", None, QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QApplication.translate("TypescriptMainWindow", "Serif", None, QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QApplication.translate("TypescriptMainWindow", "Sans", None, QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QApplication.translate("TypescriptMainWindow", "Mono", None, QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QApplication.translate("TypescriptMainWindow", "TeX Result", None, QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QApplication.translate("TypescriptMainWindow", "&File", None, QApplication.UnicodeUTF8))
        self.action_Load_Map_File.setText(QApplication.translate("TypescriptMainWindow", "&Load Map File", None, QApplication.UnicodeUTF8))
        self.actionE_xit.setText(QApplication.translate("TypescriptMainWindow", "E&xit", None, QApplication.UnicodeUTF8))

    def connect_signals_slot(self):
        self.action_Load_Map_File.triggered.connect(self.on_action_load_map_file)
        self.actionE_xit.triggered.connect(self.on_exit)
        self.lstMapFiles.currentItemChanged.connect(self.on_lst_map_files_current_item_changed)
        self.lstFont.currentItemChanged.connect(self.on_lst_font_current_item_changed)
        self.tswSans.buttonPressed.connect(self.on_typescripteditor_pressed)
        self.tswSerif.buttonPressed.connect(self.on_typescripteditor_pressed)
        self.tswMono.buttonPressed.connect(self.on_typescripteditor_pressed)
        self.btnGenerate.clicked.connect(self.on_generate_typescript)
        pass

    def on_generate_typescript(self):

        txt = ""
        for h in range(0, self.lstMapFiles.count()):
            i = self.lstMapFiles.item(h)
            txt += "\\loadmapfile[%s]\n" % (i.text())
        txt += "\n\n"


        ts = TSFramework.Structures.Typescript()
        ts.typescript_name = self.lineEdit.text()
        if (ts.typescript_name == "" ):
            ts.typescript_name = "ff-pytype"
        ts.mono = self.tswMono.typescript()
        ts.serif = self.tswSerif.typescript()
        ts.sans = self.tswSans.typescript()

        txt += "\n\n"+ts.typescript()+"\n\n" + "\\usetypescript[%s]\n\\setupbodyfont[%s,rm,10pt]\n\n" % (ts.typescript_name,ts.typescript_name)
        txt += TEX_TEMPLATE
        txt += "\n\\SpecimenFamily{%s}{rm}{%s}\n" % (ts.typescript_name,self.tswSerif.typescript().symbolic_name)
        txt += "\n\\SpecimenFamily{%s}{ss}{%s}\n" % (ts.typescript_name,self.tswSans.typescript().symbolic_name)
        txt += "\n\\SpecimenFamily{%s}{tt}{%s}\n" % (ts.typescript_name,self.tswMono.typescript().symbolic_name)
        txt += "\n\\DemoBlockFamily{rm}\n"
        txt += "\n\\DemoBlockFamily{ss}\n"
        txt += "\n\\DemoBlockFamily{tt}\n"
        txt += "\n\\stoptext\n"
        self.txtTexResult.setPlainText(txt)
        pass

    def on_typescripteditor_pressed(self,tswWidget,tswFontItem, tswEdit):
        current_item = self.lstFont.currentItem()
        print tswFontItem
        if (current_item is not None):
            txt = self.lstFont.currentItem().text()
            map_line = self.current_map_fonts[txt]
            if tswFontItem == "TF":
                tswWidget.TF = map_line
            elif tswFontItem == "BF":
                tswWidget.BF = map_line
            elif tswFontItem == "BI":
                tswWidget.BI = map_line
            elif tswFontItem == "BS":
                tswWidget.BS = map_line
            elif tswFontItem == "IT":
                tswWidget.IT = map_line
            elif tswFontItem == "SC":
                tswWidget.SC = map_line
            elif tswFontItem == "SL":
                tswWidget.SL = map_line
            tswFontItem = map_line
            tswEdit.setText(map_line.virtual_font_file)
        pass

    def on_lst_font_current_item_changed(self,current,previous):
        print "current font item changed", current.text()

        pass

    def on_lst_map_files_current_item_changed(self,current,previous):
        print "current map item changed"
        txt_file = current.text()
        map_lines = self.map_files[txt_file].map_lines
        self.current_map_fonts.clear()
        for map_line in map_lines:
            self.current_map_fonts[map_line.symbolic_name] = map_line
        self.lstFont.clear()
        my_keys = self.current_map_fonts.keys()
        my_keys.sort()
        for f in my_keys:
            self.lstFont.addItem(str(f))
        pass

    def on_action_load_map_file(self):
        print "load map file"
        try:
            (filename, mask) = QFileDialog.getOpenFileName(self,
                                               "Load Map File",
                                                "C:\\tex\\share\\texmf-local\\fonts\\map\\pdftex\\context",
                                               "TeX font map files (*.map)")
            if filename is not None or filename != "":
                print "Load map  from ", filename
                map_file = TSFramework.Structures.TTFMapFile(filename)
                print map_file
                if not map_file.map_file in self.map_files:
                    self.map_files[map_file.map_file] = map_file
                    self.lstMapFiles.addItem(map_file.map_file)
                    self.lstFont.clear()
        except Exception as exc:
            print "an error has occurred: ", exc
            pass

    def on_exit(self):
        print "exit"
        exit()
        pass

