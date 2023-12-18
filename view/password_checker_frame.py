from tkinter import StringVar

from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkProgressBar

from password.manager import PasswordManager
from view.labeled_textbox import LabeledTextBox
from view.toast import Toast


class PasswordCheckerFrame(CTkFrame):
    def __init__(self, master, password_manager: PasswordManager, width=950, height=674, **kwargs):
        self.password_manager = password_manager
        self.width = width
        self.height = height

        super().__init__(master, width=width, height=height, **kwargs)
        self.grid_propagate(False)

        self.password = StringVar(self, value="", name="password")
        self.username = StringVar(self, value="", name="username")
        self.email = StringVar(self, value="", name="email")
        self.first_name = StringVar(self, value="", name="first_name")
        self.second_name = StringVar(self, value="", name="second_name")

        info_box_height = 40
        info_box_width = int(0.7 * width)

        self.element_height = 60
        self.element_width = int(width / 2)

        # INFO BOXES
        self.warning_box = CTkLabel(self, width=info_box_width, height=info_box_height, fg_color=("#ff9966", "#cc3300"),
                                    corner_radius=5, font=("Courier", 16, "bold"), text_color="black",
                                    text="Information on this page will never leave this computer!")
        self.warning_box.grid(row=0, column=0, columnspan=2, pady=10)

        self.info_box = CTkLabel(self, width=info_box_width, height=info_box_height, fg_color=("#99cc33", "#339900"),
                                 corner_radius=5, font=("Courier", 16, "bold"), text_color="black",
                                 text="If you want extra validation, you can fill in the optional boxes below")
        self.info_box.grid(row=4, column=0, columnspan=2, pady=10)

        # PASSWORD BOX
        self.password_box = LabeledTextBox(self, label="Password", width=width, height=self.element_height,
                                           label_kwargs={"width": width},
                                           entry_kwargs={"width": width - 40, "height": 1,
                                                         "textvariable": self.password}
                                           )
        self.password_box.grid(row=1, column=0, columnspan=2, pady=10)

        # CHECK BUTTON
        self.button_frame = CTkFrame(self, width=self.element_width, height=self.element_height)
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.check_button = CTkButton(self.button_frame, text="Check", command=self._check_password)
        self.check_button.pack(expand=False)

        self.response_frame = None
        self.response_score = None
        self.response_time = None

        # OPTIONAL BOXES
        self.username_box = LabeledTextBox(self, label="Username", width=self.element_width,
                                           height=self.element_height, label_kwargs={"width": self.element_width},
                                           entry_kwargs={"width": self.element_width, "height": 1,
                                                         "textvariable": self.username}
                                           )
        self.username_box.grid(row=5, column=0, pady=10)

        self.email_box = LabeledTextBox(self, label="Email", width=self.element_width, height=self.element_height,
                                        label_kwargs={"width": self.element_width},
                                        entry_kwargs={"width": self.element_width, "height": 1, "textvariable": self.email}
                                        )
        self.email_box.grid(row=5, column=1, pady=10)

        self.first_name_box = LabeledTextBox(self, label="First Name", width=self.element_width,
                                             height=self.element_height, label_kwargs={"width": self.element_width},
                                             entry_kwargs={"width": self.element_width, "height": 1,
                                                           "textvariable": self.first_name}
                                             )
        self.first_name_box.grid(row=6, column=0, pady=10)

        self.second_name_box = LabeledTextBox(self, label="Second Name", width=self.element_width,
                                              height=self.element_height, label_kwargs={"width": self.element_width},
                                              entry_kwargs={"width": self.element_width, "height": 1,
                                                            "textvariable": self.second_name}
                                              )
        self.second_name_box.grid(row=6, column=1, pady=10)

    def _check_password(self):
        if self.response_frame:
            self.response_frame.destroy()

        password = self.password.get()
        if password == "":
            Toast(self.master, message="Please enter a password!")
            return

        user_inputs = self.username.get(), self.email.get(), self.first_name.get(), self.second_name.get()
        user_inputs = [user_input for user_input in user_inputs if user_input and user_input != ""]
        result = self.password_manager.password_checker.strength_check(password=self.password.get(),
                                                                       user_input=user_inputs)

        self._handle(result)

    def _handle(self, result):
        score, _, _, crack_times_display = result

        match score:
            case 0:
                score_color = "#cc3300"
            case 1:
                score_color = "#ff9966"
            case 2:
                score_color = "#ffcc00"
            case 3:
                score_color = "#99cc33"
            case _:
                score_color = "#339900"

        self.response_frame = CTkFrame(self, width=self.width, height=self.element_height)
        self.response_frame.grid_columnconfigure(0, weight=1)

        self.response_score = CTkProgressBar(self.response_frame, width=300, height=15, progress_color=score_color)
        self.response_score.set(score * 0.25)
        self.response_score.grid(row=0, column=0)

        if crack_times_display:
            self.response_warning = CTkLabel(self.response_frame, width=300, height=15, fg_color=score_color,
                                             corner_radius=5, font=("Courier", 16, "bold"), text_color="black",
                                             text="It would take a computer " + crack_times_display +
                                                  " to crack this password")
            self.response_warning.grid(row=1, column=0)

        self.response_frame.grid(row=3, column=0, columnspan=2, pady=10)
