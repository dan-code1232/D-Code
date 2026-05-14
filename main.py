from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from Compiler import Compiler
from VM import VM

interp = Interpreter()
vm = VM()

mode = ""

while mode not in ["1", "2"]:

    print()
    print("D-CODE")
    print()
    print("1 - Interpreter")
    print("2 - VM")
    print()

    mode = input("Select mode: ")

print()

def show_mode():
    if mode == "1":
        print("Switched to Interpreter")
    else:
        print("Switched to VM")

show_mode()

print("Type 'exit' to quit")
print("Type 'change' to switch mode")
print()

while True:

    code = input(">>> ").strip()

    if code.lower() == "exit":
        break

    if code.lower() == "change":
        mode = "2" if mode == "1" else "1"
        show_mode()
        continue

    try:

        lexer = Lexer(code)
        tokens = lexer.tokenise()

        parser = Parser(tokens)
        ast = parser.parse()

        if mode == "1":

            result = interp.eval(ast)

            if result is not None:
                print(result)

        else:

            compiler = Compiler()
            bytecode = compiler.compile(ast)

            vm.run(bytecode)

            if vm.stack:
                print(vm.stack[-1])

    except Exception as e:
        print("Error:", e)