import requests

def get_current_weather(lat, lon):
    """
    Get the current weather for a location specified by latitude and longitude.
    
    Parameters:
    lat (float): The latitude of the location
    lon (float): The longitude of the location
    
    Returns:
    dict: A dictionary containing weather information
    """
    api_key = 'e2c6dd3573c2116b3945058433c877a5'  # Replace with your OpenWeatherMap API key
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    
    # Construct the full API URL
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'metric'  # Use 'metric' to get temperature in Celsius
    }
    
    # Make the API request
    response = requests.get(base_url, params=params)
    
    # Debugging: Print the URL and response status code
    print(f"Request URL: {response.url}")
    print(f"Response Status Code: {response.status_code}")
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed']
        }
        return weather_info
    else:
        # Debugging: Print the response content
        print(f"Response Content: {response.content}")
        return {'error': 'Location not found or API request failed'}

# Example usage
""" if __name__ == "__main__":
    lat = 51.5074  # Latitude for London
    lon = -0.1278  # Longitude for London
    weather = get_current_weather(lat, lon)
    print(weather) """