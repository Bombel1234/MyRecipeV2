
from View.AddRecipeScreen.add_recipe_screen import AddRecipeScreenView


class AddRecipeScreenController:
    """
    The `AddRecipeScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.add_recipe_screen.AddRecipeScreenModel
        self.view = AddRecipeScreenView(controller=self, model=self.model)

    def screen_home(self):
        self.view.manager_screens.current = 'home screen'

    def get_view(self) -> AddRecipeScreenView:
        return self.view
