from PyQt6.QtGui import QAction

class Action(QAction):
    
    def __init__(self, name, window, shortcut=""):
        super().__init__(name)
        
        self.window = window
        if shortcut: self.setShortcut(shortcut)