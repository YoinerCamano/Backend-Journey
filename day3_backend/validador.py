def validar_lectura(data):
    claves = {"sensor", "temperatura", "humedad"}
    if not isinstance(data, dict):
        return False
    if not claves.issubset(set(data.keys())):
        return False
    if not all(isinstance(data[k], (int, float)) for k in ["temperatura", "humedad"]):
        return False
    return True