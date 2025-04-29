import requests
from dotenv import load_dotenv
import os

# Завантаження змінних середовища
load_dotenv()
api_key = os.getenv('WEATHER_API_KEY')
city = input('Введіть назву міста: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'  # Додаємо units=metric для температури в °C

try:
    res = requests.get(url)
    data = res.json()

    # Отримання міста і температури
    city_name = data.get('name', 'Місто не знайдено')
    temperature = data.get('main', {}).get('temp', 'Температура не вказана')

    print(f"Місто: {city_name}")
    print(f"Температура: {temperature}°C")
except Exception as e:
    print(f'Error: {e}')