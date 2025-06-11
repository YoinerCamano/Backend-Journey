import csv

def guardar_csv(nombre_archivo, datos):
    with open(nombre_archivo, mode='w', newline='') as archivo:
        campos = ['sensor','temperatura','humedad']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)