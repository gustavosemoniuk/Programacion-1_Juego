import random   
import json

def cargar_nivel(json_niveles):
    with open(json_niveles, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    return data


def tirar_dados(cantidad=5):
    
    dados = []
    for i in range(cantidad):
        dado = random.randint(1, 6)
        dados.append(dado)
    return dados
    

def mostrar_dados(dados, caras):
    
    print("\n---Tus dados---")
    for i, valor in enumerate(dados):
        nombre = caras[str(valor)]
        print(f" Dado {i+1}: {nombre} ({valor})")



def dados_guardar():
    
    seleccion = input("Seleccione que dados quiere guardar (ej: 1,3,5) o Enter para tirar todos nuevamente: ")

    if not seleccion.strip():
        return []
    
    partes = seleccion.split(",")
    indices_guardados = []
    
    for i in partes:
        i = i.strip()
        if i.isdigit():
            numero = int(i) - 1
            if 0 <= numero < 5:
                indices_guardados.append(numero)
        else:
            print("Numero invalido.")
    
    return indices_guardados

def jugar_ronda(caras): 
    dados = [0, 0 ,0 ,0 ,0]

    for tiro in range(1, 4):
        print(f"=== Tiro {tiro} ===")

        if tiro == 1:
            dados = tirar_dados()

        else:
            guardar = dados_guardar()
            if len(guardar) == 5:
                print("Guardaste todos los dados. Fin de la ronda.")
                break

            nuevos = tirar_dados(cantidad=5 - len(guardar))
            indice_nuevo = 0
            for i in range(5):
                if i not in guardar:
                    dados[i] = nuevos[indice_nuevo]
                    indice_nuevo += 1

        mostrar_dados(dados, caras)
    
    print("Fin de la ronda")
    return dados
 


