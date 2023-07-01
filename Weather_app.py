import requests
from datetime import datetime
import Retrograde_weather
import Future_weather
import Currently_weather


def main_1(): #Funkcja pobiera dane z pliku projektu o nazwie "Retrograde_weather" a następnie uruchamia
    
    Retrograde_weather.main() 
    print(Retrograde_weather.main())


def main_2(): #Funkcja pobiera dane z pliku projektu o nazwie "Future_weather" a następnie uruchamia
    
    Future_weather.main()
    print(Future_weather.main())
    

def main_3():  #Funkcja pobiera dane z pliku projektu o nazwie "Currently_weather" a następnie uruchamia
    
    Currently_weather.main() 
    print(Currently_weather.main())
   

def run_weather_app(): #Główna funkcja programu Weather_app 
    
    choose_option = input("Currently weather? - C / Retrograde weather? - R / Future weather ? - F:").lower()  #Pobieranie danych od użytkownika 
    
    if choose_option == "f": 
        
        main_2()
    
    elif choose_option == "r":   
       
        main_1()
        
    elif choose_option == "c":   
        
        main_3()
    
    
        
run_weather_app() #Uruchomienie aplikacji ponownie 


