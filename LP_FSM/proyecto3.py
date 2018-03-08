"""
    Lenguajes de Programacion
    Jose Luis Garcia Reymundo
    A01063645
    Proyecto 3
"""

from types import *

tipos_token = [ 'no_valido', 'Variable', 'Variable', 'Variable', 'no_valido',
                'no_valido', 'Entero', 'no_valido', 'Real','no_valido','no_valido',
                'Real', 'no_valido', 'no_valido', 'Resta', 'no_valido', 'Suma',
                'Asignacion', 'Multiplicacion', 'Division', 'no_valido',
                'Comentario', 'Potencia', 'no_valido', 'Simbolo especial',
                'Simbolo especial']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
funcion_transicion = {  (0, 'letra'): 1,
                        (1, 'letra'): 1,
                        (1, 'digito'): 2,
                        (1, 'underscore'): 3,
                        (2, 'digito'): 2,
                        (2, 'underscore'): 3,
                        (2, 'letra'): 1,
                        (3, 'digito'): 2,
                        (3, 'letra'): 1,
                        (0, 'digito'): 6,
                        (6, 'digito'): 6,
                        (6, 'punto'): 8,
                        (8, 'digito'): 8,
                        (8, 'E'): 10,
                        (10, 'digito'): 11,
                        (10, 'resta'): 12,
                        (12, 'digito'): 11,
                        (11, 'digito'): 11,
                        (0, 'resta'): 14,
                        (14, 'digito'): 6,
                        (0, 'suma'): 16,
                        (0, 'asignacion'): 17,
                        (0, 'multiplicacion'): 18,
                        (0, 'division'): 19,
                        (0, 'potencia'): 22,
                        (0, 'simbolo'): 24,
                        (0, 'simbolo'): 25,
                        (19, 'division'): 21,
                        (21, 'letra'): 21,
                        (21, 'digito'): 21,
                        (21, 'underscore'): 21,
                        (21, 'punto'): 21,
                        (21, 'E'): 21,
                        (21, 'resta'): 21,
                        (21, 'suma'): 21,
                        (21, 'asignacion'): 21,
                        (21, 'multiplicacion'): 21,
                        (21, 'division'): 21,
                        (21, 'potencia'): 21,
                        (21, 'simbolo'): 21,
                    }
estados_finales = [1,2,3,6,8,11,14,16,17,18,19,21,22,24,25]

def automata(cadena, estado_actual):
    """
        Automata que detecta el tipo de token de acuerdo a la tabla de transicion
        Recibe la cadena a evaluar
        el estado actual
    """
    if len(cadena) is 0:
        if estado_actual in estados_finales:
            return get_token(estado_actual)
    else:
        entrada = detecta_tipo(cadena[0])
        print(entrada)
        #print(type(cadena[0:1][0]))
        if (estado_actual, entrada) in funcion_transicion:
            return automata(cadena[1:], funcion_transicion[(estado_actual,entrada)])
        else:
            return 'Token no valido'


def detecta_tipo(elemento):
    if elemento in numeros:
        return 'digito'
    elif elemento == "_":
        return 'underscore'
    elif elemento == ".":
        return 'punto'
    elif elemento == "-":
        return 'resta'
    elif elemento == "+":
        return 'suma'
    elif elemento == "*":
        return 'multiplicacion'
    elif elemento == "/":
        return 'division'
    elif elemento == "^":
        return 'potencia'
    elif elemento == "=":
        return 'asignacion'
    elif elemento == "(" or elemento == ")":
        return 'simbolo'
    elif elemento == "E":
        return 'E'
    elif elemento.isspace():
        return 'espacio'
    elif type(elemento) is StringType:
        return 'letra'
    else:
        return 'no_valido'


def get_token(item):
    return tipos_token[item]


def main():
    linea = "pablito"
    cadena = list(linea)
    print(cadena)
    result = automata(cadena, 0)
    print(result)

if __name__ == "__main__":
    main()
