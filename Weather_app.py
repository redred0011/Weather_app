import requests
from datetime import datetime
import Retrograde_weather
import Future_weather
import Currently_weather


def main_1(): #The function retrieves data from a project file named "Retrograde_weather" and then runs it
    
    Retrograde_weather.main() 
    print(Retrograde_weather.main())


def main_2(): #The function retrieves data from a project file named "Future_weather" and then runs it
    
    Future_weather.main()
    print(Future_weather.main())
    

def main_3():  #The function retrieves data from a project file named "Currently_weather" and then runs it
    
    Currently_weather.main() 
    print(Currently_weather.main())
   

def run_weather_app(): #The main function of Weather_app
    
    
    choose_option = input("Currently weather? - C / Retrograde weather? - R / Future weather ? - F:").lower()  #Retrieving data from the user
    
    if choose_option == "f": 
        
        main_2()
    
    elif choose_option == "r":   
       
        main_1()
        
    elif choose_option == "c":   
        
        main_3()
    
    
        
run_weather_app() # Restarting the application


