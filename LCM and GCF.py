a = int(input("Enter Number 1:"))
b = int(input("Enter Number 2:"))
c = a
d = b
gcf = 1
for i in range(2, a):
    while a % i == 0 and b % i == 0:
        gcf = gcf * i
        a = a / i
        b = b / i
lcm = int(gcf * a * b)
print(f"GCF of {c} and {d} are {gcf}")
print(f"LCM of {c} and {d} are {lcm}")
