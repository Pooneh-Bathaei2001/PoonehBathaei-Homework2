name = input("Please enter your first name:")
family = input("Please enter your last name:")

a = int(input("Enter your first grade:"))
b = int(input("Enter your second grade:"))
c = int(input("Enter your third grade:"))
average = ((a + b + c) /3)

if average >= 17:
    print("Dear", name, family, "your result is Great")
if 17 > average >= 12 :
    print("Dear", name, family, "your result is Normal")
if average < 12:
    print("Dear", name, family, "your result is Fail")

