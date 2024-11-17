

from Model.base_model import BaseScreenModel
from kivy.logger import Logger

class SelectUrlScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SelectUrlScreen.select_url_screen.SelectUrlScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None
        self.database = database
        self.url_img = {
            "category1": 'assets/images/borszcz.jpg',
            "category2": 'assets/images/pirogi.jpg',
            "category3": 'assets/images/salat.jpg',
            "category4": 'assets/images/slodke.jpg'
        }

    def select_data(self, name_table):
        res = self.database.cursor.execute(
            f"SELECT * FROM {name_table}"
        ).fetchall()
        keys = ['id', 'url_origin', 'my_name_recipe', 'key_recipe',
                'is_img', 'img_default', 'img_select']
        data_from_base = [dict(zip(keys, values)) for values in res]
        return data_from_base
    

    
    # button перейти за посиланням
    def move_to_url(self, key_recipe, name_table):
        url = self.database.cursor.execute(
            f"SELECT url_origin FROM {name_table} WHERE key_recipe='{key_recipe}'"
        ).fetchone()
        return url[0]
    
    # numer rows
    
    def numer_rowid(self, key_recipe, name_table) -> int:
        rowid = self.database.cursor.execute(
            f"SELECT ROWID FROM {name_table} WHERE key_recipe='{key_recipe}'").fetchone()
        number_rowid = rowid[0]
        return int(number_rowid)

    # 
    def update_is_img(self, name_table, name_img, rowid):
        self.database.cursor.execute(
            f"UPDATE {name_table} SET is_img='jest' WHERE ROWID='{rowid}'"
        )
        self.database.cursor.execute(
            f"UPDATE {name_table} SET img_select='{name_img}' WHERE ROWID='{rowid}'"
        )
        self.database.connect.commit()

    def delete_recipe(self, key_recipe, name_table, rowid):
        
        self.database.cursor.execute(
            f"DELETE FROM {name_table} WHERE ROWID='{rowid}'"
        )
        self.database.connect.commit()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.SelectUrlScreen.select_url_screen.SelectUrlScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("select url screen")

    
