#Se lee el archivo de texto palabra por palabra
ru0, ru1, ru2, ru3, ru4, ru5, ru6, ru7, ru8, ru9, ru10, ru11, ru12, ru13, ru14, ru15 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
operacion = []
activar = 0

with open('Instrucciones.txt', 'r') as archivo:
    for linea in archivo:
        for palabra in linea.split():
            print(palabra)
            if (activar == 1):
                operacion.add(palabra)
            if (palabra == 'add'):
                activar = 1
                operacion.add('add')
        activar = 0
        print("")
        #if (operacion[0] == 'add'):
        #    operacion[0] = suma(operacion[1], operacion[2], operacion[3])
