#GCD function
def gcd(a,b):
    while b:
        a,b=b,a%b
        return a
#lcm
def lcm(a,b):
    return (a*b)//gcd(a,b)
#test
print(f"the gcd of 60 and 48 is:{gcd(60,48)}")
print(f"lcm of 15 and 20 is {lcm(15,20)}")