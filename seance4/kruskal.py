from collections import OrderedDict


# Fonction qui retourne l'arete contenant le sommet passe en parametre
def find(aretes, sommet):
    for arete in aretes:
        if (arete[0] == sommet) or (arete[1] == sommet):
            return arete
    return None


def kruskal(graphe):
    n = len(graphe[0])
    chemin = []
    G = dict()
    k = 0

    # Transformation de la matrice d'adjacence en un dictionnaire, avec les aretes comme clef et les poids comme valeur
    for i in range(n):
        for j in range(n):
            poids = graphe[i][j]
            if (poids != 0):
                G[(i, j)] = poids

    listearetes = list(OrderedDict(
        sorted(G.items(), key=lambda x: x[1])).keys())

    while (k < n-1):
        trouve = False
        i = 0
        # Selection de la premiere arete ne formant pas de cycle
        while (not trouve and i < len(listearetes)):
            w = listearetes[i]
            if not (find(listearetes, w[0]) in chemin and find(listearetes, w[1]) in chemin):
                chemin.append(w)
                trouve = True
            i += 1
        k += 1

    return chemin


grapheTest = [
    [0, 1, 0, 5, 0, 0, 0],
    [1, 0, 8, 9, 1, 0, 0],
    [0, 8, 0, 0, 5, 0, 0],
    [5, 9, 0, 0, 15, 6, 0],
    [0, 1, 5, 15, 0, 8, 9],
    [0, 0, 0, 6, 0, 0, 11],
    [0, 0, 0, 0, 9, 0, 0]
]

print(kruskal(grapheTest))

result = [(0, 1), (4, 1), (3, 0), (2, 4), (5, 3), (4, 6)]
