
import random

def mostrar_encabezado(puntos):
    print("====================================")
    print("        Generala - Dark Fantasy      ")
    print("====================================")
    print("Puntos actuales:", puntos)
    print()  

def mostrar_dados(lista_de_dados, caras):
    print("Dados actuales:")
    for valor in lista_de_dados:
        nombre = caras[valor]   # Convertimos el numero que nos salio al nombre de la tematica que elejimos
        print(f"[{nombre}]", end=" ")
    print() 
    print()  



