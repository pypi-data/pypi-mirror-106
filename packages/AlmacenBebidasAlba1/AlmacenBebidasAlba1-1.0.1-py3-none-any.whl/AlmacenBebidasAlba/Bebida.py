

class Bebida:

    def __init__(self, id, columna, nom, marca, precio, litros):
        self.id = id
        self.columna = columna
        self.nom = nom
        self.marca = marca
        self.precio = precio
        self.litros = litros

    def getID(self):
        return self.id

    def getColumnas(self):
        return self.columna

    def getNom(self):
        return self.nom

    def getMarca(self):
        return self.marca

    def getPrecio(self):
        return self.precio

    def getLitros(self):
        return self.litros
