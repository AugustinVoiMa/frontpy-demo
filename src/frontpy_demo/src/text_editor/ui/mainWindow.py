from frontpy_core.core.views.frame_controller.frame_controller import FrameController
from text_editor.R import R


class MainWindowController(FrameController):
    def on_create(self):
        self.set_content_view(R.layout.editor_frame)
        super(MainWindowController, self).on_create()

        self.width = 500
        self.title = "Text Editor"
