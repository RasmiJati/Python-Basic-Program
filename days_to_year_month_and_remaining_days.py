# program to convert entered number of days into years, months and remaining days

def days_converter():
    days = input("Enter number of days : ")
    year = int(days) / 365   # 365 because 365 days in a year
    month = int(days) / 30   # 30 because 30 days in a year
    day = int(days) % 30    # 30 because x remaining days in 30 days
    # int() is used as input() takes only string so, we convert from string value to int

    print(f'Year = {year.__round__(0)}  month = {month.__round__(0)} and remaining days = {day.__round__(0)}')


days_converter()
