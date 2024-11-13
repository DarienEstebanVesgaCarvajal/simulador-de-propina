from formula.logic import calcular_propina, calcular_total_con_propina

import os

def desing():
    repeatOption = 1
    while repeatOption == 1:
        print(f"""
        =============================================
                    Cálculo de Propina
        =============================================""")
        total = float(input("  Ingrese el monto total de la cuenta: $"))
        porcentaje = int(input("  Ingrese el porcentaje de propina (por ejemplo: 10, 15 o 20): "))

        propina = calcular_propina(total, porcentaje)
        total_con_propina = calcular_total_con_propina(total, propina)

        print(f"""
        =============================================
        La propina calculada es: ${propina:.2f}
        El total a pagar es: ${total_con_propina:.2f}
        =============================================
        """)

        option = int(input("¿Deseas calcular nuevamente? (1 - Sí | 0 - No): "))
    os.system('clear')
    return propina, total_con_propina, option