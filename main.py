from menu.mainMenu import desing as principalDesing
from menu.calculateTipMenu import desing as firstOptionDesing

options = principalDesing()

print(f"La opción seleccionada es {options}.")

if options == 1:
    firstOptionDesing()