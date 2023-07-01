import requests
from datetime import datetime
import Retrograde_weather
import Future_weather


def get_weather_forecast(lat, lon):
    user_api = 'ca7f97251a8e3e4fd7d10d6d94546ceb'  #Klucz API

    api_link = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={user_api}"
    api_data = requests.get(api_link).json()
    

    if api_data['cod'] == 200:
        # Pobranie danych o pogodzie z klucza
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

def get_location_name(lat, lon):   #Funkcja pobiera nazwe lokalizacji za pomocą przedstawionych poprzez użytkownika współrzędnych geograficznych (lat,lan)
    
    user_api = 'ca7f97251a8e3e4fd7d10d6d94546ceb' #Klucz API
    api_link = f"https://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid={user_api}"
    api_data = requests.get(api_link).json()
    
    if api_data: #Jeśli uzyskane dane są niepuste, funkcja pobiera nazwę lokalizacji z pierwszego elementu (indeks 0) otrzymanej odpowiedzi (api_data)
        
        location_name = api_data[0]['name']
        return location_name

    return None

def get_coordinates(location_name): #Funkcja pobiera współrzędne geograficzne za pomocą podanej przez użytkownika nazwy lokalizacji 
    
    user_api = 'ca7f97251a8e3e4fd7d10d6d94546ceb'
    api_link = f"https://api.openweathermap.org/geo/1.0/direct?q={location_name}&limit=1&appid={user_api}"
    api_data = requests.get(api_link).json()
    
    if api_data:  #Jeśli uzyskane dane są niepuste (api_data), funkcja pobiera szerokość (lat) i długość (lon) geograficzną z pierwszego elementu (indeks 0)
        lat = api_data[0]['lat']
        lon = api_data[0]['lon']
        return lat, lon
    
    return None, None

def main_2(): #Funkcja pobiera dane z pliku projektu o nazwie "Retrograde_weather" a następnie uruchamia
    
    Retrograde_weather.main()
    x = Retrograde_weather.main()
    print(x)
    
def main_3():
    
    Future_weather.main()
    print(Future_weather.main())

def run_weather_app(): #Główna funkcja programu Weather_app 
    
    choose_option = input("Currently weather? - C / Retrograde weather? - R / Future weather ? - F:").lower()  #Pobieranie danych od użytkownika 
    
    if choose_option == "f": 
        
        main_3()
    
    if choose_option == "r":   
       
       main_2()
        
    elif choose_option == "c":   
        choose_language = input("What language? (English - E / Polish - P): ") #Pobieranie danych od użytkownika 
        
    
        #Function "lower" changes all letters to lowercase    
        if choose_language.lower() == "e":
            choose_ways = input("Search Name - N / Coordinates - C: ") #Pobieranie danych od użytkownika 
        
            if choose_ways.lower() == "n":
                location_name = input("Enter city name:") #Pobieranie danych od użytkownika 
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
                print("---------------------",current_data,"--------------------------")   #Wyświetlanie pobranych danych
                print("Weather for: {} || {}".format(location_name, weather_info['location']))
                print("-------------------------------------------------------------")
                print("Temperature: {:.2f} °C".format(weather_info['temperature']))
                print("Weather description:", weather_info['weather_desc'])
                print("Humidity: {}%".format(weather_info['humidity']))
                print("Wind speed: {} km/h".format(weather_info['wind_speed']))
                if weather_info is not None and location_name is not None:   
                
                    file_name = "Weather_"+("{}_".format(location_name)) + str(datetime.now().date()) +  ".txt" #Nazwa pliku "Weather and current date"
                    with open(file_name, "w") as file:     #Zapis do pliku txt
                         
                        file.write("Weather for: {} || {}\n".format(location_name, weather_info['location']))
                        file.write("Temperature: {:.2f}°C\n".format(weather_info['temperature']))
                        file.write("Humidity: {}%\n".format(weather_info['humidity']))
                        file.write("Wind speed: {} km/h\n".format(weather_info['wind_speed']))
                    
                    run_weather_app()
                
                else:
                    print("Error fetching weather data or city name. Check the entered coordinates.")
                    run_weather_app()
            
        elif choose_language.lower() == "p":
            
            choose_ways = input("Szukanie nazwą - N / Współrzędnymi - C: ")         #Pobieranie danych od użytkownika 
        
            if choose_ways.lower() == "n":
                
                location_name = input("Wprowadź nazwę miejscowości:")    #Pobieranie danych od użytkownika 
                lat, lon = get_coordinates(location_name)
            
            elif choose_ways.lower() == "c":
               
                lat = input("Wprowadź szerokość geograficzną (np. 52.2297):")    #Pobieranie danych od użytkownika 
                lon = input("Wprowadź długość geograficzną (np. 21.0122):")      #Pobieranie danych od użytkownika 
            
            else:
                print("Nieprawidłowy wybór.")
                return
        
            weather_info = get_weather_forecast(lat, lon)
            location_name = get_location_name(lat, lon)

            if weather_info is not None and location_name is not None:   
                print("-------------------------------------------------------------") #Wyświetlanie pobranych danych
                print("Pogoda dla {} || {}".format(location_name, weather_info['location']))
                print("-------------------------------------------------------------")
                print("Temperatura: {:.2f} °C".format(weather_info['temperature']))
                print("Opis pogody:", weather_info['weather_desc'])
                print("Wilgotność: {}%".format(weather_info['humidity']))
                print("Prędkość wiatru: {} km/h".format(weather_info['wind_speed']))
                if weather_info is not None and location_name is not None:   #Z
                
                    file_name = "Pogoda_"+("{}_".format(location_name)) + str(datetime.now().date()) +  ".txt"
                    
                    with open(file_name, "w") as file:                #Zapis do pliku txt
                        
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
    
run_weather_app() #Uruchomienie aplikacji ponownie 


