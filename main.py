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
        
        self.setWindowTitle("Hears")
        self.setGeometry(100, 100, 600, 600)
        
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        edit_menu = menu.addMenu("&Edit")
        
        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addAction("Exit", self.destroy)

        undo_action = QAction("Undo", self)
        undo_action.setShortcut("CTRL+Z")
        undo_action.triggered.connect(self.text_edit.undo)
        edit_menu.addAction(undo_action)

        redo_action = QAction("Redo", self)
        redo_action.setShortcut("CTRL+Y")
        redo_action.triggered.connect(self.text_edit.redo)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()

        cut_action = QAction("Cut", self)
        cut_action.setShortcut("CTRL+X")
        cut_action.triggered.connect(self.text_edit.cut)
        edit_menu.addAction(cut_action)

        copy_action = QAction("Copy", self)
        copy_action.setShortcut("CTRL+C")
        copy_action.triggered.connect(self.text_edit.copy)
        edit_menu.addAction(copy_action)

        paste_action = QAction("Paste", self)
        paste_action.setShortcut("CTRL+V")
        paste_action.triggered.connect(self.text_edit.paste)
        edit_menu.addAction(paste_action)

        self.show()
    
    
if __name__ == "__main__":
    
    app = QApplication(argv)
    window = MainWindow()
    exit(app.exec())