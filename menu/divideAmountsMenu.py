import os
def design():
    option = 1
    while option:
        print(f"""
        =============================================
            Dividir Cuenta entre Varias Personas
        =============================================""")
        total = float(input("\tIngrese el monto total de la cuenta: $"))
        porcentaje = int(input("\tIngrese el porcentaje de propina (por ejemplo: 10, 15 o 20):"))
        personas = int(input("\tIngrese el número de personas:"))
        print(f"""=============================================
        La propina calculada es: $___
        El total a pagar es: $___
        Monto por persona: $___
        =============================================""")

        option = int(input("¿Deseas calcular nuevamente? (1 - Sí | 0 - No): "))
        os.system('clear')