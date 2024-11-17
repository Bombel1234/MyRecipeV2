from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.card import MDCard


class MyCardRecipe(MDCard):
    source_img = StringProperty()
    name_recipe = StringProperty()
    link_button = ObjectProperty()
    icon_button = ObjectProperty()
    icon_delete = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_release(self):
        """on_release"""
