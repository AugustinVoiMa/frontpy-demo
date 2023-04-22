from frontpy_core.core.views import ButtonView, TextView
from frontpy_core.core.views.frame_controller.frame_controller import FrameController
from text_editor.R import R


class MainWindowController(FrameController):

    def __init__(self):
        super(MainWindowController, self).__init__()

    def on_create(self):
        self.set_content_view(R.layout.editor_frame)
        super(MainWindowController, self).on_create()

        self.width = 1200
        self.height = 600
        self.title = "Text Editor"
