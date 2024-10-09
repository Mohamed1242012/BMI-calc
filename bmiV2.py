#!/usr/bin/env python3

import math
def main () :
    print("""BMI Calculator by
      
 /$$      /$$           /$$                                               /$$       /$$$$$$$$ /$$                                               /$$
| $$$    /$$$          | $$                                              | $$      | $$_____/| $$                                              | $$
| $$$$  /$$$$  /$$$$$$ | $$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$$      | $$      | $$  /$$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$$
| $$ $$/$$ $$ /$$__  $$| $$__  $$ |____  $$| $$_  $$_  $$ /$$__  $$ /$$__  $$      | $$$$$   | $$ /$$_____/ |____  $$| $$  | $$ /$$__  $$ /$$__  $$
| $$  $$$| $$| $$  \ $$| $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$| $$  | $$      | $$__/   | $$|  $$$$$$   /$$$$$$$| $$  | $$| $$$$$$$$| $$  | $$
| $$\  $ | $$| $$  | $$| $$  | $$ /$$__  $$| $$ | $$ | $$| $$_____/| $$  | $$      | $$      | $$ \____  $$ /$$__  $$| $$  | $$| $$_____/| $$  | $$
| $$ \/  | $$|  $$$$$$/| $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$|  $$$$$$$      | $$$$$$$$| $$ /$$$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$
|__/     |__/ \______/ |__/  |__/ \_______/|__/ |__/ |__/ \_______/ \_______/      |________/|__/|_______/  \_______/ \____  $$ \_______/ \_______/
                                                                                                                      /$$  | $$                    
                                                                                                                     |  $$$$$$/                    
                                                                                                                      \______/                   
My program is based on this BMI Datasheet: https://mohamed1242012.github.io/bmi_datasheet
This is an Open Source Project on:

    """)
    try :
        units = int(input("""Which units do you prefer (1 or 2) :
1. Kilograms and Centimeters
2. Pounds and Inches (Feet + remaining inches)
Choose: """))
        if units == 1:
            weight = float(input("Enter your weight (in Kilograms): "))
            height = float(input("Enter your height (in Centimeters): "))/100 #convert to meters
        elif units == 2:
            weight = float(input("Enter your weight (in Pounds): "))*0.45359237 #convert to kilograms
            height = (float(input("Enter your height (in Feet): "))*12 + float(input("Enter the remaining Inches: ")))*0.0254 #convert to meters

        if weight <= 0 or height <= 0 :
            raise ValueError("Height or Weight cant be 0 or a negative number.")

        #Calculate BMI and the level and store them
        bmi , level = calculate_bmi(weight, height)

        #Show result
        print(f'\nResults:\nYour BMI is: {bmi:.2f}\nWhich is {level}')
    except ValueError as e :
        print (f"Invalid Input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def calculate_bmi (weight,height) :
    bmi = weight / (height ** 2)
    if bmi < 18.5 :
        level = 'Underweight'
    elif bmi >= 18.5 and bmi <= 24.9 :
        level = 'Normal weight'
    elif bmi >= 25 and bmi <= 29.9 :
        level = 'Overweight'
    elif bmi >= 30 :
        level = 'Obesity'

    return bmi , level


if __name__ == "__main__":
    main()