from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current = tokens[0] if tokens else None

    def move(self):
        self.pos += 1
        self.current = self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def parse(self):
        statements = []

        while self.current:
            if self.current.type == "NEWLINE":
                self.move()
                continue

            stmt = self.parse_comparison()

            if stmt:
                statements.append(stmt)
            else:
                self.move()

        return ProgramNode(statements)

    def parse_expression(self):
        left = self.parse_term()

        while self.current and self.current.type == "OPERATOR" and self.current.value in "+-":
            op = self.current
            self.move()
            right = self.parse_term()
            left = BinOpNode(left, op, right)

        if self.current and self.current.type == "OPERATOR" and self.current.value == "=":
            if isinstance(left, AccessVarNode):
                name = left.name
                self.move()
                value = self.parse_expression()
                return AssignVarNode(name, value)

        return left

    def parse_term(self):
        left = self.parse_factor()

        while self.current and self.current.type == "OPERATOR" and self.current.value in "*/":
            op = self.current
            self.move()
            right = self.parse_factor()
            left = BinOpNode(left, op, right)

        return left

    def parse_comparison(self):
        left = self.parse_expression()

        while self.current and self.current.type in ("EQ", "NE", "GT", "LT", "GTE", "LTE"):
            op = self.current
            self.move()
            right = self.parse_expression()
            left = BinOpNode(left, op, right)

        return left

    def parse_factor(self):
        c = self.current

        if not c:
            return None

        if c.type == "NUMBER":
            self.move()
            return NumberNode(c.value)

        if c.type == "STRING":
            self.move()
            return StringNode(c.value)

        if c.type == "KEYWORD":

            if c.value == "say":
                self.move()
                return SayNode(self.parse_comparison())

            if c.value == "if":
                self.move()

                condition = self.parse_comparison()
                body = []
                elsebody = []

                while self.current and not (
                    self.current.type == "KEYWORD" and self.current.value in ["end", "else"]
                ):
                    if self.current.type == "NEWLINE":
                        self.move()
                        continue

                    body.append(self.parse_expression())

                if self.current and self.current.type == "KEYWORD" and self.current.value == "else":
                    self.move()

                    while self.current and not (
                        self.current.type == "KEYWORD" and self.current.value == "end"
                    ):
                        if self.current.type == "NEWLINE":
                            self.move()
                            continue

                        elsebody.append(self.parse_expression())

                self.move()  # consume "end"

                return IfNode(condition, body, elsebody)

            if c.value == "repeat":
                self.move()
                times = self.parse_expression()
                body = []

                while self.current and not (self.current.type == "KEYWORD" and self.current.value == "end"):
                    if self.current.type == "NEWLINE":
                        self.move()
                        continue
                    body.append(self.parse_expression())

                self.move()
                return RepeatNode(times, body)

        if c.type == "IDENTIFIER":
            name = c.value
            self.move()
            return AccessVarNode(name)

        return None
