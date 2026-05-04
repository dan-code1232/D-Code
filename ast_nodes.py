class ProgramNode:
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Program({self.statements})"


class NumberNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"


class StringNode:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"String('{self.text}')"


class AccessVarNode:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Var({self.name})"


class AssignVarNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name} = {self.value}"


class SayNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Say({self.value})"


class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.op.value} {self.right})"


class RepeatNode:
    def __init__(self, times, body):
        self.times = times
        self.body = body

    def __repr__(self):
        return f"Repeat({self.times}, {self.body})"