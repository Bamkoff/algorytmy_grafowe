def hamilton(succ):
    S = [1]
    u = succ[1][0]
    for i in S:
        print(i, end=" ")
    print("")
    while S:
        S.append(u)
        for i in S:
            print(i, end=" ")
        print("")
        if len(S) == len(succ.keys()) and 1 in succ[S[len(S)-1]]:
            print("CYKL HAMILTONA:", end=" ")
            for i in S:
                print(i, end=" ")
            print(1)
        copy_of_list = succ[u][:]
        for i in range(len(copy_of_list)-1, -1, -1):
            if copy_of_list[i] in S:
                copy_of_list.pop(i)
        if copy_of_list:
            u = copy_of_list[0]
        else:
            flag = True
            while S and flag:
                S.pop(len(S)-1)
                for i in S:
                    print(i, end=" ")
                print("")
                if S:
                    w = S[len(S)-1]
                    copy_of_list = succ[w][:]
                    for i in range(len(copy_of_list) - 1, 0, -1):
                        if copy_of_list[i] in S:
                            copy_of_list.pop(i)
                    u_index = copy_of_list.index(u)
                    if u_index == len(copy_of_list) - 1:
                        u = w
                    else:
                        u = copy_of_list[u_index+1]
                        flag = False


graph = []
with open("graph09.txt", 'r') as file:
    a = file.readline().split()
    while a:
        graph.append(a)
        a = file.readline().split()

successors = {}
for i in range(len(graph)):
    successors[i+1] = []
    for j in range(len(graph[i])):
        if graph[i][j] == '1':
            successors[i+1].append(j+1)
# print(successors)
hamilton(successors)
