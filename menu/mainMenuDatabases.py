import os
from requests.tipsOnlyMenu import desing as tipsOnly
# from requests.tipsDivideMenu import desing as tipsDivide

def desing():
    while True:
        try:
            print("""
            =============================================
                       MENÚ DE BASES DE DATOS
            =============================================
            1. Administrar propinas individuales
            2. Administrar propinas divididas
            3. Atrás
            =============================================
            """)
            selectedOption = int(input("Por favor, elige una opción (1-3): "))
            
            if selectedOption == 1:
                tipsOnly()
            elif selectedOption == 2:
                tipsDivide()
            elif selectedOption == 3:
                os.system('clear')
                break
            else:
                print("Error: Opción inválida.")
        except ValueError:
            print("Error: Ingresa un número válido 1, 2 o 3.")
        except KeyboardInterrupt:
            print("\nPor favor, usa la opción \"3\" para salir.")