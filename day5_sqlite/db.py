import sqlite3

def crear_base_de_datos(name:str):
    """
Crea una base de datos SQLite con una tabla llamada 'lecturas'.

Args:
    name (str): Nombre del archivo de la base de datos.

La tabla 'lecturas' contiene:
    - id: Clave primaria autoincremental.
    - sensor: Nombre del sensor.
    - temperatura: Valor de temperatura.
    - humedad: Valor de humedad.
    - fecha: Fecha y hora de la lectura.
"""
    conexion_db = sqlite3.connect(name)
    cursor = conexion_db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor TEXT NOT NULL,
            temperatura REAL NOT NULL,
            humedad REAL NOT NULL,
            fecha TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conexion_db.commit()
    conexion_db.close()

def insertar_lectura(name_db:str, sensor:str, temperatura:float, humedad:float):
    """
Inserta una nueva lectura en la base de datos.

Args:
    name_db (str): Nombre del archivo de la base de datos.  
    sensor (str): Nombre del sensor.
    temperatura (float): Valor de temperatura.
    humedad (float): Valor de humedad.
"""
    conexion_db = sqlite3.connect(name_db)
    cursor = conexion_db.cursor()
    cursor.execute('''
        INSERT INTO lecturas (sensor, temperatura, humedad)
        VALUES (?, ?, ?)
    ''', (sensor, temperatura, humedad))
    conexion_db.commit()
    conexion_db.close()

def ver_lecturas(name_db:str):
    """Obtiene todas las lecturas de la base de datos.
Args:
    name_db (str): Nombre del archivo de la base de datos.
Returns:
    list: Lista de diccionarios con las lecturas.
    """
    conexion_db = sqlite3.connect(name_db)
    cursor = conexion_db.cursor()
    cursor.execute('SELECT * FROM lecturas')
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
    
    conexion_db.close()

