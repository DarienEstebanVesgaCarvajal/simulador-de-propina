from formula.logic import calcular_propina, calcular_total_con_propina, dividir_total

import os

def desing():
    repeatOption = 1
    
    zeroInvalidMessage = "Error: El valor no puede ser 0."
    invalidInputMessage = "Error: Por favor, ingresa un valor numérico válido."
    totalPrompt = "  Ingrese el monto total de la cuenta: $"
    percentagePrompt = "  Ingrese el porcentaje de propina (por ejemplo: 10, 15 o 20): "
    peoplePrompt = "  Ingrese el número de personas: "
    repeatPrompt = "¿Deseas calcular nuevamente? (1 - Sí | 0 - No): "

    while repeatOption == 1:
        try:
            print(f"""
            =============================================
                 Dividir Cuenta entre Varias Personas
            =============================================""")

            total = float(input(totalPrompt))
            if total <= 0:
                print(zeroInvalidMessage)
                continue

            porcentaje = int(input(percentagePrompt))
            if porcentaje < 0:
                print("Error: El porcentaje de propina no puede ser negativo.")
                continue

            personas = int(input(peoplePrompt))
            if personas <= 0:
                print(zeroInvalidMessage)
                continue

            propina = calcular_propina(total, porcentaje)
            total_con_propina = calcular_total_con_propina(total, propina)
            monto_por_persona = dividir_total(total_con_propina, personas)

            print(f"""
            =============================================
            La propina calculada es: ${propina:.2f}
            El total a pagar es: ${total_con_propina:.2f}
            Monto por persona: ${monto_por_persona:.2f}
            =============================================
            """)

        except ValueError:
            print(invalidInputMessage)
            continue

        while True:
            try:
                repeatOption = int(input(repeatPrompt))
                if repeatOption not in [0, 1]:
                    print("Error: Debe ingresar un número válido 1 o 0.")
                    continue
                break
            except ValueError:
                print("Error: Debe ingresar un número válido 1 o 0.")
        
        os.system('clear')

    return propina, total_con_propina, monto_por_persona, repeatOption