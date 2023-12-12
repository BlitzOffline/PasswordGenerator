import zxcvbn


class PasswordChecker:
    @staticmethod
    def strength_check(password: str, user_input: set[str] = None):
        return zxcvbn.zxcvbn(password=password, user_inputs=user_input)
