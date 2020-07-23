for x in range (0,100):
#x=int(input("Enter Number to check if it is perfect or not:"))

    z=x
    sum=1
    for i in range (2,x):
        if(x%i==0):
            sum=sum+i;i=i+1;
    if (sum==z):
        print("Given number",sum," is perfect Number")
