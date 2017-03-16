import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
w = QtGui.QWidget()
w.setWindowTitle('Fenetre simple')
w.show()
sys.exit(app.exec_())