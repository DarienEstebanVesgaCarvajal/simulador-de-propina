def calcular_propina(total, porcentaje):  
    try:
        decimal = porcentaje / 100  
        propina = decimal * total  
    except TypeError:
        print("Error: los valores deben ser numéricos.")
        return None
    except Exception:
        print("Error: ocurrió un problema inesperado.")
        return None
    return propina  
  
def calcular_total_con_propina(total, propina):  
    try:
        total_con_propina = total + propina
    except TypeError:
        print("Error: los valores deben ser numéricos.")
        return None
    except Exception:
        print("Error: ocurrió un problema inesperado.")
        return None
    return total_con_propina  
  
def dividir_total(total, personas):  
    try:
        if personas <= 0:
            print("Error: el número de personas debe ser mayor que 0.")
            return None
        return total / personas
    except TypeError:
        print("Error: los valores deben ser numéricos.")
        return None
    except Exception:
        print("Error: ocurrió un problema inesperado.")
        return None