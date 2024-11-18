from formula.tipsLogic import updateTips

def menuUpdateTips():
    while True:
        try:
            print("""
            =============================================
                       ACTUALIZAR UNA PROPINA POR ID
            =============================================
            """)
            tipId = input("Ingrese el ID de la propina que desea actualizar: ")
            newAmount = input("Ingrese el nuevo monto de la propina: ")
            updateTips(tipId, newAmount)
            print("=============================================")
            
            selectedOption = input("Presiona '0' para regresar: ")
            if selectedOption == "0":
                print("Regresando al menú anterior...")
                break
            else:
                print("Error: Ingresa '0' para regresar.")
        except KeyboardInterrupt:
            print("\nPor favor, usa '0' para regresar.")