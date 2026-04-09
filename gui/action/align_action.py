from action.action import Action

class LeftAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.left)
        
    def left(self):
        ...

class CenterAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.center)
        
    def center(self):
        ...

class RightAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.right)
        
    def right(self):
        ...
