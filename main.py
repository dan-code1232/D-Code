from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

code = """
if 10 == 10 
	say 'hi'
else 
	say'bye'
end
"""

lexer = Lexer(code)
tokens = lexer.tokenise()

parser = Parser(tokens)
ast = parser.parse()


Interpreter().eval(ast)
