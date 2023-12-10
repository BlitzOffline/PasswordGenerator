from tkinter import IntVar, BooleanVar, StringVar

import customtkinter

from password.config import PasswordConfig
from password.manager import PasswordManager
from view.options_frame import OptionsFrame
from view.password_frame import PasswordFrame


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Password Generator')
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(index=0, weight=1)

        self.password_frame = None
        self.options_frame = None
        password_config = PasswordConfig(
            length=IntVar(master=self, value=16, name="password_length"),
            lowercase_letters=BooleanVar(master=self, value=True, name="password_lowercase_letters"),
            uppercase_letters=BooleanVar(master=self, value=True, name="password_uppercase_letters"),
            digits=BooleanVar(master=self, value=True, name="password_digits"),
            symbols=BooleanVar(master=self, value=True, name="password_symbols"),
            extras=StringVar(master=self, value="", name="password_extra_symbols"),
            blacklist=StringVar(master=self, value="", name="password_blacklist")
        )
        self._add_password_config_callbacks(password_config)
        self.password_manager = PasswordManager(password_config=password_config)

        self.generate_items()

    def generate_items(self):
        self.password_frame = PasswordFrame(self, width=960, height=140, password_manager=self.password_manager)
        self.password_frame.grid(row=0, column=0)

        self.options_frame = OptionsFrame(self, width=960, height=580, password_manager=self.password_manager)
        self.options_frame.grid(row=1, column=0)

    def _add_password_config_callbacks(self, password_config: PasswordConfig):
        password_config.length.trace_add("write", self.options_change_callback)
        password_config.lowercase_letters.trace_add("write", self.options_change_callback)
        password_config.uppercase_letters.trace_add("write", self.options_change_callback)
        password_config.digits.trace_add("write", self.options_change_callback)
        password_config.symbols.trace_add("write", self.options_change_callback)
        password_config.extras.trace_add("write", self.options_change_callback)
        password_config.blacklist.trace_add("write", self.options_change_callback)

    def options_change_callback(self, *args):
        self.password_manager.regenerate_password()
