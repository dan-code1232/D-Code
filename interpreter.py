from ast_nodes import *

class Interpreter:
    def __init__(self):
        self.memory = {}

    def eval(self, node):

        if isinstance(node, ProgramNode):
            for s in node.statements:
                self.eval(s)

        elif isinstance(node, NumberNode):
            return node.value

        elif isinstance(node, StringNode):
            return node.value

        elif isinstance(node, AccessVarNode):
            return self.memory.get(node.name, 0)

        elif isinstance(node, AssignVarNode):
            val = self.eval(node.value)
            self.memory[node.name] = val
            return val

        elif isinstance(node, SayNode):
            print(self.eval(node.value))

        elif isinstance(node, BinOpNode):
            l = self.eval(node.left)
            r = self.eval(node.right)

            op = node.op.value

            if op == "+":
                return l + r
            if op == "-":
                return l - r
            if op == "*":
                return l * r
            if op == "/":
                return l / r

            if op == "EQ":
                return l == r
            if op == "NE":
                return l != r
            if op == "GT":
                return l > r
            if op == "LT":
                return l < r
            if op == "GTE":
                return l >= r
            if op == "LTE":
                return l <= r

        elif isinstance(node, RepeatNode):
            times = int(self.eval(node.times))
            for _ in range(times):
                for s in node.body:
                    self.eval(s)
