database = [
    {"id": 1, "amount": 10.0},
    {"id": 2, "amount": 15.5},
    {"id": 3, "amount": 20.0},
]

def getAllTipsFromDB():
    return database

def getTipById(tipId):
    for tip in database:
        if tip["id"] == int(tipId):
            return tip
    return None

def updateTipInDB(tipId, newAmount):
    for tip in database:
        if tip["id"] == int(tipId):
            tip["amount"] = float(newAmount)
            return tip
    return None

def deleteTipFromDB(tipId):
    global database
    database = [tip for tip in database if tip["id"] != int(tipId)]
    return True