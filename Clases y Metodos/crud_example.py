import pyodbc
import pandas as pd

class Martillo():
    def __init__(self, peso: int, uso: str, largo_mango: int, precio: int, id: int):
        self.peso = peso
        self.uso = uso
        self.largo_mango = largo_mango
        self.id = id
        self.tipo = "Martillo"
        self.precio = precio

    def __repr__(self):
        return f"Hola, te traje un martillo para {self.uso}"

    def establecer_conexion(self):
        # Ingresamos direccion de la DB
        conection_string = r'Driver={ODBC Driver 17 for SQL Server};Server=(localdb)\MSSQLLocalDB;Database=CRUD;Trusted_Connection=yes;'
        # Establecemos la conexion con la DB usando el modulo PYODBC
        cnxn_live = pyodbc.connect(conection_string)
        cnxn_live.autocommit = True
        return cnxn_live

    def read_from_DB(self, sql_statement):
        cnxn = self.establecer_conexion()
        # Traemos de la DB los datos por medio de una SQL statement, en forma de dataframe
        return pd.read_sql(sql_statement, cnxn)

    def do_command_on_DB(self, sql_statement):
        #Este metodo hace un comando en la DB (por ej un post)
        cnxn = self.establecer_conexion()
        cursor = cnxn.cursor()
        cursor.execute(sql_statement)

    def post(self, martillo: "Martillo"):
        self.do_command_on_DB(f"INSERT INTO CRUD.dbo.Martillos ([ID], [Peso], [Uso], [Largo_Mango], [Tipo], [Precio]) VALUES ({martillo.id}, {martillo.peso}, '{martillo.uso}', {martillo.largo_mango}, '{martillo.tipo}', {martillo.precio})")

    def put(self, martillo: "Martillo"):
        self.do_command_on_DB(f"UPDATE CRUD.dbo.Martillos SET [ID] = {martillo.id}, [Peso] = {martillo.peso}, [Uso] = '{martillo.uso}',[Largo_Mango] =  {martillo.largo_mango}, [Tipo] = '{martillo.tipo}', [Precio] = {martillo.precio} WHERE [ID] = {martillo.id}")

    def delete(self,martillo: "Martillo"):
        self.do_command_on_DB(f"DELETE FROM CRUD.dbo.Martillos WHERE [ID] = {martillo.id}")

    def get(self):
        #Creamos una lista que alojará los objetos Martillo que trajimos, guardados en la variable data de la linea anterior
        martillos = []
        statement = "SELECT * FROM Martillos"
        data = self.read_from_DB(statement)
        #Creamos el bucle FOR que llenará las propiedades de los Obj Martillo
        for row, values in data.iterrows():
            identificacion = values["ID"]
            peso = values["Peso"]
            largo_mango = values["Largo_Mango"]
            uso = values["Uso"]
            tipo = values["Tipo"]
            precio = values["Precio"]
            un_martillo = Martillo(peso, uso, largo_mango, precio, identificacion)
            martillos.append(un_martillo)
        # Retornamos la lista de Martillos
        return martillos



martillo = Martillo(200, "Zapatería", 30, 990, 948756)
print(martillo.get())
martillo.delete(martillo)
print(martillo.get())


# TAREA: VOLVER ESTO UN MODULO