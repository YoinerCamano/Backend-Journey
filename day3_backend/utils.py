def filtrar_sensor(lecturas, nombre_sensor:str):
    """Filtra las lecturas por el nombre del sensor.
    Args:
        lecturas (list): Lista de lecturas de sensores.
        nombre_sensor (str): Nombre del sensor a filtrar """
    return  [x for x in lecturas if x["sensor"] == nombre_sensor]

def calcular_promedio(lecturas, campo:str = "temperatura"):
    """Calcula el promedio de las temperaturas de las lecturas."""

    if not lecturas:
        return 0
    return round(sum(data[campo] for data in lecturas)/len(lecturas), 2)