def TopologycalSort(x):
    y = x
    l = dict()
    l2 = []
    a = 0
    n = 1
    check = False
    for vertices in y:
        for i in vertices:
            if i != None:
                check = True
    if not check:
        print("La liste est vide")
    else:
        while (a < len(y)):
            i = 0
            l1 = []
            while (i < len(y)):
                es2 = any(i in sublist for sublist in l2)
                if es2:
                    i += 1
                else:
                    es1 = any(i in sublist for sublist in y)
                    if not es1:
                        l1.append(i)
                        i += 1
                    else:
                        i += 1
            if not l1:
                print("l1 est vide")
            else:
                l2.append(l1)
                l["Niveau " + str(n)] = l1

            for d in l1:
                y[d] = []
            n += 1
            a += 1

        return sorted(l.items())


G = [[1, 2], [2], [3], [4], []]

F = [[2, 3], [2], [3], [4], [5], []]
E = [[], [], [], [], [], []]

# gr = [[1], [2, 3], [5], [], [3], []]

# test(G)

result = TopologycalSort(E)
# done = test5()
print(result)
