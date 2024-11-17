from View.SelectUrlScreen.components.CardRecipe import MyCardRecipe
from View.SelectUrlScreen.select_url_screen import SelectUrlScreenView


class SelectUrlScreenController:
    """
    The `SelectUrlScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.select_url_screen.SelectUrlScreenModel
        self.view = SelectUrlScreenView(controller=self, model=self.model)

    def screen_link(self):
        self.view.manager_screens.current = 'home screen'

    def most_md_card_button(self, instance_card: MyCardRecipe) -> None:
        id_card = instance_card.id
        # self.view.click_icon_cards(id_card)

    def get_view(self) -> SelectUrlScreenView:
        return self.view
