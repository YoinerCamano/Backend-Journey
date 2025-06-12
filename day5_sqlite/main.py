from db import crear_base_de_datos, insertar_lectura, ver_lecturas
from consultas import buscar_lectura_por_sensor, validar_lecturas

crear_base_de_datos('ESP32.db') #Crea la base de datos y la tabla

insertar_lectura('ESP32.db', 'sensor1', 25.5, 60.0) #valida
insertar_lectura('ESP32.db', 'sensor1', 55.0, 55.0) #Temperatura fuera de rango
insertar_lectura('ESP32.db', 'sensor1', 22.0, 110) #humedad fuera de rango
insertar_lectura('ESP32.db', 'sensor1', 8.0, -10.0) #ambas fuera de rango

#Buscar y validar 
lecturas = buscar_lectura_por_sensor('ESP32.db', 'sensor1')
validar_lecturas(lecturas)
