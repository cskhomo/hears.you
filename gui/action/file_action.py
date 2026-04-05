from action.action import Action

class NewAction(Action):
    
    def __init__(self, name, shortcut, window):
        super().__init__(name, shortcut, window)
        self.triggered.connect(self.new)
        
    def new(self):
        self.window.canvas.clear()
 

class OpenAction(Action):
    
    def __init__(self, name, shortcut, window):
        super().__init__(name, shortcut, window)
        self.triggered.connect(self.open)
        
    def open(self):
        self.window.canvas.clear()
        
        
class SaveAction(Action):
    
    def __init__(self, name, shortcut, window):
        super().__init__(name, shortcut, window)
        self.triggered.connect(self.save)
        
    def save(self):
        ...
        
        
class CloseAction(Action):
    
    def __init__(self, name, shortcut, window):
        super().__init__(name, shortcut, window)
        self.triggered.connect(self.close)
        
    def close(self):
        self.window.canvas.clear()
        
        
class QuitAction(Action):
    
    def __init__(self, name, shortcut, window):
        super().__init__(name, shortcut, window)
        self.triggered.connect(self.quit)
        
    def quit(self):
        self.window.canvas.destroy()
        self.window.app.exit()