arr = [25, 10, 56, 7, 42, 3, 99]
n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Ascending order:", arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Descending order:", arr)