# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.home_screen import HomeScreenModel
from Controller.home_screen import HomeScreenController
from Model.add_recipe_screen import AddRecipeScreenModel
from Controller.add_recipe_screen import AddRecipeScreenController
from Model.select_url_screen import SelectUrlScreenModel
from Controller.select_url_screen import SelectUrlScreenController

screens = {
    "home screen": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
    },

    "add recipe screen": {
        "model": AddRecipeScreenModel,
        "controller": AddRecipeScreenController,
    },

    "select url screen": {
        "model": SelectUrlScreenModel,
        "controller": SelectUrlScreenController,
    },
}