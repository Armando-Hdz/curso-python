#Validar que el correo que se escriba contenga el caracter "@" para poder ser un correo valido
variable = False
if variable == False:
    i = 1
    while i <= 10 :
        def validar(email):
            caracterbuscado = "@"
            emailValido = False
            for c in email:
                if c == caracterbuscado:
                    return True
            return False
        direccion = input(" Escribe tu email: ")
        if validar(direccion):
            print("Direccion válida")
            print(" Fin del programa '_' ")
            break
        else:
            print("Direccion Invalida")
        i+=1
    else:
        print("Excediste el numero maximo de intentos... Intentalo de nuevo '_' ")
else:
    print("Fin del programa...")


    