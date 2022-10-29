import ply.lex as lex 

reserved = {
  'PROG_BEGIN' : 'PROG_BEGIN',
  'PROG_END' : 'PROG_END',
  'ADD' : 'ADD_LIB_EXT',
  'int' : 'TD_ENTERO',
  'String' : 'TD_TEXTO',
  'float' : 'TD_DECIMAL',
  'bool' : 'TD_LOGICO',
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

tokens = [
  'FIN_LINEA',
  'PICO_OPEN',
  'PICO_CLOSE',
  'PARENT_OPEN',
  'PARENT_CLOSE',

  'EXTENSION',
  'COMA',

  'VALOR_ENTERO',
  'VALOR_TEXTO',
  'DECIMAL',
  'LOGICO',

  'DPUNTOS',
  
  'ASIGNAR',
  'OPERADOR',  

  'TIPO_PIN',

  'NOMBRE_VAR'
] + list(reserved.values())


#Exp. regulares
t_PUNTO = r'\.'

t_PICO_OPEN = r'<'
t_PICO_CLOSE = r'>'
t_PARENT_OPEN = r'\('
t_PARENT_CLOSE = r'\)'

t_EXTENSION = r'\.[a-zA-Z]+'
t_COMA = r'\,'

t_VALOR_ENTERO = r'[0-9]+'
t_VALOR_TEXTO = r'\".*\"'
t_DECIMAL = r'[0-9]+\.[0-9]+'

t_DPUNTOS = r'\:'
t_ASIGNAR = r'(:=)'
t_OPERADOR = r'(\+ | - | \* | \/ | >= | <= | == | !=)'

#3. Definimos una funcion para ignorar los espacios
t_ignore_ESPACIOS = r'[ ]+'
t_ignore_COMENT = r'(\/\/.*) | (\/\*.*\*\/) ' 

def t_NOMBRE_VAR(t):
  r'[a-zA-Z][a-zA-Z0-9_]+'
  t.type = reserved.get(t.value,'NOMBRE_VAR')    # Check for reserved words
  return t

def t_error(t):
  print("Se encontró un error en %s" % repr(t.value[0]))
  t.lexer.skip(1)
  
def t_newline(t):
  r'\n'
  t.lexer.lineno+=1

#4. Guardamos el archivo y generamos el compilador
__file__ = "Avance 1 Proyecto Compiladores.ipynb"
lexer = lex.lex()

#5. Probamos el analizador lexico pasandole una cadena
data = input("Ingrese una cadena: ")
lexer.input(data)

print('Token - Lexema')
while True:
  tok = lexer.token()
  if not tok: break
  print('(', tok.type, ',', tok.value, ')')