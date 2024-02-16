from loguru import logger
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

def setup_logging():
    logger_format = (
        "<green>{time:HH:mm:ss}</green> | "
        "<level>{message}</level>"
    )
    logger.configure() # Default values
    logger.remove()
    logger.add(sys.stderr, format=logger_format)
    
    log_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "logs") # Get directory of where this script is running 
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    log_file = os.path.join(log_folder, "weather-{time:YYYYMMDD}.log")
    logger.add(log_file, rotation="100 MB", format=logger_format)    
    
if __name__ == "__main__":   
    setup_logging()
    
    logger.info("Starting weather reporter...")                
    api_key = '<YOUR_API_KEY_HERE>'  # Replace this with your actual API key
    city = 'Melbourne'  # Example city
    weather = get_weather(api_key, city)
    if weather:
        print(f"Current temperature in {city}: {weather['main']['temp']}°C")
    else:
        print("Failed to retrieve the weather data.")
