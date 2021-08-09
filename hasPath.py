#Return true if the graph contains a path from the source to destination

from typing import Counter


graph = {
    'f':['i','g'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i'],
    'k':[]
}

#using dfs
# def dfs(graph,source,destination):
#     if source == destination:
#         return True
#     for neighbour in graph[source]:
#         if dfs(graph,neighbour,destination):
#             return True
#     return False

# print(dfs(graph,'f','k'))        

#using bfs
def bfs(graph,source,destination):
    queue = [source]
    while len(queue) > 0:
        curr = queue.pop(0)
        if curr == destination: return True
        for neighbour in graph[curr]:
            queue.append(neighbour)
    return False
     


print(bfs(graph,'f','k'))