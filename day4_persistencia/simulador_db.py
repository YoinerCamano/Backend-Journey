import json
import os   

DB_FILE = 'simulador_db.json'


def insertar_registro(dato):
    """Inserta un registro en la base de datos."""
    datos = leer_todos()
    datos.append(dato)
    with open(DB_FILE, 'w') as archivo:
        json.dump(datos, archivo, indent=2)
    
def leer_todos():
    """Lee todos los registros de la base de datos."""
    if not os.path.exists(DB_FILE):
        return []  # Retorna una lista vacía si el archivo no existe
    with open(DB_FILE, 'r') as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON.")
            return []

def eliminar_por_sensor(sensor):
    """Elimina todos los registros de un sensor específico."""
    datos = leer_todos()
    datos_filtrados = [dato for dato in datos if dato['sensor'] != sensor]
    with open(DB_FILE, 'w') as archivo:
        json.dump(datos_filtrados, archivo, indent=2)