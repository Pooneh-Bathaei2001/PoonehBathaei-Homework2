import math

op= input("enter op(+, -, *, /, sin, cos, tan, cot, factorial, sqrt):")

if op == "+":
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    r = a + b 

if op == "-":
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    r = a - b

if op == "*":
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    r = a * b 

if op == "/": 
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    if b == 0:
        r = "Error"
    else:
        r = a / b

if op == "sin": 
    a = float(input("Enter a:"))
    r = math.sin(math.radians(a))

if op == "cos":
    a = float(input("Enter a:"))
    r = math.cos(math.radians(a))

if op == "tan":
    a = int(input("Enter a:"))
    if math.cos(math.radians(a)) == 0:
        print("Error")
    else: 
        r = math.tan(a)

if op == "cot":
    a = int(input("Enter a:"))
    if math.sin(math.radians(a)) == 0:
        print("Error")
    else: 
        r = 1/math.tan(math.radians(a))

if op == "factorial":
    a = int(input("Enter a:"))
    r = math.factorial(a)

if op == "sqrt":
    a = float(input("Enter a:"))
    r = math.sqrt(a)

print(r)
