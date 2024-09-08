from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class AdditionApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.num1 = TextInput(multiline=False, size_hint=(1, 0.2), hint_text="Enter first number")
        self.num2 = TextInput(multiline=False, size_hint=(1, 0.2), hint_text="Enter second number")

        self.adding_butoon = Button(text="Add", size_hint=(1, 0.2))
        self.adding_butoon.bind(on_press=lambda instance: self.addition(self.num1, self.num2))

        self.label = Label(text="", size_hint=(1, 0.2))

        self.layout.add_widget(self.num1)
        self.layout.add_widget(self.num2)
        self.layout.add_widget(self.adding_butoon)
        self.layout.add_widget(self.label)

        return self.layout

    def addition(self, n1, n2):
        try:
            n1 = float(self.num1.text)
            n2 = float(self.num2.text)
            add = n1 + n2
            self.label.text = str(add)
        except ValueError:
            self.label.text = "Please enter valid numbers!"


AdditionApp().run()
