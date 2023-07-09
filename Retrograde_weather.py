import requests
import sqlite3 

def get_historical_weather(start_date, end_date, location, api_key):
    unit_group = "metric"
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}?unitGroup={unit_group}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def main():    #Główna funkcja programu do interakcji z użytkownikiem i wyświetlania danych pogodowych.
   
    choose_language = input("What language? (English - E / Polish - P): ").lower()      #Pobieranie danych od użytkownika
    
    if choose_language == "p":
    
        choose_options = input("Okres z jakiego chcesz pogodę jest większy niż jeden dzień(Max 5 dni jednorazowo)? T/N? ").lower() #Pobieranie danych od użytkownika 
    
        if choose_options == "t":
        
            connect = sqlite3.connect('Wsteczna pogoda.db')   #Nazwa pliku w którym zostaje utworzona baza programu  (sqlite3)
            c = connect.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Weather'")
            existing_table = c.fetchone()
            if existing_table is None:
                c.execute('''CREATE TABLE Weather (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          Miejscowość TEXT, 
                          Data TEXT,
                          "Opis pogody" TEXT, 
                          "Max Temperatura" REAL, 
                          "Min Temperatura" REAL, 
                          "Prędkość Wiatru" INTEGER)''')
            
            location = input("Podaj lokalizację (np. London): ")  #Pobieranie danych od użytkownika 
            start_date = input("Podaj datę początkową (RRRR-MM-DD): ")
            end_date = input("Podaj datę końcową (RRRR-MM-DD): ")
            api_key = 'H3BHSY2VSQD8XSZ3VD76RNDZM'
    
            weather_data = get_historical_weather(start_date, end_date, location, api_key)
    
            if 'days' in weather_data:
                for day_data in weather_data['days']:       #Wyświetlanie danych pobranych z klucza API 
                    print("Data:", day_data['datetime'])
                    print("Opis pogody:", day_data['description'])
                    print("Temperatura maksymalna:", day_data['tempmax'])
                    print("Temperatura minimalna:", day_data['tempmin'])
                    print("Prędkość wiatru:", day_data['windspeed'])
                    print("--------------------")

                    Miejscowosc = location              
                    Data = day_data['datetime']
                    Opis_pogody = day_data['description']
                    Max_temperatura = day_data['tempmax']
                    Min_temperatura = day_data['tempmin']
                    Predkosc_wiatru = day_data['windspeed']

                    c.execute("INSERT INTO Weather (Miejscowość, Data, \"Opis pogody\", \"Max Temperatura\", \"Min Temperatura\", \"Prędkość Wiatru\") VALUES (?, ?, ?, ?, ?, ?)", (Miejscowosc, Data, Opis_pogody, Max_temperatura, Min_temperatura, Predkosc_wiatru))

                connect.commit()  # Zapisanie zmian w bazie danych po zakończeniu pętli 
                main()
            else:
                print("Brak danych pogodowych dla podanego zakresu dat i lokalizacji.")
                main()
         
    
        elif choose_options == "n":
        
            connect = sqlite3.connect('Wsteczna pogoda.db')     #Nazwa pliku w którym zostaje utworzona baza programu  (sqlite3)
            c = connect.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Weather'")
            existing_table = c.fetchone()
            if existing_table is None:
                c.execute('''CREATE TABLE Weather (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          Miejscowość TEXT, 
                          Data TEXT,
                          "Opis pogody" TEXT, 
                          "Max Temperatura" REAL, 
                          "Min Temperatura" REAL, 
                          "Prędkość Wiatru" INTEGER)''')
       
       
            location = input("Podaj lokalizację (np. London): ") #Pobieranie danych od użytkownika 
        
            start_date = input("Podaj datę (RRRR-MM-DD):")
            end_date = start_date
            api_key = 'H3BHSY2VSQD8XSZ3VD76RNDZM'
    
            weather_data = get_historical_weather(start_date, end_date, location, api_key)
        
            if 'days' in weather_data:          #Wyświetlanie danych pobranych z klucza API 
                for day_data in weather_data['days']:
                    print("Data:", day_data['datetime'])
                    print("Opis pogody:", day_data['description'])
                    print("Temperatura maksymalna:", day_data['tempmax'])
                    print("Temperatura minimalna:", day_data['tempmin'])
                    print("Prędkość wiatru:", day_data['windspeed'])
                    print("--------------------")

                    Miejscowosc = location      
                    Data = day_data['datetime']
                    Opis_pogody = day_data['description']
                    Max_temperatura = day_data['tempmax']
                    Min_temperatura = day_data['tempmin']
                    Predkosc_wiatru = day_data['windspeed']

                    c.execute("INSERT INTO Weather (Miejscowość, Data, \"Opis pogody\", \"Max Temperatura\", \"Min Temperatura\", \"Prędkość Wiatru\") VALUES (?, ?, ?, ?, ?, ?)", (Miejscowosc, Data, Opis_pogody, Max_temperatura, Min_temperatura, Predkosc_wiatru))

                    connect.commit()  # Zapisanie zmian w bazie danych po zakończeniu pętli
                    connect.close() #Zamknięcie połączenia z bazą sqlite3
                    break   #Przerwanie pętli po podaniu danych z jednego dnia 
                
                else:
                    print("Brak danych pogodowych dla podanego zakresu dat i lokalizacji.")
                    main()
        else:
            main()
    
    if choose_language == "e":
    
        choose_options = input("The period with which you change the settings is greater than one day (Max 5 days at a time)? Y/N?").lower() #Retrieving data from the user
    
        if choose_options == "y":
        
            connect = sqlite3.connect('Retrograde Weathers.db')     # The name of the file in which the program base is created (sqlite3)
            c = connect.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Weather'")
            existing_table = c.fetchone()
            if existing_table is None:
                c.execute('''CREATE TABLE Weather (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          Place TEXT, 
                          Date TEXT,
                          "Weather description" TEXT, 
                          "Max Temperature" REAL, 
                          "Min Temperature" REAL, 
                          "Wind speed" INTEGER)''')
            
            location = input("Enter your location (e.g. London):")  #Retrieving data from the user
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD):")
            api_key = 'H3BHSY2VSQD8XSZ3VD76RNDZM'
    
            weather_data = get_historical_weather(start_date, end_date, location, api_key)
    
            if 'days' in weather_data:
                for day_data in weather_data['days']:
                    print("Date:", day_data['datetime'])
                    print("Weather description:", day_data['description'])
                    print("Max Temperature:", day_data['tempmax'])
                    print("Min Temperature:", day_data['tempmin'])
                    print("Wind speed:", day_data['windspeed'])
                    print("--------------------")

                    Place = location
                    Date = day_data['datetime']
                    Weather_description = day_data['description']
                    Max_temperature = day_data['tempmax']
                    Min_temperature = day_data['tempmin']
                    Wind_speed = day_data['windspeed']
                    connect.commit() # Save changes to the database after the loop ends
                c.execute("INSERT INTO Weather (Place, Date, \"Weather description\", \"Max Temperature\", \"Min Temperature\", \"Wind speed\") VALUES (?, ?, ?, ?, ?, ?)", (Place, Date, Weather_description, Max_temperature, Min_temperature, Wind_speed))
                 
                connect.close()
                
                main()
            else:
                print("There are no weather data for the given date range and location.")
                main()
         
    
        elif choose_options == "n": 
        
            connect = sqlite3.connect('Retrograde Weather.db') # The name of the file in which the program base is created (sqlite3)
            c = connect.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Weather'")
            existing_table = c.fetchone()
            if existing_table is None:
                c.execute('''CREATE TABLE Weather (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          Place TEXT, 
                          Date TEXT,
                          "Weather description" TEXT, 
                          "Max Temperature" REAL, 
                          "Min Temperature" REAL, 
                          "Wind speed" INTEGER)''')
       
       
            location = input("Enter your location (e.g. London):") #Retrieving data from the user 
        
            start_date = input("Enter the date (YYYY-MM-DD):")
            end_date = start_date
            api_key = 'H3BHSY2VSQD8XSZ3VD76RNDZM'
    
            weather_data = get_historical_weather(start_date, end_date, location, api_key)
        
            if 'days' in weather_data:                      # Displaying data retrieved from the API key
                for day_data in weather_data['days']:
                    print("Date:", day_data['datetime'])
                    print("Weather description:", day_data['description'])
                    print("Max Temperature:", day_data['tempmax'])
                    print("Min Temperature:", day_data['tempmin'])
                    print("Wind speed:", day_data['windspeed'])
                    print("--------------------")

                    Place = location
                    Date = day_data['datetime']
                    Weather_description = day_data['description']
                    Max_temperature = day_data['tempmax']
                    Min_temperature = day_data['tempmin']
                    Wind_speed = day_data['windspeed']

                    c.execute("INSERT INTO Weather (Place, Date, \"Weather description\", \"Max Temperature\", \"Min Temperature\", \"Wind speed\") VALUES (?, ?, ?, ?, ?, ?)", (Place, Date, Weather_description, Max_temperature, Min_temperature, Wind_speed))

                    connect.commit()  # Save changes to the database after the loop ends
                    connect.close()   #Close connection to sqlite3 database
                    break   #Loop break after one day's data
                
                else:
                    print("There are no weather data for the given date and location.")
                    main()
        else:
            main() 
    else:
        main()
