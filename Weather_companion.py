import random
import datetime


def weather_prediction(selected_date, temperature_c, wind_spd, wind_direction, cloud, rain):
    print(f"""This is my prediction for the {selected_date}:
    The temperature: {temperature_c}°C ({temperature_c * 1.8 + 32}°F, {temperature_c + 273} K).
    The forecast for wind speed is {wind_spd} km/h. The wind will blow from: {wind_direction}.
    The rain possibility: {rain}. 
    It will be {cloud}. """)
    return


def exit_question(name):
    if input(f"<Do You want to check another date {name}? (Y)es/(N)o?> ").lower() == "n":
        print("Have a nice day! And remember about Your flawless Weather Companion! ")
        exit(0)


def get_date(name):
    while True:
        try:
            date_question = input(f'<Hello {name}, if You want me to predict the weather, '
                                  f'please enter the date in DD-MM-YYYY format:> ')
            dd, mm, yyyy = map(int, date_question.split('-'))
        except ValueError:
            print("Something went wrong, remember to input the correct date in DD-MM-YYYY format.")
            continue
        wrong_day = dd not in range(1, 32)
        wrong_month = mm not in range(1, 13)
        february_issue = dd not in range(1, 29) and mm == 2
        if wrong_day or wrong_month or february_issue:
            print("Something went wrong, remember to input the correct date in DD-MM-YYYY format.")
        else:
            return dd, mm, yyyy


def get_season(chosen_month):
    if chosen_month in range(4, 7):
        part_of_the_year = "spring"
    elif chosen_month in range(6, 10):
        part_of_the_year = "summer"
    elif chosen_month in range(9, 12):
        part_of_the_year = "autumn"
    else:
        part_of_the_year = "winter"
    return part_of_the_year


current_date = datetime.datetime.now()

__wind_directions = ("East", "West", "North", "South")
__clouds = ("cloudy", "sunny", "partially cloudy")

season = None
rain_possibility = None
customer_name = input("<Welcome to Your Weather Companion! Please enter Your name:> ").capitalize()

while True:
    winter_temp_celsius = random.randrange(-35, 3)
    spring_temp_celsius = random.randrange(4, 20)
    summer_temp_celsius = random.randrange(15, 35)
    autumn_temp_celsius = random.randrange(5, 19)
    wind_direction_choice = random.choice(__wind_directions)
    clouds_choice = random.choice(__clouds)
    wind_speed = random.randrange(0, 150)
    day, month, year = get_date(customer_name)
    season = get_season(month)
    if clouds_choice == "sunny":
        if season != 'winter':
            rain_possibility = "no rain"
        else:
            rain_possibility = "no snow"
    elif clouds_choice == "partially cloudy":
        if season != 'winter':
            rain_possibility = "possible rain"
        else:
            rain_possibility = "possible snow"
    else:
        if season != 'winter':
            rain_possibility = "rain"
        else:
            rain_possibility = "snow"
    in_the_past = year <= current_date.year and month <= current_date.month and day < current_date.day
    if in_the_past:
        print(f"Great Scott, it looks like we're traveling in time! Let's try again Marty...uhm...{customer_name}!  ")
        continue
    # elif year == current_date.year and month == current_date.month and day == current_date.day:
    elif (year, month, day) == (current_date.year, current_date.month, current_date.day):
        print(f"{customer_name}, just look out of the window. ")
    else:
        if season == "spring":
            weather_prediction(f"{day}-{month}-{year}", spring_temp_celsius,
                               wind_speed, wind_direction_choice, clouds_choice, rain_possibility)
        elif season == "summer":
            weather_prediction(f"{day}-{month}-{year}", summer_temp_celsius,
                               wind_speed, wind_direction_choice, clouds_choice, rain_possibility)
        elif season == "autumn":
            weather_prediction(f"{day}-{month}-{year}", autumn_temp_celsius,
                               wind_speed, wind_direction_choice, clouds_choice, rain_possibility)
        else:
            weather_prediction(f"{day}-{month}-{year}", winter_temp_celsius,
                               wind_speed, wind_direction_choice, clouds_choice, rain_possibility)
        exit_question(customer_name)
