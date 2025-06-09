from procesador import procesar_lecturas, extraer_datos

data_sensor = extraer_datos("ESP32.json")
nombre_sensor = "ESP32_02"

promedio_temperatura, promedio_humedad, alerta = procesar_lecturas(data_sensor, nombre_sensor, 32)

print(f"Promedio de temperatura: {promedio_temperatura}°C")
print(f"Promedio de humedad: {promedio_humedad}%")

if alerta:
    for lectura in alerta:
        print(f"Alerta: {lectura['sensor']} supera el umbral de 32°C con {lectura['temperatura']}°C")
else:
    print("No se detectaron alertas de temperatura.")
