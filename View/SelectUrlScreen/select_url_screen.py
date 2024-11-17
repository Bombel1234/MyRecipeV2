from View.SelectUrlScreen.components.CardRecipe import MyCardRecipe
from View.base_screen import BaseScreenView
from kivy.storage.jsonstore import JsonStore
import webbrowser
from kivy.clock import Clock, mainthread
from kivy.logger import Logger
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from androidstorage4kivy import SharedStorage, Chooser

from android import autoclass
from os.path import join,exists

Environment = autoclass('android.os.Environment')
 


class SelectUrlScreenView(BaseScreenView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chooser = Chooser(self.chooser_callback)
        self.category = None
        self.list_object = []
        self.number_card = None
        self.dialog = None
        
        

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """


    def on_leave(self, *args):
        if self.ids.box.children:
            self.ids.box.clear_widgets()
            self.list_object.clear()
            self.category = None
            self.number_card = None

    def on_enter(self, *args):
        store = JsonStore('my_category.json')
        self.category = store.store_get('category')['category']
        match self.category:
            case 'category1':
                self.ids.title_category.text = 'Першi страви'
            case 'category2':
                self.ids.title_category.text = 'Другi страви'
            case 'category3':
                self.ids.title_category.text = 'Салати'
            case 'category4':
                self.ids.title_category.text = 'Солодке'
        Clock.schedule_once(self.select_data_from_baza)
    
    def select_data_from_baza(self, dt):
        data = self.model.select_data(self.category)
        self.create_card_recipe(data)


    def create_card_recipe(self, data):
        ss = SharedStorage()

        for item in data:
            card = MyCardRecipe()
            card.name_recipe = item['my_name_recipe']
            card.link_button.id = item['key_recipe']
            card.icon_button.id = f"{item['key_recipe']}x"
            card.icon_delete.id = item['key_recipe']
            
            is_img = item['is_img']
            
            if is_img == 'jest':
                name_file = item['img_select']
                app_title = str(ss.get_app_title())
                path2 = ss.copy_from_shared(join(Environment.DIRECTORY_PICTURES,
                                                app_title, name_file))
                if path2:
                    card.source_img = path2
            else:
                name_file_default = item['img_default']
                card.source_img = name_file_default
                

            card.link_button.bind(on_release=lambda x: self.click_button_link(x))
            card.icon_button.bind(on_release=lambda x: self.click_icon_button(x))
            card.icon_delete.bind(on_release=lambda x: self.click_icon_delete(x))
            
            self.list_object.append(card)
            self.ids.box.add_widget(card)


    def click_button_link(self, button):
        url = self.model.move_to_url(button.id, self.category)
        webbrowser.open(url)

    def click_icon_button(self, button):
        self.id_button = str(button.id)[:-1]
        self.number_card = self.model.numer_rowid(self.id_button, self.category)
        self.open_closer()

    def click_icon_delete(self, button):
        number_card = self.model.numer_rowid(button.id, self.category)
        self.dialog = MDDialog(
            title="Видалити рецепт?",
            buttons=[
                MDFlatButton(
                    text="НI",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: self.close_dialog(x)
                ),
                MDFlatButton(
                    text="ТАК",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: self.delete_card(x, number_card, button.id)
                ),
            ],
        )
        self.dialog.open()

    def close_dialog(self, button):
        self.dialog.dismiss()
    

    def delete_card(self, button, number_card, key_recipe):
        Logger.info(f"____{number_card}")
        self.dialog.dismiss()
        if len(self.list_object) > 0:
            self.ids.box.remove_widget(self.list_object[int(number_card - 1)])
            self.model.delete_recipe(key_recipe, self.category, number_card)
            

    def open_closer(self):
        self.chooser.choose_content("image/*")
        

    def chooser_callback(self,uri_list):
        try:
            ss = SharedStorage()
            for uri in uri_list:
                self.path = ss.copy_from_shared(uri)
                if self.path:
                    self.shared = ss.copy_to_shared(self.path)
                              
            self.display()
        except Exception as e:
            pass
    @mainthread
    def display(self):
        name_img = str(self.path.split('/')[-1])
        self.list_object[self.number_card - 1].ids.img.source = self.path
        self.update_name_img(name_img)
        

    def update_name_img(self, name_img):
        self.model.update_is_img(self.category, name_img, str(self.number_card))
