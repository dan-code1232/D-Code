from ast_nodes import *

class Compiler:

    def __init__(self):
        self.code = []
        self.symbols = {}
        self.nextvar = 0

    def get_var(self, name):

        if name in self.symbols:
            return self.symbols[name]

        index = self.nextvar

        self.symbols[name] = index

        self.nextvar += 1

        return index
    

    def compile(self, node):



        if isinstance(node, ProgramNode):

            for stmt in node.statements:
                self.compile(stmt)


        elif isinstance(node, NumberNode):

            self.code.append(("PUSH", node.value))

        elif isinstance(node, AssignVarNode):

            self.compile(node.value)

            index = self.get_var(node.name)

            self.code.append(("STORE", index))
            
            
        elif isinstance(node, AccessVarNode):
            index = self.get_var(node.name)
            self.code.append(("LOAD", index))
        
        
        elif isinstance(node, BinOpNode):

            self.compile(node.left)
            self.compile(node.right)

            op = node.op.value

            if op == "+":
                self.code.append(("ADD",))

            elif op == "-":
                self.code.append(("SUBTRACT",))

            elif op == "*":
                self.code.append(("MULTIPLY",))

            elif op == "/":
                self.code.append(("DIVIDE",))

        return self.code