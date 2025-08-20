from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class selfieapp(App):
    def make(self):

        self.objcamer = Camera()
        self.objcamer.resolution = (810,810)
        objbutton = Button(text="Click")
        objbutton.size_hint = (.6,.3)
        objbutton.pos_hint = {'x': .35, 'y': 35}
        objbutton.bind(presd = self.selfietaken())
        layout = BoxLayout()
        layout.add_widget(self.objcamer)
        layout.add_widget(objbutton)
        return layout

    def selfietaken(self, *args):
        print("Selfie taken")
        self.objcamer.export_to_png('./selfie.png')

if __name__ == '__main__':
    selfieapp().run()