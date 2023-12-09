from password.config import PasswordConfig
from password.generator import PasswordGenerator


class PasswordManager:
    def __init__(self, password_config: PasswordConfig, callbacks=None):
        if callbacks is None:
            callbacks = {}

        self.password_generator = PasswordGenerator(password_config)
        self.callbacks = callbacks
        self.password = None
        self.regenerate_password()

    def regenerate_password(self):
        self.password = self.password_generator.generate_password()
        self.notify_callbacks(self.password)

    def add_callback(self, name, callback, *args, **kwargs):
        self.callbacks[name] = lambda password: callback(password, *args, **kwargs)

    def remove_callback(self, name):
        self.callbacks.remove(name)

    def notify_callbacks(self, password: str):
        for name, callback in self.callbacks.items():
            callback(password)
