import ply.lex as lex

tokens = ['MAY','MIN']
counterMAY = 0
counterMIN = 0

def t_MAY(t):
    r'[A-Z]+'
    global counterMAY
    counterMAY += 1
    return t
def t_MIN(t):
    r'[a-z]+'
    global counterMIN
    counterMIN += 1
    return t
def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
filename = 'example_text.txt'

try:
    f = open(filename)
    data = f.read()
    f.close()   
except IndexError:
    print('Error')
    data=''

lexer.input(data)
print('TOKEN - LEXEME')
while True:
    tok = lexer.token()
    if not tok: break
    print('(',tok.type, ',',tok.value, ',',tok.lineno,')')
print('Numero de MAY',counterMAY)
print('Numero de MIN',counterMIN)