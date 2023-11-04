import random

list = []
length = int(input("How many numbers do you want in your list?"))
for i in range (length):
    num = random.randint(0,100)
    if num not in list:
        list.append(num)

print(list)


