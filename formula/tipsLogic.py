from requests.databaseTipsOnly import getAllTipsFromDB, getTipById, updateTipInDB, deleteTipFromDB

def listTips():
    tips = getAllTipsFromDB()
    if not tips:
        print("No hay propinas registradas.")
    else:
        print("\n--- Lista de Propinas ---")
        for tip in tips:
            print(f"ID: {tip['id']}, Monto: {tip['amount']}, Fecha: {tip['date']}")
        print("--------------------------\n")


def seekTips(tipId):
    tip = getTipById(tipId)
    if not tip:
        print(f"No se encontró ninguna propina con el ID: {tipId}")
    else:
        print("\n--- Detalle de la Propina ---")
        print(f"ID: {tip['id']}, Monto: {tip['amount']}, Fecha: {tip['date']}")
        print("--------------------------------\n")


def updateTips(tipId, newAmount):
    success = updateTipInDB(tipId, newAmount)
    if success:
        print(f"Propina con ID {tipId} actualizada correctamente a {newAmount}.")
    else:
        print(f"No se pudo actualizar la propina con ID {tipId}. Verifica que el ID sea válido.")


def deleteTips(tipId):
    success = deleteTipFromDB(tipId)
    if success:
        print(f"Propina con ID {tipId} eliminada correctamente.")
    else:
        print(f"No se pudo eliminar la propina con ID {tipId}. Verifica que el ID sea válido.")