from PyQt5.QtWidgets import *
import sys
import playlistParser as p
import bardcontroller
import window
from fbs_runtime.application_context.PyQt5 import ApplicationContext

if __name__ == '__main__':
    appctxt = ApplicationContext()
    appctxt.app.setStyle('Fusion')
    win = window.Window()    
    win.show()
    bardcontroller.BardController(view=win)    
    sys.exit(appctxt.app.exec_())