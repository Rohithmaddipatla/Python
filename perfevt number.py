n=6
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print(n,"it is a perfect number ")
else:
    print(n,"it is not a perfect number ")