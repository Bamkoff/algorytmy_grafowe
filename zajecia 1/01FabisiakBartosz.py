weight_dictionary = {}
edges = {}
with open('graph.txt', 'r') as file:
    a = file.readline()
    for i in range(int(a)):
        weight_dictionary[i+1] = [];
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
        edges[i] = b
        b = file.readline().split()
        i += 1



successors = {}
for key in weight_dictionary.keys():
    successors[key] = []
    for index in range(len(weight_dictionary[key])):
        if weight_dictionary[key][index] != float('inf'):
            successors[key].append(index + 1)
print(successors)

