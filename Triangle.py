a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))

if a < b + c: 
    if b < a + c:
        if c < a + b:
            print("These numbers can create a triangle")
else: 
    print("These numbers cannot create a triangle")
