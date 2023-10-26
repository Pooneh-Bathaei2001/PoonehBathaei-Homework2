import random
while True:
    op = input("roll the dice or exit:")
    if op == "exit":
          break
    if op == "roll the dice":
        Dice = random.randint(1,6)   
        if Dice == 6:
             Dice = random.randint(1,6)
             print("Shans mojadad - In dafe", Dice, "avordi")
             
        else:
            print(Dice,"Avordi, Nafar Baad")
            break