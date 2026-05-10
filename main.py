from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

code = """
say '=== DRAGON HUNT ==='
say '3 rounds. Beat dragon each time!'
score = 0
say'The lower you guess,if you beat the dragon,the more points you get'
num = 1
repeat 3
    say 'Round '
    say num
    num = num +  1
    player_roll = input
    
    dragon_roll = random_num(1,10)
    say 'Dragon rolls:'
    say dragon_roll
    
    if player_roll > dragon_roll
        say 'You WIN the round!'
        player_roll = 10 - player_roll
        score = score + player_roll
    else
        say 'Dragon wins round!'
    end
end

say 'Final score:'
say score
if score > 5
    say 'HERO VICTORY!'
else
    say 'Try harder next time!'
end

"""

lexer = Lexer(code)
tokens = lexer.tokenise()

parser = Parser(tokens)
ast = parser.parse()

Interpreter().eval(ast)
