from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QPoint

from action.file_action import *
from action.edit_action import *

from canvas import Canvas

POSITION = QPoint(100, 100)
MIN_WIDTH = 600
MIN_HEIGHT = 600

class Window(QMainWindow):
    
    def __init__(self, app):
        super().__init__()
        self.app = app
        
        self.setup_window()
        self.setup_actions()
        self.setup_menu()
        self.setup_canvas()
        
        self.show()
    
    
    def setup_window(self):
        self.setWindowTitle("Terrible Text Editor")
        self.setGeometry(POSITION.x(), POSITION.y(), MIN_WIDTH, MIN_HEIGHT)
        self.setMinimumSize(MIN_WIDTH, MIN_HEIGHT)
        
        
    def setup_actions(self):
        
        self.new = NewAction("New", "CTRL+N", self)
        self.open = OpenAction("Open", "CTRL+O", self)
        self.save = SaveAction("Save", "CTRL+S", self)
        self.close = CloseAction("Close", "CTRL+W", self)
        self.quit = QuitAction("Quit", "CTRL+Q", self)
        
        self.undo = NewAction("Undo", "CTRL+Z", self)
        self.redo = NewAction("Redo", "CTRL+Y", self)
        self.cut = NewAction("Cut", "CTRL+X", self)
        self.copy = NewAction("Copy", "CTRL+C", self)
        self.paste = NewAction("Paste", "CTRL+V", self)
        
        
    def setup_menu(self):
        
        main_menu = self.menuBar()
        
        file_menu = main_menu.addMenu("&File")
        self.addActions(file_menu, [self.new, self.open, self.save])
        file_menu.addSeparator()
        self.addActions(file_menu, [self.close, self.quit])
        
        edit_menu = main_menu.addMenu("&Edit")
        self.addActions(edit_menu, [self.undo, self.redo])
        edit_menu.addSeparator()
        self.addActions(edit_menu, [self.cut, self.copy, self.paste])
   
    
    def addActions(self, menu, actions):
        for action in actions:
            menu.addAction(action)
    
    
    def setup_canvas(self):
        self.canvas = Canvas(self)
        self.setCentralWidget(self.canvas)