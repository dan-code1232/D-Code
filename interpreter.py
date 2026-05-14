from ast_nodes import *
from randomgen import *

class Interpreter:
    def __init__(self):
        self.memory = {}
        self.rng = Random()

    def eval(self, node):

        # =====================================================
        # PROGRAM ROOT
        # =====================================================
        if isinstance(node, ProgramNode):
            result = None
            for s in node.statements:
                result = self.eval(s)
            return result

        # =====================================================
        # LITERALS
        # =====================================================
        elif isinstance(node, NumberNode):
            return node.value

        elif isinstance(node, StringNode):
            return node.value

        # =====================================================
        # VARIABLES
        # =====================================================
        elif isinstance(node, AccessVarNode):
            return self.memory.get(node.name, 0)

        elif isinstance(node, AssignVarNode):
            val = self.eval(node.value)
            self.memory[node.name] = val
            return val

        # =====================================================
        # INPUT / OUTPUT
        # =====================================================
        elif isinstance(node, InputNode):
            return float(input(">>> "))

        elif isinstance(node, SayNode):
            val = self.eval(node.value)
            print(val)
            return val

        # =====================================================
        # RANDOM
        # =====================================================
        elif isinstance(node, RandintNode):
            low = self.eval(node.low)
            high = self.eval(node.high)

            if low > high:
                low, high = high, low

            return low + (self.rng.next() % (high - low + 1))

        # =====================================================
        # IF STATEMENTS
        # =====================================================
        elif isinstance(node, IfNode):
            if self.eval(node.condition):
                result = None
                for stmt in node.body:
                    result = self.eval(stmt)
                return result
            else:
                result = None
                for stmt in node.else_body:
                    result = self.eval(stmt)
                return result

        # =====================================================
        # BINARY OPERATIONS (MATH CORE)
        # =====================================================
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

        # =====================================================
        # LOOPS
        # =====================================================
        elif isinstance(node, RepeatNode):

            times = int(self.eval(node.times))
            result = None

            for _ in range(times):
                for s in node.body:
                    result = self.eval(s)

            return result

        # =====================================================
        # SAFETY FALLBACK
        # =====================================================
        else:
            raise Exception(f"Unknown node type: {type(node)}")