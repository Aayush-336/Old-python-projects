a=int(input("Input a number you want to find factors of:"))
c=a
print(f"factors of {a} are :1x",end="")
for i in range(2,a):
    while a%i==0:
        a=a/i
        if(a==1):
            print(f"{i}")
        else:
            print(f"{i}x",end="")

