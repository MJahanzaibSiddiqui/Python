# graph={
#     'A':['B','C'],
#     'B':['A','D'],
#     'C':['A','D','F'],
#     'D':['B','C','E','F'],
#     'F':['C','D','E'],
#     'E':['D','F']
# }

graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E'],
    'D': ['E', 'G', 'H'],
    'E': ['F'],
    'G': ['H'],
    'C': [],
    'F': [],
    'H': [],
}
VN = []
q = []


def bfs(VN, graph, node, goal):
    VN.append(node)
    q.append(node)
    while q:
        m = q.pop(0)
        print(m, end=" ")
        if m == goal:
            return
        for neighbour in graph[m]:
            if neighbour not in VN:
                VN.append(neighbour)
                q.append(neighbour)


print("Here is the BFS")
bfs(VN, graph, 'A', 'G')
