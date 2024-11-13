import os
def desing():
    print(f"""
    =============================================
                SIMULADOR DE PROPINA
    =============================================
    1. Calcular propina y total a pagar
    2. Calcular total a pagar divido entre varias personas
    3. Salir
    =============================================
    """)
    selectedOption = int(input("Por favor, elige una opción (1-3): "))
    os.system('clear')
    return selectedOption