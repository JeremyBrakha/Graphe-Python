
import numpy as np

def test4(x: list):
    if not any(x):
        print("Empty")
    else:
        print("rempli")


def test5():
    l = [[2], [], [], []]
    test4(l)
    l[0] = []
    test4(l)


def test6(x: list):
    y = x
    for idx, x in enumerate(y):
        for item in x:
            print(idx, item)


def test2(x: list):
    y = x
    # for i in range(len(y)):
    for vertices in range(len(y)):
        for listVertices in range(len(y[vertices])):
            # if (listVertices == i):
            #     print(listVertices)
            #     print(i)
            print("Trouvé", listVertices)

def test3(x: list):
    for z in range(len(x)):
        print(z)
        l = []
        for i in range(len(x)):
            for j in range(len(x[i])):
                if(x[i][j] == z):
                    print(x[i][j])
                # else:
                    # print("pas trouvé")


def test(x: list):
    y = x
    for idx, x in enumerate(y):
        print(idx, x)
