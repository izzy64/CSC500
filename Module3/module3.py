# Part 1
print("Input the cost of your food: ")
cost = round(float(input()), 2) # Get user-input meal cost (round to nearest cent)
tip_rate = .18
recommended_tip = round(cost*tip_rate, 2) # calculate tip (multiply meal cost by tip rate)
sales_tax_rate = .07
sales_tax = round(cost*sales_tax_rate, 2) # calculate tax (multiply meal cost by tax rate)
total = round(cost+sales_tax+recommended_tip, 2) #calculate total (sum cost, tip, and tax)
print(f"After a meal costing ${cost}, sales tax ({int(sales_tax_rate*100)}%) will be ${sales_tax} and an {int(tip_rate*100)}% tip is ${recommended_tip}, for a total cost of ${total}") # print total

# Part 2
hour = -1
while hour < 0 or hour >= 24:
    print("Input the current hour of the day: ")
    hour = int(input()) # Get user-input hour 
    if hour < 0 or hour >= 24: # validate hour (between 0 and 23)
        print(f"{hour} is an invalid input, try again")
wait = -1
while wait < 0:
    print("Input how many hours before the alarm should sound: ")
    wait = int(input())   # Get user-input hours to wait
    if wait < 0: # validate hours to wait (positive number)
        print(f"{wait} is an invalid input, try again")

hours_from_day_start = hour + wait # sum hour and hours to wait

alarm_time = hours_from_day_start % 24 # calculate alarm time (modular division)

days_distant = hours_from_day_start // 24 # calculate days distant (integer divison)

if days_distant == 0:
    days_distant_text = "today"
elif days_distant == 1:
    days_distant_text = "tomorrow"
else:
    days_distant_text = f"{days_distant} days from today"

# print alarm time and days distant
print(f"If it's currently hour {hour}, setting an alarm for {wait} hours from now means the alarm will sound at hour {alarm_time}, {days_distant_text}") 

