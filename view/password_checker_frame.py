from customtkinter import CTkFrame, CTkTextbox

from password.manager import PasswordManager


class PasswordCheckerFrame(CTkFrame):
    def __init__(self, master, password_manager: PasswordManager, width=950, height=674, **kwargs):
        self.password_manager = password_manager

        super().__init__(master, width=width, height=height, **kwargs)
        self.grid_propagate(False)

        self.test = CTkTextbox(self, width=50, height=1)
        self.test.pack()
