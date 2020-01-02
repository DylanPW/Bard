from functools import partial

class BardController:
    '''Bard Controller Class'''
    def __init__(self, view):
        self._view = view
        self._connectSignals()
    
    def _connectSignals(self):
        self._view.opensourcebutton.clicked.connect(self._view.setSourceText)
        self._view.opendestinationbutton.clicked.connect(self._view.setDestinationText)
        self._view.sourcefile.textChanged.connect(self._view.sourceTextChanged)
        self._view.copybutton.clicked.connect(self._view.copy)