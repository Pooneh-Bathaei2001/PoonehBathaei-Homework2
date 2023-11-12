n = int(input("please write a number for row:"))
m = int(input("please write a number for col:"))

print("\t\t\tmultiplication table\n")

for i in range(1,n+1):
    print(i, end = "\t")
print()
print("--------------------------------------------------------------\n")

for i in range(1,n+1):
    for j in range(1,m+1):
        print(i*j, end = "\t")
    print("\n")    