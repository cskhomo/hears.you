from action.file_action import *
from action.edit_action import *
from action.view_action import *
from action.text_action import *
from action.align_action import *

class Menu:
    
    def __init__(self, window):
        self.menuBar = window.menuBar()
        self.window = window


    def setMenu(self):

        main_menu = self.menuBar

        self.setFileMenu(main_menu)
        self.setEditMenu(main_menu)
        self.setViewMenu(main_menu)
        self.setTextMenu(main_menu)
        self.setAlignMenu(main_menu)


    def setActions(self):

        self.setFileActions()
        self.setEditActions()
        self.setViewActions()
        self.setTextActions()
        self.setAlignActions()


    def setFileMenu(self, main_menu):
        
        file_menu = main_menu.addMenu("&File")

        self.addActions(file_menu, [self.new, self.open])
        file_menu.addSeparator()

        self.addActions(file_menu, [self.save, self.save_as, self.export])
        file_menu.addSeparator()

        self.addActions(file_menu, [self.close, self.quit])


    def setEditMenu(self, main_menu):
        
        edit_menu = main_menu.addMenu("&Edit")

        self.addActions(edit_menu, [self.undo, self.redo])
        edit_menu.addSeparator()

        self.addActions(edit_menu, [self.cut, self.copy, self.paste])
    

    def setViewMenu(self, main_menu):

        view_menu = main_menu.addMenu("&View")

        self.addActions(view_menu, [self.zoom_in, self.zoom_out, self.restore_zoom])
        view_menu.addSeparator()

        self.addActions(view_menu, [self.toggle_tools, self.toggle_status])
    

    def setTextMenu(self, main_menu):

        text_menu = main_menu.addMenu("&Text")

        self.addActions(text_menu, [self.font, self.size])
        text_menu.addSeparator()

        self.addActions(text_menu, [self.bold, self.italic, self.underline])


    def setAlignMenu(self, main_menu):

        align_menu = main_menu.addMenu("&Align")
        self.addActions(align_menu, [self.align_left, self.align_right, self.align_center])


    def setFileActions(self):
        
        self.new = NewAction("New", self.window, "CTRL+N")
        self.open = OpenAction("Open", self.window, "CTRL+O")
        self.save = SaveAction("Save", self.window, "CTRL+S")
        self.save_as = SaveAsAction("Save As", self.window, "CTRL+SHIFT+S")
        self.export = ExportAction("Export", self.window, "CTRL+E")
        self.close = CloseAction("Close", self.window, "CTRL+W")
        self.quit = QuitAction("Quit", self.window, "CTRL+Q")


    def setEditActions(self):
        
        self.undo = UndoAction("Undo", self.window, "CTRL+Z")
        self.redo = RedoAction("Redo", self.window, "CTRL+Y")
        self.cut = CutAction("Cut", self.window, "CTRL+X")
        self.copy = CopyAction("Copy", self.window, "CTRL+C")
        self.paste = PasteAction("Paste", self.window, "CTRL+V")
    

    def setViewActions(self):
        
        self.zoom_in = ZoomInAction("Zoom In", self.window, "CTRL+=")
        self.zoom_out = ZoomOutAction("Zoom Out", self.window, "CTRL+-")
        self.restore_zoom = ZoomRestoreAction("Restore Zoom", self.window, "CTRL+0")
        self.toggle_tools = ToolsAction("Show Toolbar", self.window)
        self.toggle_status = StatusAction("Show Status Bar", self.window)


    def setTextActions(self):
        
        self.font = FontAction("Font Selection", self.window)
        self.size = SizeAction("Font Size", self.window)
        self.bold = BoldAction("Bold", self.window, "CTRL+B")
        self.italic = ItalicAction("Italic", self.window, "CTRL+I")
        self.underline = UnderlineAction("Underline", self.window, "CTRL+U")

    
    def setAlignActions(self):
        
        self.align_left = LeftAction("Left", self.window, "CTRL+SHIFT+L")
        self.align_center = CenterAction("Center", self.window, "CTRL+SHIFT+E")
        self.align_right = RightAction("Right", self.window, "CTRL+SHIFT+R")


    def addActions(self, menu, actions):
        for action in actions:
            menu.addAction(action)