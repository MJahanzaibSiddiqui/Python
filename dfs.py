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
VN = set()


def dfs(VN, graph, node, goal):
    if node not in VN:
        print(node)
        # VN.add(node)
        VN.add(node)
    if goal == VN:
        return
    for neighbour in graph[node]:
        dfs(VN, graph, neighbour, goal)


print("Here is the DFS")
dfs(VN, graph, 'A', 'B')
