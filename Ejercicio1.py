archivo = open('tabla-n.txt', 'w')



def tabla(n):
    for i in range(1,11):
        print(n * i)




archivo.write(tabla())

