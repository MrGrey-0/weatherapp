import tkinter as tk  # Importing the tkinter library for GUI
import requests  # Importing requests library to make HTTP requests

# API key and base URL for accessing OpenWeatherMap's weather data
api_key = "95c04ba2daacd5cf2bf1db4d88890cdc"
base_url = "https://api.openweathermap.org/data/2.5/weather"

# Function to retrieve weather data from the API
def get_api(city):
    # Construct the complete URL for the API request
    complete_url = f"{base_url}?appid={api_key}&q={city}"
    response = requests.get(complete_url)  # Sending the GET request
    data = response.json()  # Parsing response data to JSON format

    # Check if there was an error in the API call
    if response.status_code == 200:  # HTTP status code for success
        if "main" in data:  # Check if 'main' key exists in response
            main_data = data["main"]
            current_temp_kelvin = main_data["temp"]  # Get temperature in Kelvin
            current_temp_celsius = current_temp_kelvin - 273.15  # Convert Kelvin to Celsius
            weather_data = data["weather"]
            weather_description = weather_data[0]["description"]  # Weather description
            return round(current_temp_celsius, 2), weather_description
        else:
            print(f"Error: {data.get('message', 'No additional information available')}")
            return None, None  # Return None if 'main' key is not found
    else:
        print(f"Error: {data.get('message', 'City not found or invalid API key')}")
        return None, None  # Return None if there is an error

# Function to display the weather information for the entered city
def show_city(event=None):
    city = entry.get()  # Get the city name from the entry field
    temperature, weather_description = get_api(city)  # Fetch temperature and description
    if temperature is not None:
        # Display the weather information in the label
        weather_city.config(text=f"The weather in {city} is {temperature}°C with {weather_description}")
    else:
        # Display an error message if the city is not found or there was an error
        weather_city.config(text="City Not Found")

# Initialize the main application window
root = tk.Tk()
root.title("Weather App")  # Title for the window
root.configure(background="black")  # Set background color to black
root.geometry("800x800")  # Set the window size

# Create and place a label for the welcome message
label = tk.Label(root, text="Welcome to my Weather App made with Python!", background="black", foreground="white", font=("Arial", 25))
label.place(x=50, y=25)

# Label prompting the user to enter a city name
label = tk.Label(root, text="Please type in the city where you want the weather information", background="black", foreground="white", font=("Arial", 20))
label.place(x=25, y=100)

# Entry field for the user to type in the city name
entry = tk.Entry(root, width=25, background="black", foreground="white", font=("Arial", 20))
entry.place(x=225, y=200)
entry.bind("<Return>", show_city)  # Bind the Return key to trigger the show_city function

# Label to display the weather information or error message
weather_city = tk.Label(root, text="The weather information is:", background="black", foreground="white", font=("Arial", 20))
weather_city.place(x=75, y=300)

# Start the main event loop
root.mainloop()
