# logic for leap years is year/4=%0 and year/100=%0 and year/400=%0

year =int(input("Type the year you want to check \n"))

if year %4 == 0 and year %100 != 0 or year % 400 == 0:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")