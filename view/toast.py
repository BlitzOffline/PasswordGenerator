import customtkinter
from customtkinter import CTkToplevel, CTkFrame


class Toast(CTkToplevel):
    def __init__(self, *args, width: int = 200, height: int = 50, x: int = 100, y: int = 100, time: int = 2,
                 title: str = "Toast", message="This is a toast!", **kwargs):
        if args:
            parent = args[0]
            parent.update()

            parent_x = parent.winfo_rootx()
            parent_y = parent.winfo_rooty()

            parent_width = parent.winfo_width()
            parent_height = parent.winfo_height()

            # Place toast in the bottom right corner of the parent window
            x = parent_x + parent_width - width
            y = parent_y + parent_height - height

        super().__init__(*args, **kwargs)
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
