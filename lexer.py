class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}" if self.value is not None else f"{self.type}"


class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.length = len(code)

        self.nums = "0123456789"
        self.text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
        self.keywords = ["say", "repeat", "end", "if", "else","random_num"]

    def current(self):
        return self.code[self.pos] if self.pos < self.length else None

    def peek(self):
        nxt = self.pos + 1
        return self.code[nxt] if nxt < self.length else None

    def move(self):
        self.pos += 1

    def skip_whitespace(self):
        while self.current() and self.current().isspace() and self.current() != "\n":
            self.move()

    def number(self):
        num = []
        while self.current() and (self.current() in self.nums or self.current() == "."):
            num.append(self.current())
            self.move()
        return Token("NUMBER", float("".join(num)))

    def identifier(self):
        text = []
        while self.current() and (self.current() in self.text or self.current() in self.nums):
            text.append(self.current())
            self.move()

        value = "".join(text)

        if value in self.keywords:
            return Token("KEYWORD", value)

        return Token("IDENTIFIER", value)

    def string(self):
        self.move()  # skip opening '
        chars = []

        while self.current() and self.current() != "'":
            chars.append(self.current())
            self.move()

        self.move()  # skip closing '
        return Token("STRING", "".join(chars))

    def tokenise(self):
        tokens = []

        while self.current():

            c = self.current()

            if c == "\n":
                tokens.append(Token("NEWLINE"))
                self.move()
                continue

            if c.isspace():
                self.skip_whitespace()
                continue

            if c == "'":
                tokens.append(self.string())
                continue

            # ---------------- COMPARISONS ----------------

            if c == "=" and self.peek() == "=":
                tokens.append(Token("EQ", "EQ"))
                self.move()
                self.move()
                continue

            if c == "!" and self.peek() == "=":
                tokens.append(Token("NE", "NE"))
                self.move()
                self.move()
                continue

            if c == ">" and self.peek() == "=":
                tokens.append(Token("GTE", "GTE"))
                self.move()
                self.move()
                continue

            if c == "<" and self.peek() == "=":
                tokens.append(Token("LTE", "LTE"))
                self.move()
                self.move()
                continue

            if c == ">":
                tokens.append(Token("GT", "GT"))
                self.move()
                continue

            if c == "<":
                tokens.append(Token("LT", "LT"))
                self.move()
                continue
            
            if c in "(":
                tokens.append(Token("LBRACKET",c))
                self.move()
                continue
            
            if c in ")":
                tokens.append(Token("RBRACKET",c))
                self.move()
                continue
            if c in ",":
                tokens.append(Token("COMA",c))
                self.move()
                continue
                  
            # ---------------- MATH OPS ----------------

            if c in "+-*/=":
                tokens.append(Token("OPERATOR", c))
                self.move()
                continue

            # ---------------- NUMBERS ----------------

            if c in self.nums:
                tokens.append(self.number())
                continue

            # ---------------- IDENTIFIERS ----------------

            if c in self.text:
                tokens.append(self.identifier())
                continue

            raise Exception(f"Illegal character: {c}")

        return tokens
