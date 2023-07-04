import requests
import sqlite3

def get_future_weather(location, api_key):
    
    unit_group = "metric"
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup={unit_group}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data
    
def main():
    connect = sqlite3.connect('Future_weather.db')
    c = connect.cursor()

    choose_days = int(input("Podaj liczbę dni, z których chcesz otrzymać prognozę pogody - maks. 15:"))

    if 1 <= choose_days <= 15:
        location = input("Podaj lokalizację (np. London): ")
        api_key = 'H3BHSY2VSQD8XSZ3VD76RNDZM'

        weather_data = get_future_weather(location, api_key)

        # Sprawdzenie, czy tabela już istnieje
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Weather'")
        existing_table = c.fetchone()

        if existing_table is None:
            # Tworzenie tabeli, jeśli nie istnieje
            c.execute('''CREATE TABLE Weather (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      Miejscowosc TEXT, 
                      Data TEXT, Opis_pogody TEXT, 
                      Max_temperatura REAL, 
                      Min_temperatura REAL, 
                      Predkosc_wiatru INTEGER)''')

        # Wstawianie danych
        for index, day_data in enumerate(weather_data['days']):
            if index >= choose_days:
                break
            Miejscowosc = location
            Data = day_data['datetime']
            Opis_pogody = day_data['description']
            Max_temperatura = day_data['tempmax']
            Min_temperatura = day_data['tempmin']
            Predkosc_wiatru = day_data['windspeed']
            c.execute("INSERT INTO Weather (Miejscowosc, Data, Opis_pogody, Max_temperatura, Min_temperatura, Predkosc_wiatru) VALUES (?, ?, ?, ?, ?, ?)", (Miejscowosc, Data, Opis_pogody, Max_temperatura, Min_temperatura, Predkosc_wiatru))
            
        # Zapisywanie zmian
        connect.commit()

        # Zamykanie połączenia z bazą danych
        connect.close()

        print("Dane zostały dodane do bazy danych.")
    else:
        print("Wprowadzono nieodpowiednią liczbę dni. Spróbuj ponownie.")

main()