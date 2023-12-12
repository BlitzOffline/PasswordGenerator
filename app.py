from tkinter import IntVar, BooleanVar, StringVar

import customtkinter
from customtkinter import CTkTabview

from password.config import PasswordConfig
from password.manager import PasswordManager
from view.password_checker_frame import PasswordCheckerFrame
from view.password_generator_tab import PasswordGeneratorFrame


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Password Generator')
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(index=0, weight=1)

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

        tabview = CTkTabview(self, width=960, height=720, border_width=2, corner_radius=5)
        tabview.pack(expand=False)

        tab_width = 960-10  # TabView uses 10px as padding
        tab_height = 720-46  # TabView uses 46px as padding

        password_generator_tab = tabview.add("Password Generator")
        password_generator_frame = PasswordGeneratorFrame(master=password_generator_tab,
                                                          password_manager=self.password_manager,
                                                          width=tab_width,
                                                          height=tab_height,
                                                          fg_color="transparent",
                                                          bg_color="transparent",
                                                          corner_radius=5)
        password_generator_frame.pack(expand=False)

        password_checker_tab = tabview.add("Password Checker")
        password_checker_tab = PasswordCheckerFrame(master=password_checker_tab,
                                                    password_manager=self.password_manager,
                                                    width=tab_width,
                                                    height=tab_height,
                                                    fg_color="transparent",
                                                    bg_color="transparent",
                                                    corner_radius=5)
        password_checker_tab.pack(expand=False)

    def _add_password_config_callbacks(self, password_config: PasswordConfig):
        password_config.length.trace_add("write", self.options_change_callback)
        password_config.lowercase_letters.trace_add("write", self.options_change_callback)
        password_config.uppercase_letters.trace_add("write", self.options_change_callback)
        password_config.digits.trace_add("write", self.options_change_callback)
        password_config.symbols.trace_add("write", self.options_change_callback)
        password_config.extras.trace_add("write", self.options_change_callback)
        password_config.blacklist.trace_add("write", self.options_change_callback)

    def options_change_callback(self, *args):
        # On option change, regenerate password using new options
        self.password_manager.regenerate_password()
