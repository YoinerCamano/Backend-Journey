from day5_sqlite.consultas import buscar_lectura_por_sensor
from day5_sqlite.db import insertar_lectura

def obtener_lecturas_validas(name_db: str, sensor: str) -> dict:
    """
    Obtiene y valida las lecturas de un sensor específico en la base de datos.

    Args:
        name_db (str): Nombre del archivo de la base de datos.
        sensor (str): Nombre del sensor a buscar.

    Returns:
        dict: Diccionario con las lecturas válidas encontradas.
    """
    lecturas = buscar_lectura_por_sensor(name_db, sensor)
    lecturas_validas = []
   
    for lectura in lecturas:
        lecturas_validas_tempo = {}
        id_, sensor, temperatura, humedad, fecha = lectura
        lecturas_validas_tempo["id"] = id_
        lecturas_validas_tempo["sensor"] = sensor
        lecturas_validas_tempo["fecha"] = fecha

        if (10 <= temperatura <= 50):
            lecturas_validas_tempo["temperatura"] = temperatura

        if  (0 <= humedad <= 100):
            lecturas_validas_tempo["humedad"] = humedad

        lecturas_validas.append(lecturas_validas_tempo)

    return lecturas_validas

def agregar_lecturas_si_valida(name_db: str, sensor: str, temperatura: float, humedad: float) -> bool:
    """
    Agrega una lectura a la base de datos si es válida.

    Args:
        name_db (str): Nombre del archivo de la base de datos.
        sensor (str): Nombre del sensor.
        temperatura (float): Temperatura de la lectura.
        humedad (float): Humedad de la lectura.

    Returns:
        bool: True si la lectura fue agregada, False si no es válida.
    """
    if 10 <= temperatura <= 50 and 0 <= humedad <= 100:
        insertar_lectura(name_db, sensor, temperatura, humedad)               
        return True
    return False