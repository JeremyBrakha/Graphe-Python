INF = 9999999

def prim(graphe) :
    n = len(graphe)
    selected =  [True] + [False] * (n-1)
    chemin = []

    s = 0
    while (s < n - 1):
        # Pour chaque sommet, selectionner son sommet adjacent 
        # n'ayant pas encore ete selectionne et constituant le poids le plus petit
        minimum = INF
        x = 0
        y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if ((not selected[j]) and (graphe[i][j] != 0)):  
                        if minimum > graphe[i][j]:
                            minimum = graphe[i][j]
                            x = i
                            y = j
        chemin.append((x, y))
        selected[y] = True
        s += 1

    return chemin


grapheTest = [
        [ 0 , 1 , 0, 5, 0, 0, 0 ] ,
        [ 1 , 0 , 8, 9, 1, 0, 0 ] ,
        [ 0 , 8 , 0, 0, 5, 0, 0 ] ,
        [ 5 , 9 , 0, 0, 15, 6, 0 ] ,
        [ 0 , 1 , 5, 15, 0, 8, 9 ] ,
        [ 0 , 0 , 0, 6, 0, 0, 11 ] ,
        [ 0 , 0 , 0, 0, 9, 0, 0 ] 
    ]

print(prim(grapheTest))