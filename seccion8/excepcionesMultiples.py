try: 
    c = int(input("\nIngresa un valor: "))
    c/0
except ValueError:
    print("\nError, no se puede dividir una cadena de texto :( \n")
except Exception as c : # Permite guardar en una variable la excepcion
    print("\n")
    print(type(c).__name__) #Imprimes el nombre de la excepcion.