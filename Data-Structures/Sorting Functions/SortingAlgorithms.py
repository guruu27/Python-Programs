# def bubblesort(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j+1],arr[j] = arr[j],arr[j+1]
#     return arr

# c = [1,25,6,4,3,4]
# print(bubblesort(c))



# def selectedsort(arr):
#   for i in range(len(arr)):
#     min_idx = i
#     for j in range(i+1,len(arr)):
#       if arr[min_idx]>arr[j]:
#         min_idx = j

#     arr[i],arr[min_idx] = arr[min_idx],arr[i]
#   return arr

# c = [1,25,6,4,3,4]
# print(selectedsort(c))


def insertionsort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    print(arr)

c = [1,25,6,4,3,4]
print(insertionsort(c))

