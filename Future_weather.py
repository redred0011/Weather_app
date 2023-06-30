import requests

def get_future_weather(location, api_key):
    
    unit_group = "metric"
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup={unit_group}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    choose_days = int(input("Podaj liczbę dni, z których chcesz otrzymać prognozę pogody - maks. 15:"))

    if 1 <= choose_days <= 15:
        location = input("Podaj lokalizację (np. London): ")
        api_key = 'H3BHSY2VSQD8XSZ3VD76RNDZM'
        
        weather_data = get_future_weather(location, api_key)

        if 'days' in weather_data:
           
            file_name =  "Pogoda_"+("{}".format(location))+".txt" 
            with open(file_name, "w") as file:  
                for index, day_data in enumerate(weather_data['days']):
                    if index >= choose_days:
                        break
                    print("Data:", day_data['datetime'])
                    print("Opis pogody:", day_data['description'])
                    print("Temperatura maksymalna:", day_data['tempmax'])
                    print("Temperatura minimalna:", day_data['tempmin'])
                    print("Prędkość wiatru:", day_data['windspeed'])
                    print("--------------------")
                    file.write(f"Pogoda dla: {location}\n")  #Zapis do pliku txt
                    file.write(f"Data: {day_data['datetime']}\n")
                    file.write(f"Opis pogody: {day_data['description']}\n")
                    file.write(f"Temperatura maksymalna: {day_data['tempmax']}\n")
                    file.write(f"Temperatura minimalna: {day_data['tempmin']}\n")
                    file.write(f"Prędkość wiatru: {day_data['windspeed']}\n")
                    file.write("--------------------\n")
        else:
            print("Brak danych pogodowych dla podanej lokalizacji.")
    else:
        print("Wprowadzono nieodpowiednią liczbę dni. Spróbuj ponownie.")


