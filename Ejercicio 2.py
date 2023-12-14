import os

def leer_fichero():
    n = int(input('Escribe un número del 1 al 10: '))

    if os.path.isfile('tabla-{}.txt'.format(n)) == True:
        lectura = open('tabla-{}.txt'.format(n), 'r')
        print(lectura.read())
    else:
        print('No existe el fichero con la tabla del {}.'.format(n))
    return

leer_fichero()