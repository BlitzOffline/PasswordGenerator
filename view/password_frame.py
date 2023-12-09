import customtkinter
from CTkToolTip import CTkToolTip

from password.manager import PasswordManager
from PIL import Image

from view.toast import Toast


class PasswordFrame(customtkinter.CTkFrame):
    def __init__(self, *args, width=960, height=140, password_manager: PasswordManager, **kwargs):
        self.password_manager = password_manager
        self.password_manager.add_callback("password_box", self.update_password)
        if args:
            self.parent = args[0]
        else:
            self.parent = None

        super().__init__(*args, width=width, height=height, **kwargs)
        self.grid_propagate(False)

        self.password_box = customtkinter.CTkLabel(self, width=600, height=100,
                                                   text=password_manager.password,
                                                   font=("Consolas", 19), justify="left", wraplength=580)
        self.password_box.grid(row=0, column=0, padx=10, pady=15)

        copy_image = customtkinter.CTkImage(
            light_image=Image.open("assets/copy_light.png"),
            dark_image=Image.open("assets/copy_dark.png"),
            size=(50, 50)
        )

        self.copy_button = customtkinter.CTkButton(self, width=100, height=100, text="", image=copy_image,
                                                   fg_color="transparent", corner_radius=15, command=self.copy_password)
        self.copy_button.grid(row=0, column=1, pady=20, padx=20)

        self.copy_tooltip = CTkToolTip(widget=self.copy_button, message="Copy to clipboard!", corner_radius=10, delay=0,
                                       font=("Consolas", 12, "bold"))

        refresh_image = customtkinter.CTkImage(
            light_image=Image.open("assets/refresh_light.png"),
            dark_image=Image.open("assets/refresh_dark.png"),
            size=(50, 50)
        )

        self.regenerate_button = customtkinter.CTkButton(self, width=100, height=100, text="", image=refresh_image,
                                                         fg_color="transparent", corner_radius=15,
                                                         command=password_manager.regenerate_password)
        self.regenerate_button.grid(row=0, column=2, pady=20, padx=20, sticky="e")

        self.regenerate_tooltip = CTkToolTip(widget=self.regenerate_button, message="Regenerate", corner_radius=10,
                                             delay=0, font=("Consolas", 12, "bold"))

    def copy_password(self):
        self.clipboard_clear()
        self.clipboard_append(self.password_manager.password)
        Toast(self.parent if self.parent else self, message="Copied to clipboard!")

    def update_password(self, password: str):
        self.password_box.configure(text=password)
