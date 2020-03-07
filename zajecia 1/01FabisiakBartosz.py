weight_dictionary = {}
edges_to_add_delete = []
with open('graph.txt', 'r') as file:
    a = file.readline()
    for i in range(int(a)):
        weight_dictionary[i+1] = []
        line = file.readline()
        list = line.split()
        for weight in list:
            if weight == "-":
                weight_dictionary[i+1].append(float('inf'))
            else:
                weight_dictionary[i+1].append(int(weight))

    b = None
    i = 1
    b = file.readline().split()
    while(b != []):
        edges_to_add_delete.append(b)
        b = file.readline().split()
        i += 1

successors = {}
for key in weight_dictionary.keys():
    successors[key] = []
    for index in range(len(weight_dictionary[key])):
        if weight_dictionary[key][index] != float('inf'):
            successors[key].append(index + 1)


whole_graph_w_weight = {}
for key in successors:
    whole_graph_w_weight[key] = {}
    for point in successors[key]:
        whole_graph_w_weight[key][point] = weight_dictionary[key][point-1]

edges = {}
for key in weight_dictionary:
    for i in range(len(weight_dictionary[key])):
        if weight_dictionary[key][i] != float('inf'):
            new_key = "(" + str(key) + ")"
            if key < i+1:
                edges[(key, i+1)] = weight_dictionary[key][i];
                #new_key = "(" + str(key) + "," + str(i + 1) + ")"
            elif key > i+1:
                edges[(i + 1, key)] = weight_dictionary[key][i];
                #new_key = "(" + str(i + 1) + "," + str(key) + ")"

print(successors)
print(whole_graph_w_weight)
print(edges)
print("Lista następników:")

for key in successors:
    print(key, ":", end=" ")
    for point in successors[key]:
        print(point, end=" ")
    print("")

for key in weight_dictionary:
    for i in range(len(weight_dictionary[key])):
        for pair in edges_to_add_delete:
            if (key == int(pair[0]) and i+1 == int(pair[1])) or\
                    (key == int(pair[1]) and i+1 == int(pair[0])):
                if weight_dictionary[key][i] == float('inf'):
                    weight_dictionary[key][i] = 3
                else:
                    weight_dictionary[key][i] = float('inf')

successors = {}
for key in weight_dictionary.keys():
    successors[key] = []
    for index in range(len(weight_dictionary[key])):
        if weight_dictionary[key][index] != float('inf'):
            successors[key].append(index + 1)


whole_graph_w_weight = {}
for key in successors:
    whole_graph_w_weight[key] = {}
    for point in successors[key]:
        whole_graph_w_weight[key][point] = weight_dictionary[key][point-1]

edges = {}
for key in weight_dictionary:
    for i in range(len(weight_dictionary[key])):
        if weight_dictionary[key][i] != float('inf'):
            new_key = "(" + str(key) + ")"
            if key < i+1:
                edges[(key, i+1)] = weight_dictionary[key][i];
                #new_key = "(" + str(key) + "," + str(i + 1) + ")"
            elif key > i+1:
                edges[(i + 1, key)] = weight_dictionary[key][i];
                #new_key = "(" + str(i + 1) + "," + str(key) + ")"

print(successors)
print(whole_graph_w_weight)
print(edges)
print("Lista następników:")

for key in successors:
    print(key, ":", end=" ")
    for point in successors[key]:
        print(point, end=" ")
    print("")