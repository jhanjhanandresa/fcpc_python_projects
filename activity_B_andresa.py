print("Number 1") #number 1
for x in range(8):
    print(2**x, end = '\t')
print()
print()


print("Number 2") #number 2
for x in range(1,13):
    if x % 4 == 0:
        print("S", end = '\t')
    else:
        print(x, end = '\t')
print()
print()


print("Number 3") #number 3
for x in range(1, 9):
    if x % 8 == 1:
        print(x, end = '\t')
    else:
        print("E", end = '\t')

