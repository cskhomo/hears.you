from action.action import Action

class UndoAction(Action):
    
    def __init__(self, name, shortcut, window):
        super().__init__(name, shortcut, window)
        self.triggered.connect(self.undo)
        
    def undo(self):
        self.window.canvas.undo()


class RedoAction(Action):
    
    def __init__(self, name, shortcut, window):
        super().__init__(name, shortcut, window)
        self.triggered.connect(self.redo)
        
    def redo(self):
        self.window.canvas.redo()
        

class CutAction(Action):
    
    def __init__(self, name, shortcut, window):
        super().__init__(name, shortcut, window)
        self.triggered.connect(self.cut)
        
    def cut(self):
        self.window.canvas.cut()
        
        
class CopyAction(Action):
    
    def __init__(self, name, shortcut, window):
        super().__init__(name, shortcut, window)
        self.triggered.connect(self.copy)
        
    def copy(self):
        self.window.canvas.copy()
        
        
class PasteAction(Action):
    
    def __init__(self, name, shortcut, window):
        super().__init__(name, shortcut, window)
        self.triggered.connect(self.paste)
        
    def paste(self):
        self.window.canvas.paste()