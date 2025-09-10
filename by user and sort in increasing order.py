a=eval (input("enter limit"))
n=[]
for a in range (1,a+1):
    a=eval(input("enter element"))
    n.append(a)
print(n)
l=len(n)
for i in range (1):
    for j in range (0,l-i-1):
        if n[j]>n[j+1]:
            temp=n[j]
            n[j]=n[j+1]
            n[j+1]=temp
print("after sorting the list is")
print(n)