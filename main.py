def is_leap(year):
    """docstring example"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(f_year, f_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(f_year) == True and f_month==2:
        return 29
    else:
        return month_days[f_month-1]



# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
# year = 2024
month = int(input("Enter a month: "))
# month = 2
days = days_in_month(year, month)
print(days)







