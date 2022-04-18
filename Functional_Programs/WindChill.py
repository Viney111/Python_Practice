"""
        @Author: Viney Khaneja
        @Date: 2022-04-12 03:15PM
        @Last Modified by: Viney Khaneja
        @Last Modified time: None
        @Title : Windchill Calculation & Printing it on Console
        """

import math


def wind_chill():
    """
    Description: This function is used to find the wind chill.
                Temperature and wind speed are the two inputs given.
                Calculate the wind chill temperature should not be greater than 50 and wind speed should be in between 3-120.
    Parameter: None
    Return: None
    """
    # User Inputs for temperature and wind-speed
    temperature = float(input("Enter temperature in fahrenheit in between the range 0 to 50 : "))
    wind_speed = float(input("Enter wind speed in between the range 3 to 120 : "))
    # One of this condition gets true, wind chill can not be calculated
    if temperature > 50 or wind_speed < 3 or wind_speed > 120:
        print("Wind chill cannot be found for the entered condition")
    else:
        wind_chill = 35.74 + 0.6215 * temperature +(0.4275*temperature + 35.75)*math.pow(wind_speed,0.16)
        print(f"Wind chill for the given {temperature} and {wind_speed} is: ",wind_chill)


if __name__ == "__main__":
    wind_chill()