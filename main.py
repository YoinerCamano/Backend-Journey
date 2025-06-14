from day6_services.servicios_lecturas import obtener_lecturas_validas, agregar_lecturas_si_valida

if __name__ == "__main__":
    name_db = "ESP32.db"
    sensor = "sensor1"
    
    # Obtener lecturas válidas
    lecturas_validas = obtener_lecturas_validas(name_db, sensor)
    for lectura in lecturas_validas:
        print(f"ID: {lectura['id']}, Sensor: {lectura['sensor']}, Fecha: {lectura['fecha']}, Temperatura: {lectura.get('temperatura', 'N/A')}, Humedad: {lectura.get('humedad', 'N/A')}")

    # Agregar una nueva lectura si es válida
    temperatura = 23.0
    humedad = -10.0
    if agregar_lecturas_si_valida(name_db, sensor, temperatura, humedad):
        print("Lectura agregada correctamente.")
    else:
        print("Lectura no válida, no se agregó.")