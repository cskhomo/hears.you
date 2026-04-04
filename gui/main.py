from PyQt6.QtWidgets import QApplication
from main_window import MainWindow

from sys import argv
from sys import exit

def main():
    app = QApplication(argv)
    window = MainWindow()
    exit(app.exec())

if __name__ == "__main__":
    main()


# from sys import argv
# from sys import exit

# from PyQt6.QtWidgets import QMainWindow
# from PyQt6.QtWidgets import QToolBar
# from PyQt6.QtWidgets import QTextEdit
# from PyQt6.QtWidgets import QStatusBar
# from PyQt6.QtGui import QAction
# from PyQt6.QtGui import QIcon
# from PyQt6.QtWidgets import QApplication



# class MainWindow(QMainWindow):
    
    # def __init__(self, app):
        # super().__init__()

	# #icons file location
        
        # self.setWindowTitle("Hears")
        # self.setGeometry(100, 100, 600, 600)
        # self.setMinimumWidth(600)
        # self.setMinimumHeight(600)
  
        # menu = self.menuBar()
        # tools = QToolBar()
        # self.addToolBar(tools)
        # self.text_edit = QTextEdit(self)
        # self.setCentralWidget(self.text_edit)
        # self.status = QStatusBar()
        # self.setStatusBar(self.status)

        # file_menu = menu.addMenu("&File")

        # new_action = QAction(QIcon("./assets/icons/menu/new.png"),"New", self)
        # new_action.setShortcut("CTRL+N")
        # new_action.triggered.connect(self.new)
        # file_menu.addAction(new_action)

        # open_action = QAction(QIcon("./assets/icons/menu/open.png"), "Open", self)
        # open_action.setShortcut("CTRL+O")
        # open_action.triggered.connect(self.open)
        # file_menu.addAction(open_action)

        # save_action = QAction(QIcon("./assets/icons/menu/save.png"),"Save", self)
        # save_action.setShortcut("CTRL+S")
        # save_action.triggered.connect(self.save)
        # file_menu.addAction(save_action)

        # file_menu.addSeparator()

        # close_action = QAction(QIcon("./assets/icons/menu/close.png"),"Close", self)
        # close_action.setShortcut("CTRL+W")
        # close_action.triggered.connect(self.close)
        # file_menu.addAction(close_action)
        
        # quit_action = QAction(QIcon("./assets/icons/menu/quit.png"), "Quit", self)
        # quit_action.setShortcut("CTRL+Q")
        # quit_action.triggered.connect(self.quit)
        # file_menu.addAction(quit_action)


        # edit_menu = menu.addMenu("&Edit")

        # undo_action = QAction(QIcon("./assets/icons/menu/undo.png"),"Undo", self)
        # undo_action.setShortcut("CTRL+Z")
        # undo_action.triggered.connect(self.text_edit.undo)
        # edit_menu.addAction(undo_action)
        # tools.addAction(undo_action)

        # redo_action = QAction(QIcon("./assets/icons/menu/redo.png"),"Redo", self)
        # redo_action.setShortcut("CTRL+Y")
        # redo_action.triggered.connect(self.text_edit.redo)
        # edit_menu.addAction(redo_action)
        # tools.addAction(redo_action)

        # edit_menu.addSeparator()

        # cut_action = QAction(QIcon("./assets/icons/menu/cut.png"),"Cut", self)
        # cut_action.setShortcut("CTRL+X")
        # cut_action.triggered.connect(self.text_edit.cut)
        # edit_menu.addAction(cut_action)

        # copy_action = QAction(QIcon("./assets/icons/menu/copy.png"),"Copy", self)
        # copy_action.setShortcut("CTRL+C")
        # copy_action.triggered.connect(self.text_edit.copy)
        # edit_menu.addAction(copy_action)

        # paste_action = QAction(QIcon("./assets/icons/menu/paste.png"),"Paste", self)
        # paste_action.setShortcut("CTRL+V")
        # paste_action.triggered.connect(self.text_edit.paste)
        # edit_menu.addAction(paste_action)

        # self.show()
    
    # def new(self):
        # self.text_edit.clear()
        # self.status.showMessage("File Created")

    # def open(self):
        # self.text_edit.clear()
        # self.status.showMessage("File Opened")

    # def save(self):
        # self.status.showMessage("File Saved")
    
    # def close(self):
        # self.text_edit.clear()
        # self.status.showMessage("File Closed")

    # def quit(self):
        # self.destroy()
        # app.exit()
    
    
# if __name__ == "__main__":
    
    # app = QApplication(argv)
    # window = MainWindow(app)
    # exit(app.exec())