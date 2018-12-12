import numpy as np
import matric

def kruskal(M):

    #On crée un tableau ordonné de toutes les arrêtes
    Ak = []

    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != 0:
                Ak.append([M[i][j],i,j])
    
    Ak.sort()

    sommet_connectes = []
    Ak_acm = []
    representants = [x for x in range(len(M))]

    print(Ak)

    for elem in Ak :
        if not elem[1] in sommet_connectes or not elem[2] in sommet_connectes or (representants[elem[1]] != representants[elem[2]]):
            Ak_acm.append(elem)
            if not elem[1] in sommet_connectes and not elem[2] in sommet_connectes:
                sommet_connectes.append(elem[1])
                sommet_connectes.append(elem[2])
                representants[elem[1]] = elem[1]
                representants[elem[2]] = elem[1]
            elif not elem[1] in sommet_connectes:
                sommet_connectes.append(elem[1])
                rep = representants[elem[2]]
                representants[elem[1]] = rep
            elif not elem[2] in sommet_connectes:
                rep = representants(elem[1])
                sommet_connectes.append(elem[2])
                representants[elem[2]] = rep
            else:
                rep = representants[elem[1]]
                rep2 = representants[elem[2]]
                for i in range(len(representants)):
                    if representants[i] == rep:
                        representants[i] = rep2

            print(sommet_connectes)
    print(Ak_acm)


   # print(Ak)

kruskal(matric.createMatrix())



