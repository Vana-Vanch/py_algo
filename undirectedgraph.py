#Search in undirected graph

#create adjacency list
def makeGraph(edges):
    graph = {}
    for edge in edges:
        a,b = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph    

#traverse graph
def hasPath(graph,source,destination,visited):
    if source == destination: return True
    if source in visited: return False
    visited.add(source)
    for neightbour in graph[source]:
        if hasPath(graph,neightbour,destination,visited) == True: 
            return True
    return False


#using dfs
def dfs(edges,source,destination):
    graph = makeGraph(edges)
    return hasPath(graph,source,destination,set())


Theedges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n']
]

print(dfs(Theedges,'i','k'))
# TestEdges = [
#     [1,2],
#     [1,3],
#     [4,1],
#     [3,5],
#     [2,5],
#     [6,5],
#     [2,6],
#     [7,4],
#     [5,8],
    
#     [8,7],
    
#     [3,4],
#     [6,8],
#     [4,5],
#     [2,3],
#     [5,7],
    
# ]

# graph = {
#     1:[2,3,4],
#     2:[6,5,3,4,1],
#     3:[2,5,4,1],
#     4:[1,3,4,7],
#     5:[8,7,4,3,2,6],
#     6:[2,8,5],
#     7:[5,8,4],
#     8:[6,5,7]
# }







