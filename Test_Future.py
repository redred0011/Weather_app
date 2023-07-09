import requests
from unittest import mock
import pytest

def get_future_weather(location, api_key):
    unit_group = "metric"
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup={unit_group}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def test_get_future_weather():
    location = 'London'
    api_key = 'H3BHSY2VSQD8XSZ3VD76RNDZM'

    # Mock response data
    mock_response = {
        'days': [
            {
                'datetime': '2023-07-01',
                'description': 'Sunny',
                'tempmax': 25,
                'tempmin': 18,
                'windspeed': 10
            },
            {
                'datetime': '2023-07-02',
                'description': 'Cloudy',
                'tempmax': 22,
                'tempmin': 15,
                'windspeed': 12
            }
        ]
    }

    with mock.patch('requests.get') as mock_get:
       
        mock_get.return_value.json.return_value = mock_response  # Setting the values ​​that will be returned by calling json() on mock_get.return_value

        data = get_future_weather(location, api_key) # Calling the function under test

        # Check if requests.get() was called with the correct URL
        mock_get.assert_called_once_with(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&key={api_key}")
        
        
        assert data == mock_response # Check if the returned data is as expected

