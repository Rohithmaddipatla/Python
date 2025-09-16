arr=[1,2,2,3,4,3,2,5,1]
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print("Array:",arr)
print("Frequency:")
for key,value in freq.items():
    print(key,":",value)