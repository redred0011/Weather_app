import pytest
import requests
from datetime import datetime
import sqlite3
from Currently_weather import get_weather_forecast, get_location_name, get_coordinates


def test_get_weather_forecast():
    # Preparation of test data
    lat = 52.2297
    lon = 21.0122
    expected_result = {
        'location': '(52.2297, 21.0122)',
        'temperature': 20.0,
        'weather_desc': 'Cloudy',
        'humidity': 75,
        'wind_speed': 5.5
    }
    
    # Mocking responses from the API
    expected_data = {
        "cod": 200,
        "weather": [{"description": "Cloudy"}],
        "main": {"temp": 293.15, "humidity": 75},
        "wind": {"speed": 5.5},
    }
    response_mock = requests.models.Response()
    response_mock.status_code = 200
    response_mock.json = lambda: expected_data
    requests.get = lambda url: response_mock
    
    # Calling the function under test
    result = get_weather_forecast(lat, lon)
    
    # Sprawdzenie wyników
    assert result == expected_result

def test_get_location_name():
    # Preparation of test data
    lat = 52.2297
    lon = 21.0122
    expected_result = 'Warsaw'
    
    # Mocking responses from the API
    expected_data = [{"name": "Warsaw"}]
    response_mock = requests.models.Response()
    response_mock.status_code = 200
    response_mock.json = lambda: expected_data
    requests.get = lambda url: response_mock
    
    # Calling the function under test
    result = get_location_name(lat, lon)
    
    # Checking the results
    assert result == expected_result

def test_get_coordinates():
    # Preparation of test data
    location_name = 'Warsaw'
    expected_lat = 52.2297
    expected_lon = 21.0122
    
    # Mocking responses from the API
    expected_data = [{"lat": 52.2297, "lon": 21.0122}]
    response_mock = requests.models.Response()
    response_mock.status_code = 200
    response_mock.json = lambda: expected_data
    requests.get = lambda url: response_mock
    
    # Calling the function under test
    lat, lon = get_coordinates(location_name)
    
    # Checking the results
    assert lat == expected_lat
    assert lon == expected_lon

