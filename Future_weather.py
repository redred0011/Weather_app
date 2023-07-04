import requests
import sqlite3

def get_future_weather(location, api_key):
    
    unit_group = "metric"
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup={unit_group}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data
    
def main():
    connect = sqlite3.connect('Future Weather.db')
    c = connect.cursor()
    
    choose_days = int(input("Podaj liczbę dni, z których chcesz otrzymać prognozę pogody - maks. 15:"))

    if 1 <= choose_days <= 15:
        location = input("Podaj lokalizację (np. London): ")
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

        # Wstawianie danych
        for index, day_data in enumerate(weather_data['days']):
            if index >= choose_days:
                break
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
        
        # Zatwierdzanie zmian
        connect.commit()

        # Zamykanie połączenia
        connect.close()
        print("Dane zostały dodane do bazy danych.")
    else:
        print("Wprowadzono nieodpowiednią liczbę dni. Spróbuj ponownie.")

main()