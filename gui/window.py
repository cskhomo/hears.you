from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QToolBar

from menu import Menu
from tools import Tools
from canvas import Canvas

POSITION = QPoint(100, 100)
MIN_WIDTH = 600
MIN_HEIGHT = 600

class Window(QMainWindow):
    
    def __init__(self, app):
        super().__init__()
        self.app = app
        
        self.setup_window()
        self.setup_menu()
        self.setup_tools()
        self.setup_canvas()
        
        self.show()
    
    def setup_window(self):
        self.setWindowTitle("Terrible Text Editor")
        self.setGeometry(POSITION.x(), POSITION.y(), MIN_WIDTH, MIN_HEIGHT)
        self.setMinimumSize(MIN_WIDTH, MIN_HEIGHT)
            
    def setup_menu(self):
       self.menu = Menu(self)
       self.menu.setActions()
       self.menu.setMenu()

    def setup_tools(self):
        self.tools = Tools(self)
        self.tools.setTools()
    
    def setup_canvas(self):
        self.canvas = Canvas(self)
        self.setCentralWidget(self.canvas)