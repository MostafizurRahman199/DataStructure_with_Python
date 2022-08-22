def add_node(v):
    if v in graph:
        print(v,"is already present")
    else:
        graph[v] = []
        
#----------------------------unweighted & undirected graph   
def add_edge(v1,v2): 
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1) #it does not in directed graph  

#---------------------------weighted & undirected graph  
def add_edge(v1,v2,cost): 
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]       #it does not in directed graph  
        graph[v1].append(list1)
        graph[v2].append(list2) #it does not in directed graph  
    
    
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",22)
print(graph)