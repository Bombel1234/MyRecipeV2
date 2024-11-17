"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""

from kivymd.app import MDApp
from kivy.uix.screenmanager import NoTransition, ScreenManager

from View.screens import screens
from Model.database import DataBase
from kivy.core.window import Window
from os.path import exists

from android_permissions import AndroidPermissions
from androidstorage4kivy import SharedStorage
from android import mActivity
from shutil import rmtree

Window.softinput_mode = 'below_target'



class ProjectRecipe(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = ScreenManager(transition=NoTransition())
        self.database = DataBase()

    def build(self) -> ScreenManager:
        Window.bind(on_keyboard=self.quit_app)
        temp = SharedStorage().get_cache_dir()
        if temp and exists(temp):
            rmtree(temp)
        self.generate_application_screens()
        # self.theme_cls.primary_palette = "Orange"
        return self.manager_screens
    
    def on_start(self):
        self.dont_gc = AndroidPermissions(self.start_app)

    def start_app(self):
        self.dont_gc = None
        
    def quit_app(self, window, key, *args):

        if key == 27:
            mActivity.finishAndRemoveTask()
            return True
        else:
            return False

    def generate_application_screens(self) -> None:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"](self.database)
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)


ProjectRecipe().run()
