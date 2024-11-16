import os

def desing():
    invalidInputMessage = "Error: Ingresa un número válido 1, 2 o 3."
    while True:
        try:
            print(f"""
            =============================================
                        SIMULADOR DE PROPINA
            =============================================
            1. Calcular propina y total a pagar
            2. Calcular total a pagar dividido entre varias personas
            3. Salir
            =============================================
            """)
            selectedOption = int(input("Por favor, elige una opción (1-3): "))
            
            if selectedOption in [1, 2, 3]:
                os.system('clear')
                return selectedOption
            else:
                print(invalidInputMessage)
        
        except ValueError:
            print(invalidInputMessage)
        except KeyboardInterrupt:
            print("\nPor favor, usa la opción \"3\" para salir.")