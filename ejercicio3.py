#1) Escribir ub programa que almacene la cadena de caracteres de la contraseña en una variable,
#preguntar al usuario por la contraseña hasta que sea a misma.
pas = "Contraseña"
password = ""
while password != pas:
    password = input("Ingrese su contraseña: ")
print("Contraseña correcta")

#2) Escribir un programa que solicite una palabra al usuario y lo muestre 10 veces en pantalla
i = input("Introduce una palabra: ")
for h in range(10):
    print(i)
#3) Escribir un programa que pregunte al usuario su edad y muestre en pantalla todos los años que ha cumplido (desde 1 ...)
año =  int(input("¿Cual es su edad? "))
for i in range(año):
    print("Has cumplido " + str(i+1) + " años")
#4) Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba "salir" quer terminará
while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)
#5) Para tributar un impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000e menssuales
edad = int(input("Ingresa tu edad: "))
salario = float(input("¿Cuales so tus ingresos mensuales? : "))

if edad > 16 and salario  >= 1000:
    print("Puedes cotizar...")
else: 
    print("No tienes que cotizar ....")