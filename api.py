import requests
from datetime import datetime

def get_weather_forecast(lat, lon):
    user_api = 'ca7f97251a8e3e4fd7d10d6d94546ceb'  # Twój klucz API
    
    api_link = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={user_api}"
    api_data = requests.get(api_link).json()
    
    if api_data['cod'] == 200:
        # Pobranie danych o pogodzie z odpowiednich kluczy
        weather_data = api_data['weather'][0]
        main_data = api_data['main']
        wind_data = api_data['wind']

        # Wyciągnięcie wartości z danych o pogodzie
        temp_city = main_data['temp'] - 273.15
        weather_desc = weather_data['description']
        hmdt = main_data['humidity']
        wind_spd = wind_data['speed']

        # Utworzenie słownika z danymi pogodowymi
        weather_info = {
            'location': f"({lat}, {lon})",
            'temperature': temp_city,
            'weather_desc': weather_desc,
            'humidity': hmdt,
            'wind_speed': wind_spd
        }

        return weather_info

    else:
        return None


# Przykładowa funkcja uruchamiająca aplikację
def run_weather_app():
    lat = input("Wprowadź szerokość geograficzną:")
    lon = input("Wprowadź długość geograficzną:")
    
    weather_info = get_weather_forecast(lat,lon)
    
    if weather_info is not None:
        print("-------------------------------------------------------------")
        print("Pogoda dla {}  ||".format(weather_info['location']))
        print("-------------------------------------------------------------")
        print("Temperatura: {:.2f} °C".format(weather_info['temperature']))
        print("Opis pogody:", weather_info['weather_desc'])
        print("Wilgotność: {}%".format(weather_info['humidity']))
        print("Prędkość wiatru: {} km/h".format(weather_info['wind_speed']))
    else:
        print("Błąd w pobieraniu danych o pogodzie. Sprawdź wprowadzone współrzędne.")

# Uruchomienie aplikacji
run_weather_app()
