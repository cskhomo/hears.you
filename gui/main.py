from PyQt6.QtWidgets import QApplication
from window import Window

from sys import argv
from sys import exit

def main():
    app = QApplication(argv)
    window = Window(app)
    exit(app.exec())

if __name__ == "__main__":
    main()

# from PyQt6.QtWidgets import QStatusBar


	# #icons file location


        # self.status = QStatusBar()
        # self.setStatusBar(self.status)

        # QIcon("./assets/icons/menu/new.png")
        # QIcon("./assets/icons/menu/open.png")
        # QIcon("./assets/icons/menu/save.png")
        # QIcon("./assets/icons/menu/close.png")
        # QIcon("./assets/icons/menu/quit.png")
        # QIcon("./assets/icons/menu/redo.png")
        # (QIcon("./assets/icons/menu/cut.png")
        # QIcon("./assets/icons/menu/copy.png")
        # QIcon("./assets/icons/menu/paste.png")


        # self.status.showMessage("File Created")
        # self.status.showMessage("File Opened")
        # self.status.showMessage("File Saved")
        # self.status.showMessage("File Closed")