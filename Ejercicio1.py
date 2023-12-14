def tabla():
    n = int(input('Escribe un número del 1 al 10: '))
    archivo = open('tabla-{}.txt'.format(n), 'a')
    archivo.write('La tabla del {} es:'.format(n) + '\n')

    for i in range(1,11):
        archivo.write(str('{} X {} = {}'.format(n, i, i * n)) + '\n')

    archivo.close()
    return

tabla()