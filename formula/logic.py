invalidInputMessage = "Error: Por favor, ingresa un valor numérico válido."
teapotProblemMessage = "Error: Soy una tetera."

def calcular_propina(total, porcentaje):  
    try:
        decimal = porcentaje / 100  
        propina = decimal * total  
    except TypeError:
        print(invalidInputMessage)
        return None
    except Exception:
        print(teapotProblemMessage)
        return None
    return propina  
  
def calcular_total_con_propina(total, propina):  
    try:
        total_con_propina = total + propina
    except TypeError:
        print(invalidInputMessage)
        return None
    except Exception:
        print(teapotProblemMessage)
        return None
    return total_con_propina  
  
def dividir_total(total, personas):  
    try:
        if personas <= 0:
            print("Error: el número de personas debe ser mayor que 0.")
            return None
        return total / personas
    except TypeError:
        print(invalidInputMessage)
        return None
    except Exception:
        print(teapotProblemMessage)
        return None