from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class Calcul(App):
    def build(self):
        widget = BoxLayout(orientation="vertical")
        self.label = Label(text="", size_hint_y=0.75, font_size=51)
        
        # Symbols for calculator buttons
        symbutton = (
            '1', '2', '3', '+',
            '4', '5', '6', '*',
            '7', '8', '9', '.',
            '0', '/', '-', '=')

        grid = GridLayout(cols=4, size_hint_y=2)
        
        # Add buttons to grid
        for symb in symbutton:
            btn = Button(text=symb)
            btn.bind(on_press=self.on_button_press)
            grid.add_widget(btn)

        # Bottom row: CE and Back
        bottom_row = BoxLayout(size_hint_y=None, height=100)
        
        clear_button = Button(text="CE")
        clear_button.bind(on_press=self.clear_text)

        back_button = Button(text="Back")
        back_button.bind(on_press=self.backspace)

        bottom_row.add_widget(clear_button)
        bottom_row.add_widget(back_button)

        widget.add_widget(self.label)
        widget.add_widget(grid)
        widget.add_widget(bottom_row)
        return widget

    def on_button_press(self, instance):
        if instance.text == "=":
            try:
                self.label.text = str(eval(self.label.text))
            except Exception:
                self.label.text = "Error"
        else:
            self.label.text += instance.text
            
    def on_button_press(self, instance):
        if instance.text == "=":
            self.label.text = "miss kita"
        else:
            self.label.text += instance.text

    def clear_text(self, instance):
        self.label.text = ""

    def backspace(self, instance):
        self.label.text = self.label.text[:-1]

if __name__ == '__main__':
    Calcul().run()
