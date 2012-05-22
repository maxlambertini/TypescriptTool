'''
Created on 13/dic/2011

@author: massi
'''
from PySide.QtCore import *
from PySide.QtGui import *
from TSFramework.Widgets.TSMainWindow import QTSMainWindow


if __name__ == '__main__':

    import sys\

    app = QApplication(sys.argv)
    print QDir.currentPath()
    print QDir.homePath()


    mainWin = QTSMainWindow()
    mainWin.setWindowTitle("Typescript Tool")
    mainWin.show()
    sys.exit(app.exec_())
