arr=[14,16,87,36,25,89,34]
m=1
n=3
arr.sort()
#get m-th maximum (from the end)
max_num=arr[-m]
#get n-th minimum (from the start)
min_num=arr[n-1]
#total
total =max_num+min_num
#diff
diff=max_num-min_num

print(f"mth maximum number ={max_num}")
print(f"nth minimum number ={min_num}")
print(f"sum={total}")
print(f"difference={diff}")

