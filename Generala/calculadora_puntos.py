def calcular_puntos_base(dados, categoria):
    
    numero_categoria = {"unos": 1,
                        "doses": 2,
                        "treses": 3,
                        "cuatros": 4,
                        "cincos": 5,
                        "seises": 6}[categoria]
    puntos = 0
    for dado in dados:
        if dado == numero_categoria:
            puntos += dado
    
    return puntos

def es_escalera(dados):
    dados_ordenados = sorted(dados)
    escalera1 = [1, 2, 3, 4, 5]
    escalera2 = [2, 3, 4, 5, 6]
    return dados_ordenados == escalera1 or dados_ordenados == escalera2

def es_full(dados):
    
    conteo = {}
    for dado in dados:
        if dado in conteo:
            conteo[dado] += 1
        else:
            conteo[dado] = 1

    tiene_tres = False
    tiene_dos = False
    
    for cantidad in conteo.values():
        if cantidad == 3:
            tiene_tres = True
        if cantidad == 2:
            tiene_dos = True
        if cantidad == 5:  
            return True
    
    return tiene_tres and tiene_dos

def es_poker(dados):
    conteo = {}
    for dado in dados:
        if dado in conteo:
            conteo[dado] += 1
        else:
            conteo[dado] = 1
    
    for cantidad in conteo.values():
        if cantidad >= 4:
            return True
    
    return False

def es_generala(dados):
    primer_dado = dados[0]
    for dado in dados:
        if dado != primer_dado:
            return False
    return True

def evaluar_todas_categorias(dados):
    puntajes = {}
    
    # Categorias basicas
    puntajes["unos"] = calcular_puntos_base(dados, "unos")
    puntajes["doses"] = calcular_puntos_base(dados, "doses")
    puntajes["treses"] = calcular_puntos_base(dados, "treses")
    puntajes["cuatros"] = calcular_puntos_base(dados, "cuatros")
    puntajes["cincos"] = calcular_puntos_base(dados, "cincos")
    puntajes["seises"] = calcular_puntos_base(dados, "seises")
    
    # Categorias especiales
    puntajes["escalera"] = 20 if es_escalera(dados) else 0
    puntajes["full"] = 30 if es_full(dados) else 0
    puntajes["poker"] = 40 if es_poker(dados) else 0
    puntajes["generala"] = 50 if es_generala(dados) else 0
    
    return puntajes