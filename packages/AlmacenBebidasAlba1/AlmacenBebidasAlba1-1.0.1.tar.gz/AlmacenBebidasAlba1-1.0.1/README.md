# practicaUUF4

Codigo de ejemplo para utilizar el paquete:

import self as self
from Almacen import Almacen
from Clases.Bebida import Bebida
class Main:
    a = Almacen
    bebida = Bebida
    bebida = [[1, 1, 'Bezoya', 2, 2, 'Guadarrama', '', ''],
              [2, 1, 'Fanta', 1.5, 1.5, '', 'True', 'Free'],
              [3, 1, 'Coca-Cola', 1.75, 2, '', 'False', '5%'],
              [4, 1, 'Viladrau', 1.5, 1.5, 'Fontalegre', '', ''],
              [5, 1, 'Pepsi', 1.85, 1, '', 'True', '6%'],
              [6, 2, 'Fontvella', 2.5, 2, 'Girona', '', ''],
              [7, 2, 'Bezoya', 2, 1, 'Guadarrama', '', ''],
              [8, 2, 'Viladrau', 1.5, 2, 'Fontalegre', '', ''],
              [9, 2, 'Trina', 1.75, 1.5, '', 'False', '6%'],
              [10, 2, 'Coca-Cola', 1.75, 1.5, '', 'False', 'Free']]
    Almacen().afegirBeguda(bebida)
    print("¡Bebidas añadidas!")
    a.mostrarEstanteria(self)

    print("El precio total de todas las bebidas es: " + a.calcularPrecioTotal(self))
    print("El precio total de las bebidas de la marca Bezoya es: " + a.calcularPrecioMarca(self, "Fanta"))
    print("El precio total de la columna 1: " + a.calcularPrecioColumna(self, 1))

    print("Se va a eliminar una bebida")
    a.eliminarBebida(self, 3)

    a.mostrarEstanteria(self)

    print("El precio total de todas las bebidas es: " + a.calcularPrecioTotal(self))
    print("El precio total de las bebidas de la marca Bezoya es: " + a.calcularPrecioMarca(self, "Bezoya"))
    print("El precio total de la columna 2: " + a.calcularPrecioColumna(self, 2))
