import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from revista import Revista
class TestRevista(unittest.TestCase):
    # TODO Adiciona tus pruebas unitarias aquí.
    # Ejemplo:
    '''
    def test_multiplicar_positivos(self):
        valor_esperado = 15
        mi_cuenta = CuentaBancaria()
        valor_actual = mi_cuenta.multiplicar(3, 5)
        self.assertEqual(valor_esperado, valor_actual)
    '''
    def test_mostrar_info(self):
        valor_esperado = "Titulo: Mondongo\nAño publicacion: 2024\nNombre Revista: Punisher Magazine\nNumero Revista: 10"
        mi_revista = Revista("Mondongo", 2024, 10, "Punisher Magazine")
        valor_actual = mi_revista.mostrar_info()
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_mostrar_info_dos(self):
        valor_esperado = "Titulo: Mondongo\nAño publicacion: 2021\nNombre Revista: Rochinok Fest\nNumero Revista: 11"
        mi_revista = Revista("Mondongo", 2021, 11, "Rochinok Fest")
        valor_actual = mi_revista.mostrar_info()
        self.assertEqual(valor_esperado, valor_actual)


        
if __name__ == '__main__':
    unittest.main()
