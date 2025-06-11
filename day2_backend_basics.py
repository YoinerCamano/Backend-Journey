def extraer_datos(name:str):
    """Extrae datos de un archivo JSON."""
    import json

    with open(name, "r") as archivo:
        lecturas = json.load(archivo)

    return lecturas

def filtrar_sensor(lecturas, nombre_sensor:str):
    """Filtra las lecturas por el nombre del sensor.
    Args:
        lecturas (list): Lista de lecturas de sensores.
        nombre_sensor (str): Nombre del sensor a filtrar """
    return  [x for x in lecturas if x["sensor"] == nombre_sensor]

def calcular_promedio(lecturas,campo:str = "temperatura"):
    """Calcula el promedio de las temperaturas de las lecturas."""

    if not lecturas:
        return 0
    sum = sum(x[campo] for x in lecturas)
    return round(sum/len(lecturas), 2)

def verificar_alerta(lecturas):
    """Verifica si alguna lectura supera un umbral de temperatura."""
    if not lecturas:
        return False
    for lectura in lecturas:
        if lectura["temperatura"] > 32:
            print(f"Alerta: {lectura['sensor']} supera el umbral de 32°C con {lectura['temperatura']}°C")
            return True
    return False

if __name__ == "__main__":
    sensor_data = extraer_datos("ESP32.json")
    ESP32_01 = filtrar_sensor(sensor_data, "ESP32_01")
    promedio_ESP32_01 = calcular_promedio(ESP32_01)
    print(f"Promedio de temperatura: {promedio_ESP32_01[0]}°C, Promedio de humedad: {promedio_ESP32_01[1]}%")
    verificar_alerta(ESP32_01)
