import requests
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from urllib.parse import urljoin
from kivy.logger import Logger

from View.base_screen import BaseScreenView
from View.AddRecipeScreen.components import InputText  # NOQA


class Content(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type('on_release')

    def on_release(self, category):
        """jhvhv"""


class AddRecipeScreenView(BaseScreenView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.category = None
        self.dialog = MDDialog()
        self.obj = None

    def on_leave(self, *args):
        self.obj = None
        self.category = None
        self.ids.text_field.text = ''
        self.ids.name_recipe.text = ''

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """


    def click_button1(self):
        if not self.window:
            if self.ids.text_field.text != '' and self.ids.name_recipe.text != '':
                link = self.ids.text_field.text
                first_url = "https://google.com"
                final_url = urljoin(first_url, link)
                if requests.get(final_url).status_code == 200:
                    self.obj = Content()
                    self.obj.on_release = self.select_category
                    self.add_widget(self.obj)
                else:
                    self.dialog.title = 'Такого посилання не iснуе'
                    self.dialog.open()
            else:
                self.dialog.title = 'Заповни всi поля'
                self.dialog.open()
        else:
            key_recipe = str(self.ids.name_recipe.text).lower().replace(' ', '')
            data = {
                'url_origin': self.ids.text_field.text,
                'my_name_recipe': self.ids.name_recipe.text,
                'key_recipe': key_recipe,
                'category': self.category
            }
            self.window = None
            self.obj = None
            
            link = str(self.ids.text_field.text)
            or_is_link = self.model.is_link(link, self.category)
            if or_is_link:
                self.dialog.title = 'Таке посилання вже є записано'
                self.dialog.open()
            else:
                self.save_data_in_base(data)
                self.ids.text_field.text = ''
                self.ids.name_recipe.text = ''


    def click_button(self):
        
        if self.ids.text_field.text != '' and self.ids.name_recipe.text != '':
            link = self.ids.text_field.text
            first_url = "https://google.com"
            final_url = urljoin(first_url, link)
            key_recipe = str(self.ids.name_recipe.text).lower().replace(' ', '')
            data = {
                    'url_origin': self.ids.text_field.text,
                    'my_name_recipe': self.ids.name_recipe.text,
                    'key_recipe': key_recipe,
                    'category': self.category
                }
            if requests.get(final_url).status_code == 200:
                self.obj = Content()
                self.obj.on_release = lambda x: self.select_category(x, data)
                self.add_widget(self.obj)
                
            else:
                self.dialog.title = 'Такого посилання не iснуе'
                self.dialog.open()
        else:
            self.dialog.title = 'Заповни всi поля'
            self.dialog.open()


    def select_category(self, category, data):
        self.category = category
        data['category'] = category
        self.save_data_in_base(data)
        Clock.schedule_once(self.delete_window, .5)
    
    def save_data_in_base(self, data):
        url = data['url_origin']
        or_is_link = self.model.is_link(url)
        
        if or_is_link:
            self.dialog.title = 'Таке посилання вже записано!!!'
            self.dialog.open()
            self.ids.text_field.text = ''
            self.ids.name_recipe.text = ''
        else:
            self.model.add_data_baza(data, self.category)
            self.ids.text_field.text = ''
            self.ids.name_recipe.text = ''
            toast('Посилання додано')

    def delete_window(self, dt):
        self.remove_widget(self.obj)
