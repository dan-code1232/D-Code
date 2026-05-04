from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

code = """
x = 5
y = 10
say x + y
repeat 3
    say 'hi'
end
"""

lexer = Lexer(code)
tokens = lexer.tokenise()

parser = Parser(tokens)
ast = parser.parse()

print(ast)

Interpreter().eval(ast)