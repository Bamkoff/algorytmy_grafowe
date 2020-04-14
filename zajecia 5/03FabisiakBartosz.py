
def print_matrix(sign, matrix):
    print(sign)
    for line in matrix:
        for element in line:
            print(str(element) + " ", end="")
        print("")
    print("")

def floyd_warshall(graph):
    p = []
    w = []
    for line_number in range(len(graph)):
        p.append([])
        w.append([])
        for weight in graph[line_number]:
            if weight != "-":
                p[line_number].append(line_number + 1)
                w[line_number].append(int(weight))
            else:
                p[line_number].append(None)
                w[line_number].append(float('inf'))
    for t in range(len(w)):
        print_matrix("W " + str(t) + " =", w)
        print_matrix("P " + str(t) + " =", p)
        for i in range(len(w)):
            if w[i][i] < 0:
                print("Ujemny cykl. Nie ma rozwiazania.")
                return True
        for i in range(len(w)):
            if i == t:
                continue
            for j in range(len(w[0])):
                if j == t:
                    continue
                if w[i][j] > w[i][t] + w[t][j]:
                    w[i][j] = w[i][t] + w[t][j]
                    p[i][j] = p[t][j]
    print_matrix("Ostateczna macierz odleglosci:", w)
    print_matrix("Ostateczna macierz poprzednikow:", p)
    print("Najkrotsze sciezki:")
    for i in range(len(w)):
        path = [i+1]
        j = i
        while j != 0:
            j = p[0][j] - 1
            path.append(j+1)
        print("z 1 do", str(i+1), ": ", end ="")
        for j in range(len(path), 0, -1):
            print(path[j-1], "", end="")
        print("")
    return False


graph = []
with open("graph05bez.txt", 'r') as file:
    a = file.readline().split()
    while(a != []):
        graph.append(a)
        a = file.readline().split()

floyd_warshall(graph)






