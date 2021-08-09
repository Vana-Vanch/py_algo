#directed graph
graph = {
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
    }

def depthFirstSearch(graph,start):
    stack = [start]
    while len(stack) > 0:
        curr = stack.pop()
        print(curr, end=" ")
        for neighbour in graph[curr]:
            stack.append(neighbour)



depthFirstSearch(graph,'a')