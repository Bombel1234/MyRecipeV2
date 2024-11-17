from View.HomeScreen.home_screen import HomeScreenView
from View.HomeScreen.components import ContentNavigation


class HomeScreenController:
    """
    The `HomeScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.home_screen.HomeScreenModel
        self.view = HomeScreenView(controller=self, model=self.model)

    def screen_add_recipe(self):
        self.view.manager_screens.current = 'add recipe screen'


    def get_view(self) -> HomeScreenView:
        return self.view
