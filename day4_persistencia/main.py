from simulador_db import insertar_registro, leer_todos, eliminar_por_sensor

insertar_registro({'sensor': 'ESP32_01', 'temperatura': 33, 'humedad': 62})
insertar_registro({'sensor': 'ESP32_01', 'temperatura': 28, 'humedad': 50})

print("Lecturas Actuales:")

print(leer_todos())


#eliminar_por_sensor('ESP32_01')
print("Lecturas Después de Eliminar sensor ESP32_01:")
print(leer_todos())
