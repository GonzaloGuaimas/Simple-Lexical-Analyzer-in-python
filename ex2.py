import ply.lex as lex

tokens = ['CADMB']
counter = 0

def t_CADMB(t):
    r'[a-zA-Z]*(mb|MB|Mb|mB)+[a-zA-Z]*'
    global counter
    counter += 1
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
print('Numero de MB',counter)