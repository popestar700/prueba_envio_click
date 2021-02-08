import unittest
import conteo_vocales

class TestConteoVocales(unittest.TestCase):

    def test_conteo_vocales(self):
        self.assertEqual(conteo_vocales.contarVocales('agua'), 3)
        self.assertRaises(TypeError, conteo_vocales.contarVocales('agua'))
    
if __name__ == "__main__":
    unittest.main()