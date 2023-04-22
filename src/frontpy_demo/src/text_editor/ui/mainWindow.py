from frontpy_core.core.views import ButtonView, TextView
from frontpy_core.core.views.frame_controller.frame_controller import FrameController
from text_editor.R import R


class MainWindowController(FrameController):

    def __init__(self):
        super(MainWindowController, self).__init__()
        self.counter_value = 0
        self.counter_view: TextView = None

    def on_create(self):
        self.set_content_view(R.layout.editor_frame)
        super(MainWindowController, self).on_create()

        self.width = 500
        self.title = "Text Editor"

        self.counter_value = 0

        btn_inc: ButtonView = self.find_view_by_id(R.id.btn_inc_counter)
        btn_inc.on_click_listener = self.increment_counter

        self.counter_view: TextView = self.find_view_by_id(R.id.counter)

    def increment_counter(self):
        self.counter_value += 1
        self.counter_view.text = str(self.counter_value)
