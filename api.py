import requests
from datetime import datetime, timedelta

def get_weather_forecast(date_time, location):
    user_api = 'ca7f97251a8e3e4fd7d10d6d94546ceb'  # Twój klucz API

    # Konwersja podanej daty i godziny na obiekt datetime
    forecast_datetime = datetime.strptime(date_time, "%Y-%m-%d %H:%M")

    # Obliczenie czasu 24 godziny (1 dzień) wstecz
    start_datetime = forecast_datetime - timedelta(days=1)

    # Formatowanie daty i godziny do używanego formatu w zapytaniu API
    start_time_unix = int(start_datetime.timestamp())
    forecast_time_unix = int(forecast_datetime.timestamp())

    complete_api_link = f"https://history.openweathermap.org/data/2.5/history/city?lat={location['lat']}&lon={location['lon']}&type=hour&start={start_time_unix}&end={forecast_time_unix}&appid={user_api}"
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

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
        date_time = forecast_datetime.strftime("%d %b %Y | %I:%M:%S %p")

        # Utworzenie słownika z danymi prognozy
        forecast = {
            'location': location,
            'date_time': date_time,
            'temperature': temp_city,
            'weather_desc': weather_desc,
            'humidity': hmdt,
            'wind_speed': wind_spd
        }

        return forecast

    else:
        return None

# Przykładowe użycie API
forecast_date_time = input("Podaj datę i godzinę w formacie RRRR-MM-DD HH:MM: ")
forecast_location = {'lat': 51.5074, 'lon': -0.1278}  # Przykładowe współrzędne dla Londynu

forecast = get_weather_forecast(forecast_date_time, forecast_location)

if forecast is not None:
    print("-------------------------------------------------------------")
    print("Weather Forecast for - {}  || {}".format(forecast_location, forecast['date_time']))
    print("-------------------------------------------------------------")
    print("Temperature: {:.2f} deg C".format(forecast['temperature']))
    print("Weather description:", forecast['weather_desc'])
    print("Humidity: {}%".format(forecast['humidity']))
    print("Wind speed: {} km/h".format(forecast['wind_speed']))
else:
    print("Błąd w pobieraniu danych o pogodzie. Sprawdź wprowadzone dane.")
