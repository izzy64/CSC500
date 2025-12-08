# Part 1

# test data:
# 0, 0, 3, 6, 9, 6, 4, 3, 4, 2, 2, 0
# 0, 1, 1, 7, 8, 7, 3, 2, 3, 2, 1, 0

print("How many years worth of data to analyze?")
years_count = int(input())
print(years_count)

month_count = years_count * 12
rain_total = 0

for year in range(1, years_count + 1):
    for month in range(1, 13):
        print(f"How many inches of rainfall were observed in month {month} of year {year}?")
        rainfall = int(input())
        print(rainfall)
        rain_total += rainfall

print(f"Over a period of {years_count} years ({month_count} months), a total of {rain_total} inches of rain were observed for an average of {(rain_total/month_count):.3f} inches of rain per month")


# Part 2

print("How many books did you purchase this month?")
book_count = int(input())
print(book_count)
if book_count < 2:
    monthly_points = 0
elif book_count < 4:
    monthly_points = 5
elif book_count < 6:
    monthly_points = 15
elif book_count < 8:
    monthly_points = 30
else:
    monthly_points = 60
print(f"You earned {monthly_points} points this month")