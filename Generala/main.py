from dados import jugar_ronda
from calculadora_puntos import evaluar_todas_categorias
from logica_juego import inicializar_juego, actualizar_puntaje, categorias_disponibles, juego_terminado, avanzar_ronda
from archivos import cargar_nivel, guardar_puntaje

def jugar_turno_jugador(juego, caras):
    """
    Maneja un turno completo del jugador (sin rival por ahora)
    """
    print(f"\n🎲 TURNO {juego['ronda_actual']} - {juego['categorias_restantes']} categorías restantes")
    
    print("🎲 Tirando dados...")
    dados_finales, es_generala_servida = jugar_ronda(caras)
    
    # Si hay generala servida, el juego termina
    if es_generala_servida and juego["puntajes"]["generala"] is None:
        print("🎉 ¡GENERALA SERVIDA! ¡PARTIDA GANADA!")
        actualizar_puntaje(juego, "generala", 300)
        juego["categorias_restantes"] = 0
        return juego
    
    # Evaluar categorías normales
    puntajes_posibles = evaluar_todas_categorias(dados_finales)
    
    print("\n PUNTAJES POSIBLES:")
    disponibles = categorias_disponibles(juego)
    
    for i, categoria in enumerate(disponibles, 1):
        puntos = puntajes_posibles[categoria]
        print(f"  [{i}] {categoria}: {puntos} puntos")
    
    # categoria a puntuar
    eleccion_valida = False
    while not eleccion_valida:
        eleccion = input(f"\nElige categoría (1-{len(disponibles)}): ")
        
        if eleccion.isdigit():
            numero = int(eleccion) - 1
            
            if numero >= 0 and numero < len(disponibles):
                categoria_elegida = disponibles[numero]
                puntos_a_anotar = puntajes_posibles[categoria_elegida]
                eleccion_valida = True
            else:
                print(f"Elige un número entre 1 y {len(disponibles)}")
        else:
            print("Ingresa un número válido")
    
    # se anotan los puntos
    if actualizar_puntaje(juego, categoria_elegida, puntos_a_anotar):
        print(f"Anotados {puntos_a_anotar} puntos en {categoria_elegida}")
    else:
        print("Error: no se pudo anotar")
    
    # pasamos de ronda
    avanzar_ronda(juego)
    
    return juego

def jugar_partida_completa():
    """
    Juega una partida completa
    """
    # se carga el json
    nivel = cargar_nivel("niveles.json")
    if nivel:
        caras = nivel
    else:
        print("Error: No se pudo cargar niveles.json")
        return
    
    jugador = inicializar_juego()
    
    print("¡COMIENZA LA GENERALA!")
    
    # se juega hasta completar categorias
    while not juego_terminado(jugador):
        print(f"\n=== RONDA {jugador['ronda_actual']} ===")
        
        jugador = jugar_turno_jugador(jugador, caras)
    
    # RESULTADO FINAL
    print(f"\n¡PARTIDA TERMINADA!")
    print(f"TU PUNTAJE FINAL: {jugador['puntaje_total']}")
    
    # Guardar puntaje
    nombre = input("Ingresa tu nombre para guardar el puntaje: ")
    guardar_puntaje(nombre, jugador['puntaje_total'])
    print("Puntaje guardado correctamente")
    
    return jugador

if __name__ == "__main__":
    from interfaz_consola import ejecutar_menu
    ejecutar_menu()