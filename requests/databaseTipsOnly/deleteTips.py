from formula.tipsLogic import deleteTips

def menuDeleteTips():
    while True:
        try:
            print("""
            =============================================
                       ELIMINAR UNA PROPINA POR ID
            =============================================
            """)
            tipId = input("Ingrese el ID de la propina que desea eliminar: ")
            deleteTips(tipId)  # Ejecuta la función directamente para eliminar la propina
            print("=============================================")
            
            selectedOption = input("Presiona '0' para regresar: ")
            if selectedOption == "0":
                print("Regresando al menú anterior...")
                break
            else:
                print("Error: Ingresa '0' para regresar.")
        except KeyboardInterrupt:
            print("\nPor favor, usa '0' para regresar.")