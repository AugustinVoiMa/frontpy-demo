import tkinter.filedialog
from os.path import basename
from tkinter.messagebox import askokcancel

from frontpy_core.core.event import KeyEvent
from frontpy_core.core.views import ButtonView, EditTextView
from frontpy_core.core.views.frame_controller.frame_controller import FrameController
from text_editor.R import R


class MainWindowController(FrameController):

    def __init__(self):
        super(MainWindowController, self).__init__()
        self.filename = None
        self.edit_text: EditTextView = None
        self.encoding = 'utf-8'
        self.save_btn: ButtonView = None
        self.initial_text = None

    def on_create(self):
        self.set_content_view(R.layout.editor_frame)
        super(MainWindowController, self).on_create()

        self.width = 1200
        self.height = 600
        self.update_title()

        open_btn: ButtonView = self.find_view_by_id(R.id.open_btn)
        open_btn.on_click_listener = self.on_open_file

        self.save_btn: ButtonView = self.find_view_by_id(R.id.save_btn)
        self.save_btn.on_click_listener = self.on_save_file

        saveas_btn: ButtonView = self.find_view_by_id(R.id.saveas_btn)
        saveas_btn.on_click_listener = self.on_saveas_file

        self.edit_text: EditTextView = self.find_view_by_id(R.id.text_edition)
        self.edit_text.on_edit_listener = self.on_edit_text

        self.edit_text.add_event_listener(KeyEvent('Ctrl', "s"), self.on_save_file)
        self.edit_text.add_event_listener(KeyEvent('Ctrl', "Shift", "S"), self.on_saveas_file)

        if self.filename is None:
            self.save_btn.disabled = True

    def update_title(self):
        self.title = "Text Editor" + ((" ~ .../" + basename(self.filename)) if self.filename else "")

    @property
    def pending_changes(self):
        current_text = self.edit_text.text.strip(' \n')
        if self.initial_text is None:
            return current_text != ""
        else:
            return current_text != self.initial_text.strip('\n ')

    def on_open_file(self):
        if self.pending_changes:
            answ = askokcancel("Unsaved changes",
                               "Some changes to the previous file were not saved. "
                               "Opening a new file will discard these changes. Continue?")
            if not answ:
                return

        new_filename = tkinter.filedialog.askopenfilename(defaultextension=".txt",
                                                          filetypes=[
                                                              ("Text File", "*.txt"),
                                                              ("Other", "*.*")
                                                          ])
        if new_filename is not None and new_filename != '':
            self.filename = new_filename
        else:
            return
        with open(self.filename, encoding=self.encoding) as fic:
            self.initial_text = '\n'.join(fic.readlines())

        self.edit_text.text = self.initial_text
        self.save_btn.disabled = True
        self.update_title()

    def on_save_file(self):
        print("on_save_file")
        if self.filename is None:
            return self.on_saveas_file()

        assert self.filename is not None
        assert self.pending_changes

        self.save()

    def on_edit_text(self):
        self.save_btn.disabled = not self.pending_changes

    def on_saveas_file(self):
        print("on_saveas_file")
        new_filename = tkinter.filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text file", "*.txt"),
                ("Any", "*.*")
            ],
            confirmoverwrite=True
        )
        if new_filename is None:
            return
        self.filename = new_filename
        self.save()
        self.update_title()

    def save(self):
        text = self.edit_text.text
        with open(self.filename, 'w', encoding=self.encoding) as fic:
            fic.write(text)
        self.save_btn.disabled = True
        self.initial_text = text
