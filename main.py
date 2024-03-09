from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class ForestryCollegeApp(MDApp):
    def build(self):
        return MDLabel(text="Привет, это Личная Библиотека!", halign="center")


ForestryCollegeApp().run()