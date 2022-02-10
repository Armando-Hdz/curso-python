class Gelatina:
    def __init__(self, sabor, color, tamano):
        self.sabor = sabor
        self.color = color
        self.tamano = tamano

    def imprimir(self):
        print("La gelatina es ", self.sabor)
        print("La gelatina se ve de ", self.color)
        print("La gelatina es ", self.tamano)

gel1 = Gelatina("Roja", "Manzana", "Mediana \n")
gel2 = Gelatina("Amarilla", "Piña", "Grande \n")
gel3 = Gelatina("Azul", "Mora", "Grande \n")
gel4 = Gelatina("Morada", "Uva", "Chica \n")

gel1.imprimir()
gel2.imprimir()
gel3.imprimir()
gel4.imprimir()
