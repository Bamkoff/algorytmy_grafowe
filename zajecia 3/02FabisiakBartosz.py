def BFS_check(edge, successors):
    succ = {}
    for key in successors:
        succ[key] = successors[key][:]

    succ[edge[0]].pop(succ[edge[0]].index(edge[1]))
    succ[edge[1]].pop(succ[edge[1]].index(edge[0]))
    queue = [edge[0]]
    visited = []
    while(queue != []):
        key = queue.pop(0)
        visited.append(key)
        for i in succ[key]:
            if i == edge[1]:
                return False
            if i not in queue and i not in visited:
                queue.append(i)
    return True


edges = []
successors = {}
graph = []
with open("graph03.txt", 'r') as file:
    a = file.readline().split()
    while(a != []):
        graph.append(a)
        a = file.readline().split()

for i in range(len(graph)):
    successors[i+1] = []
    for j in range(len(graph[0])):
        if graph[i][j] == "1":
            successors[i+1].append(j+1)
            if j>i:
                if (i+1, j+1) not in edges:
                    edges.append((i+1, j+1))
            else:
                if (j+1, i+1) not in edges:
                    edges.append((j+1, i+1))
for edge in edges:
    if BFS_check(edge, successors):
        print(edge, "TAK")
    else:
        print(edge, "NIE")