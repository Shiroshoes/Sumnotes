from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

Window.size = (412, 917)  # phone-like preview on desktop


class MainScreen(Screen):
    pass


class NotesApp(MDApp):
    def build(self):
        return MainScreen()

    def toggle_delete_icons(self):
        """Show or hide all delete icons"""
        for widget in self.root.walk():
            # find all MDIconButtons with 'delete'
            if widget.__class__.__name__ == "MDIconButton" and widget.icon == "delete":
                widget.opacity = 0 if widget.opacity == 1 else 1

    def delete_note(self, note_title):
        print(f"Deleting note: {note_title}")

    def show_note_detail(self, note_title):
        print(f"Open note detail: {note_title}")
    
    def toggle_new_note_form(self):
        """Show/Hide the floating new note form"""
        form = self.root.ids.new_note_form
        form.opacity = 1 if form.opacity == 0 else 0

    def create_new_note(self):
        """Action when clicking the form"""
        print("New note form clicked!")



if __name__ == "__main__":
    NotesApp().run()
