
arr = [25,42,15,54,2,75,85]


def Insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
         
        while j >= 0 and key < arr[j] : 
            arr[j + 1] = arr[j] 
            j -= 1
            arr[j + 1] = key 
      
    return arr

       
       
       
       
        
                

if __name__ == "__main__":
    a = Insertion_sort(arr)
    print(a)