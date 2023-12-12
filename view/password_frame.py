import customtkinter
from CTkToolTip import CTkToolTip
from PIL import Image

from password.manager import PasswordManager
from paths import get_app_path
from view.toast import Toast


class PasswordFrame(customtkinter.CTkFrame):
    def __init__(self, master, password_manager: PasswordManager, width=950, height=100, **kwargs):
        self.master = master
        self.password_manager = password_manager
        self.password_manager.add_callback("password_box", self.update_password_box)

        super().__init__(master, width=width, height=height, **kwargs)
        self.grid_propagate(False)
        self.grid_rowconfigure(index=0, weight=1)

        self.password_box = customtkinter.CTkLabel(self, width=630, height=100, fg_color="transparent",
                                                   corner_radius=15, text=password_manager.password,
                                                   font=("Consolas", 19), justify="left", wraplength=580)
        self.password_box.grid(row=0, column=0, sticky="nsw", padx=30)

        copy_image = customtkinter.CTkImage(
            light_image=Image.open(f"{get_app_path()}/assets/copy_light.png"),
            dark_image=Image.open(f"{get_app_path()}/assets/copy_dark.png"),
            size=(50, 50)
        )

        self.copy_button = customtkinter.CTkButton(self, width=100, height=100, text="", image=copy_image,
                                                   fg_color="transparent", corner_radius=15, command=self.copy_password)
        self.copy_button.grid(row=0, column=1, sticky="nse")

        self.copy_tooltip = CTkToolTip(widget=self.copy_button, message="Copy to clipboard!", corner_radius=10, delay=0,
                                       font=("Consolas", 12, "bold"))

        refresh_image = customtkinter.CTkImage(
            light_image=Image.open(f"{get_app_path()}/assets/refresh_light.png"),
            dark_image=Image.open(f"{get_app_path()}/assets/refresh_dark.png"),
            size=(50, 50)
        )

        self.regenerate_button = customtkinter.CTkButton(self, width=100, height=100, text="", image=refresh_image,
                                                         fg_color="transparent", corner_radius=15,
                                                         command=password_manager.regenerate_password)
        self.regenerate_button.grid(row=0, column=2, sticky="nse", padx=30)

        self.regenerate_tooltip = CTkToolTip(widget=self.regenerate_button, message="Regenerate", corner_radius=10,
                                             delay=0, font=("Consolas", 12, "bold"))

    def copy_password(self):
        self.clipboard_clear()
        self.clipboard_append(self.password_manager.password)
        Toast(self.master, message="Copied to clipboard!")

    def update_password_box(self, password: str):
        self.password_box.configure(text=password)
