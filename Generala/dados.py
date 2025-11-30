import random   

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
    dados = tirar_dados()
    es_generala_servida = False
    dados_a_guardar = []
    
    # Verificar si es generala servida
    if len(set(dados)) == 1:
        es_generala_servida = True
    
    for tiro in range(1, 4):
        print(f"\n=== Tiro {tiro} de 3 ===")
        
        if tiro > 1:
            # Tirar solo dados NO guardados
            nuevos = tirar_dados(cantidad=5 - len(dados_a_guardar))
            indice_nuevo = 0
            for i in range(5):
                if i not in dados_a_guardar:
                    dados[i] = nuevos[indice_nuevo]
                    indice_nuevo += 1
        
        mostrar_dados(dados, caras)
        
        if tiro < 3:
            dados_a_guardar = dados_guardar()
            if len(dados_a_guardar) == 5:
                print("Guardaste todos los dados. Fin de la ronda.")
                break
    
    print("Fin de la ronda")
    return dados, es_generala_servida