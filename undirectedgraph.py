#search in an undirected graph
def buildGraph(edges):
    graph = {}
    for edge in edges:
        a,b = edge
        if(a not in graph): graph[a] = []
        if(b not in graph): graph[b] = []
        graph[a].append(b) 
        graph[b].append(a)
    return graph

def hasPath(graph,src,dst,visited):
    if src == dst: return True
    if src in visited: return False
    visited.append(src)
    for neighbour in graph[src]:
        if hasPath(graph,neighbour,dst,visited): return True
    return False

def dfs(edges,nodeA,nodeB):
    graph = buildGraph(edges)
    return hasPath(graph,nodeA,nodeB, list())




Theedges = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n']
]

print(dfs(Theedges,'i','l'))      