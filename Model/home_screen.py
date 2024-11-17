

from Model.base_model import BaseScreenModel




class HomeScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.HomeScreen.home_screen.HomeScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None
        self.background_home = 'assets/images/1-cae19057.jpg'
        self.database = database

    # def select_all_data(self):
    #     res = self.database.cursor.execute(
    #         "SELECT * FROM my_baza"
    #     ).fetchall()
    #     return res

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.HomeScreen.home_screen.HomeScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("home screen")

    
