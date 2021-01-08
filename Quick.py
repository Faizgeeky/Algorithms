A = [15 , 5, 69, 5 ,58 ]



def Partition(a,l,h):
    key = a[l]
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
        Qucik(a,j+1,h)

Quick(A,0,len(A)-1)
print("Here")
    
