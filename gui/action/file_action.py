from action.action import Action

class NewAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.new)
        
    def new(self):
        self.window.canvas.clear()
 

class OpenAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.open)
        
    def open(self):
        self.window.canvas.clear()
        
        
class SaveAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.save)
        
    def save(self):
        ...
        
        
class CloseAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.close)
        
    def close(self):
        self.window.canvas.clear()
        
        
class QuitAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.quit)
        
    def quit(self):
        self.window.canvas.destroy()
        self.window.app.exit()


class SaveAsAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.save_as)
        
    def save_as(self):
        ...


class ExportAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.export)
        
    def export(self):
        ...