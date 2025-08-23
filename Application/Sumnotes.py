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


width, height = Window.size
print("Window width:", width)
print("Window height:", height)

Window.size = (360, 640)


class MainSumNotesApp(MDApp):
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
        """Show/Hide the floating new note form"""
        form = self.root.ids.new_note_form
        form.opacity = 1 if form.opacity == 0 else 0

class UpperLayout(BoxLayout):
    pass

class LowerLayout(BoxLayout):
    pass

class LowerLayoutDotslist(BoxLayout):
    pass

class menuform(BoxLayout):
    pass

class Settingsform(BoxLayout):
    line_color = ListProperty([0, 0, 0, 1])

class MainForm(BoxLayout):
    pass

class NoteForm(BoxLayout):
    pass

class DeleteNoteForm(BoxLayout):
    pass

class ConditionalSummarizeAIForm(BoxLayout):
    pass

class SummarizerResultsForm(BoxLayout):
    pass

MainSumNotesApp().run()