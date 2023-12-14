import os

def busqueda_linea_funcion():
    n = int(input('Escribe un número del 1 al 10: '))
    m = int(input('Escribe otro número del 1 al 10: '))


    if os.path.isfile('tabla-{}.txt'.format(n)) == True:
        lectura = open('tabla-{}.txt'.format(n), 'r')
        linea_lectura = lectura.readlines()
        print(linea_lectura[m])
    else:
        print('No existe el fichero con la tabla del {}.'.format(n))
    return

busqueda_linea_funcion()