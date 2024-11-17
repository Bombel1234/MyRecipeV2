

from Model.base_model import BaseScreenModel
from kivy.logger import Logger




class AddRecipeScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.AddRecipeScreen.add_recipe_screen.AddRecipeScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None
        self.database = database
        self.create_table_in_database()
        self.category = None
        self.img_default = None
        self.url_img = {
            "category1": 'assets/images/borszcz.jpg',
            "category2": 'assets/images/pirogi.jpg',
            "category3": 'assets/images/salat.jpg',
            "category4": 'assets/images/slodke.jpg'
        }
    def create_table_in_database(self):
        name_tables = [
            'category1',
            'category2',
            'category3',
            'category4',
        ]
        for name_table in name_tables:
            self.database.cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {name_table} ("
                f"id INTEGER PRIMARY KEY,"
                f"url_origin TEXT NOT NULL,"
                f"my_name_recipe TEXT NOT NULL,"
                f"key_recipe TEXT NOT NULL,"
                f"is_img NOT NULL,"
                f"img_default NOT NULL,"
                f"img_select NOT NULL)"
            )
            self.database.connect.commit()

    def add_data_baza(self, data, name_table):
        url_origin = data['url_origin']
        my_name_recipe = data['my_name_recipe']
        key_recipe = data['key_recipe']
        match data['category']:
            case 'category1':
                self.img_default = self.url_img['category1']
            case 'category2':
                self.img_default = self.url_img['category2']
            case 'category3':
                self.img_default = self.url_img['category3']
            case 'category4':
                self.img_default = self.url_img['category4']

        self.database.cursor.execute(
            f"INSERT INTO {name_table} ("
            f"url_origin, my_name_recipe, key_recipe, is_img, img_default, img_select"
            f") VALUES (?, ?, ?, ?, ?, ?)",
            (url_origin, my_name_recipe, key_recipe, 'no', self.img_default, 'no')
        )
        self.database.connect.commit()

    
    
    def is_link(self, url):
        name_tables = [
            'category1',
            'category2',
            'category3',
            'category4',
        ]
        for names in name_tables:
            if self.database.cursor.execute(f"SELECT url_origin FROM {names} WHERE url_origin='{url}'").fetchone():   
                return True
            return False


    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.AddRecipeScreen.add_recipe_screen.AddRecipeScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("add recipe screen")

   


