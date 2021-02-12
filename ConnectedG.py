N = 100000
   
graph1 = {}; graph2 = {};  
  
vis1 = [0] * N; vis2 = [0] * N;  
  
#  add edges  
def Add_edge(u, v) :  
  
    if u not in graph1 : 
        graph1[u] = []; 
          
    if v not in graph2 : 
        graph2[v] = []; 
          
    graph1[u].append(v); 
    graph2[v].append(u);  
  
# DFS   
def dfs1(x) :  
    vis1[x] = True; 
    if x not in graph1 : 
        graph1[x] = {}; 
          
    for i in graph1[x] : 
        if (not vis1[i]) : 
            dfs1(i)  
  
# DFS function  
def dfs2(x) :  
  
    vis2[x] = True;  
  
    if x not in graph2 : 
        graph2[x] = {}; 
          
    for i in graph2[x] :  
        if (not vis2[i]) : 
            dfs2(i);  
  
def connection(n) :  
  
    global vis1; 
    global vis2; 
      
    # Call for correct direction 
    vis1 = [False] * len(vis1); 
    dfs1(1); 
      
    # Call for reverse direction 
    vis2 = [False] * len(vis2); 
    dfs2(1); 
      
    for i in range(1, n + 1) : 
   
        if (not vis1[i] and not vis2[i]) : 
            return False; 
      
    return True;  
  
# Driver code  
if __name__ == "__main__" :  
  
    n = 4;  
  
    # Add edges  
    Add_edge(1, 2);  
    Add_edge(1, 3);  
    Add_edge(2, 3);  
    Add_edge(3, 4);  
  
    #  call  
    if (connection(n)) : 
        print("Yes")
    else : 
        print("No")