from formula.logic import calcular_propina, calcular_total_con_propina, dividir_total 

import os

def desing():
    option = 1
    while option == 1:
        print(f"""
        =============================================
            Dividir Cuenta entre Varias Personas
        =============================================""")
        total = float(input("\tIngrese el monto total de la cuenta: $"))
        porcentaje = int(input("\tIngrese el porcentaje de propina (por ejemplo: 10, 15 o 20):"))
        personas = int(input("\tIngrese el número de personas:"))

        propina = calcular_propina(total, porcentaje)
        total_con_propina = calcular_total_con_propina(total, propina)
        personas = dividir_total(total, personas)
        print(f"""=============================================
        La propina calculada es: ${propina:.2f}
        El total a pagar es: ${total_con_propina:.2f}
        Monto por persona: ${personas:.2f}
        =============================================""")

        option = int(input("¿Deseas calcular nuevamente? (1 - Sí | 0 - No): "))
    os.system('clear')
    return total_con_propina, propina, personas, porcentaje