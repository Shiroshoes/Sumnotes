from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.properties import Clock
from kivymd.app import MDApp
from kivy.properties import ListProperty
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import DictProperty
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.dialog import MDDialog
from kivy.uix.textinput import TextInput



width, height = Window.size
print("Window width:", width)
print("Window height:", height)

Window.size = (360, 640)


class MainSumNotesApp(MDApp):
    fab_items = DictProperty()

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        return MainForm()

    def show_note_form(self):
        print("FAB clicked")
        self.root.ids.screen_manager.current = "notes"

    def toggle_theme(self, is_active):
        if is_active:
            self.theme_cls.theme_style = "Dark"
            self.root.line_color = [1, 1, 1, 1]
        else:
            self.theme_cls.theme_style = "Light"
            self.root.line_color = [0, 0, 0, 1]
                
        self.root.ids.save_button.disabled = False

    def get_mode_text(self, is_active):
        return "Dark Mode" if is_active else "White Mode"

    def get_mode_color(self, is_active):
        return (1, 1, 1, 1) if is_active else (0, 0, 0, 1)
    
    def get_line_color(self, is_active):
        return (1, 1, 1, 1) if is_active else (0, 0, 0, 1)
    
    def toggle_summarizer(self, is_active):
        if is_active:
            print("Summarizer enabled")
        else:
            print("Summarizer disabled")

class UpperLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type('on_menu_press')

    def on_menu_press(self, *args):
        """Default handler for the event (can be empty)."""
        pass


class PlusMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        menu_items = [
            {
                "viewclass": "OneLineIconListItem",
                "text": "New Note",
                "on_release": self.new_note,
            },
            {
                "viewclass": "OneLineIconListItem",
                "text": "New Pinned Note",
                "on_release": self.new_pinned_note,
            },
        ]

        self.menu = MDDropdownMenu(
            caller=None,
            items=menu_items,
            width_mult=4,
        )

    def open_menu(self, caller):
        self.menu.caller = caller
        self.menu.open()

    def new_note(self):
        app = MDApp.get_running_app()
        app.show_note_form()
        self.menu.dismiss()

    def new_pinned_note(self):
        print("Pinned Note creation not implemented yet")
        self.menu.dismiss()

class LowerLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # dropdown menu items
        menu_items = [
            {
                "viewclass": "OneLineIconListItem",
                "text": "Delete",
                "on_release": lambda x="Delete": self.menu_callback(x),
            },
            {
                "viewclass": "OneLineIconListItem",
                "text": "Share",
                "on_release": lambda x="Share": self.menu_callback(x),
            },
            {
                "viewclass": "OneLineIconListItem",
                "text": "Settings",
                "on_release": self.go_to_settings,
            },
        ]

        self.menu = MDDropdownMenu(
            caller=None,
            items=menu_items,
            width_mult=4,
        )

    def open_menu(self, caller):
        self.menu.caller = caller
        self.menu.open()

    def menu_callback(self, text_item):
        print(f"Selected: {text_item}")
        self.menu.dismiss()

    def go_to_settings(self):
        app = MDApp.get_running_app()
        app.root.ids.nav_drawer.set_state("close")
        app.root.ids.screen_manager.current = "settings"
        self.menu.dismiss()


class Settingsform(BoxLayout):
    line_color = ListProperty([0, 0, 0, 1])
    nav_drawer = ObjectProperty()


class MainForm(MDScreen):
    pass


class NoteForm(MDScreen):
    dialog = None

    def open_summarize_form(self):
        if not self.dialog:
            content = ConditionalSummarizeAIForm()
            content.dialog_ref = self
            self.dialog = MDDialog(
                type="custom",
                content_cls=content,
                auto_dismiss=False,
            )
        self.dialog.open()


class DeleteNoteForm(BoxLayout):
    pass


class ConditionalSummarizeAIForm(BoxLayout):
    dialog_ref = ObjectProperty(None)

    def do_summarize(self):
        print("Summarization started")
        if self.dialog_ref.dialog:
            self.dialog_ref.dialog.dismiss()
            self.dialog_ref.dialog = None

    def close_dialog(self):
        if self.dialog_ref.dialog:
            self.dialog_ref.dialog.dismiss()
            self.dialog_ref.dialog = None


class SummarizerResultsForm(BoxLayout):
    pass


MainSumNotesApp().run()