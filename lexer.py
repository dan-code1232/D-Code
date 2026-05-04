class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}" if self.value is not None else f"{self.type}"


class Lexer:
    def __init__(self, code):
        self.code = code
        self.nums = "1234567890"
        self.char = 0
        self.length = len(self.code)
        self.operators = "+-*/="
        self.string_begin = "'"
        self.text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
        self.keywords = ["say", "repeat", "end"]

    def move(self):
        self.char += 1

    def current_char(self):
        return self.code[self.char] if self.char < self.length else None

    def skip_whitespace(self):
        while self.current_char() and self.current_char().isspace() and self.current_char() != "\n":
            self.move()

    def get_nums(self):
        c = self.current_char()
        return c is not None and (c in self.nums or c == ".")

    def get_text(self):
        c = self.current_char()
        return c is not None and (c in self.text or c in self.nums)

    def get_string(self):
        self.move()
        chars = []

        while self.current_char() and self.current_char() != self.string_begin:
            chars.append(self.current_char())
            self.move()

        if self.current_char() is None:
            raise Exception("Unterminated string")

        self.move()
        return Token("STRING", "".join(chars))

    def number(self):
        num = []
        while self.get_nums():
            num.append(self.current_char())
            self.move()
        return Token("NUMBER", float("".join(num)))

    def identifier(self):
        text = []
        while self.get_text():
            text.append(self.current_char())
            self.move()

        value = "".join(text)

        if value in self.keywords:
            return Token("KEYWORD", value)

        return Token("IDENTIFIER", value)

    def tokenise(self):
        tokens = []

        while self.current_char():
            c = self.current_char()

            if c == "\n":
                tokens.append(Token("NEWLINE"))
                self.move()
                continue

            if c.isspace():
                self.skip_whitespace()
                continue

            if c == "'":
                tokens.append(self.get_string())
                continue

            if c in self.operators:
                tokens.append(Token("OPERATOR", c))
                self.move()
                continue

            elif c in self.nums:
                tokens.append(self.number())
                continue

            elif c in self.text:
                tokens.append(self.identifier())
                continue

            else:
                raise Exception(f"Illegal character: {c}")

        return tokens