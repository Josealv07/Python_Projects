import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text='Hello, world! Jose creó esto')

if __name__ == '__main__':
    TestApp().run()
