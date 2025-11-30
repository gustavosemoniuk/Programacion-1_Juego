from utilidades import limpiar_pantalla
from archivos import cargar_mejores_puntajes

def mostrar_menu_principal():
    print("\n" + "=" * 60)
    print("         𝔾𝔼ℕ𝔼ℝ𝔸𝕃𝔸 𝔻𝔸ℝ𝕂 𝔽𝔸ℕ𝕋𝔸𝕊𝕐 ".center(60))
    print("=" * 60)
    
    print("""
            1) Jugar
            2) Estadisticas
            3) Creditos
            4) Salir
    """)

    opcion = input("       → Elegi una opción (1-4): ").strip()
    return opcion

def mostrar_estadisticas():
    mejores = cargar_mejores_puntajes()
    print("\nMEJORES PUNTAJES")
    print("=" * 30)
    
    if mejores:
        for i, (nombre, puntos) in enumerate(mejores, 1):
            print(f"{i}. {nombre}: {puntos} puntos")
    else:
        print("Aún no hay puntajes guardados")
    
    input("\nPresiona ENTER para continuar...")

def mostrar_creditos():
    limpiar_pantalla()
    print("========================================")
    print("            CRÉDITOS")
    print("========================================")
    print("Generala - Fantasía Oscura")
    print("Programación I")
    print("Desarrollado por: [Gustavo Semoniuk, Santiago Aderian]")
    print("Fecha: 2025")
    print("========================================")
    input("\nPresiona ENTER para continuar...")

def ejecutar_menu():
    from main import jugar_partida_completa  
    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            print("\n🩸 Iniciando partida...")
            jugar_partida_completa()
        
        elif opcion == "2":
            print("\n📜 Mostrando estadisticas...")
            mostrar_estadisticas()
        
        elif opcion == "3":
            print("\n🕯️ Mostrando creditos...\n")
            mostrar_creditos()
        
        elif opcion == "4":
            print("\n⚰️ Saliendo del reino oscuro...")
            break
        
        else:
            print("\n❗ Opcion invalida. Intenta de nuevo.")

if __name__ == "__main__":
    ejecutar_menu()