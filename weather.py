import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    api_key = 'YOUR_API_KEY_HERE'  # Replace this with your actual API key
    city = 'London'  # Example city
    weather = get_weather(api_key, city)
    if weather:
        print(f"Current temperature in {city}: {weather['main']['temp']}°C")
    else:
        print("Failed to retrieve the weather data.")
