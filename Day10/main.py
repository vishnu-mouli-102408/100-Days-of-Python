# Functions with output

def v(fname,lname):
    x = fname.title();
    y = lname.title();
    return x + y

m = v("mouLi", "gANivAdA")

print(m)

#  Early return
#  returning before executing the condition on some cases

# No of Days in a Month

def isLeap(year):
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
    

months_days = ['31','28','31','30','31','30','31','31','30','31','30','31']
year = int(input("Enter a Year: "))
month = int(input("Enter a Month: "))
def month_day(year,month):
    if isLeap(year) and month == 2:
        return 29
    else:
        return months_days[month-1]

x =month_day(year,month) 
print(x)

# Doc Strings 

#  It allow us to add doc Strings to documentation about what function we are writing

# It uses triple quotatio

