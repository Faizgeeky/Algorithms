# ADA PGM For Binary Search

arr = [2, 15, 15, 25, 42, 54, 75, 85]

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
    return "NOt EXIST!"
    #if Element is Not present
element = int(input("Please enter element to search :-"))
print(search(arr,element))
# search(sorted_arr,42,len(sorted_arr))
