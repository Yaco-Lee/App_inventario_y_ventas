import pyodbc
import pandas as pd

class Dal:
    def __init__(self):
        pass

    @staticmethod
    def establecer_conexion():
        # Ingresamos direccion de la DB
        conection_string = r'Driver={ODBC Driver 17 for SQL Server};Server=(localdb)\MSSQLLocalDB;Database=CRUD;Trusted_Connection=yes;'
        # Establecemos la conexion con la DB usando el modulo PYODBC
        cnxn_live = pyodbc.connect(conection_string)
        cnxn_live.autocommit = True
        return cnxn_live

    @staticmethod
    def read_from_DB(sql_statement):
        cnxn = Dal.establecer_conexion()
        # Traemos de la DB los datos por medio de una SQL statement, en forma de dataframe
        return pd.read_sql(sql_statement, cnxn)

    @staticmethod
    def do_command_on_DB(sql_statement):
        # Este metodo lleva a cabo un comando en la DB (por ej un post)
        cnxn = Dal.establecer_conexion()
        cursor = cnxn.cursor()
        cursor.execute(sql_statement)

