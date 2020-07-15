from .dal import Dal

class Armonizador_Giratorio:
    def __init__(self, cant_tubos: int, acorde: str, precio: int, id: int):
        self.precio = precio
        self.id = id
        self.acorde = acorde
        self.cant_tubos = cant_tubos
        self.tipo = "Armonizador Giratorio"

    def __repr__(self):
        return f"Este objeto de la tabla es del tipo {self.tipo}, tiene como Id el numero {self.id}, está afinado en {self.acorde}, tiene {self.cant_tubos} y vale {self.precio}"

    def post(self, armonizador: "Armonizador_Giratorio"):
        Dal.do_command_on_DB(f"INSERT INTO CRUD.dbo.Armonizadores ([ID], [Tipo], [Precio], [Acorde], [Cantidad_de_tubos]) VALUES ({armonizador.id}, '{armonizador.tipo}', {armonizador.precio}, '{armonizador.acorde}', {armonizador.cant_tubos})")

    def put(self, armonizador: "Armonizador_Giratorio"):
        Dal.do_command_on_DB(f"UPDATE CRUD.dbo.Armonizadores SET [ID] = {armonizador.id}, [Acorde] = '{armonizador.acorde}', [Cantidad_de_tubos] = {armonizador.cant_tubos} WHERE [ID] = {armonizador.id}")

    def delete(self, armonizador: "Armonizador_Giratorio"):
        Dal.do_command_on_DB(f"DELETE FROM CRUD.dbo.Armonizadores WHERE [ID] = {armonizador.id}")

    def get(self):
        #Creamos una lista que alojará los objetos armonizador que trajimos, guardados en la variable data de la linea anterior
        armonizadores = []
        statement = "SELECT * FROM Armonizadores"
        data = Dal.read_from_DB(statement)
        #Creamos el bucle FOR que llenará las propiedades de los Obj Martillo
        for row, values in data.iterrows():
            precio = values["Precio"]
            identificacion = values["ID"]
            acorde = values["Acorde"]
            cantidad_tubos = values["Cantidad_de_tubos"]
            un_armonizador = Armonizador_Giratorio(cantidad_tubos, acorde, precio, identificacion)
            armonizadores.append(un_armonizador)
        # Retornamos la lista de Martillos
        return armonizadores



armon = Armonizador_Giratorio(4, "B", 2000, 555000)
print(armon.get())
armon.delete(armon)
print(armon.get())


# TAREA: VOLVER ESTO UN MODULO