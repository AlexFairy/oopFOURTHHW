"""
# Weather Forecast Application Script - ORIGINAL SCRIPT

def fetch_weather_data(city):
    # Simulated function to fetch weather data for a given city
    print(f"Fetching weather data for {city}...")
    # Simulated data based on city
    weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }
    return weather_data.get(city, {})

def parse_weather_data(data):
    # Function to parse weather data
    if not data:
        return "Weather data not available"
    city = data["city"]
    temperature = data["temperature"]
    condition = data["condition"]
    humidity = data["humidity"]
    return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

def get_detailed_forecast(city):
    # Function to provide a detailed weather forecast for a city
    data = fetch_weather_data(city)
    return parse_weather_data(data)

def display_weather(city):
    # Function to display the basic weather forecast for a city
    data = fetch_weather_data(city)
    if not data:
        print(f"Weather data not available for {city}")
    else:
        weather_report = parse_weather_data(data)
        print(weather_report)

def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = get_detailed_forecast(city)
        else:
            forecast = display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()
"""
# Weather Forecast Application Script - UPDATED SCRIPT

class WeatherDataFetcher:
    def __init__(self, city):
        self.city = city

    def fetch_weather_data(self):
        print(f"Fetching weather data for {self.city}...")
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(self.city, {})

class DataParser:
    def __init__(self, data):
        self.data = data

    def parse_weather_data(self):
        if not self.data:
            return "Weather data not available"
        city = self.data["city"]
        temperature = self.data["temperature"]
        condition = self.data["condition"]
        humidity = self.data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class UserInterface:
    def __init__(self, city):
        self.city = city

    def get_detailed_forecast(self):
        try:
            data = WeatherDataFetcher(self.city).fetch_weather_data()
            parsing_data = DataParser(data)
            return parsing_data.parse_weather_data()
        except Exception as e:
            return f"Error: {e}"

    def display_weather(self):
        try:
            data = WeatherDataFetcher(self.city).fetch_weather_data()
            if not data:
                print(f"Weather data not available for {self.city}")
            else:
                parsing_data = DataParser(data)
                weather_report = parsing_data.parse_weather_data()
                print(weather_report)
        except Exception as e:
            print(f"Error as shown {e}!")

def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        user_interface = UserInterface(city)
        if detailed == 'yes':
            forecast = user_interface.get_detailed_forecast()
        else:
            user_interface.display_weather()
            forecast = "Weather displayed above."
        print(forecast)

if __name__ == "__main__":
    main()