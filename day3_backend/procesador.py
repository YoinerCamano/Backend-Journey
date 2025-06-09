from utils import filtrar_sensor, calcular_promedio
from validador import validar_lectura

def extraer_datos(nombre_archivo):
    """Extrae datos de un archivo JSON."""
    import json

    with open(nombre_archivo, "r") as archivo:
        lecturas = json.load(archivo)

    return lecturas

def procesar_lecturas(lecturas:list, nombre_sensor:str, umbral_temperatura:float = 32):
    """Procesa las lecturas de un sensor y calcula promedios y alertas."""
    
    lecturas_validas = [lectura for lectura in lecturas if validar_lectura(lectura)]
    sensor_data = filtrar_sensor(lecturas_validas, nombre_sensor)

    promedio_temperatura = calcular_promedio(sensor_data, "temperatura")
    promedio_humedad = calcular_promedio(sensor_data, "humedad")

    alerta = [data for data in sensor_data if data["temperatura"] > umbral_temperatura]
    
    return promedio_temperatura, promedio_humedad, alerta