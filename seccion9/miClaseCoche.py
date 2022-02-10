class Coche():  #Se crea un molde
    def __init__(self):     #Se aplican cracteristicas o atributos
        self.__marca = "Audi"  #PERMITE ENCAPSULAMIENTO CON DOBLE _ _
        self.__color="Rojo"
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):     #Se crea un metodo
        self.__enmarcha = arrancamos
        if(self.__enmarcha):
            return "\nEl coche esta en marcha\n"
        else:
            return "\nEl coche se encuentra apagado\n"

    def __str__(self):      #Se crea otro metodo
        return "El coche esta en marcha y es de la marca {}, de color {} y tiene {} ruedas \n".format(self.__marca,
         self.__color, self.__ruedas)
    
miCoche = Coche()      #Se instanacia la clase
print(miCoche.arrancar(True))       #Mostrar en pantalla
print(str(miCoche))     #Se enciende y apaga el coche 