import sqlite3

def buscar_lectura_por_sensor(name_db:str, sensor:str):
    """
Busca y devuelve todas las lecturas de un sensor específico en la base de datos.

Args:
    name_db (str): Nombre del archivo de la base de datos.
    sensor (str): Nombre del sensor a buscar.

Returns:
    list[tuple]: Lista de lecturas de encontradas.
    """
    conexion_db = sqlite3.connect(name_db)
    cursor = conexion_db.cursor()
    cursor.execute('SELECT * FROM lecturas WHERE sensor = ?', (sensor,))
    resultados = cursor.fetchall()
    conexion_db.close()
    return resultados

def validar_lecturas(lecturas:list[tuple]):
    """
Valida si las lecturas tienen valores coherentes.

Args:
    lecturas (list[tuple]): Lista de tuplas con lecturas a de la base de datos.

Returns:
    reporte de cada lectura validad o invalida.
    """
    for lectura in lecturas:
        id_, sensor, temperatura, humedad, fecha = lectura
        errores = []
        if not (10 <= temperatura <= 50):
            errores.append("Temperatura fuera de rango")

        if not (0 <= humedad <= 100):
            errores.append("Humedad fuera de rango")
        
        if errores:
            print(f"[X] Lectura ID {id_} invalida ({fecha}): {', '.join(errores)}")
        else:
            print(f"[✓] Lectura ID {id_} valida ({fecha})'")

