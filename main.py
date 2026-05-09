from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

code = """
random_num (50,30)
if 10 == 10 
	say 'hi'
else 
	say'bye'
end
"""

lexer = Lexer(code)
tokens = lexer.tokenise()
print(tokens)
parser = Parser(tokens)
ast = parser.parse()
print(ast)
Interpreter().eval(ast)
