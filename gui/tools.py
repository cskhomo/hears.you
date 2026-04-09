from PyQt6.QtWidgets import QToolBar

class Tools(QToolBar):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.window.addToolBar(self)
    
    def setTools(self):
        self.addAction(self.window.menu.export)
        self.addSeparator()

        self.addAction(self.window.menu.undo)
        self.addAction(self.window.menu.redo)
        self.addSeparator()
        
        self.addAction(self.window.menu.restore_zoom)
        self.addSeparator()

        self.addAction(self.window.menu.font)
        self.addAction(self.window.menu.size)
        self.addAction(self.window.menu.bold)
        self.addAction(self.window.menu.italic)
        self.addAction(self.window.menu.underline)
        self.addSeparator()

        self.addAction(self.window.menu.align_left)
        self.addAction(self.window.menu.align_center)
        self.addAction(self.window.menu.align_right)   