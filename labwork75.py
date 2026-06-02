start_year = 2000
end_year = 2025
leap_years = []

for year in range(start_year, end_year + 1):
    # Leap year logic
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_years.append(year)

print("Leap years array:", leap_years)
'''
Output:
Leap years array: [2000, 2004, 2008, 2012, 2016, 2020, 2024]
'''