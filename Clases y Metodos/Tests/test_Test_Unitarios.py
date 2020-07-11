from unittest import TestCase
from clases_metodos import *


class Test_Vendedor(TestCase):

    def test_vender_fresa_existente(self):
        #arrange
        fresa = Fresa(10, "redondeo", 14, 200, 25321)
        vendedor = Vendedor()

        #act
        ret = vendedor.vender_fresa(fresa)

        #assert
        self.assertTrue(fresa not in vendedor.lista_de_prod_para_vender, "La fresa sigue estando en la lista de prod para vender")
        self.assertTrue(fresa in vendedor.productos_vendidos, "La fresa no está en la lista de prods vendidos")
        self.assertEqual("Se vendió una {}".format(fresa.tipo), ret, "La expresion para printear no coincide")

    def test_vender_fresa_inexistente(self):
        #arrange
        fresa = Fresa(10, "redondeo", 14, 200, 25322)
        vendedor = Vendedor()

        #act
        ret = vendedor.vender_fresa(fresa)

        #assert
        self.assertTrue(fresa not in vendedor.lista_de_prod_para_vender, "La fresa por alguna razon aparece en productos para vender")
        self.assertTrue(fresa not in vendedor.productos_vendidos, "La fresa por alguna razon aparece en productos vendidos")
        self.assertEqual("No tenemos {} en stock".format(fresa.tipo), ret, "La expresion para printear no coincide")

    def test_vender_mecha_existente(self):
        #arrange
        mecha = Mecha(100, 10, "madera", 252525, 1200)
        vendedor = Vendedor()

        #act
        ret = vendedor.vender_mecha(mecha)

        #assert
        self.assertTrue(mecha not in vendedor.lista_de_prod_para_vender, "La mecha sigue estando en la lista de prod para vender")
        self.assertTrue(mecha in vendedor.productos_vendidos, "La fresa por alguna razon no aparece en productos vendidos")
        self.assertEqual("Se vendió una {}".format(mecha.tipo), ret, "La expresion para printear no coincide")


    def test_vender_mecha_inexistente(self):
        #arrange
        mecha = Mecha(100, 15, "madera", 666589, 1200)
        vendedor = Vendedor()

        #act
        ret = vendedor.vender_mecha(mecha)

        #assert
        self.assertTrue(mecha not in vendedor.lista_de_prod_para_vender, "La mecha por alguna razon aparece en productos para vender")
        self.assertTrue(mecha not in vendedor.productos_vendidos, "La mecha por alguna razon aparece en productos vendidos")
        self.assertEqual("No tenemos {} en stock".format(mecha.tipo), ret, "La expresion para printear no coincide")

    def test_buscar_producto_Mecha(self):
        #arrange
        vendedor = Vendedor()
        cosa = Mecha(100, 10, "madera", 252525, 1200)

        #act
        ret = vendedor.buscar_producto(cosa)

        #assert
        self.assertEqual("Tenemos {} disponible".format(cosa.tipo), ret, "La expresion para printear no coincide")

    def test_buscar_producto_Fresa(self):
        # arrange
        vendedor = Vendedor()
        consulta_producto = Fresa(10, "redondeo", 14, 2000, 25321)

        # act
        ret = vendedor.buscar_producto(consulta_producto)

        # assert
        self.assertEqual("Tenemos {} disponible".format(consulta_producto.tipo), ret, "La expresion para printear no coincide")

    def test_buscar_producto_inexistente(self):
        # arrange
        vendedor = Vendedor()
        cosa = Mecha(15, 10, "Madera", 265489, 1520)

        # act
        ret = vendedor.buscar_producto(cosa)

        # assert
        self.assertEqual("No tenemos {} disponible".format(cosa.tipo), ret, "La expresion para printear no coincide")

    def test_vender_martillo_existente(self):
        #arrange
        vendedor = Vendedor()
        cosa = Martillo(400, "Construccion", 30, 990, 777890)

        #act
        ret = vendedor.vender_martillo(cosa)

        #assert
        self.assertEqual(f"Se vendió un {cosa.tipo}", ret, "La expresion para printear no coincide")
        self.assertTrue(cosa not in vendedor.lista_de_prod_para_vender)
        self.assertTrue(cosa in vendedor.productos_vendidos)

    def test_vender_martillo_inexistente(self):
        #arrange
        vendedor = Vendedor()
        cosa = Martillo(400, "Construccion", 30, 990, 777000)

        #act
        ret = vendedor.vender_martillo(cosa)

        #assert
        self.assertEqual(f"No tenemos este {cosa.tipo} en stock", ret, "La expresion para printear no coincide")
        self.assertTrue(cosa not in vendedor.lista_de_prod_para_vender, "Por alguna razon la cosa está en la list_de_prod a vender")
        self.assertTrue(cosa not in vendedor.productos_vendidos, "Por alguna razon la cosa está en la lista de prod_vendidos")

    def test_buscar_producto_martillo_existente(self):
        #arrange
        vendedor = Vendedor()
        cosa = Martillo(400, "Construccion", 30, 990, 777890)

        #act
        ret = vendedor.buscar_producto(cosa)

        #assert
        self.assertEqual("Tenemos este {} disponible".format(cosa.tipo), ret, "La expresion para printear no coincide")

    def test_buscar_producto_martillo_inexistente(self):
        #arrange
        vendedor = Vendedor()
        cosa = Martillo(300, "Construccion", 30, 990, 888888)

        #act
        ret = vendedor.buscar_producto(cosa)

        #assert
        self.assertEqual("No tenemos ese {} disponible".format(cosa.tipo), ret, "La expresion para printear no coincide")

#Probar si se pueden vender dos mechas con el mismo codigo de barras y dos identicas con distinto codigo de barra. Una debe existir y venderla y la otra no deberia existir
