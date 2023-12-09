from tkinter import IntVar
from typing import Union, Callable

import customtkinter


class IntSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args, width: int = 100, height: int = 32, step_size: int = 1, from_: int = 0, to: int = 100,
                 variable: IntVar = None, command: Callable[[int | None, int], None] = None, **kwargs):
        """
        :param args: Other arguments to pass to the CTkFrame constructor
        :param width: Width of the spinbox
        :param height: Height of the spinbox
        :param step_size: Amount to increase/decrease the value by when the buttons are pressed. If the resulting value
                            is less than the minimum value or greater than the maximum value, the value will roll over.
        :param from_: Minimum value
        :param to: Maximum value
        :param variable: IntVar to store the value in
        :param command: Function to call when the value changes. The function should take two parameters: the old value
                        and the new value.
        :param kwargs: Other named arguments to pass to the CTkFrame constructor
        """

        if from_ > to:
            raise ValueError("'from_' must be less than or equal to 'to'")

        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.from_ = from_
        self.to = to

        self.variable = variable
        if not self.variable:
            self.variable = IntVar(master=self, value=0, name="variable")
        # Update Entry text when variable changes
        self.variable.trace_add("write", self.variable_change_callback)

        self.command = command

        self.grid_columnconfigure((0, 2), weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0,
                                            fg_color="transparent", validate="all",
                                            validatecommand=(self.register(self._validate), "%P"),)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")
        self.entry.insert(0, self.variable.get())
        self.entry.configure(state="disabled")

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.value_subtract_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.add_button = customtkinter.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.value_add_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

    def variable_change_callback(self, *args):
        self.entry.configure(state="normal")
        self.entry.delete(0, "end")
        self.entry.insert(0, self.variable.get())
        self.entry.configure(state="disabled")

    def value_add_callback(self):
        self.value_change_callback(self.step_size)

    def value_subtract_callback(self):
        self.value_change_callback(-self.step_size)

    def value_change_callback(self, change_size: int):
        try:
            self.set(int(self.entry.get()) + change_size)
        except ValueError:
            return

    def get(self) -> Union[int, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, new_value: int):
        try:
            old_value = int(self.entry.get())
        except ValueError:
            old_value = None

        # TODO: Determine if rolling over is better for the user experience than blocking
        # while new_value < self.from_ or new_value > self.to:
        #     new_value = self._roll_off(new_value)

        if new_value < self.from_:
            new_value = self.from_
        elif new_value > self.to:
            new_value = self.to

        self.entry.configure(state="normal")
        self.entry.delete(0, "end")
        self.entry.insert(0, new_value)
        self.entry.configure(state="disabled")

        if self.command is not None:
            self.command(old_value, new_value)

        if self.variable is not None:
            self.variable.set(new_value)

    def _roll_off(self, value: int):
        if value < self.from_:
            diff = self.from_ - value
            value = self.to - diff + 1
        if value > self.to:
            diff = value - self.to
            value = self.from_ + diff - 1

        return value

    def _validate(self, value: str) -> bool:
        if value == "":
            return True

        try:
            value = int(value)
            if value < self.from_ or value > self.to:
                return False
            return True
        except ValueError:
            return False
