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

    def toggle_new_note_form(self):
        form = self.root.ids.new_note_form
        if form.opacity == 0:
            form.opacity = 1
            form.disabled = False
        else:
            form.opacity = 0
            form.disabled = True

class UpperLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type('on_menu_press')

    def on_menu_press(self, *args):
        """Default handler for the event (can be empty)."""
        pass

class LowerLayout(BoxLayout):
    pass

class LowerLayoutDotslist(BoxLayout):
    pass

class Settingsform(BoxLayout):
    line_color = ListProperty([0, 0, 0, 1])
    nav_drawer = ObjectProperty()

class MainForm(MDScreen):
    pass

class NoteForm(MDScreen):
    pass

class DeleteNoteForm(BoxLayout):
    pass

class ConditionalSummarizeAIForm(BoxLayout):
    pass

class SummarizerResultsForm(BoxLayout):
    pass

MainSumNotesApp().run()