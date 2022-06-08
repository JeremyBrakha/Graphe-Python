import numpy as np
import random

src = [[1, 2], [2], [3], [4], []]

graph = [[0, 2, 3, 4], [1, 2, 4], [0, 2, 3, 4], [1, 2, 3, 4], [0, 2, 4]]

graph2 = [[4, 6, 8, 9], [1, 2, 7, 9], [0, 2, 9], [1, 4, 5, 6, 8, 9], [1, 8, 9], [
    3, 4, 6, 9], [2, 3, 5, 6, 8, 9], [3, 4, 5, 6, 8, 9], [0, 1, 3, 6, 8, 9], [0, 1, 2, 5, 7, 9]]

graph3 = [[0, 1, 2, 6, 7, 9], [1, 8, 9], [1, 3, 5, 8, 9], [0, 2, 3, 4, 6, 9], [
    1, 3, 4, 7, 9], [1, 4, 9], [4, 6, 7, 9], [1, 2, 5, 9], [0, 3, 5, 6, 9], [2, 5, 9]]

graph4 = [[], [0], [0, 1], [2], [3]]

# rendre une matrice adjacente
def adjacente(graph):
    matrix = np.zeros((len(graph), len(graph)), dtype=int)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            matrix[i, graph[i][j]] = 1
    return matrix

# algorithme de Roy-Warshall
def algo_roy(graph):
    size = len(graph)
    for w in range(size):
        for u in range(size):
            for v in range(size):
                if graph[w][u] == 1 and graph[v][w] == 1:
                    graph[v][u] = 1

    return graph

# Permet de recuperer un graphe sous forme de dictionnaire. Sert pour l'algo dfs
def dictGraphe(matriceAdjc):
    graphe = dict()
    for index, node in enumerate(matriceAdjc):
        indexes = graphe.setdefault(index, [])
        for idx, adj in enumerate(node):
            if adj == 1:
                indexes.append(idx)
    return graphe

# algo de parcours de graphe en profondeur pour un noeud donne
def dfs(visited, graph, node):  # function for dfs
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# fonction qui donne la liste des predecesseurs d'un sommet passe en parametre
def predecesseurs(graphe, sommet) :
    pred = []
    for i in range(len(graphe)) :
        if sommet in graphe[i] :
            pred.append(i)

    return pred



def composantes_fconnexes(graphe):
    n = len(graphe)
    E = range(n)
    flags = []
    for i in range(n) :
        flags.append([])
    outcome = [] 

    # Tant que1 E non vide faire
    while (len(E) != 0) :

        # marquer + et - un sommet x de E;
        trouve = False
        s = random.randint(0, n-1)
        while ( not trouve ) :
            if ( '+' not in flags[s] and '-' not in flags[s] ) :
                flags[s].append('+')
                flags[s].append('-')
                trouve = True
            elif ( '+' not in flags[s] and '-' in flags[s] ) :
                flags[s].append('+')
                trouve = True
            elif ( '+'  in flags[s] and '-' not in flags[s] ) :
                flags[s].append('-')
                trouve = True
            else :
                s = random.randint(0, n-1) 

        # tant que2 c'est possible faire :
        possible = True
        while ( possible ) :
            # 1) marquer par + tout successeur (non encore marque par +) d'un sommet deja marque + ;
            for succ in graphe[s] :
                if '+' not in flags[succ] :
                    flags[succ].append('+')

            # 2) marquer par - tout predecesseur (non encore marque par -) d'un sommet deja marque - ;
            for pred in predecesseurs(graphe, s) :
                if '-' not in flags[pred] :
                    flags[pred].append('-')

            possible = False
            

        # Ecrire C l'ensemble des sommets marques + et -;
        C = []
        for i in range(n) :
            check = False
            for l in  outcome :
                if i in l :
                    check = True
            if ( '+' in flags[i] and '-' in flags[i] and not check ) :
                C.append(i)
                

        # Ajout des composantes fortement connexes
        outcome.append(C)

        
        # E <- E-C; C <- [];
        for i in C :
            E.remove(i)
        C = []


    return outcome



# new_src = adjacente(graph3)
# print(new_src)
# print()
# myDictGraphe = dictGraphe(new_src)
# print(myDictGraphe)
# test = algo_roy(new_src)
# print(test)
# print()
# visited = set()
# print(dfs(visited, myDictGraphe, 0))

G = [[1, 2], [2], [3], [4], []]

print(composantes_fconnexes(G))
