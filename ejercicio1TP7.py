import ply.lex as lex
from ply import yacc

#TOKEN
tokens = ['E','T','F','PRODUCT','NUMBER','PAREN','ADDITION']

t_E = r'(E)'
t_T = r'(T)'
t_F = r'(F)'
t_PRODUCT = r'\*'
t_NUMBER = r'[0-9]+'
t_PAREN = r'(\(|\))+'
t_ADDITION = r'\+'

def t_error(t):
    t.lexer.skip(1)
def t_newline(t):
  r'\n'
  t.lexer.lineno+=1

lexer = lex.lex()

#####################################################

def p_EE(p):
  '''EE : EE ADDITION TT
        | TT'''
  pass
def p_TT(p):
  '''TT : TT PRODUCT FF
        | FF'''
  pass
def p_FF(p):
  '''FF : NUMBER
        | PAREN EE PAREN'''
  pass

def p_error(p):
  print("Error sintáctico en la línea: " + str(p.lineno)
              + ". No se esperaba el token: " + str(p.value))        
  raise Exception('syntax', 'error')


parser = yacc.yacc('LALR')

try:
        while True:
          data=input('Ingrese cadena: ')
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