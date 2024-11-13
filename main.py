from menu.mainMenu import desing as principalDesing
from menu.calculateTipMenu import desing as firstOptionDesing
from menu.divideAmountsMenu import desing as secondOptionDesing
from menu.thanksMenu import desing as thirdOptionDesing

userSelection = principalDesing()

print(f"La opción seleccionada es {userSelection}.")

if userSelection == 1:
    firstOptionDesing()
elif userSelection == 2:
    secondOptionDesing()
elif userSelection == 3:
    thirdOptionDesing()
else:
    print("Opción inválida. Por favor, intenta de nuevo.")