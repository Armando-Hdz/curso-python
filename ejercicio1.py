 # 2) Determinar sin programar el resultado quw aparecera en la pantalla
 # a partir de las siguientes variables
a = 20
b = 10
c = "Pepe"
d = [1,2,3]

print(a*4) # a*4 es 80
print(a-b) # a-b es 10
print(c + "Garcia") # "Pepe" "Garcia"
print(c*2) # "Pepe" "Pepe"
print(c[-1]) # La letra e final de Pepe
print(c[1:]) # sin la primera p = "epe"
print(d+d) # Dos listas [1,2,3],[1,2,3]

#3) El siguiente codigo pretende realizar una media entre 3 numero
#pero algo anda mal, ¿Puedes identificar el problema y solucionarlo?

num_1 = 9
num_2 = 3
num_3 = 6

media = (num_1 + num_2 + num_3)/3
print("La media es: ", media)

#Aqui hay otro prblema, ¿Eres capaz de resolverlo? Al querer sumar entrada mas 10 
#sale un error. ¿Que es lo que esta faltando?

entrada = input("Introduzca un numero: ") #colocar int(input("Introduzca un numero: "))
 