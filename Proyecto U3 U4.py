#Se lee el archivo de texto palabra por palabra
with open('Instrucciones.txt', 'r') as archivo:
    for linea in archivo:
        for palabra in linea.split():
            print(palabra)
        print("")

