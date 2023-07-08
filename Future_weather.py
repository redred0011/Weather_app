import requests
import sqlite3

def get_future_weather(location, api_key):
    
    unit_group = "metric"
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup={unit_group}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data
    
def main():
    
    choose_language = input("What language? (English - E / Polish - P): ").lower() #Pobieranie danych od użytkownika 
    
    if choose_language == "p":
        connect = sqlite3.connect('Prognoza pogody.db')  #Nazwa pliku w którym zostaje utworzona baza programu  (sqlite3)
        c = connect.cursor()
    
        choose_days = int(input("Podaj liczbę dni, z których chcesz otrzymać prognozę pogody - maks. 15:"))   #Pobieranie danych od użytkownika 

        if 1 <= choose_days <= 15:
            location = input("Podaj lokalizację (np. London): ") #Pobieranie danych od użytkownika 
            api_key = 'H3BHSY2VSQD8XSZ3VD76RNDZM'
        
            weather_data = get_future_weather(location, api_key)

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

            
            for index, day_data in enumerate(weather_data['days']):
                if index >= choose_days:
                    break
                print("Data:", day_data['datetime'])   #Wyświetlanie danych pobranych z klucza API 
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
            
            connect.close()  #Zamknięcie połączenia z bazą sqlite3
            
            print("Dane zostały dodane do bazy danych.")
        else:
            print("Wprowadzono nieodpowiednią liczbę dni. Spróbuj ponownie.")
            
    if choose_language == "e":
        connect = sqlite3.connect('Future Weather.db')  # The name of the file in which the program base is created (sqlite3)
        c = connect.cursor()
    
        choose_days = int(input("Enter the number of days for which you want to receive a weather forecast - max. 15:"))   #Retrieving data from the user

        if 1 <= choose_days <= 15:
            location = input("Enter your location (e.g. London): ") #Retrieving data from the user
            api_key = 'H3BHSY2VSQD8XSZ3VD76RNDZM'
        
            weather_data = get_future_weather(location, api_key)

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
            
            for index, day_data in enumerate(weather_data['days']):
                if index >= choose_days:
                    break
                print("Date:", day_data['datetime'])
                print("Weather description:", day_data['description'])
                print("Min Temperature:", day_data['tempmax'])
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
            
            connect.close()  #Close connection to sqlite3 database
            
            print("The data has been added to the database.")
        else:
            print("Incorrect number of days entered. Try again.")
            main()
    else:
        main()
