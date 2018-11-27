
for x in range(1, 11):
    for y in range(1, 11):
       z = x * y

       if z % 2 ==0:
           print ("E", end = '\t')
       else:
           print(x*y, end = '\t')
    print()

 #EVEN NUMBER
for x in range(1, 11):
    for y in range(1, 11):
       z = x * y

       if z % 2 ==0:
           print ("o", end = '\t')
       else:
           print(x*y, end = '\t')
    print()
