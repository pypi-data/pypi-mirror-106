

class Agua():
    def __init__(self, bebida, origen, id, nom, marca, precio, litros):
        super().__init__(id, nom, marca, precio, litros)
        self.bebida = bebida
        self.origen = origen

    def getBebida(self):
        return self.bebida

    def getOrigen(self):
        return self.origen
