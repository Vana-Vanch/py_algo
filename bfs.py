#directed graph
graph = {
    'a':['c','b'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}

def breadthFirstSearch(graph,start):
    queue = [start]
    while len(queue) > 0:
        curr = queue.pop(0)
        print(curr, end=" ")
        for neighbour in graph[curr]:
            queue.append(neighbour)





breadthFirstSearch(graph,'a')

