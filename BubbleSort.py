# ADA PGM For Bubble Sort

arr = [25,42,15,54,92,75,85]


def BubbleSort(arr):
    for i in range(0,len(arr)-1,1):
        for j in range(0,len(arr)-1,1): 
            # loop it till i
            if arr[j] > arr[j+1]:
                #Swapping
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr



if __name__ == "__main__":
    a = BubbleSort(arr)
    print(a)

