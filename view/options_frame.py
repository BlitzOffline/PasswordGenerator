import customtkinter

from password.manager import PasswordManager
from view.int_spinbox import IntSpinbox
from view.tricolumn_frame import TripleColumnFrame


class OptionsFrame(customtkinter.CTkFrame):
    def __init__(self, master, password_manager: PasswordManager, width=950, height=574, **kwargs):
        self.password_manager = password_manager

        super().__init__(master, width=width, height=height, **kwargs)
        self.grid_propagate(False)

        self.options_title = customtkinter.CTkLabel(self, width=width, height=25, text="OPTIONS",
                                                    fg_color="transparent", font=("Consolas", 20, "bold"))
        self.options_title.grid(row=0, column=0, columnspan=3, pady=10)

        elements = 7  # Number of elements in the OptionsFrame
        element_height = int((574 - 25 - 20 - 20 * elements) / elements)
        print(element_height)

        # TODO: Determine why elements of a TripleColumnFrame are not centered
        self.length_frame = TripleColumnFrame(self, width=width, height=element_height,
                                              column_1_element=self.get_length_label(),
                                              column_2_element=self.get_length_slider(),
                                              column_3_element=self.get_length_spinbox(),
                                              fg_color="transparent")
        self.length_frame.grid(row=1, column=0, pady=10)
        self.length_frame.grid_propagate(False)

        self.lowercase_frame = TripleColumnFrame(self, width=width, height=element_height,
                                                 column_1_element=self.get_lowercase_letters_label(),
                                                 column_3_element=self.get_lowercase_letters_checkbox(),
                                                 fg_color="transparent")
        self.lowercase_frame.grid(row=2, column=0, pady=10)

        self.uppercase_frame = TripleColumnFrame(self, width=width, height=element_height,
                                                 column_1_element=self.get_uppercase_letters_label(),
                                                 column_3_element=self.get_uppercase_letters_checkbox(),
                                                 fg_color="transparent")
        self.uppercase_frame.grid(row=3, column=0, pady=10)

        self.numbers_frame = TripleColumnFrame(self, width=width, height=element_height,
                                               column_1_element=self.get_numbers_label(),
                                               column_3_element=self.get_numbers_checkbox(),
                                               fg_color="transparent")
        self.numbers_frame.grid(row=4, column=0, pady=10)

        self.symbols_frame = TripleColumnFrame(self, width=width, height=element_height,
                                               column_1_element=self.get_symbols_label(),
                                               column_3_element=self.get_symbols_checkbox(),
                                               fg_color="transparent")
        self.symbols_frame.grid(row=5, column=0, pady=10)

        self.extras_frame = TripleColumnFrame(self, width=width, height=element_height,
                                              column_1_element=self.get_extras_label(),
                                              column_2_element=self.get_extras_entry(),
                                              fg_color="transparent")
        self.extras_frame.grid(row=6, column=0, pady=10)

        self.blacklist_frame = TripleColumnFrame(self, width=width, height=element_height,
                                                 column_1_element=self.get_blacklist_label(),
                                                 column_2_element=self.get_blacklist_entry(),
                                                 fg_color="transparent")
        self.blacklist_frame.grid(row=7, column=0, pady=10)

    @staticmethod
    def get_length_label():
        return (customtkinter.CTkLabel, [],
                {"text": "Length", "anchor": "w", "justify": "left", "font": ("Consolas", 17, "bold")})

    def get_length_slider(self):
        return (customtkinter.CTkSlider, [],
                {"width": 340, "height": 15, "button_length": 5, "from_": 4, "to": 174, "number_of_steps": 170,
                 "variable": self.password_manager.password_generator.password_config.length})

    def get_length_spinbox(self):
        return (IntSpinbox, [],
                {"width": 100, "height": 32, "step_size": 1, "from_": 4, "to": 174, "fg_color": "transparent",
                 "variable": self.password_manager.password_generator.password_config.length})

    @staticmethod
    def get_lowercase_letters_label():
        return (customtkinter.CTkLabel, [],
                {"text": "a-z", "anchor": "w", "justify": "left", "font": ("Consolas", 17, "bold")})

    def get_lowercase_letters_checkbox(self):
        return (customtkinter.CTkCheckBox, [],
                {"text": "", "variable": self.password_manager.password_generator.password_config.lowercase_letters})

    @staticmethod
    def get_uppercase_letters_label():
        return (customtkinter.CTkLabel, [],
                {"text": "A-Z", "anchor": "w", "justify": "left", "font": ("Consolas", 17, "bold")})

    def get_uppercase_letters_checkbox(self):
        return (customtkinter.CTkCheckBox, [],
                {"text": "", "variable": self.password_manager.password_generator.password_config.uppercase_letters})

    @staticmethod
    def get_numbers_label():
        return (customtkinter.CTkLabel, [],
                {"text": "0-9", "anchor": "w", "justify": "left", "font": ("Consolas", 17, "bold")})

    def get_numbers_checkbox(self):
        return (customtkinter.CTkCheckBox, [],
                {"text": "", "variable": self.password_manager.password_generator.password_config.digits})

    @staticmethod
    def get_symbols_label():
        return (customtkinter.CTkLabel, [],
                {"text": "!@#$%^&*", "anchor": "w", "justify": "left", "font": ("Consolas", 17, "bold")})

    def get_symbols_checkbox(self):
        return (customtkinter.CTkCheckBox, [],
                {"text": "", "variable": self.password_manager.password_generator.password_config.symbols})

    @staticmethod
    def get_extras_label():
        return (customtkinter.CTkLabel, [],
                {"text": "Extras", "anchor": "w", "justify": "left", "font": ("Consolas", 17, "bold")})

    def get_extras_entry(self):
        return (customtkinter.CTkEntry, [],
                {"width": 450, "height": 32,
                 "textvariable": self.password_manager.password_generator.password_config.extras})

    @staticmethod
    def get_blacklist_label():
        return (customtkinter.CTkLabel, [],
                {"text": "Blacklist", "anchor": "w", "justify": "left", "font": ("Consolas", 17, "bold")})

    def get_blacklist_entry(self):
        return (customtkinter.CTkEntry, [],
                {"width": 450, "height": 32,
                 "textvariable": self.password_manager.password_generator.password_config.blacklist})
