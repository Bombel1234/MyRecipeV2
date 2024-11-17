import sqlite3
from android import mActivity


class DataBase:
    """
    Your methods for working with the database should be implemented in this
    class.
    """

    name = "My Baza"

    def __init__(self):
        context = mActivity.getApplicationContext()
        self.result =  context.getExternalFilesDir(None)
        self.storage_path =  str(self.result.toString())
        self.connect = sqlite3.connect(f'{self.storage_path}/baza.db')
        self.cursor = self.connect.cursor()
