import tkinter

from utils.constants import LOWERCASE_LETTERS, UPPERCASE_LETTERS, DIGITS, SYMBOLS


class PasswordConfig:
    def __init__(self, length: tkinter.IntVar, lowercase_letters: tkinter.BooleanVar,
                 uppercase_letters: tkinter.BooleanVar, digits: tkinter.BooleanVar, symbols: tkinter.BooleanVar,
                 extras: tkinter.StringVar, blacklist: tkinter.StringVar):
        self.length = length
        self.lowercase_letters = lowercase_letters
        self.uppercase_letters = uppercase_letters
        self.digits = digits
        self.symbols = symbols
        self.extras = extras
        self.blacklist = blacklist

    @property
    def characters(self):
        characters = ""
        if self.lowercase_letters.get():
            characters += LOWERCASE_LETTERS
        if self.uppercase_letters.get():
            characters += UPPERCASE_LETTERS
        if self.digits.get():
            characters += DIGITS
        if self.symbols.get():
            characters += SYMBOLS
        if self.extras.get():
            characters += self.extras.get()
        if self.blacklist.get():
            for character in self.blacklist.get():
                characters = characters.replace(character, '')

        final = self.de_duplicate(characters)

        if not final:
            return LOWERCASE_LETTERS

        return final

    @staticmethod
    def de_duplicate(characters: str) -> str:
        result = ""
        for character in characters:
            if character not in result:
                result += character
        return result
