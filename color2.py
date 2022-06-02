# def Welsh_Powell(G):
#     colors = ["White", "Black", "Green", "Yellow", "Blue"]
#     sommetsColories = dict()

#     Gp = G
#     deg = dict()
#     for i in range(len(G)):
#         deg[i] = 0
#         sommetsColories[i] = "None"

#     for liste in G:
#         for i in range(len(liste)):
#             deg[liste[i]] += 1
#     for i in range(len(G)):
#         deg[i] += len(G[i])

#     deg = list(deg.items())
#     deg.sort(key=lambda x: x[1])
#     deg.reverse()
#     sommetTab = []
#     for i in range(len(deg)):
#         sommetTab.append(deg[i][0])

#     i = 0

#     check = False
#     for element in sommetsColories.values():
#         if element == "None":
#             check = True

#     print("vrai faux", check)
#     while (check):
#         for i in range(len(deg)):
#             voisin = voisins(Gp, deg[i][0])
#             sommetsSelectionnable = list(set(sommetTab) - set(voisin))
#             print("mes sommets", sommetsSelectionnable)

#             for i in range(len(sommetsSelectionnable)):
#                 print("sommetsSelectionnable[i]", sommetsSelectionnable[i])
#                 voisinDeVoisin = voisins(Gp, deg[sommetsSelectionnable[i]][0])
#                 print("voisin de voins", voisinDeVoisin)
#                 print("voisins", voisin)

#                 elementsEnCommun = list(
#                     set(sommetsSelectionnable).intersection(voisinDeVoisin))
#                 print("elements en commun", elementsEnCommun)

#                 if elementsEnCommun == []:
#                     print("crochet i",
#                           sommetsColories[sommetsSelectionnable[i]])
#                     if sommetsColories[sommetsSelectionnable[i]] == "None":
#                         sommetsColories[sommetsSelectionnable[i]] = colors[0]
#                     print("crochet z",
#                           sommetsColories[sommetsSelectionnable[i]])
#                 else:
#                     print()

#             colors.pop(0)
#             print(sommetsColories)

#         for element in sommetsColories.values():
#             if element == "None":
#                 check = True
#                 break
#             else:
#                 check = False

#     return sommetsColories
