# ADA PGM For Selection Sort
arr = [25,42,15,54,2,75,85]


def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i #Take i'th pos 

        for j in range(i,len(arr)-1):   
            if arr[j] < arr[min]:
                min = j # Replace Var min with minumum value
             

        temp = arr[i] # store temp with current val
        arr[i] = arr[min] # replace current index wit minimum value
        arr[min] = temp # give temp value to min index 
    return arr



if __name__ == "__main__":
    a= selection_sort(arr)
    print(a)

