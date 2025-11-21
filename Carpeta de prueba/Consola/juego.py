
def pedir_dados_a_conservar():
    texto = input("ingresa los dados a conservar (ej: 1,3,5) o ENTER si ninguno: ")

    if texto.strip() == "":
        return []

    # Separar por comas 
    partes = texto.split(",")

    # Convertimos el numero o los numeros a entero
    dados = []
    for p in partes:
        numero = int(p) 
        if 1 <= numero <= 5:
            dados.append(numero)

    return dados