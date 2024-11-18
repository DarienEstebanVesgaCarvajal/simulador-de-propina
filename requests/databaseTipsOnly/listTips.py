import requests

API_URL = 'https://673a2c14a3a36b5a62f0f21d.mockapi.io'

def list_tips(resource):
    try:
        response = requests.get(f'{API_URL}/{resource}')
        response.raise_for_status()
        tips = response.json()
        return tips
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos: {e}")
        return None

if __name__ == "__main__":
    resource = 'calcular_propinas'
    tips = list_tips(resource)
    if tips:
        print(f"Lista de propinas: {tips}")
