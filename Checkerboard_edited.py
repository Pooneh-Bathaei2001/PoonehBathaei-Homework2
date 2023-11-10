
n = int(input("Enter the length of your board:"))
m = int(input("Enter the width of your board:"))

for i in range(n):
        for k in range(m):
            if (i+k) %2==0:
                print("#", end = "")
            else:
                print("*", end = "")
        print()
