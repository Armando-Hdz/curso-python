class Coche:
    def __init__(self, marca, kilometros, anio):
        self.marca = marca
        self.kilometros = kilometros
        self.anio = anio
        print(f'Se ha creado un auto marca {self.marca} con {self.kilometros} kilometros')

    def __del__(self):
        print(f'Se ha vendido el auto marca {self.marca}')

    def __str__(self):
        return "El auto es un {}, tiene {} y es del año {}".format(self.marca, self.kilometros, self.anio)

miCoche = Coche('Audi', 10, 1995)
#del(miCoche) PERTENECE AL METODO DEL
print(str(miCoche))