# Wheatherforcasting-Python

Step-by-step process for the provided code:

1.Import the required modules: requests, json, and pyttsx3.

2.Set up an infinite loop using while True to continuously check the weather conditions.

3.Print the heading "Weather Condition Checking".

4.Ask the user to enter a city name. If the user enters "Q", break the loop and exit the program.

5.Construct the API URL for the Weather API using the user's input city.

6.Send a GET request to the API URL using requests.get() and store the response in the variable r.

7.Parse the JSON response from the API using json.loads() and store the weather data in the variable weather_data.

8.Extract relevant information from the weather_data dictionary: city name, state, temperature, and weather condition.

9.Print the extracted information using formatted strings.

10.Initialize the text-to-speech engine using pyttsx3.init().

11.Use the engine's say() function to convert the extracted information into speech.

12.Run the text-to-speech engine using engine.runAndWait() to hear the spoken information.

13.Repeat the loop from step 3.

Output:

The code prompts the user to enter a city name. It then retrieves the current weather conditions for that city using the Weather API. The code extracts information such as the city name, state, temperature, and weather condition from the API response.

The extracted information is then printed to the console and spoken aloud using a text-to-speech engine.

The loop continues until the user enters "Q" to quit the program.
