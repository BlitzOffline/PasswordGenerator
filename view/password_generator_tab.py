import customtkinter

from password.manager import PasswordManager
from view.options_frame import OptionsFrame
from view.password_frame import PasswordFrame


class PasswordGeneratorFrame(customtkinter.CTkFrame):
    def __init__(self, master, password_manager: PasswordManager, width=950, height=674, **kwargs):
        self.password_manager = password_manager

        super().__init__(master, width=width, height=height, **kwargs)
        self.grid_propagate(False)
        self.grid_columnconfigure(index=0, weight=1)

        password_frame = PasswordFrame(self, password_manager=self.password_manager, width=950, height=100,
                                       fg_color="transparent")
        password_frame.grid(row=0, column=0, sticky="new")

        options_frame = OptionsFrame(self, password_manager=self.password_manager, width=950, height=574,
                                     fg_color="transparent")
        options_frame.grid(row=1, column=0, sticky="sew")
