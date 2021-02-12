
import numpy as np 

def DegreeVer(nodes):
    main_arr = np.zeros([nodes,nodes])
    # print(main_arr)
    for i in range(0,nodes):
        for j in range(0,nodes):
            main_arr[i][j] = int(input("Please eneter elemenet - "))
        
    print(main_arr)
    print("\n")
    for i in range(0,nodes):
        ind =0
        out =0
        for j in range(0,nodes):
            if main_arr[i][j] > 0:
                out = out+1
            if main_arr[j][i] >0:
                ind = ind + 1
        print("Node ",i+1," Indegree - ", ind, " Outdegree - ", out)


try:
    total_n = int(input("Please enter total NODES : -"))
    DegreeVer(total_n)
except:
    print("Something went wrong")