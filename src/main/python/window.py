from PyQt5 import  QtGui
from PyQt5.QtWidgets import *
import sys
import playlistParser as p
from pathlib import Path

class Window(QMainWindow):
    ''' Main Window '''
    def __init__(self, parent=None):
        '''Initializer'''
        super().__init__(parent)
        # Setting icon
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle('Bard')
        self.setGeometry(200, 200, 500, 500)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)      
        self._centralWidget.setLayout(self.generalLayout) 
        self._createGroupBox()
        self._createStatusBar() 
        self._createWidgets()
        
    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Bard Playlist Copier v0.1")
        self.setStatusBar(status)

    def _createGroupBox(self):
        ''' create the groupbox '''
        self.GroupBox = QGroupBox(" ")        
        grouplayout = QGridLayout()
        # Playlist file related components
        grouplayout.addWidget(QLabel('Playlist Source: '), 0, 0, 1, 2)
        self.sourcefile = QLineEdit('')
        grouplayout.addWidget(self.sourcefile, 0, 2, 1, 7)
        self.opensourcebutton = QPushButton('Open')
        grouplayout.addWidget(self.opensourcebutton, 0, 9)

        # Preview of playlist contents
        self.previewlist = QListWidget()
        grouplayout.addWidget(self.previewlist, 1, 0, 6, 10)

        # Playlist destination components
        grouplayout.addWidget(QLabel('Destination Folder: '), 8, 0, 1, 2)
        self.destinationpath = QLineEdit('')
        grouplayout.addWidget(self.destinationpath, 8, 2, 1, 7)
        self.opendestinationbutton = QPushButton('Open')
        grouplayout.addWidget(self.opendestinationbutton, 8, 9)

        self.GroupBox.setLayout(grouplayout)

    def _createWidgets(self):
        '''Create the display'''        
        # Settings Controls     
        layout = QGridLayout()
        layout.addWidget(QLabel('<h1>Bard Playlist Copier</h1>'), 0, 0, 1, 14)
        layout.addWidget(self.GroupBox, 1, 0, 13, 14)
        self.copybutton = QPushButton('Copy!')
        layout.addWidget(self.copybutton, 15, 1, 1, 12)

        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(3702)

        layout.addWidget(self.progressBar, 14, 0, 1, 14)
        # Add to general layout
        self.generalLayout.addLayout(layout)

    def setSourceText(self, text):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Playlist", "", "Playlist Files (*.m3u)", options=options)
        if fileName:
            self.sourcefile.setText(fileName)

    def getSourceText(self):
        return self.sourcefile.text()

    def setDestinationText(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Destination")
        if folder:
            self.destinationpath.setText(folder)

    def getDestinationText(self):
        return self.destinationpath.text()

    def sourceTextChanged(self):   
        temp = self.getSourceText()     
        if (p.valid_m3u_playlist(temp)):
            playlist = p.load_m3u_playlist(temp)
            self.populatePreview(playlist)

    def populatePreview(self, playlist):
        self.previewlist.clear()
        for item in playlist:
            QListWidgetItem(item, self.previewlist)

    def updateProgressBar(self, currentval, maxval):
        pass

    def setStatusText(self, text):
        pass
        
    def copy(self):
        # Get the source and destination paths
        playlistpath = self.getSourceText()
        destinationpath = self.getDestinationText()
        relativepath = p.get_relpath(playlistpath)
        playlist = p.load_m3u_playlist(playlistpath)
        # Verify that the files do exist, and rebuild playlist.
        fullpath, playlist = p.verify_files(playlist, relativepath)
        p.create_folders(playlist, destinationpath)
        p.copy_playlist_file(playlistpath, destinationpath)

        for file in fullpath:
            p.copy_file(file, destinationpath, playlistpath)



