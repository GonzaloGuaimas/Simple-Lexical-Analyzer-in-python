import ply.lex as lex
from ply import yacc

#TOKEN
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
    t.lexer.skip(1)
def t_newline(t):
  r'\n'
  t.lexer.lineno+=1

lexer = lex.lex()

#####################################################

def p_S(p):
  '''S : TAG_HTML H B TAG_HTML'''
  pass
def p_H(p):
  '''H : TAG_HEAD T TAG_HEAD'''
  pass
def p_T(p):
  '''T : TAG_TITLE L TAG_TITLE'''
  pass
def p_B(p):
  '''B : TAG_BODY P'''
  pass
def p_P(p):
  '''P : TAG_P L C TAG_HR TAG_P'''
  pass
def p_C(p):
  '''C : TAG_B L TAG_B'''
  pass
def p_L(p):
  '''L : TEXT
        | empty'''
  pass
def p_empty(p):
  '''empty : '''
  pass


def p_error(p):
  print("Error sintáctico en la línea: " + str(p.lineno)
              + ". No se esperaba el token: " + str(p.value))        
  raise Exception('syntax', 'error')


parser = yacc.yacc('LALR')

try:
        while True:
          data=input('Ingrese cadena: ')
          data = '<HTML>\n<HEAD>\n<TITLE> Practica </TITLE>\n</HEAD>\n<BODY>\n<P> Analizador <B> HTML </B>\n<HR>\n</P>\n<HEAD>'
          lexer.input(data)   
          print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
          print('ANALISIS LÉXICO')
          print('TOKEN-LEXEMA')
          while True:
                  tok = lexer.token()
                  if not tok: break
                  print(tok.type,' - ',tok.value)
          print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
          print('ANALISIS SINTÁCTICO')
          parser.parse(data)
          print('¡Analisis sintactico corecto!')            
except:
        print('Analisis sintactico incorrecto')