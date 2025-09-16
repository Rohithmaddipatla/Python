n=input("Enter the customer name: ")
m=int(input("Enter the mobile number: "))
c=int(input("Enter the cost of purchase: "))

d=c*(40/100)
t=c-d

print()
print("Customer details: ")
print("Customer name: ", n)
print("Mobile number: ", m)
print("Cost of purchase: ", c)
print("Discount: ", d)
print("Total Amount to be paid: ", t)