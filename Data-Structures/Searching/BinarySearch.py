def BinarySearch(arr,target):
    arr.sort()
    l,r=0,len(arr) - 1
    
    while l<=r:
        m = l + (r-l)//2

        if target ==  arr[m]:
            return f"Found at {m}"
        elif target>arr[m]:
            l = m+1
        else:
            r = m-1
    
    return "Not found"

arr = [1,2,3,4,6,7,8,9,0]
print(BinarySearch(arr,0))