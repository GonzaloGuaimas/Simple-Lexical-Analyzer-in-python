#CANTIDAD DE PALABRAS QUE TIENE MAS DE DOS DIGITOS
import ply.lex as lex

#TOKEN
tokens = ['NUM']

counterMAY = 0

def t_NUM(t):
    r'[a-zA-Z]*[0-9]+[0-9]+[a-zA-Z]*'
    global counterMAY
    counterMAY += 1
    return t

def t_error(t):
    print("Se encontró un error: %s" % repr(t.value[0]))
    t.lexer.skip(1)

lexer = lex.lex()
#CONSTRUCTOR LEXICAL ANALYZER
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