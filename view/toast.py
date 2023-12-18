import customtkinter
from customtkinter import CTkToplevel, CTkFrame


class Toast(CTkToplevel):
    def __init__(self, master, width: int = 200, height: int = 50, x: int = None, y: int = None, time: int = 2,
                 title: str = "Toast", message="This is a toast!", **kwargs):

        master.update()

        parent_x = master.winfo_rootx()
        parent_y = master.winfo_rooty()

        parent_width = master.winfo_width()
        parent_height = master.winfo_height()

        # Place toast in the bottom right corner of the parent window by default
        if not x:
            x = parent_x + parent_width - width
        if not y:
            y = parent_y + parent_height - height

        super().__init__(**kwargs)
        self.minsize(width=width, height=height)
        self.maxsize(width=width, height=height)
        self.geometry("+{}+{}".format(x, y))
        self.resizable(width=False, height=False)
        self.title(title)
        self.after(ms=time*1000, func=self.destroy)
        self.lift()
        self.wm_overrideredirect(True)

        self.label = customtkinter.CTkLabel(self, width=width, height=height, text=message, justify="center")
        self.label.pack()
