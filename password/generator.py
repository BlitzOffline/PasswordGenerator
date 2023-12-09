import secrets

from password.config import PasswordConfig


class PasswordGenerator:
    def __init__(self, password_config: PasswordConfig):
        self.password_config = password_config

    def generate_password(self) -> str:
        password = ''
        characters = self.password_config.characters
        for i in range(self.password_config.length.get()):
            password += secrets.choice(characters)
        return password
