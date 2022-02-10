nombre = input("Ingresa tu nombre: ")
print("Tu nombre en mayusculas es: ", nombre.upper()) #Convierte todo a mayusculas
print("Tu nombre en minusculas es: ", nombre.lower()) #Convierte todo a minusculas
print("Tu nombre en minusculas es: ", nombre.capitalize()) #Coloca la primer letra en mayusculas

a = "Hola me llamo Juan en Juangas"
print("Las veces que aparece el nombre es: ", a.count("Juan")) #Encuentra la palabra tal y como esta escrita
print("La posicion de la letra 'J' es: ", a.find("J")) #Encuentra la posicion de una letra o caracter

b = "Esta es una prueba"
print(b.isdigit) #Arroja un booleano, de acuerdo si es o no un digito (numerico)

print(b.split(" ")) #Arroja una tipo Lista (sustituye los espacios por comas)

c = "abc123"
print(c.isalnum()) #Muestra un boleano si es un caracter ALFANUMERICO