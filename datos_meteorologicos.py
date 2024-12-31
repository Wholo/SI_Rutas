import requests

def obtener_datos_meteorologicos(ciudad):
    """
    Consulta datos meteorológicos en tiempo real para una ciudad específica.

    Args:
        ciudad (str): Nombre de la ciudad.

    Returns:
        dict: Diccionario con la temperatura y el clima, o None si ocurre un error.
    """
    API_KEY = '6ef46f82a7f13e8a3e6e9777961514af'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        datos = response.json()

        return {
            "temperatura": datos['main']['temp'],
            "clima": datos['weather'][0]['description']
        }
    except requests.exceptions.RequestException as e:
        print("Error al obtener datos meteorológicos:", e)
        return None
