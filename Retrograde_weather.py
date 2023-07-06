import requests
import sqlite3 

def get_historical_weather(start_date, end_date, location, api_key):
    unit_group = "metric"
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}?unitGroup={unit_group}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def main():    #Główna funkcja programu do interakcji z użytkownikiem i wyświetlania danych pogodowych.
   
    choose_options = input("Okres z jakiego chcesz pogodę jest większy niż jeden dzień(Max 5 dni jednorazowo)? T/N? ").lower() #Pobieranie danych od użytkownika 
    
    if choose_options == "t":
        
        connect = sqlite3.connect('Retrograde Weathers.db')
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
                main()
            else:
                print("Brak danych pogodowych dla podanego zakresu dat i lokalizacji.")
                main()
         
    
    elif choose_options == "n":
        
        connect = sqlite3.connect('Retrograde Weather.db')
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
        
        if 'days' in weather_data:
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
                connect.close()
                break
                
            else:
                print("Brak danych pogodowych dla podanego zakresu dat i lokalizacji.")
                main()
    else:
        main()
