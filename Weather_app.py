import requests
from datetime import datetime
import Retrograde_weather


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

def get_location_name(lat, lon):
    user_api = 'ca7f97251a8e3e4fd7d10d6d94546ceb'

    api_link = f"https://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid={user_api}"
    api_data = requests.get(api_link).json()

    if api_data:
        location_name = api_data[0]['name']
        return location_name

    return None

def get_coordinates(location_name):
    user_api = 'ca7f97251a8e3e4fd7d10d6d94546ceb'
    
    api_link = f"https://api.openweathermap.org/geo/1.0/direct?q={location_name}&limit=1&appid={user_api}"
    api_data = requests.get(api_link).json()
    
    if api_data:
        lat = api_data[0]['lat']
        lon = api_data[0]['lon']
        return lat, lon
    
    return None, None
def main_2():
    
    Retrograde_weather.main()
    x = Retrograde_weather.main()
    print(x)
    
def run_weather_app():
    
    choose_option = input("Currently weather? - C / Retrograde weather? - R ").lower()
    
    if choose_option == "r":   
       
       main_2()
        
    elif choose_option == "c":   
        choose_language = input("What language? (English - E / Polish - P): ")
        
    
        #Function "lower" changes all letters to lowercase    
        if choose_language.lower() == "e":
            choose_ways = input("Search Name - N / Coordinates - C: ")
        
            if choose_ways.lower() == "n":
                location_name = input("Enter city name:")
                lat, lon = get_coordinates(location_name)
            elif choose_ways.lower() == "c":
                lat = input("Enter latitude (e.g., 52.2297):")
                lon = input("Enter longitude (e.g., 21.0122):")
            else:
                print("Invalid selection.")
                return
        
            weather_info = get_weather_forecast(lat, lon)
            location_name = get_location_name(lat, lon)

            if weather_info is not None and location_name is not None:
                current_data = datetime.now().date()
                print("---------------------",current_data,"--------------------------")
                print("Weather for: {} || {}".format(location_name, weather_info['location']))
                print("-------------------------------------------------------------")
                print("Temperature: {:.2f} °C".format(weather_info['temperature']))
                print("Weather description:", weather_info['weather_desc'])
                print("Humidity: {}%".format(weather_info['humidity']))
                print("Wind speed: {} km/h".format(weather_info['wind_speed']))
                if weather_info is not None and location_name is not None:    #save to file txt
                
                    file_name = "Weather_"+("{}_".format(location_name)) + str(datetime.now().date()) +  ".txt" #name file is "Weather and current date"
                
                    with open(file_name, "w") as file:
                        file.write("Weather for: {} || {}\n".format(location_name, weather_info['location']))
                        file.write("Temperature: {:.2f}°C\n".format(weather_info['temperature']))
                        file.write("Humidity: {}%\n".format(weather_info['humidity']))
                        file.write("Wind speed: {} km/h\n".format(weather_info['wind_speed']))
                    run_weather_app()
                else:
                    print("Error fetching weather data or city name. Check the entered coordinates.")
                    run_weather_app()
            
        elif choose_language.lower() == "p":
            
            choose_ways = input("Szukanie nazwą - N / Współrzędnymi - C: ")
        
            if choose_ways.lower() == "n":
                location_name = input("Wprowadź nazwę miejscowości:")
                lat, lon = get_coordinates(location_name)
            elif choose_ways.lower() == "c":
                lat = input("Wprowadź szerokość geograficzną (np. 52.2297):")
                lon = input("Wprowadź długość geograficzną (np. 21.0122):")
            else:
                print("Nieprawidłowy wybór.")
                return
        
            weather_info = get_weather_forecast(lat, lon)
            location_name = get_location_name(lat, lon)

            if weather_info is not None and location_name is not None:   
                print("-------------------------------------------------------------")
                print("Pogoda dla {} || {}".format(location_name, weather_info['location']))
                print("-------------------------------------------------------------")
                print("Temperatura: {:.2f} °C".format(weather_info['temperature']))
                print("Opis pogody:", weather_info['weather_desc'])
                print("Wilgotność: {}%".format(weather_info['humidity']))
                print("Prędkość wiatru: {} km/h".format(weather_info['wind_speed']))
                if weather_info is not None and location_name is not None:   #save to file txt
                
                    file_name = "Pogoda_"+("{}_".format(location_name)) + str(datetime.now().date()) +  ".txt"
                    with open(file_name, "w") as file:
                        file.write("Pogoda dla {} || {}\n".format(location_name, weather_info['location']))
                        file.write("Temperatura: {:.2f}°C\n".format(weather_info['temperature']))
                        file.write("Wilgotność: {}%\n".format(weather_info['humidity']))
                        file.write("Prędkość wiatru: {} km/h\n".format(weather_info['wind_speed']))
                run_weather_app()
            
            
            else:
                print("Błąd w pobieraniu danych o pogodzie lub nazwy miejscowości. Sprawdź wprowadzone dane.")
                run_weather_app()
        else: 
            run_weather_app()
    else:
        run_weather_app()
    
run_weather_app()

