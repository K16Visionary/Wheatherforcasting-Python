import requests
import json
import pyttsx3

while True:
    print("________________________Weather Condition Checking________________________")
    print("If you want to exit the program type == Q\n")
    city = input("Enter the city name: ")
    if city == "Q":
        break
    url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

    r = requests.get(url)
    weather_data = json.loads(r.text)
    city = weather_data["location"]["name"]
    state = weather_data["location"]["region"]
    temperature = weather_data["current"]["temp_c"]
    condition = weather_data["current"]["condition"]["text"]


    print(f"The name of city is {city}.")
    print(f"The name of State of the city {city} is {state}.")
    print(f"The current temperature in {city} is {temperature}°C.")
    print(f"The weather condition is {condition}.")


    engine = pyttsx3.init()
    engine.say(f"The name of city is {city}.")
    engine.say(f"The name of State of the city {city} is {state}.")
    engine.say(f"The current temperature in {city} is {temperature} degrees Celsius.")
    engine.say(f"The weather condition is {condition}.")
    engine.runAndWait()
