import random
import json

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

caras = {
      "1": "Espectro",
      "2": "Demonio",
      "3": "Guerrero Maldito",
      "4": "Hechicera",
      "5": "Dragón",
      "6": "Dios Antiguo"
    }

dados = tirar_dados()
mostrar_dados(dados, caras)