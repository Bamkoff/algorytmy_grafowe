def metoda_wegierska(X, Y):
    X_keys = []
    for x in X.keys():
        X_keys.append(x)
    M = []
    M_Y = []
    skoj = True
    while len(M) != len(X) and skoj:
        for skojarzenie in M:
            if skojarzenie[1] not in M_Y:
                M_Y.append(skojarzenie[1])
        u = X_keys[0]
        X_keys.pop(0)
        P_y = {}
        P_x = {}
        S = [u]
        S_copy = [u]
        T = []
        procedura_wykonana = False
        while skoj and not procedura_wykonana:
            x = S.pop(0)
            for y in X[x]:
                if y not in T:
                    T.append(y)
                    P_y[y] = x
                    if y not in M_Y:
                        M_scierzka = []
                        procedura_wykonana = True
                        temp = y
                        while P_y[temp] != u:
                            M_scierzka.append(temp)
                            M_scierzka.append(P_y[temp])
                            M.append((P_y[temp], temp))
                            M.pop(M.index((P_y[temp], P_x[P_y[temp]])))
                            temp = P_x[P_y[temp]]
                        M.append((P_y[temp], temp))
                        M_scierzka.append(temp)
                        M_scierzka.append(P_y[temp])
                        print("Sciezka M-zasilona: ", end="")
                        for i in range(len(M_scierzka)-1, -1, -1):
                            print(M_scierzka[i], end=" ")
                        print("")
                        break
                    else:
                        for v in X:
                            if (v, y) in M:
                                P_x[v] = y
                                S.append(v)
                                S_copy.append(v)
            if len(S) == 0 and not procedura_wykonana:
                skoj = False
        if skoj:
            print("Aktualne skojarzenie:", end="")
            for skojarzenie in M:
                print(skojarzenie, end="")
            print("")
        else:
            print("Nie ma skojarzenia w grafie. Dla S=( ", end="")
            for i in S_copy:
                print(i, end=" ")
            print(") mamy |N(S)| < |S|")

        if len(M) == len(X) and skoj:
            print("Znalezlismy skojarzenie nasycajace zbior X:")
            print("Aktualne skojarzenie:", end="")
            for skojarzenie in M:
                print(skojarzenie, end="")
            print("")


graph = []
with open("graph11.txt", 'r') as file:
    a = file.readline().split()
    while a:
        graph.append(a)
        a = file.readline().split()

X = {}
Y = {}
for i in range(len(graph)):
    Y[i+1] = []
    X[i + 1] = []
    for j in range(len(graph[i])):
        if graph[i][j] == '1':
            Y[i+1].append(j+1)
        if graph[j][i] == '1':
            X[i+1].append(j+1)

metoda_wegierska(X, Y)
