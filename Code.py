import requests

def get_weather(city):
    api_key = "d8ecfce3b4123eabe15aff844f60c79d"  # Your OpenWeatherMap API key #this is from my own API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API call
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # For temperature in Celsius
    }
    
    # API request
    response = requests.get(base_url, params=params)
    
    # Check if the city was found
    if response.status_code == 200:
        data = response.json()
        
        # Extract weather data
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        # Display weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather['description'].title()}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("City not found. Please enter a valid city name.")

# Main program execution
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
