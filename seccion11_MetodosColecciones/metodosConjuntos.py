set_conjunto1 = set({1,2,3,4})
set_conjunto1.add(22) #agrega un elemento
print(set_conjunto1)

paquete = set({"Hola", 2, 3, 5})
print(paquete)
paquete.discard("Hola") #Descarta este elemento del conjunto
print(paquete)


paquete2 = set({"Hola", 2, 3, 5, "Python"})
print(paquete2)
paquete2.remove("Python") #Elimina este elemento del conjunto
print(paquete2)