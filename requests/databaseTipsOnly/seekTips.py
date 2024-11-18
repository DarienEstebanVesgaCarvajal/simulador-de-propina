import requests

API_URL = 'https://673a2c14a3a36b5a62f0f21d.mockapi.io'

def seek_tip(resource, tip_id):
    try:
        response = requests.get(f'{API_URL}/{resource}/{tip_id}')
        response.raise_for_status()
        tip = response.json()
        return tip
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos: {e}")
        return None

if __name__ == "__main__":
    resource = 'calcular_propinas'
    id = '1'
    tip = seek_tip(resource, id)
    if tip:
        print(f"Propina encontrada: {tip}")
