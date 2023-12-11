archivo = open('tabla-n.txt', 'a')


def tabla(n):
    for i in range(1,11):
        archivo.write(str(n * i) + '\n')
    return

tabla(7)