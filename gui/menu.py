from action.file_action import *
from action.edit_action import *

class Menu:
    
    def __init__(self, window):
        self.menuBar = window.menuBar()
        self.window = window
        
    def setActions(self):
        self.setFileActions()
        self.setEditActions()
    
    def setMenu(self):
        main_menu = self.menuBar
        self.setFileMenu(main_menu)
        self.setEditMenu(main_menu)
    
    def setFileActions(self):
        
        self.new = NewAction("New", "CTRL+N", self.window)
        self.open = OpenAction("Open", "CTRL+O", self.window)
        self.save = SaveAction("Save", "CTRL+S", self.window)
        self.close = CloseAction("Close", "CTRL+W", self.window)
        self.quit = QuitAction("Quit", "CTRL+Q", self.window)
    
    def setEditActions(self):
        
        self.undo = NewAction("Undo", "CTRL+Z", self.window)
        self.redo = NewAction("Redo", "CTRL+Y", self.window)
        self.cut = NewAction("Cut", "CTRL+X", self.window)
        self.copy = NewAction("Copy", "CTRL+C", self.window)
        self.paste = NewAction("Paste", "CTRL+V", self.window)
    
   
    def setFileMenu(self, main_menu):
        
        file_menu = main_menu.addMenu("&File")
        self.addActions(file_menu, [self.new, self.open, self.save])
        file_menu.addSeparator()
        self.addActions(file_menu, [self.close, self.quit])
    
    def setEditMenu(self, main_menu):
        
        edit_menu = main_menu.addMenu("&Edit")
        self.addActions(edit_menu, [self.undo, self.redo])
        edit_menu.addSeparator()
        self.addActions(edit_menu, [self.cut, self.copy, self.paste])
    
    def addActions(self, menu, actions):
        for action in actions:
            menu.addAction(action)