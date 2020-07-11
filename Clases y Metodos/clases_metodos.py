
class Interfaz_Producto:
    def __init__(self, id, tipo, precio):
        self.id = id
        self.tipo = tipo
        self.precio = precio

    def buscar(self, lista_prod_para_vender: []):
        pass

class Martillo():
    def __init__(self, peso: int, uso: str, largo_mango: int, precio: int, id: int):
        self.peso = peso
        self.uso = uso
        self.largo_mango = largo_mango
        self.id = id
        self.tipo = "Martillo"
        self.precio = precio

    def __eq__(self, other):
        id = self.id
        if id == other.id:
            return True
        else:
            return False

    def buscar(self, lista_prod_para_vender: []):
        for producto in lista_prod_para_vender:
            if producto.tipo == self.tipo and producto.largo_mango == self.largo_mango and producto.peso == self.peso:
                return "Tenemos este {} disponible".format(self.tipo)

        return "No tenemos ese {} disponible".format(self.tipo)


class Fresa:
    def __init__(self, diametro: int, tipo_de_corte: str, vastago: int, precio: int, id: int):
        self.diametro = diametro
        self.tipo_de_corte = tipo_de_corte
        self.vastago = vastago
        self.marca = "Bosch"
        self.precio = precio
        self.id = id
        self.tipo = "Fresa"

    def __eq__(self, other):
        id = self.id
        his_id = other.id
        if id == his_id:
            return True
        else:
            return False

    def buscar(self, lista_prod_para_vender: []):
        for producto in lista_prod_para_vender:
            if producto.tipo == self.tipo and producto.vastago == self.vastago and producto.tipo_de_corte == self.tipo_de_corte:
                return "Tenemos {} disponible".format(self.tipo)

        return "No tenemos {} disponible".format(self.tipo)




class Mecha:
    def __init__(self, largo: int, diametro: int, uso: str, id: int, precio: int):
        self.id = id
        self.largo = largo
        self.diametro = diametro
        self.uso = uso
        self.tipo = "Mecha"
        self.precio = precio

    def __eq__(self, other):
        id = self.id
        if id == other.id:
            return True
        else:
            return False

    def buscar(self, lista_prod_para_vender: []):
        for producto in lista_prod_para_vender:
            if producto.tipo == self.tipo and producto.largo == self.largo and producto.uso == self.uso:
                return "Tenemos {} disponible".format(self.tipo)

        return f"No tenemos {self.tipo} disponible"



class Vendedor:

    def __init__(self):
        self.lista_de_prod_para_vender = [Fresa(10, "redondeo", 14, 2000, 25321), Mecha(100, 10, "madera", 252525, 1200), Martillo(400, "Construccion", 30, 990, 777890)]
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

    def vender_martillo(self, martillo: Martillo):
        if martillo in self.lista_de_prod_para_vender:
            self.lista_de_prod_para_vender.remove(martillo)
            self.productos_vendidos.append(martillo)
            return "Se vendió un {}".format(martillo.tipo)
        else:
            return "No tenemos este {} en stock".format(martillo.tipo)

    def buscar_producto(self, prod_a_buscar: "Interfaz_Producto"):
        return prod_a_buscar.buscar(self.lista_de_prod_para_vender)


#comentario







