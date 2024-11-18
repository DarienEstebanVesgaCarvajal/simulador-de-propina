from requests.databaseTipsOnly import listAllTips, listFilteredTips

def menuListTips():
    while True:
        try:
            print("""
            =============================================
                       LISTAR PROPINAS
            =============================================
            1. Mostrar todas las propinas
            2. Filtrar por un criterio
            3. Atrás
            =============================================
            """)
            selectedOption = int(input("Por favor, elige una opción (1-3): "))

            if selectedOption == 1:
                listAllTips()  # Asume que esta función lista todas las propinas
            elif selectedOption == 2:
                filterValue = input("Ingrese el criterio de búsqueda (ejemplo: monto, fecha): ")
                listFilteredTips(filterValue)  # Función para filtrar propinas según el criterio
            elif selectedOption == 3:
                print("Regresando al menú anterior...")
                break
            else:
                print("Error: Opción inválida. Por favor elige 1, 2 o 3.")
        except ValueError:
            print("Error: Ingresa un número válido 1, 2 o 3.")
        except KeyboardInterrupt:
            print("\nPor favor, usa la opción \"3\" para regresar.")
