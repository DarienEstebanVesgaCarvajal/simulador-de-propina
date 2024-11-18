from menu.mainMenu import desing as tipeUserSelection
from menu.mainMenuCalculate import desing as principalDesing
from menu.calculateTipMenu import desing as firstOptionDesing
from menu.divideAmountsMenu import desing as secondOptionDesing
from menu.thanksMenu import desing as thirdOptionDesing

userSelection = 0
invalidOptionMessage = "Error: Opción inválida."
invalidInputMessage = "Error: Ingresa un número válido 1, 2 o 3."
userSelectionMesage = f"La opción seleccionada es {userSelection}."

while True:

    try:
        
        userSelection = tipeUserSelection()
        print()

        if userSelection == 1:

            try:
                userSelection = principalDesing()
                print(userSelectionMesage)
                
                if userSelection == 1:
                    firstOptionDesing()
                elif userSelection == 2:
                    secondOptionDesing()
                elif userSelection == 3:
                    thirdOptionDesing()
                    break  
                else:
                    print(invalidOptionMessage)

            except ValueError:
                print(invalidInputMessage)

        elif userSelection == 2:

            try:
                userSelection = principalDesing()
                print(userSelectionMesage)
                
                if userSelection == 1:
                    firstOptionDesing()
                elif userSelection == 2:
                    secondOptionDesing()
                elif userSelection == 3:
                    thirdOptionDesing()
                    break  
                else:
                    print(invalidOptionMessage)

            except ValueError:
                print(invalidInputMessage)
        
        elif userSelection == 3:
            thirdOptionDesing()
            break
        else:
            print(invalidOptionMessage)


    except ValueError:
        print(invalidInputMessage)