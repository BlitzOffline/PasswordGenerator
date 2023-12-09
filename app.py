from tkinter import IntVar, BooleanVar, StringVar

import customtkinter

from password.config import PasswordConfig
from password.manager import PasswordManager
from view.options_frame import OptionsFrame
from view.password_frame import PasswordFrame
from view.toast import Toast


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.password_frame = None
        self.options_frame = None
        password_config = PasswordConfig(
            length=IntVar(master=self, value=16, name="password_length"),
            lowercase_letters=BooleanVar(master=self, value=True, name="password_lowercase_letters"),
            uppercase_letters=BooleanVar(master=self, value=True, name="password_uppercase_letters"),
            numbers=BooleanVar(master=self, value=True, name="password_numbers"),
            symbols=BooleanVar(master=self, value=True, name="password_symbols"),
            extras=StringVar(master=self, value="", name="password_extra_symbols"),
            blacklist=StringVar(master=self, value="", name="password_blacklist")
        )
        self.set_callbacks(password_config)
        self.password_manager = PasswordManager(password_config=password_config)

        self.grid_columnconfigure(index=0, weight=1)
        self.title('Password Generator')

        self.generate_items()

    def generate_items(self):
        self.password_frame = PasswordFrame(self, password_manager=self.password_manager)
        self.password_frame.grid(row=0, column=0)

        self.options_frame = OptionsFrame(self, password_manager=self.password_manager)
        self.options_frame.grid(row=1, column=0)

    def set_callbacks(self, password_config: PasswordConfig):
        password_config.length.trace_add("write", self.options_change_callback)
        password_config.lowercase_letters.trace_add("write", self.options_change_callback)
        password_config.uppercase_letters.trace_add("write", self.options_change_callback)
        password_config.numbers.trace_add("write", self.options_change_callback)
        password_config.symbols.trace_add("write", self.options_change_callback)
        password_config.extras.trace_add("write", self.options_change_callback)
        password_config.blacklist.trace_add("write", self.options_change_callback)

    def options_change_callback(self, *args):
        self.password_manager.regenerate_password()
