import time

class VM:
    def __init__(self):
        self.vars = []
        self.stack = []
        self.instruction_count = 0

    def run(self, code):
        ip = 0
        self.instruction_count = 0

        stack = self.stack
        vars_ = self.vars

        while ip < len(code):
            curr = code[ip]
            op = curr[0]

            self.instruction_count += 1

            if op == "PUSH":
                stack.append(curr[1])

            elif op == "ADD":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            elif op == "MULTIPLY":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            elif op == "SUBTRACT":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif op == "DIVIDE":
                b = stack.pop()
                a = stack.pop()
                stack.append(a / b)

            elif op == "STORE":
                index = curr[1]
                value = stack.pop()

                while len(vars_) <= index:
                    vars_.append(None)

                vars_[index] = value

            elif op == "LOAD":
                index = curr[1]
                stack.append(vars_[index])

            ip += 1