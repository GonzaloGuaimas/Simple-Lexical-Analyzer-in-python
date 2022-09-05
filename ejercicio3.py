import ply.lex as lex

#TOKEN
tokens = ['CADENA']

t_CADENA = r'[1][0-1]*[0][0]|[0][0-1]*[1][1]'

def t_error(t):
    print("Se encontró un error: %s" % repr(t.value[0]))
    t.lexer.skip(1)

#CONSTRUCTOR LEXICAL ANALYZER
lexer = lex.lex()

while True:
    data=input('Ingrese cadena: ')

    lexer.input(data)

    print('TOKEN-LEXEMA')
    while True:
        tok = lexer.token()
        if not tok: break
        print(tok.type,' - ',tok.value)