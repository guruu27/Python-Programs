# import math

# # def bubblesort(arr):
# #     for i in range(len(arr)-1):
# #         for j in range(len(arr)-i-1):
# #             if arr[j]>arr[j+1]:
# #                 arr[j+1],arr[j] = arr[j],arr[j+1]
# #     return arr

# # c = [1,25,6,4,3,4]
# # print(bubblesort(c))



# # def selectedsort(arr):
# #   for i in range(len(arr)):
# #     min_idx = i
# #     for j in range(i+1,len(arr)):
# #       if arr[min_idx]>arr[j]:
# #         min_idx = j

# #     arr[i],arr[min_idx] = arr[min_idx],arr[i]
# #   return arr

# # c = [1,25,6,4,3,4]
# # print(selectedsort(c))


# def insertionsort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j>=0 and key < arr[j]:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
#     return arr

# # c = [1,25,6,4,3,4]
# # print(insertionsort(c))

# def bucketsort(arr):
#     numofbuckets = round(math.sqrt(len(arr)))
#     maxval = max(arr)
#     arr_ = []
#     for i in range(numofbuckets):
#         arr_.append([])
#     for j in arr:
#         index_bucket = math.ceil(j*numofbuckets/maxval)
#         arr_[index_bucket-1].append(j)
#     for i in range(numofbuckets):
#         arr_[i] = insertionsort(arr_[i])
    
#     k=0
#     for i in range(numofbuckets):
#         for j in range(len(arr_[i])):
#             arr[k]=arr_[i][j]
#             k+=1
    
#     return arr

# c = [1,25,6,4,3,4]
# print(bucketsort(c))

def merge(arr,l,m,r):
    n1 = m - l + 1
    n2 = r - m 
    L = [0]*n1
    R = [0]*n2

    for i in range(0,n1):
        L[i] = arr[l+i]

    for j in range(0,n2):
        R[j] = arr[m+1+j]

    i,j,k=0,0,l
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1    

def mergeSort(arr,l,r):
    if l<r:
        m =(l+(r-l)//2)
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)
    return arr

c = [1,25,6,4,3,4]
print(mergeSort(c,0,len(c)-1))
