diccionario = {
    "clave1":123,
    "clave2":True,
    "clave3":[1,2,3]
}

print(type(diccionario["clave1"])) #Muestra el tipo de valor que tiene una variable o clave

print(diccionario.keys()) #Muestra el nombre de las claves de un diccionario

print(diccionario.values()) #Muestra el nombre de los valores de un diccionario

print(diccionario.items()) #Muestra cada clave y valor del diccionario
print("\n")
for i, c in diccionario.items():
    print(i,c)