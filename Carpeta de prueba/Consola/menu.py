# menu/menu.py

def mostrar_menu_principal():
    print("\n" + "=" * 60)
    print("        ⚔️ 𝔾𝔼ℕ𝔼ℝ𝔸𝕃𝔸 𝔻𝔸ℝ𝕂 𝔽𝔸ℕ𝕋𝔸𝕊𝕐 ⚔️".center(60))
    print("=" * 60)
    
    print("""
            1) Jugar
            2) Estadisticas
            3) Créditos
            4) Salir
    """)

    opcion = input("       → Elegi una opción (1-4): ").strip()
    return opcion


def ejecutar_menu():
    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            print("\n🩸 Iniciando partida... (aca llamamos a la funcion de juego)")
        
        elif opcion == "2":
            print("\n📜 Mostrando estadisticas... (acá llamamos a estadísticas)")

        elif opcion == "3":
            print("\n🕯️ Mostrando creditos...\n")

        elif opcion == "4":
            print("\n⚰️ Saliendo del reino oscuro...")
            break
        
        else:
            print("\n❗ Opcion invalida. Intenta de nuevo.")
