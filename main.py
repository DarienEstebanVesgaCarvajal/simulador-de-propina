from menu.mainMenu import desing as tipeUserSelection
from menu.mainMenuCalculate import desing as calculateMenu
# from menu.mainMenuDatabases import desing as databasesMenu
from menu.thanksMenu import desing as thanksMenu

def main():
    while True:
        try:
            userSelection = tipeUserSelection()
            if userSelection == 1:
                calculateMenu()
            elif userSelection == 2:
                print("Trabajo en mantenimiento.")
                # databasesMenu()
            elif userSelection == 3:
                thanksMenu()
                break
            else:
                print("Error: Opción inválida.")
        except ValueError:
            print("Error: Ingresa un número válido 1, 2 o 3.")
        except KeyboardInterrupt:
            print("\nPor favor, usa la opción \"3\" para salir.")