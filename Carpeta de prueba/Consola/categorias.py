
def elegir_categoria(planilla):
    print("Categorias disponibles:")
    
    for i in range(10):
        if planilla[i] is None:
            print(f"{i+1}. (Disponible)")

    while True:
        opcion = int(input("Elegi una categoria (1-10): "))

        if 1 <= opcion <= 10 and planilla[opcion - 1] is None:
            return opcion - 1   
        else:
            print("Categoria no valida o ya utilizada. Elija otra.")