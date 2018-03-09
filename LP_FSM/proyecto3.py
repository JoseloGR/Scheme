"""
    Lenguajes de Programacion
    Jose Luis Garcia Reymundo
    A01063645
    Proyecto 3

    Correr:
        python proyecto3.py
"""
import os, sys
from types import *

filepath = 'expresiones.txt'

tipos_token = [ 'no_valido', 'Variable', 'Variable', 'Variable', 'no_valido',
                'Variable', 'Entero', 'Entero', 'Real','Real','no_valido',
                'Real', 'no_valido', 'Real', 'Resta', 'no_valido', 'Suma',
                'Asignacion', 'Multiplicacion', 'Division', 'no_valido',
                'Comentario', 'Potencia', 'Comentario', 'Simbolo especial',
                'Simbolo especial']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
funcion_transicion = {  (0, 'letra'): 1,
                        (0, 'digito'): 6,
                        (0, 'punto'): 8,
                        (0, 'resta'): 14,
                        (0, 'suma'): 16,
                        (0, 'asignacion'): 17,
                        (0, 'multiplicacion'): 18,
                        (0, 'division'): 19,
                        (0, 'potencia'): 22,
                        (0, 'simbolo_a'): 24,
                        (0, 'simbolo_c'): 25,
                        (0, 'espacio'): 0,
                        (1, 'letra'): 1,
                        (1, 'digito'): 2,
                        (1, 'underscore'): 3,
                        (1, 'fin'): 5,
                        (2, 'fin'): 5,
                        (2, 'espacio'): 5,
                        (2, 'digito'): 2,
                        (2, 'underscore'): 3,
                        (2, 'letra'): 1,
                        (3, 'digito'): 2,
                        (3, 'letra'): 1,
                        (3, 'underscore'): 3,
                        (3, 'espacio'): 5,
                        (3, 'fin'): 5,
                        (5, 'espacio'): 5,
                        (5, 'fin'): 0,
                        (5, 'asignacion'): 0,
                        (5, 'digito'): 0,
                        (6, 'digito'): 6,
                        (6, 'fin'): 7,
                        (6, 'punto'): 8,
                        (8, 'digito'): 8,
                        (8, 'multiplicacion'): 0,
                        (8, 'fin'): 9,
                        (8, 'E'): 10,
                        (10, 'digito'): 11,
                        (10, 'resta'): 12,
                        (11, 'digito'): 11,
                        (11, 'fin'): 13,
                        (12, 'digito'): 11,
                        (14, 'digito'): 6,
                        (14, 'letra'): 1,
                        (17, 'espacio'): 0,
                        (17, 'fin'): 0,
                        (17, 'digito'): 6,
                        (18, 'simbolo_a'): 0,
                        (19, 'division'): 21,
                        (21, 'letra'): 23,
                        (21, 'digito'): 23,
                        (21, 'underscore'): 23,
                        (21, 'punto'): 23,
                        (21, 'E'): 23,
                        (21, 'resta'): 23,
                        (21, 'suma'): 23,
                        (21, 'asignacion'): 23,
                        (21, 'multiplicacion'): 23,
                        (21, 'division'): 23,
                        (21, 'potencia'): 23,
                        (21, 'simbolo_a'): 23,
                        (21, 'simbolo_c'): 23,
                        (21, 'fin'): 23,
                        (21, 'espacio'): 23,
                        (23, 'espacio'): 23,
                        (23, 'letra'): 23,
                        (23, 'digito'): 23,
                        (23, 'underscore'): 23,
                        (23, 'punto'): 23,
                        (23, 'E'): 23,
                        (23, 'resta'): 23,
                        (23, 'suma'): 23,
                        (23, 'asignacion'): 23,
                        (23, 'multiplicacion'): 23,
                        (23, 'division'): 23,
                        (23, 'potencia'): 23,
                        (23, 'simbolo_a'): 23,
                        (23, 'simbolo_c'): 23,
                        (23, 'fin'): 23,
                        (25, 'resta'): 0,
                        (24, 'resta'): 0,
                        (25, 'division'): 0
                    }
estados_finales = [1,2,3,5,6,7,8,9,11,13,14,16,17,18,19,21,22,23,24,25]
estados_excepciones = [1,2,3,5,6,16,17,18,19,21,22,24]

def automata(cadena, estado_actual, stack):
    """ Automata que detecta el tipo de token de acuerdo a la tabla de transicion
        Argumentos:
            name: cadena,           summary: caracteres por cada linea,                 type: list
            name: estado_actual,    summary: estado de transcion,                       type: number
            name: stack,            summary: caracteres pertenecientes al mismo estado, type: list
    """
    if len(cadena) is 0:
        if estado_actual in estados_finales:
            return get_token(estado_actual)
    else:
        entrada = detecta_tipo(cadena[0])
        if entrada is not "fin":
            stack.append(cadena[0])

        #print("{} - {} => {}".format(estado_actual, entrada, stack))

        if (estado_actual, entrada) in funcion_transicion:
            if len(cadena) > 1:
                if estado_actual in estados_finales and (estado_actual, detecta_tipo(cadena[1])) in funcion_transicion:
                    return automata(cadena[1:], funcion_transicion[(estado_actual, entrada )], stack)
                else:
                    print("Token - {} | Tipo => {}".format(stack, get_token(estado_actual)))
                    stack = []
                    return automata(cadena[1:], funcion_transicion[(estado_actual,entrada)], stack)
            else:
                if len(stack) is not 0:
                    print("Token - {} | Tipo => {}".format(stack, get_token(estado_actual)))
                    stack = []
                    return automata(cadena[1:], funcion_transicion[(estado_actual,entrada)], stack)
                return

        else:
            if estado_actual in estados_excepciones:
                print_token(stack, entrada)
                if estado_actual == 1:
                    estado_actual = 0
                return automata(cadena[1:], estado_actual, [])
            else:
                return 'Token no valido'


def automata_unitario(cadena, estado_actual):
    """ Automata que detecta el tipo de token de acuerdo a la tabla de transicion
        Argumentos:
            name: cadena           summary: Cadena a evaluar        type: list
            name: estado_actual    summary: Estado actual           type: int
    """
    if len(cadena) is 0:
        if estado_actual in estados_finales:
            return get_token(estado_actual)
    else:
        entrada = detecta_tipo(cadena[0])
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
    elif elemento == "(":
        return 'simbolo_a'
    elif elemento == ")":
        return 'simbolo_c'
    elif elemento == "E":
        return 'E'
    elif elemento == "\n":
        return 'fin'
    elif elemento.isspace():
        return 'espacio'
    elif type(elemento) is StringType:
        return 'letra'
    else:
        return 'no_valido'


def get_token(item):
    return tipos_token[item]


def print_token(stack, tipo):
    print("Token - {} | Tipo => {}".format(stack, get_token(funcion_transicion[(0,tipo)])))


def main():
    if not os.path.isfile(filepath):
        print("La ruta del archivo {} no existe. Verifica que exista el archivo en el mismo directorio...".format(filepath))
        sys.exit()

    content = []
    with open(filepath) as f:
        for line in f:
            content.append(list(line))

    for line in content:
        estado = funcion_transicion[(0,detecta_tipo(line[0]))]
        automata(line, estado, [])

if __name__ == "__main__":
    main()
