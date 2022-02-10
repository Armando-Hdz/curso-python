class Persona():
    def __init__(self):
        self.cedula = 12345

    def mensaje(self):  #Se llama OVERRIDE (Sobre cargo de metodos)
        print("Este mensaje viene de la clase Persona ")

class Obrero(Persona):
    def __init__(self):
        self.especialista = 1

    def mensaje(self): #Se llama OVERRIDE (Sobre cargo de metodos)
        print("Este mensaje viene de la clase Obrero ")