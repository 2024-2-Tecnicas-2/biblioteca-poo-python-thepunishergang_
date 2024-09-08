import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from publicacion import Publicacion
class TestPublicacion(unittest.TestCase):
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
        valor_esperado = "Titulo: Mondongo\nAño publicacion: 2024"
        mi_publicacion = Publicacion("Mondongo", 2024)
        valor_actual = mi_publicacion.mostrar_info()
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_mostrar_info_dos(self):
        valor_esperado = "Titulo: Locura\nAño publicacion: 2020"
        mi_publicacion = Publicacion("Locura", 2020)
        valor_actual = mi_publicacion.mostrar_info()
        self.assertEqual(valor_esperado, valor_actual)
        
if __name__ == '__main__':
    unittest.main()
