

import kruskal as kk

def readGraph():

    with open("E:/PROG/Python/Graphe/Graphes/Kruskal_AA/matrice.txt", 'r') as f:
        prog = f.read().split('\n')

        taille = len(prog)
        Matrix = [[0 for x in range(taille)] for y in range(taille)]

        for ligne in prog:
            sommet, sommet_dest = ligne.split(':');
            valuation = sommet_dest.split(',')
            for partie in valuation:
                Matrix[int(sommet)][int(partie.split('.')[0])] = int(partie.split('.')[1])
        return Matrix

Matrix = readGraph()
liste = []

for i, som in enumerate(Matrix):
    for j, val in enumerate(som):
        liste.append([[i, j], val])

sommets = [x for x in range(len(Matrix))]

#print(sommets)
#print(Matrix)
#print(liste)

app_ = []
som_ = []

for app in liste:
    app_.append(app[0])
    som_.append(app[1])


bon_matrice, val = kk.kruskal_matrice(Matrix)

kk.affiche_graphe(app_, som_, "origine")
kk.affiche_graphe(bon_matrice, val, "Ma Matrice")
            