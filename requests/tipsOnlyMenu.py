import os

def desing():
    invalidInputMessage = "Error: Ingresa un número válido 1, 2, 3, 4 o 5."
    while True:
        try:
            print(f"""
            =============================================
                        OPERACIÓN A REALIZAR
            =============================================
            1. Listar.
            2. Buscar una Específica.
            3. Actualizar.
            4. Eliminar.
            5. Salir
            =============================================
            """)
            selectedOption = int(input("Por favor, elige una opción (1-5): "))
            
            if selectedOption in [1, 2, 3, 4, 5]:
                os.system('clear')
                return selectedOption
            else:
                print(invalidInputMessage)
        
        except ValueError:
            print(invalidInputMessage)
        except KeyboardInterrupt:
            print("\nPor favor, usa la opción \"5\" para salir.")