arr=[5,10,15,20,25]
total=0
count=len(arr)
for num in arr:
    total+=num
average=total/count
print("Array:",arr)
print("Sum of elements:",total)
print("Average of elements:",average)