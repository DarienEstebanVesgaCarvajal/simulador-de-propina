from formula.logic import calcular_propina, calcular_total_con_propina

import os

def desing():
    repeatOption = 1

    invalidInputMessage = "Error: Por favor, ingresa un valor numérico válido."
    totalPrompt = "  Ingrese el monto total de la cuenta: $"
    percentagePrompt = "  Ingrese el porcentaje de propina (por ejemplo: 10, 15 o 20): "
    repeatPrompt = "¿Deseas calcular nuevamente? (1 - Sí | 0 - No): "

    while repeatOption == 1:
        try:
            print(f"""
            =============================================
                        Cálculo de Propina
            =============================================""")
            
            total = float(input(totalPrompt))
            if total < 0:
                print("Error: El monto total no puede ser negativo.")
                continue

            porcentaje = int(input(percentagePrompt))
            if porcentaje < 0:
                print("Error: El porcentaje de propina no puede ser negativo.")
                continue

            propina = calcular_propina(total, porcentaje)
            total_con_propina = calcular_total_con_propina(total, propina)

            print(f"""
            =============================================
            La propina calculada es: ${propina:.2f}
            El total a pagar es: ${total_con_propina:.2f}
            =============================================
            """)

        except ValueError:
            print(invalidInputMessage)
            continue

        try:
            repeatOption = int(input(repeatPrompt))
            if repeatOption not in [0, 1]:
                print("Error: Ingresa 1 para continuar o 0 para salir.")
                repeatOption = 1
        except ValueError:
            print(invalidInputMessage)
            repeatOption = 1

        os.system('clear')

    return propina, total_con_propina, repeatOption