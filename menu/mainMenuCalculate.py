import os
from menu.calculateTipMenu import desing as calculateTip
from menu.divideAmountsMenu import desing as divideAmounts

def desing():
    while True:
        try:
            print("""
            =============================================
                        SIMULADOR DE PROPINA
            =============================================
            1. Calcular propina y total a pagar
            2. Calcular total a pagar dividido entre varias personas
            3. Atrás
            =============================================
            """)
            selectedOption = int(input("Por favor, elige una opción (1-3): "))
            
            if selectedOption == 1:
                calculateTip()
            elif selectedOption == 2:
                divideAmounts()
            elif selectedOption == 3:
                os.system('clear')
                break
            else:
                print("Error: Opción inválida.")
        except ValueError:
            print("Error: Ingresa un número válido 1, 2 o 3.")
        except KeyboardInterrupt:
            print("\nPor favor, usa la opción \"3\" para salir.")