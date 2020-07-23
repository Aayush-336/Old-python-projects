a = input("Enter Data seperated by comma(,):")
b = a.split(',')
su = 0
sut = 0

for i in b:
    su += int(i)
    print(int(i), "  ", int(i) ** 2)
    sut += int(i) ** 2
print(f"Sum ={su} , {sut}")
md = su / len(b)

print("\nMean = ", md)
vr = sut / len(b) - md ** 2
print("Variance = ", vr)
sd=vr**(1/2)
print("Standard Deviation = ",sd)
