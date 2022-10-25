import ply.lex as lex
from ply import yacc

#TOKEN
tokens = ['PROC','IDENT','PAREN','VAR','CONST']

t_PROC =  r'(proc)'
t_IDENT = r'(ident)'
t_PAREN = r'(\(|\))+'
t_VAR = r'(var)'
t_CONST = r'(const)'

def t_error(t):
    t.lexer.skip(1)
def t_newline(t):
  r'\n'
  t.lexer.lineno+=1

lexer = lex.lex()

#####################################################

def p_S(p):
  '''S : PROC IDENT PAREN P PAREN'''
  pass
def p_P(p):
  '''P : VAR P
        | CONST P 
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