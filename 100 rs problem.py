def chk(a):
    global rem
    if(rem>=a):
        dic[a]=1
        rem-=a
dic={32:0,37:0,16:0,8:0,4:0,2:0,1:0}
rem=int(input("Enter your purchase amount:"))
rem=100-rem
print(f"Remaining amount to be returned:{rem}")
# if(rem>=37):
#     dic[37]=1
#     rem-=37
# if(rem>=32):
#     dic[32]=1
#     rem-=32
# if(rem>=16):
#     dic[16]=1
#     rem-=16
# if(rem>=8):
#     dic[8]=1
#     rem-=8
# if(rem>=4):
#     dic[4]=1
#     rem-=4
# if(rem>=2):
#     dic[2]=1
#     rem-=2
# if(rem>=1):
#     dic[1]=1
#     rem-=1
chk(37)
chk(32)
chk(16)
chk(8)
chk(4)
chk(2)
chk(1)
print("I'll give back ",end="")
for k in dic:
    if dic[k]==1:
        print(f"{k}:{dic[k]} ",end="")