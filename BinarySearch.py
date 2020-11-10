# ADA PGM2 For Binary Search

arr = [2, 15, 15, 25, 42, 54, 75, 85]

#method
def search(arr1,target):
    left = 0
    right = int(len(arr1)) - 1
    while (left <= right):
        mid = int((left + right) /2)
        if arr1[mid] == target:
            return mid
        elif arr1[mid] > target:
            right = mid -1
        elif arr1[mid] < target:
            left = mid + 1
    return -1
    #if Element is Not present
print(search(arr,42))
# search(sorted_arr,42,len(sorted_arr))
