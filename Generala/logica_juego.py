from dados import tirar_dados

def inicializar_juego():
    
    estado = {
        "puntajes": {
            "unos": None,
            "doses": None, 
            "treses": None,
            "cuatros": None,
            "cincos": None,
            "seises": None,
            "escalera": None,
            "full": None,
            "poker": None,
            "generala": None
        },
        "categorias_restantes": 10,
        "puntaje_total": 0,
        "ronda_actual": 1
    }
    return estado


def juego_terminado(estado_juego):
    
    return estado_juego["categorias_restantes"] == 0


def obtener_mejor_categoria(dados, estado_juego):
    
    from calculadora_puntos import evaluar_todas_categorias  
    
    puntajes_posibles = evaluar_todas_categorias(dados)
    mejor_puntaje = 0
    mejor_categoria = None

    for categoria in puntajes_posibles:
        puntos = puntajes_posibles[categoria]
        
        if estado_juego["puntajes"][categoria] is None:
            if puntos > mejor_puntaje:
                mejor_puntaje = puntos
                mejor_categoria = categoria


    return mejor_categoria, mejor_puntaje


def categorias_disponibles(estado_juego):
    
    disponibles = []
   
    for categoria in estado_juego["puntajes"]:
        puntos = estado_juego["puntajes"][categoria]
        if puntos is None:
            disponibles.append(categoria)
    return disponibles

def actualizar_puntaje(estado_juego, categoria, puntos):
        #verifica si la categoria esta en uso
    if estado_juego["puntajes"][categoria] is None:
        #guarda puntaje
        estado_juego["puntajes"][categoria] = puntos
        #resta la categorias 
        estado_juego["categorias_restantes"] -= 1
        #suma al punaje
        estado_juego["puntaje_total"] += puntos
        return True
    else:
        return False

def avanzar_ronda(estado_juego):
    
    estado_juego["ronda_actual"] += 1

"""
def turno_rival(dados, juego_maquina):
   
    from calculadora_puntos import evaluar_todas_categorias
    
    puntajes_posibles = evaluar_todas_categorias(dados)
    mejor_categoria = None
    mejor_puntaje = 0
    
    #busca mejor categoria
    for categoria in juego_maquina["puntajes"]:
        if juego_maquina["puntajes"][categoria] is None:
            puntos = puntajes_posibles[categoria]
            if puntos > mejor_puntaje:
                mejor_puntaje = puntos
                mejor_categoria = categoria
    
    #anota puntos
    if mejor_categoria:
        actualizar_puntaje(juego_maquina, mejor_categoria, mejor_puntaje)
        return mejor_categoria, mejor_puntaje
    
    return None, 0
"""

def mostrar_comparativa(jugador, maquina):
    """
    Muestra la comparativa de puntajes
    """
    print("\n" + "="*40)
    print("="*40)
    print(f" TUS PUNTOS: {jugador['puntaje_total']}")
    print(f" RIVAL: {maquina['puntaje_total']}")
    
    diferencia = jugador['puntaje_total'] - maquina['puntaje_total']
    if diferencia > 0:
        print(f"Vas ganando por {diferencia} puntos")
    elif diferencia < 0:
        print(f"Vas perdiendo por {abs(diferencia)} puntos")
    else:
        print("Están empatados")
    print("="*40)


