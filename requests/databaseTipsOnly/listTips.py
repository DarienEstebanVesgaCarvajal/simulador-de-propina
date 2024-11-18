from formula.tipsLogic import listTips

def menuListTips():
    while True:
        try:
            print("""
            =============================================
                          LISTAR TODAS LAS PROPINAS
            =============================================
            """)
            listTips()
            print("=============================================")
            
            selectedOption = input("Presiona '0' para regresar: ")
            if selectedOption == "0":
                print("Regresando al menú anterior...")
                break
            else:
                print("Error: Ingresa '0' para regresar.")
        except KeyboardInterrupt:
            print("\nPor favor, usa '0' para regresar.")