import os
from requests.databaseTipsOnly import listTips, seekTips, updateTips, deleteTips 


def desing():
    while True:
        try:
            print("""
            =============================================
                   ADMINISTRACIÓN DE PROPINAS INDIVIDUALES
            =============================================
            1. Listar propinas
            2. Buscar propina
            3. Actualizar propina
            4. Eliminar propina
            5. Atrás
            =============================================
            """)
            selectedOption = int(input("Por favor, elige una opción (1-5): "))
            
            if selectedOption == 1:
                listTips()
            elif selectedOption == 2:
                seekTips()
            elif selectedOption == 3:
                updateTips()
            elif selectedOption == 4:
                deleteTips()
            elif selectedOption == 5:
                os.system('clear')
                break
            else:
                print("Error: Opción inválida.")
        except ValueError:
            print("Error: Ingresa un número válido 1, 2, 3, 4 o 5.")
        except KeyboardInterrupt:
            print("\nPor favor, usa la opción \"5\" para salir.")