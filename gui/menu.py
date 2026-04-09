from action.file_action import *
from action.edit_action import *

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
        
        self.new = NewAction("New", "CTRL+N", self.window)
        self.open = OpenAction("Open", "CTRL+O", self.window)
        self.save = SaveAction("Save", "CTRL+S", self.window)
        self.save_as = SaveAsAction("Save As", "CTRL+SHIFT+S", self.window)
        self.export = ExportAction("Export", "CTRL+E", self.window)
        self.close = CloseAction("Close", "CTRL+W", self.window)
        self.quit = QuitAction("Quit", "CTRL+Q", self.window)


    def setEditActions(self):
        
        self.undo = UndoAction("Undo", "CTRL+Z", self.window)
        self.redo = RedoAction("Redo", "CTRL+Y", self.window)
        self.cut = CutAction("Cut", "CTRL+X", self.window)
        self.copy = CopyAction("Copy", "CTRL+C", self.window)
        self.paste = PasteAction("Paste", "CTRL+V", self.window)
    

    def setEditActions(self):
        
        self.undo = UndoAction("Undo", "CTRL+Z", self.window)
        self.redo = RedoAction("Redo", "CTRL+Y", self.window)
        self.cut = CutAction("Cut", "CTRL+X", self.window)
        self.copy = CopyAction("Copy", "CTRL+C", self.window)
        self.paste = PasteAction("Paste", "CTRL+V", self.window)
    

    def setViewActions(self):
        
        self.undo = ZoomInAction("Zoom In", "CTRL+=", self.window)
        self.redo = ZoomOutAction("Zoom Out", "CTRL+-", self.window)
        self.cut = ZoomRestoreAction("Restore Zoom", "CTRL+0", self.window)
        self.copy = ToolsAction("Show Toolbar", self.window)
        self.paste = StatusAction("Show Status Bar", self.window)


    def setTextActions(self):
        
        self.font = FontAction("Font", self.window)
        self.size = SizeAction("Size", self.window)
        self.bold = BoldAction("Bold", "CTRL+B", self.window)
        self.italic = ItalicAction("Italic", "CTRL+I", self.window)
        self.underline = UnderlineAction("Underline", "CTRL+U", self.window)

    
    def setTextActions(self):
        
        self.left = LeftAction("Left", "CTRL+SHIFT+L", self.window)
        self.center = CenterAction("Center", "CTRL+SHIFT+E", self.window)
        self.right = RightAction("Right", "CTRL+SHIFT+R", self.window)


    def addActions(self, menu, actions):
        for action in actions:
            menu.addAction(action)