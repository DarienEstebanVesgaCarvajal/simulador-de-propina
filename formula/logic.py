def calcular_propina(total, porcentaje):  
    try:
        decimal = porcentaje / 100  
        propina = decimal * total  
    except TypeError:
        print("Error al calcular la propina: los valores deben ser numéricos.")
        return None
    except Exception:
        print("Error al calcular la propina: ocurrió un problema inesperado.")
        return None
    return propina  
  
def calcular_total_con_propina(total, propina):  
    try:
        total_con_propina = total + propina
    except TypeError:
        print("Error al calcular el total con propina: los valores deben ser numéricos.")
        return None
    except Exception:
        print("Error al calcular el total con propina: ocurrió un problema inesperado.")
        return None
    return total_con_propina  
  
def dividir_total(total, personas):  
    try:
        if personas <= 0:
            print("Error al dividir el total: el número de personas debe ser mayor que 0.")
            return None
        return total / personas
    except TypeError:
        print("Error al dividir el total: los valores deben ser numéricos.")
        return None
    except Exception:
        print("Error al dividir el total: ocurrió un problema inesperado.")
        return None