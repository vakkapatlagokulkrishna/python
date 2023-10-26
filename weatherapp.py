import requests

# Replace with your OpenWeatherMap API Key
api_key = "YOUR_API_KEY"
base_url = "https://lnkd.in/eQ8_h9JG?"

def get_weather_data(city_name):
  try:
    complete_url = f"{base_url}q={city_name}&appid={api_key}"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] == 200:
      main_data = data["main"]
      weather_data = data["weather"][0]
      temperature = main_data["temp"]
      humidity = main_data["humidity"]
      description = weather_data["description"]
      return temperature, humidity, description
    else:
      return None
  except requests.exceptions.RequestException as e:
    return None

def main():
  print("Welcome to the Weather App!")
  city_name = input("Enter the city name: ")

  weather_data = get_weather_data(city_name)

  if weather_data:
    temperature, humidity, description = weather_data
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description}")
  else:
    print("Unable to fetch weather data. Please check your city name or network connection.")