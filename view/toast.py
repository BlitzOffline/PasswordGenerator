import customtkinter
from customtkinter import CTkToplevel


class Toast(CTkToplevel):
    def __init__(self, *args, width: int = 200, height: int = 50, x: int = 100, y: int = 100, time: int = 2,
                 title: str = "Toast", message="This is a toast!", **kwargs):
        if args:
            parent = args[0]
            parent.update()

            # Get the width and height of the screen
            screen_width = parent.winfo_screenwidth()
            screen_height = parent.winfo_screenheight()

            # Get the width and height of the top-level window
            window_width = parent.winfo_reqwidth()
            window_height = parent.winfo_reqheight()

            # Calculate the position to center the window
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

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
