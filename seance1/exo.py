import random
import numpy as np

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

# Permet de récupérer un graphe sous forme de dictionnaire. Sert pour l'algo dfs
def dictGraphe(matriceAdjc):
    graphe = dict()
    for index, node in enumerate(matriceAdjc):
        indexes = graphe.setdefault(index, [])
        for idx, adj in enumerate(node):
            if adj == 1:
                indexes.append(idx)
    return graphe

# algo de parcours de graphe en profondeur pour un noeud donné
def dfs(visited, graph, node):  # function for dfs
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)




new_src = adjacente(graph3)
print(new_src)
print()
myDictGraphe = dictGraphe(new_src)
print(myDictGraphe)
# test = algo_roy(new_src)
# print(test)
print()
visited = set()
print(dfs(visited, myDictGraphe, 0))
