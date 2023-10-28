import random
pc_number = random.randint(0,10)
n=0
while True:
    user_number = int(input("enter a num:"))
    n+=1
    if user_number == pc_number: 
        print("Yesss!")
        break
    if user_number < pc_number:
        print("Adad bozorgtar please")
    if user_number > pc_number:
        print("Adad koochektar please")
print(pc_number)
print(n)