import os

def design():
    invalidInputMessage = "Error: Ingresa un número válido entre 1 y 5."

    while True:
        try:
            print("""
            =============================================
                          MENÚ DE OPERACIONES
            =============================================
            1. Listar propinas.
            2. Buscar una propina específica.
            3. Actualizar una propina.
            4. Eliminar una propina.
            5. Salir.
            =============================================
            """)
            selectedOption = int(input("¿Qué operación deseas realizar? (1-5): "))
            
            if selectedOption in [1, 2, 3, 4, 5]:
                os.system('clear')
                return selectedOption
            else:
                print(invalidInputMessage)
        
        except ValueError:
            print(invalidInputMessage)
        except KeyboardInterrupt:
            print(f"\nPor favor, usa la opción \"5\" para salir.")