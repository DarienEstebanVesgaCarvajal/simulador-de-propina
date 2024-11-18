from formula.tipsLogic import seekTips

def menuSeekTips():
    while True:
        try:
            print("""
            =============================================
                        BUSCAR UNA PROPINA POR ID
            =============================================
            """)
            tipId = input("Ingrese el ID de la propina que desea buscar: ")
            seekTips(tipId)
            print("=============================================")
            
            selectedOption = input("Presiona '0' para regresar: ")
            if selectedOption == "0":
                print("Regresando al menú anterior...")
                break
            else:
                print("Error: Ingresa '0' para regresar.")
        except KeyboardInterrupt:
            print("\nPor favor, usa '0' para regresar.")