
A = [9,8,2,1,15249,1542,45,-10,0,999,42,78]

def MaxMin(arr,s,l):
    max = arr[0]
    min = arr[0]
    if(s==l):
        max = min 
    
    elif l==s+1:
        if arr[l] > arr[s]:
            max = arr[l]
            min = arr[s]
        else:
            max = arr[s]
            min = arr[l]
    else:
        mid = int((l+s)/2)
        left = MaxMin(arr,s,mid)
  
        right = MaxMin(arr,mid,l)
     

        if left[0] > right[0]:
            max = left[0]
        else:
            max = right[0]
            
        if left[1] < right[1]:
            min = left[1]
        else:
            min = right[1]
   
    return max,min
            


mm= MaxMin(A,0,len(A)-1)
print(" \n\tMaximum element  --->",mm[0]," \n\tMinimum element  ---> ",mm[1],"\n")