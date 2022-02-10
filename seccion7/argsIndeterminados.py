def infinito(*args): #Permite ingresar cualquier tipo de argumentos
    print(args) #Imprime los argumentos.
infinito("Hola", 20, 10.1, [1,2,3])

def infinitoUno(*args):
    for args in args: #Permite imprimir uno a la vez
        print(args)
infinitoUno("Hola", 20, 10.1, [1,2,3])

def infinitoDos(**kwargs):
    for kwarg in kwargs:
        print(kwarg, "--->", kwargs[kwarg])
infinitoDos(a = "Hola", b = 20, c = ["Maria","Pedro","Jose"])
