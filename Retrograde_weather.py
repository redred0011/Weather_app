import requests

def get_historical_weather(start_date, end_date, location, api_key):
    unit_group = "metric"
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}?unitGroup={unit_group}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    
    choose_options = input("Okres z jakiego chcesz pogodę jest większy niż jeden dzień? T/N? ").lower()
    
    if choose_options == "t":
        location = input("Podaj lokalizację (np. London): ")
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
            else:
                print("Brak danych pogodowych dla podanego zakresu dat i lokalizacji.")
    
    elif choose_options == "n":
        location = input("Podaj lokalizację (np. London): ")
        start_date = input("Podaj datę (RRRR-MM-DD): ")
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
                break # Pętla zostanie przerwana po pierwszym przejściu przez pętlę for 
            else:
                print("Brak danych pogodowych dla podanego zakresu dat i lokalizacji.")


    
    