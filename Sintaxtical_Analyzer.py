import ply.lex as lex 
from ply import yacc
# Import Data
filename='textoPrueba2.txt'
try:
    f = open(filename)
    data = f.read()
    f.close()   
except IndexError:
    print('Error')
    data=''

reserved = {
  'PROG_BEGIN' : 'PROG_BEGIN',
  'PROG_END' : 'PROG_END',
  'ADD' : 'ADD_LIB_EXT',
  'entero' : 'TD_ENTERO',
  'texto' : 'TD_TEXTO',
  'decimal' : 'TD_DECIMAL',
  'logico' : 'TD_LOGICO',
  'VAR' : 'DEF_VAR',
  'FUNC' : 'DEF_FUN',
  'retorno' : 'RETORNO',
  'PIN' : 'DEF_PIN',

  'TRUE' : 'BOOL_T',
  'FALSE' : 'BOOL_F',
  'OUT' :  'TP_OUT',
  'INP' : 'TP_INP',

  'IF' : 'IF',
  'ELSE' : 'ELSE',
  'BEGIN' : 'BEGIN',
  'END' : 'END',
  'WHILE' : 'WHILE',

  'FOWARD' : 'FWD',
  'BACKWARD' : 'BWD',
  'LEFT' : 'LEFT',
  'RIGHT' : 'RIGHT',
  'WAIT' : 'WAIT',
  'STOP' : 'STOP',
  }

tokens = ['PUNTO','PICO_OPEN','PICO_CLOSE','PARENT_OPEN','PARENT_CLOSE','COMA','VALOR_ENTERO','VALOR_TEXTO','DECIMAL','LOGICO','DPUNTOS','ASIGNAR','OPERADOR','NOMBRE_VAR'] + list(reserved.values())

#Exp. regulares
t_PUNTO = r'\.' #change name more general
t_PICO_OPEN = r'<'
t_PICO_CLOSE = r'>'
t_PARENT_OPEN = r'\('
t_PARENT_CLOSE = r'\)'
t_COMA = r'\,'
t_VALOR_ENTERO = r'[0-9]+'
t_VALOR_TEXTO = r'\".*\"'
t_DECIMAL = r'[0-9]+\.[0-9]+'
t_ASIGNAR = r'(:=)'
t_DPUNTOS = r'\:'
t_OPERADOR = r'(\+ | - | >= | <= | == | !=)' # disable / signs
#3. Ignores
t_ignore_ESPACIOS = r'[ ]+'
t_ignore_COMENT =  r'(/\*(.|\n)*?\*/)|(//.*)' #fix

def t_NOMBRE_VAR(t):
  r'[a-zA-Z][a-zA-Z0-9_]+'
  t.type = reserved.get(t.value,'NOMBRE_VAR') # Check for reserved words
  return t

def t_error(t):
  print("Se encontró un error en %s" % repr(t.value[0]))
  t.lexer.skip(1)
  
def t_newline(t):
  r'\n'
  t.lexer.lineno+=1

#-------------------------------------------------------------------------------------------------
def p_S(p):
  '''S : PROG_BEGIN LIBS CUERPO PROG_END'''
  pass
def p_CUERPO(p):
  '''CUERPO : SENTENCIA PUNTO CUERPO 
    | empty'''
  pass
def p_SENTENTCIA(p):
  '''SENTENCIA : DEF_VBLES 
    | ASIGNACIONES
    | SETUP
    | LOOP PICO_OPEN PICO_CLOSE'''
  pass

#def loops-------------------------------------------------------------
def p_SETUP(p):
  '''SETUP : DEF_PIN PICO_OPEN TIPO_PIN DPUNTOS TD_ENTERO PICO_CLOSE
    | DEF_PIN PICO_OPEN TIPO_PIN DPUNTOS NOMBRE_VAR PICO_CLOSE'''
  pass
def p_TIPO_PIN(p):
  '''TIPO_PIN : TP_OUT 
    | TP_INP'''
  pass
#def setup-------------------------------------------------------------
def p_LOOP(p):
  '''LOOP : BWD
    | FWD
    | RIGHT
    | LEFT
    | WAIT
    | STOP'''
  pass
#definición de Variables----------------------------------------------
def p_DEF_VBLES(p):
  '''DEF_VBLES : DEF_VAR PICO_OPEN VARIABLE PICO_CLOSE'''
  pass
def p_VARIABLE(p):
  '''VARIABLE : TIPO DPUNTOS NOMBRE_VAR'''
  pass
def p_TIPO(p):
  '''TIPO : TD_ENTERO
    | TD_TEXTO
    | TD_DECIMAL
    | TD_LOGICO'''
  pass
#asignaciones-----------------------------------------------------------
def p_ASIGNACIONES(p):
  '''ASIGNACIONES : NOMBRE_VAR ASIGNAR ASIGN_LDERECHO'''
  pass
def p_ASIGN_LDERECHO(p):
  '''ASIGN_LDERECHO : NOMBRE_VAR 
    | VALOR_ENTERO
    | VALOR_TEXTO
    | DECIMAL
    | LOGICO'''
  pass

#Producciones Librerías------------------------------------------------
def p_LIBS(p):
  '''LIBS : ADD_LIB_EXT PICO_OPEN LIBRERIA PICO_CLOSE PUNTO'''
  pass
def p_LIBRERIA(p):
  '''LIBRERIA : NOMBRE_VAR PUNTO NOMBRE_VAR 
    | NOMBRE_VAR PUNTO NOMBRE_VAR COMA LIBRERIA'''
  pass
def p_empty(p):
  '''empty : '''
  pass

def p_error(p):
  print("Error sintáctico en la línea: " + str(p.lineno)
              + ". No se esperaba el token: " + str(p.value))        
  raise Exception('syntax', 'error')



#DEF LEX
lexer = lex.lex()
lexer.input(data)
parser = yacc.yacc('LALR')

print('Token - Lexema - Line')
while True:
  tok = lexer.token()
  if not tok: break
  print('(', tok.type, ',', tok.value, ',', tok.lineno, ')')

try:
  print('ANALISIS SINTÁCTICO')
  parser.parse(data)
  print('¡Analisis sintactico corecto!')           
except: 
  print ('Analisis sintáctico incorrecto')