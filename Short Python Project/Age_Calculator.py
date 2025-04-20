
import datetime


print("If You Enter your DOB Year Enter 1")
print("If You Enter your Age Enter 2")
print("If You Know Your Current Age Only  Enter 3")
print()
choosen=input("What You Choose Enter First 1 Or 2 Or 3 :")
if(choosen=='1'):
    year = int(input('Enter Your DOB Year:'))
    if(year>=1900 and year<=1920):
        print(f"You Are The Most Oldest Person And Your Current Age IS :{2023-year}")
    elif(year>2023):
        print("You Are Not Born Yet !!!")
    else:
        print("You Enter Any Wrong Condition")
elif(choosen=='2'):
    Age = int(input('Enter Your Age:'))
    if(Age>=100 and Age<=120):
        print(f"You Are The Most Oldest Person")
    elif(Age<=0):
        print("You Are Not Born Yet !!!")
    elif(Age<100):
        print(f"Your Age Will Be 100 After {100-Age} Years Latter")
    elif(Age>120):
        print(f"A Normal Men Not Alive In This Old Your Current Age Is You Think About That !!!")
    else:
        print("You Enter Any Wrong Condition")
elif(choosen=='3'):
 current_date = datetime.date.today()    # Find Current Date
 year_of_birth = int(input("Enter the year of your birth (YYYY): "))
 month_of_birth = int(input("Enter the month of your birth (MM): "))
 day_of_birth = int(input("Enter the day of your birth (DD): "))

 #  Current Date create object
 birthdate = datetime.date(year_of_birth, month_of_birth, day_of_birth)

# Calculate age
 age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))

# Display the result
 print(f"You are {age} years old.")
else:
    print("You Wrong Condition Enter Please Check And Try Again ....")
    exit()
