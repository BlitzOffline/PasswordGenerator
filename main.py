from app import App


def run():
    app = App()
    app.iconbitmap(bitmap="assets/icon.ico")
    app.mainloop()


if __name__ == '__main__':
    run()
