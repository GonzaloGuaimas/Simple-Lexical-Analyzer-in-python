
import ply.lex as lex

tokens = ['TEXTO']
t_TEXTO = r'[//]|(/\*)|(\*/)'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

while True:
    text = input('Ingresar cadena:  ')
    lexer.input(text)
    print('TOKEN - LEXEME')
    while True:
        token = lexer.token()
        if not token: break
        print('(',token.type,',',token.value,')')
