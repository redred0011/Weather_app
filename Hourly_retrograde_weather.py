import requests
import pprint

def get_historical_weather(start_date, end_date, location):
    api_key = "KWNPFYPS8WRKY8THZMJTJGRKG"  # Zaktualizuj klucz API
    unit_group = "metric"  # Jednostki metryczne
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}?unitGroup={unit_group}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    choose_options = input("Okres z jakiego chcesz pogodę jest większy niż jeden dzień? T/N? ").lower()
    
    if choose_options == "t":
        
        day_start = input("Podaj datę pierwszego dnia(RRRR-MM-DD): ")
        day_end = input("Podaj datę drugiego dnia(RRRR-MM-DD): ")
        place = input("Podaj miejsce: ")
        weather_data = get_historical_weather(day_start, day_end, place)
        
        if 'days' in weather_data:
            for day_data in weather_data['days']:
                print("Data", day_data['datetime'])
                print("Opis pogody :", day_data['description'])
                print("Temperatura max:", day_data['tempmax'])
                print("Temperatura min:", day_data['tempmin'])
                print("Prędokść wiatru:", day_data['windspeed'])
        else:
            print("Brak danych pogodowych dla podanej daty i miejsca.")
        
        main()
    
    elif choose_options == "n":
        
        start_end_date = input("Podaj datę pierwszego dnia (RRRR-MM-DD): ")
        end_date = start_end_date
        start_date = start_end_date
        place = input("Podaj miejsce: ")
        weather_data = get_historical_weather(start_date, end_date, place)
        
        if 'days' in weather_data:
            for day_data in weather_data['days']:
                print("Data", day_data['datetime'])
                print("Opis pogody:", day_data['description'])
                print("Temperatura max:", day_data['tempmax'])
                print("Temperatura min:", day_data['tempmin'])
                print("Prędkość wiatru:", day_data['windspeed'])
        
        else:
            print("Brak danych pogodowych dla podanej daty i miejsca.")
        
        main()
    
    else:
        print("Niepoprawny wybór.")
        main()
    
main()
