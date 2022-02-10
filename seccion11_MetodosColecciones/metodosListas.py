lista = ["Jose", "Maria", "Pedro"]
lista.append("Armando") #agrega un elemento a la lista
print(lista)

lista2 = ["Juan", "Antonio", "Luis"]
lista.extend(lista2) # Anexa la segunda lista a la primera (convierte en una sola)
print(lista)

print("Las veces que aparece el nombre es: ", lista.count("Jose")) #Cuenta las veces que aparece
print(lista.index("Maria")) # Marca el INDICE de donde se encuentra lo buscado

lista2.insert(0, "Miguel") # Inserta un elemento a la lista en determinada posicion
print(lista2)

lista.reverse() #Muestra la lista de REVERSA (Ultimo a primero)
print(lista)