arr=[1,5,10,23,99,36]
max=arr[0]
min=arr[0]
for num in arr:
    if num>max:
        max=num
    if num<min:
        min=num
print("Array:",arr)
print("Maximun number:",max)
print("Minimum number:",min)