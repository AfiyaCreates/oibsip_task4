import datetime as dt
import requests

# function to read api key from a file
def read_api_key(file_path='API.txt'):
    try:
        with open(file_path, 'r') as file:
            API = file.read().strip()
            return API
    except FileNotFoundError:
        print(f"Error: API key file '{file_path}' not found.")
        return None


BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
API_KEY=  read_api_key()

# Function to convert temperature from Kelvin to Celsius and Fahrenheit
def k_to_c_f(kelvin):
    celsius=kelvin-273.15
    fahrenheight= celsius * (9/5) + 32
    return celsius,fahrenheight

# Function to get weather information for a given city
def get_weather(CITY):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url)

    if response.status_code==200:

         data= response.json()
         # print(response)

        # Extracting relevant weather information         
         temp_k= data['main']['temp']
         temp_c,temp_f = k_to_c_f(temp_k)
         feelslike_k = data['main']['feels_like']
         feelslike_c,feelslike_f = k_to_c_f(feelslike_k)
         wind_speed= data['wind']['speed']
         humidity= data['main']['humidity']
         description= data['weather'][0]['description']
         sunrise=dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
         sunset=dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])

        # Printing weather information
         print(f"Temperature in {CITY}: {temp_c:.2f}°C or {temp_f:.2f}°F")
         print(f"Temperature in {CITY} feels like: {feelslike_c:.2f}°C or {feelslike_f:.2f}°F")
         print(f"Humidity in {CITY}: {humidity}%")
         print(f"Wind Speed in {CITY}: {wind_speed}m/s")
         print(f"General Weather in {CITY}: {description}")
         print(f"Sun rises  in {CITY} at : {sunrise} local time.")
         print(f"Sun sets  in {CITY} at : {sunset} local time.")
    else:
        print(f"ERROR:unable to fetch data for {CITY} . please enter a valid city name")     

# Main function to run the weather app
def main():
    print("WELCOME TO WEATHER APP!!!")

    while True:
      CITY = input("Enter the location or Type 'exit' to quit:")    

      if CITY.lower() =='exit':
         break
      if not CITY:
         print("Please enter a valid city name")
         continue
      get_weather(CITY) 

      retry= input("DO you want to check data for another city?(yes/no)")  
      if retry.lower() != "yes":
            break

    print("Thank you!!!")    

if __name__=="__main__":
    main()
    



