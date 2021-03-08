

def LeapYear(x):
    if x%4 == 0:
        if x%100 == 0:
            return "Not a leap year"
        else:
            return "Is a leap year"
    else:
        return "Not a leap year"