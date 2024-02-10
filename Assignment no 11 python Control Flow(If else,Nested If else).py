# Logical Problem:
# problem no 1:
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

num = float(input("Enter a number: "))

result = check_number(num)
print("The number is", result)
# problem no 2:
def check_age(age):
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior citizen"

age = int(input("Enter your age: "))

result = check_age(age)
print("You are a", result)
# problem no 3:
def find_larger(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

larger_number = find_larger(num1, num2)
print("The larger number is:", larger_number)
# problem no 4:
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
# problem no 5:
def find_max_min(num1, num2, num3):
    maximum = max(num1, num2, num3)
    minimum = min(num1, num2, num3)
    return maximum, minimum

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

max_number, min_number = find_max_min(num1, num2, num3)
print("Maximum number:", max_number)
print("Minimum number:", min_number)
# problem no 6:
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

exam_score = float(input("Enter your exam score: "))

grade = calculate_grade(exam_score)
print("Your grade is:", grade)
# Simple Practical Problem:
# problem no 1:
def calculate_total_cost(unit_price, quantity):
    total_cost = unit_price * quantity
    if total_cost > 1000:
        total_cost *= 0.9  
    return total_cost

unit_price = float(input("Enter the unit price of the item: "))
quantity = int(input("Enter the quantity purchased: "))

total_cost = calculate_total_cost(unit_price, quantity)
print("Total cost of items purchased:", total_cost)
# problem no 2
def should_wear_jacket(temperature):
    if temperature < 20:
        return True
    else:
        return False

temperature_celsius = float(input("Enter the current temperature in Celsius: "))

if should_wear_jacket(temperature_celsius):
    print("You should wear a jacket.")
else:
    print("You don't need to wear a jacket.")
# problem no 3:
def triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    else:
        return "Scalene"

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

triangle = triangle_type(side1, side2, side3)
print("The triangle is", triangle)
# problem no 4
class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def verify_pin(self, entered_pin):
        return entered_pin == self.pin

    def withdraw_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful. Remaining balance:", self.balance)
        else:
            print("Insufficient funds. Withdrawal failed.")

pin = input("Enter your PIN: ")
initial_balance = float(input("Enter your initial balance: "))
atm = ATM(pin, initial_balance)

entered_pin = input("Enter your PIN again for verification: ")
if atm.verify_pin(entered_pin):
    amount_to_withdraw = float(input("Enter the amount to withdraw: "))
    atm.withdraw_money(amount_to_withdraw)
else:
    print("Invalid PIN. Access denied.")
# problem no 5
def days_in_month(month):
    days_in_months = {
        1: 31,  # January
        2: 28,  # February (assuming non-leap year for simplicity)
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31, # October
        11: 30, # November
        12: 31  # December
    }
    
    if month < 1 or month > 12:
        return "Invalid month"
    
    return days_in_months[month]

month = int(input("Enter the month (as a number): "))

print("Number of days in the month:", days_in_month(month))
# problem no 6
import calendar

def days_in_month(year, month):
    days = calendar.monthrange(year, month)[1]
    return days

year = int(input("Enter the year: "))
month = int(input("Enter the month (as a number): "))

num_days = days_in_month(year, month)
print("Number of days in the month:", num_days)
# Healthy Life Style:
# 1. Calorie Counter:
def calculate_calorie_goal(age, weight, activity_level):
    bmr = 10 * weight + 6.25 * 160.934 - 5 * age
    
    if activity_level == "sedentary":
        bmr *= 1.2
    elif activity_level == "lightly active":
        bmr *= 1.375
    elif activity_level == "moderately active":
        bmr *= 1.55
    elif activity_level == "very active":
        bmr *= 1.725
    elif activity_level == "extra active":
        bmr *= 1.9
    
    return bmr

age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kilograms: "))
activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, very active, extra active): ")

calorie_goal = calculate_calorie_goal(age, weight, activity_level)
print("Your daily calorie goal is approximately:", calorie_goal, "calories.")
# 2. Sleep Tracker:
def calculate_sleep_duration(bedtime, wakeup_time):
    sleep_duration = (wakeup_time - bedtime) % 24
    return sleep_duration

def get_sleep_feedback(sleep_duration):
    if sleep_duration >= 7 and sleep_duration <= 9:
        return "You've met the recommended amount of sleep. Well done!"
    elif sleep_duration < 7:
        return "You didn't get enough sleep. Try to get more rest."
    else:
        return "You've overslept. Try to maintain a consistent sleep schedule."

bedtime = float(input("Enter your bedtime (in hours, 24-hour format): "))
wakeup_time = float(input("Enter your wake-up time (in hours, 24-hour format): "))

sleep_duration = calculate_sleep_duration(bedtime, wakeup_time)

feedback = get_sleep_feedback(sleep_duration)
print("Your total sleep duration is:", sleep_duration, "hours.")
print(feedback)
# 3. Hydration Helper:
def suggest_water_intake(weight, activity_level):
    LIGHT_INTAKE = 0.03
    MODERATE_INTAKE = 0.035
    INTENSE_INTAKE = 0.04

    if activity_level == "light":
        water_intake = weight * LIGHT_INTAKE
    elif activity_level == "moderate":
        water_intake = weight * MODERATE_INTAKE
    elif activity_level == "intense":
        water_intake = weight * INTENSE_INTAKE
    else:
        return "Invalid activity level. Please choose light, moderate, or intense."

    return water_intake

weight = float(input("Enter your weight in kilograms: "))
activity_level = input("Enter your desired level of hydration (light, moderate, intense exercise): ")

recommended_intake = suggest_water_intake(weight, activity_level)
if isinstance(recommended_intake, str):
    print(recommended_intake)
else:
    print("Recommended water intake throughout the day:", recommended_intake, "liters.")
# Time Management:
# 1. To Do List:
def categorize_task(due_date, priority):
    if due_date < 3:
        return "Urgent"
    elif due_date < 7:
        return "Important"
    else:
        return "Less important"

to_do_list = []

def add_task(task, due_date, priority):
    category = categorize_task(due_date, priority)
    to_do_list.append((task, due_date, priority, category))

while True:
    task = input("Enter the task: ")
    due_date = int(input("Enter the due date (in days): "))
    priority = int(input("Enter the priority (1 for high, 2 for medium, 3 for low): "))
    add_task(task, due_date, priority)
    
    more_tasks = input("Do you want to add more tasks? (yes/no): ")
    if more_tasks.lower() != "yes":
        break

print("\nCategorized To-Do List:")
print("=======================")
print("Task\t\tDue Date\tPriority\tCategory")
for task_info in to_do_list:
    print(f"{task_info[0]}\t\t{task_info[1]} days\t{task_info[2]}\t\t{task_info[3]}")
# 2. Pomodoro Timer:
import time

def pomodoro_timer(total_cycles):
    for cycle in range(1, total_cycles + 1):
        print(f"Cycle {cycle} - Work for 25 minutes")
        time.sleep(25 * 60)  

        print("Take a 5-minute break")
        time.sleep(5 * 60)  

total_cycles = int(input("Enter the number of Pomodoro cycles: "))

pomodoro_timer(total_cycles)
print("Pomodoro session finished!") 
# 3. Meeting Sschedular:
def find_common_meeting_time(users_calendars, meeting_duration):
    common_time_slots = []
    for time_slot in range(24 * 60):  # 24 hours * 60 minutes
        is_available = True
        for calendar in users_calendars:
            if time_slot not in calendar:
                is_available = False
                break
        if is_available:
            common_time_slots.append(time_slot)
    
    suitable_times = []
    for time_slot in common_time_slots:
        start_time = time_slot
        end_time = time_slot + meeting_duration
        if end_time <= 24 * 60:  
            suitable_times.append((start_time, end_time))
    
    return suitable_times
user1_calendar = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660]  # User 1's calendar in minutes
user2_calendar = [90, 150, 210, 270, 330, 390, 450, 510, 570, 630, 690]  # User 2's calendar in minutes
user3_calendar = [100, 160, 220, 280, 340, 400, 460, 520, 580, 640, 700]  # User 3's calendar in minutes

users_calendars = [user1_calendar, user2_calendar, user3_calendar]

meeting_duration = 60  

common_meeting_times = find_common_meeting_time(users_calendars, meeting_duration)

print("Suitable meeting times:")
for start_time, end_time in common_meeting_times:
    print(f"{start_time // 60:02d}:{start_time % 60:02d} - {end_time // 60:02d}:{end_time % 60:02d}")