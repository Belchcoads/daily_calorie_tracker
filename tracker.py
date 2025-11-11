"""
Project: Daily Calorie Tracker - Advanced CLI Tool

Author: Deepanshu Gulia
Date: 27 October 2025

Description:
    A Python program to log meals, calculate total and average calorie intake,
    give health warnings, and help users track daily eating habits.
"""

# ========================================================= #
#                      TASK 1: INTRODUCTION
# ========================================================= #

print("=" * 40)
print("         DAILY CALORIE TRACKER")
print("=" * 40)
print("Track your meals and maintain a healthy lifestyle\n")


# ========================================================= #
#               TASK 2: INPUT AND DATA COLLECTION
# ========================================================= #

meals = []
calories_list = []

response = input("Would you like to log today's meals? (yes/no): ").strip().lower()

if response == "yes":
    try:
        count = int(input("How many meals or snacks did you have today? "))

        for num in range(1, count + 1):
            print(f"\nMeal {num}")
            meal_name = input("Enter meal name: ").strip()
            calorie = float(input("Enter calories for this meal: "))

            meals.append(meal_name.title())
            calories_list.append(calorie)

        print("\nMeals successfully recorded")

    except ValueError:
        print("\nInvalid entry. Please restart and enter numbers correctly.")
        exit()

else:
    print("\nNo meals entered. Calorie tracking might be incomplete today.")
    exit()


# ========================================================= #
#           TASK 3 AND 4: CALCULATIONS AND WARNING SYSTEM
# ========================================================= #

total = sum(calories_list)
avg = total / len(calories_list)

daily_goal = float(input("\nEnter your daily calorie limit: "))

print("\nCALORIE SUMMARY")
print("-" * 40)
print(f"Total Calories Consumed : {total:.2f} cal")
print(f"Average Calories Per Meal : {avg:.2f} cal")

if total < daily_goal:
    print("You are within your daily calorie limit")
elif total == daily_goal:
    print("You are exactly at the calorie limit")
else:
    print("You exceeded your daily calorie limit")


# ========================================================= #
#                 TASK 5: FORMATTED REPORT
# ========================================================= #

print("\nToday's Meal Report")
for m, c in zip(meals, calories_list):
    print(f"{m:<20} - {c:.2f} cal")

print("-" * 40)
print(f"Total Intake : {total:.2f} cal")
print(f"Average Intake Per Meal : {avg:.2f} cal")
print("-" * 40)

# OR #
# SIMPLER VERSION #

"""


#--------------------------------------------#

             # TASK 1 #

#--------------------------------------------#

print("=============================")
print("*****************************")
print("Welcome to Calorie Tracker")
print("*****************************")
print("=============================\n")

# functions of this code #

print("Tracks your daily calorie intakr")
print("You can know your total and avarage calorie intake")
print("We can use this code to meet our daily calorie intake goal\n")

#--------------------------------------------#

              # TASK 2 #
     # INPUT AND DATA COLLECTING #
 
#--------------------------------------------#


meal_names = []
calorie_values = []

conf = input("Would you like to add meals? (yes/no): ").lower()

if conf == "yes":
    meal_count = int(input("How many meals do you want to enter today? "))

    for i in range(meal_count):
        print("\nMeal", i + 1)
        meal = input("Enter meal name: ")
        calories = float(input("Enter calories for this meal: "))

        meal_names.append(meal)
        calorie_values.append(calories)

    print("\nYour meals and calories are saved")

else:
    print("\nOkay! Remember to add your meals later.")



#--------------------------------------------#

              # TASK 3 & 4 #
    # callorie calculation and warning #
 
#--------------------------------------------#


total_calories = sum(calorie_values)
average_calories = total_calories / len(calorie_values)

daily_limit = float(input("\nEnter your daily calorie limit: "))

print("\n----- Calorie Summary -----")
print("Total calories:", total_calories)
print("Average per meal:", average_calories)

if total_calories <= daily_limit:
    print("You are within your total calorie limit")
else:
    print("You have exceeded your daily calorie limit")

#--------------------------------------------#

              # TASK 5 #
     # PRINTING A FORMATTED OUTPUT #
 
#--------------------------------------------#

print("\nCalorie Report")
print("-----------------------------")

for i in range(len(meal_names)):
    print(meal_names[i], "=", calorie_values[i], "calories")

print("-----------------------------")
print("Total calories:", total_calories)
print("Average calories:", average_calories)

"""



