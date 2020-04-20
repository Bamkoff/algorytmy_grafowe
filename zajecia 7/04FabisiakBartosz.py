def prim(g):
    labels = []
    for i in range(len(g)):
        labels.append([])
        labels[i].append(None)
        if i == 0:
            labels[i].append(0)
        else:
            labels[i].append(float('inf'))
    tree = [1]
    z = 0
    print('Rozpatrywany wierzchołek:', z+1)
    while len(tree) != len(graph):
        for i in range(len(graph)):
            if i+1 not in tree:
                if labels[i][1] > graph[z][i]:
                    labels[i][0] = z+1
                    labels[i][1] = int(graph[z][i])
        min_index = -1
        minimum = float('inf')
        for i in range(len(graph)):
            print(labels[i], end=' ')
            if i+1 not in tree:
                if labels[i][1] < minimum:
                    minimum = labels[i][1]
                    min_index = i
        z = min_index
        tree.append(z+1)
        print('')
        print('Rozpatrywany wierzchołek:', z+1)
    print('Krawędzie drzewa:', end=' ')
    weight = 0
    for i in range(1, len(tree)):
        print("("+str(i+1)+", "+str(labels[i][0])+")", end=",")
        weight = weight + labels[i][1]
    print()
    print("Waga drzewa:", weight)


with open("graph07.txt", 'r') as file:
    graph = []
    a = file.readline().split()
    while a:
        graph.append(a)
        a = file.readline().split()
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == '-':
                graph[i][j] = float('inf')
            else:
                graph[i][j] = int(graph[i][j])
    prim(graph)