import random
import datetime


def weather_prediction(selected_day, temperature_c, temperature_f, temperature_k, wind_sp, wind_dir, cloud, rain):
    print(f"""This is my prediction for the {selected_day}:
    The temperature: {temperature_c}°C ({temperature_f}°F, {temperature_k} K).
    The forecast for wind speed is {wind_sp} km/h. The wind will blow from: {wind_dir}.
    The rain possibility: {rain}. 
    It will be {cloud}. """)
    return


def exit_question(name):
    if input(f"<Do You want to check another date {name}? (Y)es/(N)o?> ").lower() == "n":
        print("Have a nice day! And remember about Your flawless Weather Companion! ")
        exit(0)


current_date = datetime.datetime.now()

wind_directions = ["East", "West", "North", "South"]
clouds = ["cloudy", "sunny", "partially cloudy"]

season = None
rain_possibility = None
customer_name = input("<Welcome to Your Weather Companion! Please enter Your name:> ").capitalize()

while True:
    winter_temp_celsjus = random.randrange(-35, 3)
    spring_temp_celsjus = random.randrange(4, 20)
    summer_temp_celsjus = random.randrange(15, 35)
    autumn_temp_celsjus = random.randrange(5, 19)
    winter_temp_farenheit = int(winter_temp_celsjus * 1.8 + 32)
    spring_temp_farenheit = int(spring_temp_celsjus * 1.8 + 32)
    summer_temp_farenheit = int(summer_temp_celsjus * 1.8 + 32)
    autumn_temp_farenheit = int(autumn_temp_celsjus * 1.8 + 32)
    winter_temp_kelvin = int(winter_temp_celsjus + 273.15)
    spring_temp_kelvin = int(spring_temp_celsjus + 273.15)
    summer_temp_kelvin = int(summer_temp_celsjus + 273.15)
    autumn_temp_kelvin = int(autumn_temp_celsjus + 273.15)
    wind_direction_choice = random.choice(wind_directions)
    clouds_choice = random.choice(clouds)
    wind_speed = random.randrange(0, 150)
    try:
        date_question = input(f'<Hello {customer_name}, if You want me to predict the weather, '
                              f'please enter the date in DD-MM-YYYY format:> ')
        day, month, year = map(int, date_question.split('-'))
    except ValueError:
        print("Something went wrong, remember to input the correct date in DD-MM-YYYY format.")
        continue
    if day not in range(1,32):
        print("Something went wrong, remember to input the correct date in DD-MM-YYYY format.")
        continue
    elif month not in range(1, 13):
        print("Something went wrong, remember to input the correct date in DD-MM-YYYY format.")
        continue
    elif day in range(1,32) and month == 2:
        print("Something went wrong, remember to input the correct date in DD-MM-YYYY format.")
        continue
    if month in range(4, 7):
        season = "spring"
    elif month in range(6, 10):
        season = "summer"
    elif month in range(9, 12):
        season = "autumn"
    else:
        season = "winter"
    if clouds == "sunny":
        rain_possibility = "no rain"
    elif clouds == "partially cloudy":
        rain_possibility = 'possible rain'
    else:
        rain_possibility = "rain"
    if year < current_date.year or year > current_date.year:
        print(f"Great Scott, it looks like we're traveling in time! Let's try again Marty...uhm...{customer_name}!  ")
        continue
    elif year <= current_date.year and month <= current_date.month and day < current_date.day:
        print(f"Great Scott, it looks like we're traveling in time! Let's try again Marty...uhm...{customer_name}!  ")
        continue
    elif year == current_date.year and month <= current_date.month and day == current_date.day:
        print(f"{customer_name}, just look out of the window. ")
    else:
        if season == "spring":
            weather_prediction(date_question, spring_temp_celsjus, spring_temp_farenheit, spring_temp_kelvin,
                               wind_speed, wind_direction_choice, clouds_choice, rain_possibility)
            if not exit_question(customer_name):
                continue
        elif season == "summer":
            weather_prediction(date_question, summer_temp_celsjus, summer_temp_farenheit, summer_temp_kelvin,
                               wind_speed, wind_direction_choice, clouds_choice, rain_possibility)
            if not exit_question(customer_name):
                continue
        elif season == "autumn":
            weather_prediction(date_question, autumn_temp_celsjus, autumn_temp_farenheit, autumn_temp_kelvin,
                               wind_speed, wind_direction_choice, clouds_choice, rain_possibility)
            if not exit_question(customer_name):
                continue
        else:
            weather_prediction(date_question, winter_temp_celsjus, winter_temp_farenheit, winter_temp_kelvin,
                               wind_speed, wind_direction_choice, clouds_choice, rain_possibility)
            if not exit_question(customer_name):
                continue
