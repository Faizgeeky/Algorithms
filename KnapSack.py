def knapSack(W, wt, val, n):
    if n==0 or W==0:
       return 0
    elif W < wt[n-1]:
        return knapSack(W, wt,val,n-1)
    else:
        return max(val[n-1] + knapSack(W-wt[n-1],wt,val,n-1), knapSack(W,wt,val,n-1) )


#Main
val = [50,100,250,200]
wt = [8,16,18,40]
W = 65
n = len(val)
print(knapSack(W, wt, val, n))