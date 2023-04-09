import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy import Config 
Config.set('graphics', 'multisamples', '0')


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        layout = GridLayout(cols=4)
        self.display = TextInput(text='0', halign='right', font_size=40, readonly=True)
        layout.add_widget(self.display)
        buttons = ['7', '8', '9', '/',
                    '4', '5', '6', '*',
                    '1', '2', '3', '-',
                    '.', '0', 'C', '+',
                    '=']
        for button in buttons:
            layout.add_widget(Button(text=button, on_press=self.handle_button))
        return layout

    def handle_button(self, instance):
        if instance.text == 'C':
            self.display.text = '0'
        elif instance.text == '=':
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = 'Error'
        else:
            self.display.text += instance.text

if __name__ == '__main__':
    CalculatorApp().run()
