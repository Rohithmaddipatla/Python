a=int (input("enter marks out of 300"))
b=a/300*100
print("percentageis ",b,"%")
if(a>300):
    print("you entered a worong number")
elif(b>60):
    print("your division is first")
elif(b>50 and b<60):
    print("your division is second")
elif(b>30 and b<50):
    print("your division is third")
else:
    print("fail")