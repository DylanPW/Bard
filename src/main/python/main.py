from PyQt5.QtWidgets import *
import sys
import playlistParser as p
import bardcontroller
import window

if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    win = window.Window()    
    win.show()
    bardcontroller.BardController(view=win)    
    sys.exit(app.exec_())