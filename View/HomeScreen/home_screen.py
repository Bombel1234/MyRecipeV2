from View.base_screen import BaseScreenView
from View.HomeScreen.components.ContentNavigation import ContentNavigationDrawer
from kivy.logger import Logger


class HomeScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    # def on_enter(self, *args):
    #     res = self.model.select_all_data()
    #     Logger.info(str(res))