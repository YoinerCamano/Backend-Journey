import json

def guardar_lecturas_json(ruta_archivo, datos):
    """Guarda las lecturas en un archivo JSON."""
    with open(ruta_archivo, 'w') as archivo:
        json.dump(datos, ruta_archivo, indent=2)
        

def cargar_lecturas_json(ruta_archivo):
    """Carga las lecturas desde un archivo JSON."""
    try:
        with open(ruta_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []  # Retorna una lista vacía si el archivo no existe
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return []