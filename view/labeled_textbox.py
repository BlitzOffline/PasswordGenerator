from customtkinter import CTkFrame, CTkLabel, CTkTextbox, CTkEntry


class LabeledTextBox(CTkFrame):
    def __init__(self, master, label: str, label_kwargs: dict = None, entry_kwargs: dict = None,
                 **kwargs):

        super().__init__(master=master, **kwargs)
        self.grid_propagate(False)
        self.grid_columnconfigure(index=0, weight=1)

        if label_kwargs is None:
            label_kwargs = {}
        if entry_kwargs is None:
            entry_kwargs = {}

        label = CTkLabel(self, text=label, font=("Courier", 17, "bold"), **label_kwargs)
        label.grid(row=0, column=0)

        textbox = CTkEntry(self, **entry_kwargs)
        textbox.grid(row=1, column=0, padx=20)
