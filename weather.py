import requests
import tkinter as tk

def get_weather():
    city = city_entry.get()
    api_key = "f31f841d4ece3af44b574f0556b7215a"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description'].title()
        temperature = data['main']['temp']

        weather_label.config(text=f"Weather in {city.title()}:\n\nTemperature: {temperature}°C\nCondition: {weather}")
    else:
        weather_label.config(text="City not found. Please check the name and try again.")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

city_label = tk.Label(root, text="Enter city name:")
city_label.pack(pady=5)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

weather_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
weather_label.pack(pady=20)

root.mainloop()
