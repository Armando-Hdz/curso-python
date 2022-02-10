class Gato():
    def hablar(self):
        print("Miau!")

class Perro():
    def hablar(self):
        print("Guau!")

def escucharMascotas(animal):
    animal.hablar()

miMascota = Perro()
escucharMascotas(miMascota)