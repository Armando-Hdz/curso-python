#Ejemplo de Diccionario
nombre = input("¿Como te llamas? ")
edad = input("¿Cuantos años tienes? ")
direc = input("¿Cual es tu direccion? ")
tel = input("Cual es tu telefono? " )

persona = {"nombre": nombre, "edad": edad, "direccion": direc, "telefono":tel}

print("Su nombre es ", persona["nombre"], " tiene ", persona["edad"], " años y vive en ", persona["direccion"], 
" y su numero de telefono es ", persona["telefono"])

#Ejemplo de una lista
lista = []
i = 1
while i <= 100:
    lista.append(i)
    i=i+1
print(lista)