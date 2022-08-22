from operator import index


def add_node(v):
    global node_count
    if v in nodes:
        print(v, "is already present in the graph")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph: # n = inner list
             n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
        
        
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print("")

#undirected unweighted graph

# def add_edge(v1,v2):
#     if v1 not in nodes:
#         print(v1,"is not present in the graph")
#     elif v2 not in nodes:
#         print(v2,"is not present in the graph")
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = 1
#         graph[index2][index1] = 1
        
        
#weighted graph
    
def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost #it does not needed directed weighted graph
        
        
        
def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,"is not present in the graph")
    else:
        index1 = nodes.index(v)
        node_count = node_count -1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)
        
        
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2) #does not in directed graph
        graph[index1][index2] = 0
        graph[index2][index1] = 0 #does not in directed graph
    
            


nodes = []
graph = []

node_count = 0
print("Before adding nodes")
print(nodes)
print(graph)

add_node("A")
add_node("B")
add_node("C")

add_edge("A","B",10)
add_edge("A","C",20)
add_edge("B","C",30)

print("After adding nodes")
print(nodes)
print_graph()

delete_node("A")
print(graph)
print(nodes)

delete_edge("B","C")
print_graph()
print(nodes)

