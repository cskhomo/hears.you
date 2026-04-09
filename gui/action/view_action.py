from action.action import Action

class ZoomInAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.zoom)
        
    def zoom(self):
        ...

class ZoomOutAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.zoom)
        
    def zoom(self):
        ...

class ZoomRestoreAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.restore)
        
    def restore(self):
        ...

class ToolsAction(Action):
    
    def __init__(self, name, window):
        super().__init__(name, window)
        self.triggered.connect(self.tools)
        
    def tools(self):
        ...


class StatusAction(Action):
    
    def __init__(self, name, window):
        super().__init__(name, window)
        self.triggered.connect(self.status)
        
    def status(self):
        ...