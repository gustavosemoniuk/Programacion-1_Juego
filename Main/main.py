while True:
    print("\n" + "=" * 40)
    print("           🎲 GENERALA  🎲")
    print("=" * 40)
    print("1. Jugar")
    print("2. Estadísticas")
    print("3. Créditos")
    print("4. Salir")
    print("=" * 40)

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        print("\nIniciando el juego...\n")
        # Acá iría la función que maneja la partida
    elif opcion == "2":
        print("\nMostrando estadísticas...\n")
        # Acá iría la función que muestra las estadísticas
    elif opcion == "3":
        pass
    elif opcion == "4":
        print("\nGracias por jugar. ¡Hasta la próxima!\n")
        break
    else:
        print("\nOpción incorrecta. Intente nuevamente.\n")
