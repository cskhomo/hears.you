from sys import argv
from sys import exit

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QTextEdit


from PyQt6.QtWidgets import QToolBar
from PyQt6.QtWidgets import QApplication


from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
    
        self.setWindowTitle("Hears")
        self.setGeometry(100, 100, 600, 600)
        self.show()
    
    
if __name__ == "__main__":
    
    app = QApplication(argv)
    window = MainWindow()
    exit(app.exec())