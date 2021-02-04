A = [9,8,2,1,45,100 , 0]
B = [10,6,4,3,98,60]
A.sort()
B.sort()



def Merge(A,B,m,n):
    i=0
    j=0
   
    C = []
    while i< len(A) and j<len(B):
        if(A[i] < B[j]):
            C.append(A[i])
            
            i+=1
            
        elif(A[i] > B[j]):
            C.append(B[j])
            
            j+=1
    while(i<len(A)):
        C.append(A[i])
        i+=1
    while(j<len(B)):
        C.append(B[j])
        j+=1
    print(C)
    
Merge(A,B,len(A),len(B))
