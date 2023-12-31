import requests
from datetime import datetime
import sqlite3


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
        
def main(): 

    
    
    choose_language = input("What language? (English - E / Polish - P): ")  #Retrieving data from the user 
    
    
         
    if choose_language.lower() == "e":
            connect = sqlite3.connect('Currently Weather.db')
            c = connect.cursor()
            choose_ways = input("Search Name - N / Coordinates - C: ")  #Retrieving data from the user  
        
            if choose_ways.lower() == "n":
                location_name = input("Enter city name:") #Retrieving data from the user 
                lat, lon = get_coordinates(location_name)
            elif choose_ways.lower() == "c":
                lat = input("Enter latitude (e.g., 52.2297):") 
                lon = input("Enter longitude (e.g., 21.0122):")
            else:
                print("Invalid selection.")
                main()
        
            weather_info = get_weather_forecast(lat, lon)
            location_name = get_location_name(lat, lon)
            
            c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Weather'")
            existing_table = c.fetchone()

            if existing_table is None:
                c.execute('''CREATE TABLE Weather (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          Place TEXT, 
                          Date TEXT,
                          "Weather description" TEXT, 
                          "Temperature" REAL, 
                          "Humidity" REAL, 
                          "Wind speed" INTEGER)''')

            if weather_info is not None and location_name is not None:  
                current_data = datetime.now().date()
                print("---------------------",current_data,"--------------------------")   # Displaying data retrieved from the API key
                print("Weather for: {} || {}".format(location_name, weather_info['location']))
                print("-------------------------------------------------------------")
                print("Temperature: {:.2f} °C".format(weather_info['temperature']))
                print("Weather description:", weather_info['weather_desc'])
                print("Humidity: {}%".format(weather_info['humidity']))
                print("Wind speed: {} km/h".format(weather_info['wind_speed']))
                
                Place = location_name
                Date = current_data
                Weather_description =  weather_info['weather_desc']
                Temperature = weather_info['temperature']
                Humidity = weather_info['humidity']
                Wind_speed = weather_info['wind_speed']
                    
                c.execute("INSERT INTO Weather (Place, Date, \"Weather description\", \"Temperature\", \"Humidity\", \"Wind speed\") VALUES (?, ?, ?, ?, ?, ?)", (Place, Date, Weather_description, Temperature, Humidity, Wind_speed))

                connect.commit()  # Save changes to the database after the loop ends
                    
                connect.close() #Close connection to sqlite3 database
                main()
            else:
                print("Error fetching weather data or city name. Check the entered coordinates.")
                main()
       
                    
            
    elif choose_language.lower() == "p":
            
            connect = sqlite3.connect('Aktualna pogoda.db')
            c = connect.cursor()
            
            c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Weather'")
            existing_table = c.fetchone()

            if existing_table is None:
                c.execute('''CREATE TABLE Weather (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          Miejscowość TEXT, 
                          Data TEXT,
                          "Opis pogody" TEXT, 
                          "Temperatura" REAL, 
                          "Wilgotność" REAL, 
                          "Prędkość Wiatru" INTEGER)''')

            choose_ways = input("Szukanie nazwą - N / Współrzędnymi - C: ")         #Pobieranie danych od użytkownika 
        
            if choose_ways.lower() == "n":
                
                location_name = input("Wprowadź nazwę miejscowości:")    #Pobieranie danych od użytkownika 
                lat, lon = get_coordinates(location_name)
            
            elif choose_ways.lower() == "c":
               
                lat = input("Wprowadź szerokość geograficzną (np. 52.2297):")    #Pobieranie danych od użytkownika 
                lon = input("Wprowadź długość geograficzną (np. 21.0122):")      #Pobieranie danych od użytkownika 
            
            else:
                print("Nieprawidłowy wybór.")
                main()
        
            weather_info = get_weather_forecast(lat, lon)
            location_name = get_location_name(lat, lon)

            if weather_info is not None and location_name is not None:   
                current_data = datetime.now().date()
                print("-------------------------------------------------------------") #Wyświetlanie pobranych danych
                print("Pogoda dla {} || {}".format(location_name, weather_info['location']))
                print("-------------------------------------------------------------")
                print("Temperatura: {:.2f} °C".format(weather_info['temperature']))
                print("Opis pogody:", weather_info['weather_desc'])
                print("Wilgotność: {}%".format(weather_info['humidity']))
                print("Prędkość wiatru: {} km/h".format(weather_info['wind_speed']))
                Miejscowosc = location_name
                Data = current_data
                Opis_pogody =  weather_info['weather_desc']
                Temperatura = weather_info['temperature']
                Wilgotnosc = weather_info['humidity']
                Predkosc_wiatru = weather_info['wind_speed']
                    
                c.execute("INSERT INTO Weather (Miejscowość, Data, \"Opis pogody\", \"Temperatura\", \"Wilgotność\", \"Prędkość Wiatru\") VALUES (?, ?, ?, ?, ?, ?)", (Miejscowosc, Data, Opis_pogody, Temperatura, Wilgotnosc, Predkosc_wiatru))

                connect.commit()  # Zapisanie zmian w bazie danych po zakończeniu pętli
                    
                connect.close()
                main()
            else:
                print("Błąd w pobieraniu danych o pogodzie lub nazwy miejscowości. Sprawdź wprowadzone dane.")
                main()
    else:
        main()

