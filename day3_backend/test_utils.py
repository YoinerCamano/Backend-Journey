import unittest 
from utils import calcular_promedio

class TestUtils(unittest.TestCase):
    def test_calcular_promedio(self):
        """Test para la función calcular_promedio."""
        datos = [
            {"temperatura": 30, "humedad": 50},
            {"temperatura": 32, "humedad": 55},
            {"temperatura": 28, "humedad": 60}
        ]
        promedio_temperatura = calcular_promedio(datos, "temperatura")
        promedio_humedad = calcular_promedio(datos, "humedad")
        
        self.assertEqual(promedio_temperatura, 30.0)
        self.assertEqual(promedio_humedad, 55.0)
    
    def test_calcular_promedio_vacio(self):
        """Test para calcular el promedio con una lista vacía."""
        datos_vacios = []
        promedio_temperatura = calcular_promedio(datos_vacios, "temperatura")
        promedio_humedad = calcular_promedio(datos_vacios, "humedad")
        
        self.assertEqual(promedio_temperatura, 0)
        self.assertEqual(promedio_humedad, 0)

if __name__ == "__main__":
    unittest.main()