size = 5
for i in range(size):
    for j in range(1,size - i):
        print("",end="")
    for k in range(1,i+2):
        print(k,end="")
    print()
