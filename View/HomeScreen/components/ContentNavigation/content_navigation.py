from kivymd.uix.floatlayout import MDFloatLayout
from kivy.storage.jsonstore import JsonStore


class ContentNavigationDrawer(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.store = JsonStore('my_category.json')

    def save_json(self, category):
        self.store.put('category', category=category)
