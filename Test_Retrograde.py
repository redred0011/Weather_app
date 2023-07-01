import requests
from unittest import mock
import pytest

def get_historical_weather(start_date, end_date, location, api_key):
    unit_group = "metric"
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}?unitGroup={unit_group}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def test_get_historical_weather():
    start_date = '2023-06-01'
    end_date = '2023-06-05'
    location = 'London'
    api_key = 'H3BHSY2VSQD8XSZ3VD76RNDZM'

    # Mock response data
    mock_response = {
        'days': [
            {
                'datetime': '2023-06-01',
                'description': 'Sunny',
                'tempmax': 25,
                'tempmin': 18,
                'windspeed': 10
            },
            {
                'datetime': '2023-06-02',
                'description': 'Cloudy',
                'tempmax': 22,
                'tempmin': 15,
                'windspeed': 12
            },
            {
                'datetime': '2023-06-03',
                'description': 'Rainy',
                'tempmax': 20,
                'tempmin': 14,
                'windspeed': 8
            }
        ]
    }

    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_response

        data = get_historical_weather(start_date, end_date, location, api_key)

        mock_get.assert_called_once_with(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}?unitGroup=metric&key={api_key}")
        assert data == mock_response

if __name__ == '__main__':
    pytest.main()
