'''
Created on 13/dic/2011

@author: massi
'''

from PySide.QtCore import *
from PySide.QtGui import *
import TSFramework

class QTypescriptWidget(QWidget):
    '''
    classdocs
    '''
    
    tfPressed = Signal(object,object)
    bfPressed = Signal(object,object)
    itPressed = Signal(object,object)
    biPressed = Signal(object,object)
    slPressed = Signal(object,object)
    bsPressed = Signal(object,object)
    scPressed = Signal(object,object)    
    
    buttonPressed = Signal(object,object,object)
    
    def __init__(self,Parent=None):
        '''
        Constructor
        '''
        super(QTypescriptWidget,self).__init__(Parent)
        self.TF = None
        self.BF = None
        self.IT = None
        self.BI = None
        self.SL = None
        self.BS = None
        self.SC = None
        self.setupUI()
        
    def typescript(self):
        res = "";
        tiItem = TSFramework.Structures.TypescriptItem()
        tiItem.encoding = self.cboEncoding.currentText()
        tiItem.macro_family = self.cboMacroFamily.currentText()
        tiItem.symbolic_name = self.txtSynonymName.text()
        tiItem.mass_add(self.TF, self.BF, self.IT, self.BI, self.SL, self.BS, self.SC)
        return tiItem
        
        
    def setupUI(self):
        
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtSynonymName = QLineEdit(self)
        self.txtSynonymName.setObjectName("txtSynonymName")
        self.horizontalLayout.addWidget(self.txtSynonymName)
        self.label_2 = QLabel(self)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cboEncoding = QComboBox(self)
        self.cboEncoding.setEditable(True)
        self.cboEncoding.setObjectName("cboEncoding")
        self.cboEncoding.addItem("")
        self.cboEncoding.addItem("")
        self.cboEncoding.addItem("")        
        self.horizontalLayout.addWidget(self.cboEncoding)
        self.label_3 = QLabel(self)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.cboMacroFamily = QComboBox(self)
        self.cboMacroFamily.setEditable(True)
        self.cboMacroFamily.setObjectName("cboMacroFamily")
        self.cboMacroFamily.addItem("")
        self.cboMacroFamily.addItem("")
        self.cboMacroFamily.addItem("")        
        self.horizontalLayout.addWidget(self.cboMacroFamily)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnSetTF = QPushButton(self)
        self.btnSetTF.setObjectName("btnSetTF")
        self.gridLayout.addWidget(self.btnSetTF, 0, 0, 1, 1)
        self.btnSetBF = QPushButton(self)
        self.btnSetBF.setObjectName("btnSetBF")
        self.gridLayout.addWidget(self.btnSetBF, 1, 0, 1, 1)
        self.txtBF = QLineEdit(self)
        self.txtBF.setObjectName("txtBF")
        self.gridLayout.addWidget(self.txtBF, 1, 1, 1, 1)
        self.txtTF = QLineEdit(self)
        self.txtTF.setObjectName("txtTF")
        self.gridLayout.addWidget(self.txtTF, 0, 1, 1, 1)
        self.btnSetIT = QPushButton(self)
        self.btnSetIT.setObjectName("btnSetIT")
        self.gridLayout.addWidget(self.btnSetIT, 2, 0, 1, 1)
        self.txtIT = QLineEdit(self)
        self.txtIT.setObjectName("txtIT")
        self.gridLayout.addWidget(self.txtIT, 2, 1, 1, 1)
        self.btnSetBI = QPushButton(self)
        self.btnSetBI.setObjectName("btnSetBI")
        self.gridLayout.addWidget(self.btnSetBI, 3, 0, 1, 1)
        self.txtBI = QLineEdit(self)
        self.txtBI.setObjectName("txtBI")
        self.gridLayout.addWidget(self.txtBI, 3, 1, 1, 1)
        self.btnSetSL = QPushButton(self)
        self.btnSetSL.setObjectName("btnSetSL")
        self.gridLayout.addWidget(self.btnSetSL, 4, 0, 1, 1)
        self.txtSL = QLineEdit(self)
        self.txtSL.setObjectName("txtSL")
        self.gridLayout.addWidget(self.txtSL, 4, 1, 1, 1)
        self.btnSetBS = QPushButton(self)
        self.btnSetBS.setObjectName("btnSetBS")
        self.gridLayout.addWidget(self.btnSetBS, 5, 0, 1, 1)
        self.txtBS = QLineEdit(self)
        self.txtBS.setObjectName("txtBS")
        self.gridLayout.addWidget(self.txtBS, 5, 1, 1, 1)
        self.txtSC = QLineEdit(self)
        self.txtSC.setObjectName("txtSC")
        self.gridLayout.addWidget(self.txtSC, 6, 1, 1, 1)
        self.btnSetSC = QPushButton(self)
        self.btnSetSC.setObjectName("btnSetSC")
        self.gridLayout.addWidget(self.btnSetSC, 6, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QSpacerItem(20, 71, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label.setBuddy(self.txtSynonymName)
        self.label_2.setBuddy(self.cboEncoding)
        self.label_3.setBuddy(self.cboMacroFamily)

        self.retranslateUi()
        self.bindEvents()
        
    def retranslateUi(self):
        self.label.setText(QApplication.translate("TypescriptWidget", "Synonym &Name", None, QApplication.UnicodeUTF8))
        self.label_2.setText(QApplication.translate("TypescriptWidget", "&Encoding", None, QApplication.UnicodeUTF8))
        self.label_3.setText(QApplication.translate("TypescriptWidget", "&Macro family", None, QApplication.UnicodeUTF8))
        self.btnSetTF.setText(QApplication.translate("TypescriptWidget", "Regular", None, QApplication.UnicodeUTF8))
        self.btnSetBF.setText(QApplication.translate("TypescriptWidget", "Bold", None, QApplication.UnicodeUTF8))
        self.btnSetIT.setText(QApplication.translate("TypescriptWidget", "Italic", None, QApplication.UnicodeUTF8))
        self.btnSetBI.setText(QApplication.translate("TypescriptWidget", "Bold Italic", None, QApplication.UnicodeUTF8))
        self.btnSetSL.setText(QApplication.translate("TypescriptWidget", "Slanted", None, QApplication.UnicodeUTF8))
        self.btnSetBS.setText(QApplication.translate("TypescriptWidget", "Bold Slanted", None, QApplication.UnicodeUTF8))
        self.btnSetSC.setText(QApplication.translate("TypescriptWidget", "Small &Caps", None, QApplication.UnicodeUTF8))        
        self.cboEncoding.setItemText(0, QApplication.translate("TypescriptWidget", "texnansi", None, QApplication.UnicodeUTF8))
        self.cboEncoding.setItemText(1, QApplication.translate("TypescriptWidget", "ec", None, QApplication.UnicodeUTF8))
        self.cboEncoding.setItemText(2, QApplication.translate("TypescriptWidget", "cork", None, QApplication.UnicodeUTF8))
        self.cboMacroFamily.setItemText(0, QApplication.translate("TypescriptWidget", "serif", None, QApplication.UnicodeUTF8))
        self.cboMacroFamily.setItemText(1, QApplication.translate("TypescriptWidget", "sans", None, QApplication.UnicodeUTF8))
        self.cboMacroFamily.setItemText(2, QApplication.translate("TypescriptWidget", "mono", None, QApplication.UnicodeUTF8))
    
    
    def bindEvents(self):
        self.btnSetTF.clicked.connect(self._tfPressed)
        self.btnSetBF.clicked.connect(self._bfPressed)
        self.btnSetBI.clicked.connect(self._biPressed)
        self.btnSetIT.clicked.connect(self._itPressed)
        self.btnSetSL.clicked.connect(self._slPressed)
        self.btnSetBS.clicked.connect(self._bsPressed)
        self.btnSetSC.clicked.connect(self._scPressed)
        
    def _tfPressed(self):
        print "pressed TF"
        self.buttonPressed.emit(self,"TF", self.txtTF)
        pass
    
    def _bfPressed(self):
        print "pressed BF"
        self.buttonPressed.emit(self,"BF", self.txtBF)
        pass
        
    def _biPressed(self):
        print "pressed BI"
        self.buttonPressed.emit(self,"BI", self.txtBI)
        pass
        
    def _bsPressed(self):
        print "pressed BS"
        self.buttonPressed.emit(self,"BS", self.txtBS)
        pass
        
    def _itPressed(self):
        print "pressed IT"
        self.buttonPressed.emit(self,"IT", self.txtIT)
        pass
        
    def _slPressed(self):
        print "pressed SL"
        self.buttonPressed.emit(self,"SL", self.txtSL)
        pass
        
    def _scPressed(self):
        print "pressed SC"
        self.buttonPressed.emit(self,"SC", self.txtSC)
        pass
        
        