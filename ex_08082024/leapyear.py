# Program for Leap Year

enter_year = int(input("Enter the Year"))
if enter_year % 4 == 0:
    print(enter_year, "is a Leap Year")
else:
    print(enter_year, "is not a leap year")