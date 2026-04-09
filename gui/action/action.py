from PyQt6.QtGui import QAction
from PyQt6.QtGui import QIcon

class Action(QAction):
    
    def __init__(self, name, window, shortcut=""):
        super().__init__(name)
        
        self.window = window
        if shortcut: self.setShortcut(shortcut)

        try:
            self.setIcon(QIcon(f"./assets/icons/menu/{name.lower()}.png"))
        except:
            pass