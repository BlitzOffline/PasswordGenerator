from app import App
from paths import get_app_path


def run():
    app = App()
    app.iconbitmap(bitmap=f"{get_app_path()}/assets/icon.ico")
    app.mainloop()


if __name__ == '__main__':
    run()
