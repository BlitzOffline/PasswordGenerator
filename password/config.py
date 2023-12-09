import tkinter


class PasswordConfig:
    def __init__(self, length: tkinter.IntVar, lowercase_letters: tkinter.BooleanVar,
                 uppercase_letters: tkinter.BooleanVar, numbers: tkinter.BooleanVar, symbols: tkinter.BooleanVar,
                 extras: tkinter.StringVar, blacklist: tkinter.StringVar):
        self.length = length
        self.lowercase_letters = lowercase_letters
        self.uppercase_letters = uppercase_letters
        self.numbers = numbers
        self.symbols = symbols
        self.extras = extras
        self.blacklist = blacklist

    @property
    def characters(self):
        characters = ""
        if self.lowercase_letters.get():
            characters += "abcdefghijklmnopqrstuvwxyz"
        if self.uppercase_letters.get():
            characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.numbers.get():
            characters += "0123456789"
        if self.symbols.get():
            characters += "!@#$%^&*"
        if self.extras.get():
            characters += self.extras.get()
        if self.blacklist.get():
            for character in self.blacklist.get():
                characters = characters.replace(character, '')

        final = self.de_duplicate(characters)

        if not final:
            self.lowercase_letters.set(True)
            return "abcdefghijklmnopqrstuvwxyz"

        return final

    @staticmethod
    def de_duplicate(characters: str) -> str:
        result = ""
        for character in characters:
            if character not in result:
                result += character
        return result
