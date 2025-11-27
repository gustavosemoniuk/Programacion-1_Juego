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
    
    from calculadora_puntos import evaluar_todas_categorias  # Importamos la evaluación
    
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

