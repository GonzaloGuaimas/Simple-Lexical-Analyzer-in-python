import ply.lex as lex

filename = 'example_text.txt'
tokens = ['TEXT','TAG_HTML','TAG_HEAD','TAG_TITLE','TAG_BODY','TAG_P','TAG_B','TAG_HR']
t_TEXT = r'[a-zA-Z0-9]+'
t_TAG_HTML = r'(<HTML>)'
t_TAG_HEAD = r'(<HEAD>|</HEAD>)'
t_TAG_TITLE = r'(<TITLE>|</TITLE>)'
t_TAG_BODY = r'(<BODY>)'
t_TAG_P = r'(<P>|</P>)'
t_TAG_B = r'(<B>|</B>)'
t_TAG_HR = r'(<HR>)'
t_ignore_ESPACIOS = r'[ ]+'

def t_error(t):
    print("Error: %s" % repr(t.value[0]))
    t.lexer.skip(1)
def t_line(t):
    r'\n'

try:
    f = open(filename)
    data = f.read()
    f.close()   
except:
    print('error')

lexer = lex.lex()
lexer.input(data)
print('TOKEN - LEXEME')
while True:
    token = lexer.token()
    if not token: break
    print('(',token.type,',',token.value,')')

