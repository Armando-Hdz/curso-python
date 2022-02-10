class Persona:
    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

    def datosPersonales(self):
        print("El nombre de la persona es: ", self.nombre)
        print("El apellido de la persona es: ", self.apellido)
        print("La edad de la persona es: ", self.edad)
        print("El sexo de la persona es: ", self.sexo)

miPersona = Persona("Pepe", "Lopez", 25, "Masculino")
miPersona.datosPersonales()
print(" ********************* Aqui comienza otra Persona *********************** \n")

class Empleado(Persona):    #Para heredar se debe colocar entre parentesis el nombre de la SUPERCLASE
    def datosEmpleado(self, vacaciones, salario):
        print("Sus días de vacaciones son: ", vacaciones)
        print("Su salario es: ", salario)

miPersona2 = Empleado("Guadalupe", "Montez", 30, "Femenino")
miPersona2.datosPersonales()
miPersona2.datosEmpleado(20, 8000)