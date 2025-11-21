
def mostrar_planilla(planilla):
    categorias = [
        "Espectros",
        "Demonios",
        "Guerreros Malditos",
        "Hechiceras",
        "Dragones",
        "Dioses Antiguos",
        "Escalera",
        "Full",
        "Poker",
        "Generala"
    ]

    print("------ Planilla de Categorías ------")
    for i in range(10):
        nombre = categorias[i]
        puntaje = planilla[i]

        if puntaje is None:
            puntaje_mostrar = " "
        else:
            puntaje_mostrar = str(puntaje)

        print(f"{i+1}. {nombre:<20} [{puntaje_mostrar}]")
    print() 