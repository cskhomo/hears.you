from PyQt6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setup_window()
        self.show()
    
    def setup_window(self):
        
        self.setWindowTitle("Terrible Text Editor")
        self.setGeometry(100, 100, 600, 600)
        self.setMinimumWidth(600)
        self.setMinimumHeight(600)