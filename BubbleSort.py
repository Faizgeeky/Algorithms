# ADA PGM For Bubble Sort

arr = [25,42,15,54,92,75,85]


def BubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        # loop reverse as we need -1 elemnt each time 
        for j in range(i): 
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

