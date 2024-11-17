from kivymd.uix.textfield import MDTextField
from kivymd.uix.behaviors.focus_behavior import FocusBehavior


class InputText(MDTextField, FocusBehavior):
    """jhvjvj"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

