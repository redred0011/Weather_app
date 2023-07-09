# _Weather Application_ 

### About program:

> The weather application allows you to present the weather forecast for the next 15 
days, the current weather and historical data from the last 5 days for the selected
location. The program uses API keys available for free on the OpenWeatherMap and Weather 
Visual Crossing portals to download weather information.

> The application provides detailed weather information for each location, such as
temperature, humidity, weather description, etc. The weather data is stored in an 
SQLite3 database, which was created specifically for this purpose.

> I invite you to test
my personal weather app.
            _redred0011_   


### Main functions program:
- Currently Weather 
- Retrograde weather
- Future weather
 
### Currently Weather
   > The application includes a feature that allows the user to check the current weather 
    for a specific place or geographic coordinates. This feature allows you to quickly
    get information about temperature, humidity, wind speed and other weather parameters
    in real time.

#### Using the function
- The user choose option - in case he enters "c"
- The user choose language 
- The user choose how will be search Weather place 
- The user enters Search name or Coordinaties 
- The user can enter the place or geographical coordinates for which he
wants to get a weather forecast.
- The user receives final result 
#### Sample result 
    Weather for: Warsaw || (52.2319581, 21.0067249)
    -------------------------------------------------------------
    Temperature: 23.41 °C
    Weather description: clear sky
    Humidity: 61%
    Wind speed: 4.12 km/h
    
### Retrograde Weather

> The Retrograde Weather application includes a feature that allows the
user to check the past weather (up to 30 years back) for a specific
place or geographic coordinates. This function provides information
about temperature, humidity, wind speed and other weather parameters
for the past time

#### Using the function
- The user selects if the weather he wants has more than one day
- The user choose location
- The user enters start data
- The user enters end data 
- The user receives final result 

#### Sample result 
    Date: 2020-10-10
    Weather description: Partly cloudy throughout the day with late afternoon rain.
    Max Temperature: 18.8
    Min Temperature: 10.9
    Wind speed: 21.9
    --------------------
    Date: 2020-10-11
    Weather description: Partly cloudy throughout the day with early morning rain.
    Max Temperature: 12.4
    Min Temperature: 7.1
    Wind speed: 17.1
    --------------------
    Date: 2020-10-12
    Weather description: Cloudy skies throughout the day with rain.
    Max Temperature: 9.3
    Min Temperature: 6.4
    Wind speed: 21.5
    --------------------
    Date: 2020-10-13
    Weather description: Cloudy skies throughout the day with a chance of rain throughout the day.
    Max Temperature: 9.8
    Min Temperature: 6.0
    Wind speed: 33.6
    --------------------
-

### Future Weather
>  The Future Weather app includes a feature that allows you to
user to check future weather (up to 15 days) for a specific one
place. This feature provides information
about temperature, humidity, wind speed and other weather parameters
in the future

#### Using the function
-  The user enters the number of days he wants to know
-  The user enters location 
-  The user receives final result 

#### Sample result 
    Date: 2023-06-30
    Weather description: Partly cloudy throughout the day with late afternoon rain.
    Max Temperature: 26.9
    Min Temperature: 14.0
    Wind speed: 18.3
    --------------------
    Date: 2023-07-01
    Weather description: Partly cloudy throughout the day with early morning rain.
    Max Temperature: 23.8
    Min Temperature: 17.5
    Wind speed: 9.0
    --------------------
    Date: 2023-07-02
    Weather description: Partly cloudy throughout the day.
    Max Temperature: 22.4
    Min Temperature: 17.2
    Wind speed: 19.8

## Things used

- [PyTest] - Testing functions and finding bugs
- [SQLite3] - Stores weather data
- [Visual Studio Code] - Helps me with the code I entered
- [Git Bash] - Helps me connect online and standard repository
- [Github] - My main repositories
- [Openweatherma] - Gives me the current date
- [Weather.visualcrossing.com] - Gives me past and future weather

## License 

_redred0011_   
