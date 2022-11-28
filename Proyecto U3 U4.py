#Se lee el archivo de texto palabra por palabra

#arreglo que contiene los registros que se pueden utilizar
ru0, ru1, ru2, ru3, ru4, ru5, ru6, ru7, ru8, ru9, ru10, ru11, ru12, ru13, ru14, ru15 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
#arreglo que contiene la lista de instrucciones
innstrucciones = ["add", "sub", "mul", "div", "mod", "cmp", "and", "or", "not", "mov", "isl", "isr", "asr", "nop", "ld", "st", "beq", "bgt", "b", "call", "ret"]

with open('Instrucciones.txt', 'r') as archivo:
    for linea in archivo:
        for palabra in linea.split():
            #print(palabra)
            for i in innstrucciones:
                if (palabra == i):
                    print (palabra, "potito")
        #activar = 0
        print("")
        #if (operacion[0] == 'add'):
        #    operacion[0] = suma(operacion[1], operacion[2], operacion[3])
