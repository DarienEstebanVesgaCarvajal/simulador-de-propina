from formula.logic import calcular_propina, calcular_total_con_propina, dividir_total 

import os

def desing():
    option = 1
    while option:
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
        La propina calculada es: ${propina:.2}
        El total a pagar es: ${total_con_propina:.2}
        Monto por persona: ${personas:.2}
        =============================================""")

        option = int(input("¿Deseas calcular nuevamente? (1 - Sí | 0 - No): "))
        os.system('clear')
        return total, porcentaje, personas