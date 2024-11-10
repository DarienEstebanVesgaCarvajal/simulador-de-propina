def calcular_propina(total, porcentaje):
    return total * (porcentaje / 100)

def calcular_total_con_propina(total, propina):
    return total + propina

def desing():
    print(f"""
    =============================================
                Cálculo de Propina
    =============================================""")
    total = float(input("   Ingrese el monto total de la cuenta: $"))
    porcentaje = int(input("   Ingrese el porcentaje de propina (por ejemplo: 15): "))

    propina = calcular_propina(total, porcentaje)
    total_con_propina = calcular_total_con_propina(total, propina)

    print(f"""
    =============================================
    La propina calculada es: ${propina:.2f}
    El total a pagar es: ${total_con_propina:.2f}
    =============================================
    ¿Deseas calcular nuevamente? (S/N)
    """)
    
    return propina, total_con_propina