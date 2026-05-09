from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

code = """
say 10 == 5
x = 5
y = 10
say x + y
repeat 3
    say 'hi'
end
"""

lexer = Lexer(code)
tokens = lexer.tokenise()
print(tokens)
parser = Parser(tokens)
ast = parser.parse()

print(ast)

Interpreter().eval(ast)
