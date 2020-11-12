
arr = [25,42,15,54,2,75,85,15]


def Insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
    return arr

       
       
       
       
        # for j in range(i-1,0, -1):
        #     print("J",j)
        #     if arr[j] < cur:
        #         arr[j+1] =arr[j]
        #     else:
        #         arr[j+1] = cur
        #         break
                

if __name__ == "__main__":
    a = Insertion_sort(arr)
    print(a)