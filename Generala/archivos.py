import json
import csv

def cargar_nivel(ruta_json):
    archivo = open(ruta_json, "r", encoding='utf-8')
    data = json.load(archivo)
    archivo.close()
    return data

def guardar_puntaje(nombre_jugador, puntaje_total, ruta_csv="puntajes.csv"):
    archivo = open(ruta_csv, "a", newline="", encoding="utf-8")
    writer = csv.writer(archivo)
    writer.writerow([nombre_jugador, puntaje_total])
    archivo.close()

def cargar_mejores_puntajes(ruta_csv="puntajes.csv", cantidad=10):
    import os
    if not os.path.exists(ruta_csv):
        return []
    
    archivo = open(ruta_csv, "r", encoding="utf-8")
    reader = csv.reader(archivo)
    puntajes = []
    
    for fila in reader:
        if len(fila) == 2:
            nombre = fila[0]
            puntos = int(fila[1])
            puntajes.append((nombre, puntos))
    
    archivo.close()
    
    for i in range(len(puntajes)):
        for j in range(i + 1, len(puntajes)):
            if puntajes[i][1] < puntajes[j][1]:
                temp = puntajes[i]
                puntajes[i] = puntajes[j]
                puntajes[j] = temp
    
    return puntajes[:cantidad]