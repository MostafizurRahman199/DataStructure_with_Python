def add_node(v):
    if v in graph:
        print(v,"is already present")
    else:
        graph[v] = []
        
  
def add_edge_unweighted_undirected(v1,v2): 
    if v1 not in graph:
        print(v1,message)
    elif v2 not in graph:
        print(v2,message)
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)  


def add_edge_weighted_directed(v1,v2,cost): 
    if v1 not in graph:
        print(v1,message)
    elif v2 not in graph:
        print(v2,message)
    else:
        list1 = [v2,cost]
        graph[v1].append(list1)
       
        

def add_edge_weighted_undirected(v1,v2,cost):
    if v1 not in graph:
        print(v1,message)
    elif v2 not in graph:
        print(v2,message)
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]     
        graph[v1].append(list1)
        graph[v2].append(list2) 

def delete_node_unweighted_directed(v): 
    if v not in graph:
        print(v,message)
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)

def delete_node_weighted_directed(v):
    if v not in graph:
        print(v,message)
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for innerList in list1:
                if v == innerList[0]:
                    list1.remove(innerList)
                    break

def delete_edge_unweighted_undirected(v1,v2):
    if v1 not in graph:
        print(v1,message)
    elif v2 not in graph:
        print(v2,message)
    else:
       if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)
        
        
    
    
graph = {}
message = "is not present in the graph"
add_node("A")
add_node("B")
add_node("C")
# add_edge_weighted_directed("A","B",10)
# add_edge_weighted_directed("A","C",10)

add_edge_unweighted_undirected("A","B")
add_edge_unweighted_undirected("A","C")
print(graph)

# delete_node_weighted_directed("D")
delete_edge_unweighted_undirected("A","C")
print(graph)

