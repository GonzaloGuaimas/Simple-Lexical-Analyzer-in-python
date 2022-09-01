import ply.lex as lex

#TOKENS DECLARATION
tokens = ['ID','NUM','OP','SUM','REST','PRODUCT','DIVIDE','LPAREN','RPAREN']

#INIT TOKENS
t_ID = r'[a-zA-Z][a-zA-Z0-9_]*'
t_NUM = r'[0-9]+'
t_OP = '[<>]'
t_SUM    = r'\+'
t_REST   = r'-'
t_PRODUCT   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
#IGNORE SPACES
t_ignore_ESPACIOS = r'[ ]+'

##FUNCTIONS
#ERRORS
def t_error(t):
    print("Se encontró un error: %s" % repr(t.value[0]))
    t.lexer.skip(1)
#lines counter
def t_newline(t):
  r'\n'
  t.lexer.lineno+=1

#CONSTRUCTOR LEXICAL ANALYZER
lexer = lex.lex()

#FILE NAME
filename='example_text.txt'

#OPEN FILE TO READ
try:
    f = open(filename)
    data = f.read()
    f.close()   
except IndexError:
    print('Error')
    data=''
#START LEXICAL ANALYZER
lexer.input(data)

print('TOKEN - LEXEME - LINE')
while True:
    tok = lexer.token()
    if not tok: break
    print('(',tok.type, ',',tok.value, ',',tok.lineno,')')