import pvlib
import pandas as pd
import datetime

def generate_times():
    start_date = datetime.date(2024, 12, 1)
    end_date = datetime.date(2024, 12, 4)

    delta = end_date - start_date

    times = []
    for i in range(delta.days + 1):
        day = start_date + datetime.timedelta(days=i)
        times.append(pd.Timestamp(day))

    return times

def get_solar_positions():

    times = generate_times()
    locations = [pvlib.location.Location(32.2, -111, 'America/Phoenix'), pvlib.location.Location(34.052235, -118.243683, 'America/Los_Angeles'), pvlib.location.Location(40.712776, -74.005974, 'America/New_York')]

    solar_positions_list = []
    for location in locations:
        solar_positions = location.get_solarposition(times=times)
        print(f"Solar positions for {location.tz}\n {solar_positions}")
        solar_positions_list.append((location, solar_positions))

    return solar_positions_list

def get_solar_irradiance():
    time = pd.Timestamp('2024-01-01')
    location = pvlib.location.Location(32.2, -111, 'America/Phoenix')

    solar_irradiance = location.get_irradiance(time)

    return solar_irradiance

get_solar_positions()