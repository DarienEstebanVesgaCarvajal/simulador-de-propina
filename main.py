from menu.mainMenu import desing as principalDesing
from menu.calculateTipMenu import desing as firstOptionDesing
from menu.divideAmountsMenu import desing as secondOptionDesing
from menu.thanksMenu import desing as thirdOptionDesing

options = principalDesing()

print(f"La opción seleccionada es {options}.")

if options == 1:
    firstOptionDesing()
elif options == 2:
    secondOptionDesing()
elif options == 3:
    thirdOptionDesing()
else:
    print("Opción inválida. Por favor, intenta de nuevo.")