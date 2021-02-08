import cambiar_vocales
import unittest

class TestCambiarVocales(unittest.TestCase):

    def test_cambio_vocales(self):
        self.assertEqual(cambiar_vocales.cambiarVocales('agua'), 'egae')
        self.assertRaises(TypeError, cambiar_vocales.cambiarVocales('agua'))

if __name__ == "__main__":
    unittest.main()
