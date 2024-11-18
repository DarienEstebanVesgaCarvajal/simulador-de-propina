import requests

API_URL = 'https://673a2c14a3a36b5a62f0f21d.mockapi.io'

def update_tip(resource, tip_id, data):
    try:
        response = requests.put(f'{API_URL}/{resource}/{tip_id}', json=data)
        response.raise_for_status()
        updated_tip = response.json()
        return updated_tip
    except requests.exceptions.RequestException as e:
        print(f"Error al actualizar los datos: {e}")
        return None

if __name__ == "__main__":
    resource = 'cuentas_divididas'
    tip_id = '1'
    data = {
        'totalAccount': 500,
        'percentageTip': 15,
        'calculatedTip': 75,
        'numberPersons': 2,
        'accountPerPerson': 287.5,
        'totalAcoundAndTip': 575
    }
    updated_tip = update_tip(resource, tip_id, data)
    if updated_tip:
        print(f"Propina actualizada: {updated_tip}")
