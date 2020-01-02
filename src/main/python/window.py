from PyQt5 import  QtGui
from PyQt5.QtWidgets import *
import sys
import playlistParser as p
import pathExist as pe
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
        self.status = QStatusBar()
        self.status.showMessage("Bard Playlist Copier v0.1")
        self.setStatusBar(self.status)

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
        self.progressBar.setValue(0)

        layout.addWidget(self.progressBar, 14, 0, 1, 14)
        # Add to general layout
        self.generalLayout.addLayout(layout)

    def setSourceText(self, text):
        ''' set the source file text contents '''
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Playlist", "", "Playlist Files (*.m3u)", options=options)
        if fileName:
            self.sourcefile.setText(fileName)

    def getSourceText(self):
        ''' return the content of the sourcefile contents '''
        return self.sourcefile.text()

    def setDestinationText(self):
        ''' set the destination folder text''' 
        folder = QFileDialog.getExistingDirectory(self, "Select Destination")
        if folder:
            self.destinationpath.setText(folder)

    def getDestinationText(self):
        ''' return the content of the destination path lineedit '''
        return self.destinationpath.text()

    def sourceTextChanged(self):   
        ''' attempt to preview the playlist file contents on source
            text being changed '''
        temp = self.getSourceText()
        self.previewlist.clear()     
        if (p.valid_m3u_playlist(temp)):
            playlist = p.load_m3u_playlist(temp)
            self.populatePreview(playlist)

    def populatePreview(self, playlist):
        ''' populate the preview contents with the given list of files '''
        for item in playlist:
            QListWidgetItem(item, self.previewlist)

    def updateProgressBar(self, currentval, maxval):
        ''' update the progress bar value '''
        self.progressBar.setMaximum(maxval)
        self.progressBar.setValue(currentval)

    def setStatusText(self, text):
        ''' set the statusbar message '''
        self.status.showMessage(text)

    def validateInputs(self):
        ''' validate that the playlist is a valid file and that the directory is a valid path '''
        if (p.valid_m3u_playlist(self.getSourceText()) and pe.does_path_exist_or_creatable(self.getDestinationText())):
            return True
        return False
        
    def copy(self):
        if (self.validateInputs() == True):
            ''' copy files to the destination directory '''
            # Get the source and destination paths
            playlistpath = self.getSourceText()
            destinationpath = self.getDestinationText()
            relativepath = p.get_relpath(playlistpath)
            playlist = p.load_m3u_playlist(playlistpath)
            
            self.setStatusText("Loading playlist " + p.output_filename(playlistpath) + "...")
            # Verify that the files do exist, and rebuild playlist.
            fullpath, playlist = p.verify_files(playlist, relativepath)
            self.setStatusText("Verifying playlist...")
            p.create_folders(playlist, destinationpath)
            self.setStatusText("Creating folders...")
            p.copy_playlist_file(playlistpath, destinationpath)
            self.setStatusText("Copying playlist file...")

            maxval = len(fullpath)
            counter = 1
            for file in fullpath:
                self.updateProgressBar(counter, maxval)
                self.setStatusText("Copying file " + p.output_filename(file) + "...")
                p.copy_file(file, destinationpath, playlistpath)
                counter += 1
            
            self.setStatusText("Done!")
        else: 
            pass


