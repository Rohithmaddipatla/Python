arr=[10,25,7,99,56,3,42]
key=99
found=False
for i in range(len(arr)):
  if arr[i]==key:
    print(f"Element {key} found at index{i}")
    found=True
    break
if not found:
    print(f"Element {key} not found in the array")