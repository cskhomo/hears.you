from PyQt6.QtWidgets import QTextEdit

class Canvas(QTextEdit):
    
    def __init__(self, window):
        super().__init__()