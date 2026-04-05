from PyQt6.QtGui import QAction

class Action(QAction):
    
    def __init__(self, name, shortcut, window):
        super().__init__(name)
        self.setShortcut(shortcut)
        self.window = window