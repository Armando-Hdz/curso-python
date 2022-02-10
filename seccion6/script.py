import sys
#Se utilizara CMD para manipular el script
if len (sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for i in range(repeticiones):
        print(texto)
else:
    print("Error: Introdujo uno o mas de dos argumentos ")
    print("Solucion: Introduce correctamente los argumentos")
    print("Ejemplo: scritp.py 'texto' 5 ")

