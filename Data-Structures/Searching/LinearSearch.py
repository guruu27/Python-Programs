def LinearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return f"Found at {i}"
    return "Not found"
arr = [1,2,3,4]
print(LinearSearch(arr,3))