A = [9,8,2,1,45,100 , 0]



def Partition(a,l,h):
    key = a[h]
    i=l
    j=h
    while i<j:
        while a[i] < key:
            i+=1
        while a[j] > key:
            j-=1
        if i<j:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    
        if i>j:
            temp = a[j]
            a[j] = key
            a[l] = temp
    return j

def Quick(a,l,h):
    if l < h:
        j = Partition(a,l,h)
        Quick(a,l,j-1)
        Quick(a,j+1,h)
    return a

ar = Quick(A,0,len(A)-1)
print(ar)
# print("Here")
    
