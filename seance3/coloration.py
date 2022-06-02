import networkx as nx
import matplotlib.pyplot as mat

# renvoie les voisins d'un sommet donnée dans un graphe
def voisins(graphe, i):
    voi = list()
    for j in range(len(graphe)):
        if (i in graphe[j]):
            voi.append(j)
    if (len(graphe[i]) != 0):
        voi.extend(graphe[i])
    return voi

# renvoie les couleurs en fonctions des sommets
def get_color(G, node, sommetsColories):
    for i in range(len(G)):
        if node == i:
            return sommetsColories[i]


def Welsh_Powell(G):
    colors = ["Blue", "Pink", "Green", "Yellow",
              "Purple", "Orange", "Black", "White"]
    sommetsColories = dict()

    Gp = G
    deg = dict()
    for i in range(len(G)):
        deg[i] = 0
        sommetsColories[i] = "None"

    for liste in G:
        for i in range(len(liste)):
            deg[liste[i]] += 1
    for i in range(len(G)):
        deg[i] += len(G[i])

    deg = list(deg.items())
    deg.sort(key=lambda x: x[1])
    deg.reverse()

    i = 0
    while ("None" in sommetsColories.values()):
        # Selection de tous les sommets n'ayant pas de voisins selectionne :
        sommetsTraités = []
        sommetsSelectione = []
        for i in range(len(deg)):
            sommet = deg[i][0]
            voisinDuSommet = voisins(Gp, sommet)
            for f in range(len(deg)):
                if f not in voisinDuSommet and f not in sommetsTraités:
                    yes = False
                    for l in sommetsSelectione:
                        if (f in voisins(Gp, l)):
                            yes = True
                    if (yes == False):
                        sommetsSelectione.append(f)

            # Coloration de ces sommets :
            for s in sommetsSelectione:
                sommetsColories[s] = colors[0]
                sommetsTraités.append(s)
            colors.pop(0)
            sommetsSelectione.clear()

        i += 1

        # Suppression des sommets selectionnes de Gp
        sommetsSelectione.sort(reverse=True)
        for s in sommetsSelectione:
            Gp.pop(s)

        # Création du graphe
        Graphe = nx.DiGraph()

        # Création des arêtes
        for index, vertices in enumerate(G):
            print(vertices)
            for element in vertices:
                print("index", index, "element", element)
                Graphe.add_edge(index, element)

        # Attribution des bonnes couleurs aux arêtes
        colors = [get_color(Graphe, node, sommetsColories)
                  for node in Graphe.nodes()]
        nx.draw_networkx(Graphe, node_color=colors, with_labels=True)
        mat.show()

    return sommetsColories


G = [[1, 2], [2], [3], [4], []]
F = [[3, 5, 7], [2, 4, 6], [5, 7], [4, 6],
     [7], [6], [], []]
Z = [[2], [], [3], [1]]

result = Welsh_Powell(F)

print(result)
