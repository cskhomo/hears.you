from action.action import Action

class FontAction(Action):
    
    def __init__(self, name, window):
        super().__init__(name, window)
        self.triggered.connect(self.font)
        
    def font(self):
        ...

class SizeAction(Action):
    
    def __init__(self, name, window):
        super().__init__(name, window)
        self.triggered.connect(self.size)
        
    def size(self):
        ...

class BoldAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.bold)
        
    def bold(self):
        ...

class ItalicAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.italic)
        
    def italic(self):
        ...


class UnderlineAction(Action):
    
    def __init__(self, name, window, shortcut):
        super().__init__(name, window, shortcut)
        self.triggered.connect(self.underline)
        
    def underline(self):
        ...