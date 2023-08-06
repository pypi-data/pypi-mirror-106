import pandas as pd


class Almacen:
    global df

    def afegirBeguda(self, bebida):
        #Se pasa por parametro la list con las bebidas
        to_append = bebida
        #Se introducen en un DataFrame con sus respectivas columnas
        df = pd.DataFrame(to_append, columns=['ID','Columna', 'Marca', 'Preu', 'Litros', 'Origen', 'Promo', 'Azúcar'])
        #print(df)
        #Toda la información se guarda en archivo pickle
        df.to_pickle("./dummy.pkl")

    def calcularPrecioTotal(self):
        #Cargamos el documeto
        dataf = pd.read_pickle("./dummy.pkl")
        #Sumamos todos los valores que hay en la columna preu
        Total = dataf['Preu'].sum()
        #Se devuelve al programa principañ
        return str(Total)

    def calcularPrecioMarca(self, marca):
        #Cargamos el documento
        dataf = pd.read_pickle("./dummy.pkl")
        #Buscamos en la columna Marca aquella marca que nos han pasado por parametro y sumamos el valor de esto
        total = dataf.loc[dataf['Marca'] == marca, 'Preu'].sum()
        return str(total)

    def calcularPrecioColumna(self, columna):
        #Cargamos el documento
        dataf = pd.read_pickle("./dummy.pkl")
        #Buscamos en la columna Columna aquella columna que nos han pasado por parametro y sumamos el valor de esto
        total = dataf.loc[dataf['Columna'] == columna, 'Preu'].sum()
        return str(total)

    def eliminarBebida(self, id):
        #Cargamos el documento
        dataf = pd.read_pickle("./dummy.pkl")
        #Buscamos el id que nos han pasado y lo convertimos en indice
        indexID = dataf[dataf['ID'] == id ].index
        #Este se busca y elimina la linia entera
        dataf.drop(indexID, inplace=True)
        #Ponemos los cambios en el archivo pkl
        dataf.to_pickle("./dummy.pkl")


    def mostrarEstanteria(self):
        #Cargamos el documento
        unpickled_df = pd.read_pickle("./dummy.pkl")
        #Lo imprimimos
        print(unpickled_df)
