

class BebidaConGas():
    def __init__(self, bebida, porcentajeAzucar, promocion, id, nom, marca, precio, litros):
        super().__init__(id, nom, marca, precio, litros)
        self.bebida = bebida
        self.porcentajeAzucar = porcentajeAzucar
        self.promocion = promocion

    def getBebida(self):
        return self.bebida

    def getPorcentajeAzucar(self):
        return self.porcentajeAzucar

    def getPromocion(self):
        return self.promocion
