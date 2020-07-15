
class Interfaz_Producto:
    def __init__(self, id, tipo, precio):
        self.id = id
        self.tipo = tipo
        self.precio = precio

    def buscar(self, lista_prod_para_vender: []):
        pass

class Caja_Armonizadora:
    def __init__(self, tamaño: str, chakra: str, nota: int, precio: int, id: int):
        self.tamaño = tamaño
        self.chakra = chakra
        self.id = id
        self.tipo = "Caja Armonizadora"
        self.precio = precio
        self.nota = nota

    def __eq__(self, other):
        id = self.id
        if id == other.id:
            return True
        else:
            return False

    def buscar(self, lista_prod_para_vender: []):
        for producto in lista_prod_para_vender:
            if producto.tipo == self.tipo and producto.nota == self.nota and producto.tamaño == self.tamaño:
                return "Tenemos esta {} en stock".format(self.tipo)

        return "No tenemos esa {} en sotck".format(self.tipo)


class Armonizador_Giratorio:
    def __init__(self, cant_tubos: int, acorde: str, precio: int, id: int):
        self.precio = precio
        self.id = id
        self.acorde = acorde
        self.cant_tubos = cant_tubos
        self.tipo = "Armonizador Giratorio"

    def __eq__(self, other):
        id = self.id
        his_id = other.id
        if id == his_id:
            return True
        else:
            return False

    def buscar(self, lista_prod_para_vender: []):
        for producto in lista_prod_para_vender:
            if producto.tipo == self.tipo and producto.cant_tubos == self.cant_tubos and producto.acorde == self.acorde:
                return f"Tenemos este {self.tipo} disponible"

        return f"No tenemos este {self.tipo} disponible"




class Stand_Campanas:
    def __init__(self, cant_campanas: int, notas: [str], id: int, precio: int):
        self.id = id
        self.tipo = "Stand de Campanas"
        self.cant_campanas = cant_campanas
        self.notas = notas
        self.precio = precio

    def __eq__(self, other): 
        id = self.id
        if id == other.id:
            return True
        else:
            return False

    def buscar(self, lista_prod_para_vender: []):
        for producto in lista_prod_para_vender:
            if producto.tipo == self.tipo and producto.cant_campanas == self.cant_campanas and producto.notas == self.notas:
                return f"Tenemos ese {self.tipo} disponible"

        return f"No tenemos ese {self.tipo} disponible"

class Campana_Individual:
    def __init__(self, nota: str, id: int, precio: int):
        self.id = id
        self.tipo = "Campana"
        self.nota = nota
        self.precio = precio

    def __eq__(self, other):
        id = self.id
        if id == other.id:
            return True
        else:
            return False

    def buscar(self, lista_prod_para_vender: []):
        for producto in lista_prod_para_vender:
            if producto.tipo == self.tipo and producto.nota == self.nota:
                return f"Tenemos esa {self.tipo} disponible"

        return f"No tenemos esa {self.tipo} disponible"


class Vendedor:

    def __init__(self):
        self.lista_de_prod_para_vender = [Fresa(10, "redondeo", 14, 2000, 25321), Mecha(100, 10, "madera", 252525, 1200), Caja_Armonizadora(400, "Construccion", 30, 990, 777890)]
        self.productos_vendidos = []

    def vender_fresa(self, fresa: Fresa):
        if fresa in self.lista_de_prod_para_vender:
            self.lista_de_prod_para_vender.remove(fresa)
            self.productos_vendidos.append(fresa)
            return "Se vendió una {}".format(fresa.tipo)
        else:
            return "No tenemos {} en stock".format(fresa.tipo)

    def vender_mecha(self, mecha: Mecha):
        if mecha in self.lista_de_prod_para_vender:
            self.lista_de_prod_para_vender.remove(mecha)
            self.productos_vendidos.append(mecha)
            return "Se vendió una {}".format(mecha.tipo)
        else:
            return "No tenemos {} en stock".format(mecha.tipo)

    def vender_martillo(self, martillo: Caja_Armonizadora):
        if martillo in self.lista_de_prod_para_vender:
            self.lista_de_prod_para_vender.remove(martillo)
            self.productos_vendidos.append(martillo)
            return "Se vendió un {}".format(martillo.tipo)
        else:
            return "No tenemos este {} en stock".format(martillo.tipo)

    def buscar_producto(self, prod_a_buscar: "Interfaz_Producto"):
        return prod_a_buscar.buscar(self.lista_de_prod_para_vender)


#comentario







