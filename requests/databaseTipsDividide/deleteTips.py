import requests

API_URL = 'https://673a2c14a3a36b5a62f0f21d.mockapi.io'

def delete_tip(resource, id):
    try:
        response = requests.delete(f'{API_URL}/{resource}/{id}')
        response.raise_for_status()
        print("Propina eliminada correctamente.")
    except requests.exceptions.RequestException as x:
        print(f"Error al eliminar los datos: {x}")

if __name__ == "__main__":
    resource = 'cuentas_divididas'
    id = '1' 
    delete_tip(resource, id)
