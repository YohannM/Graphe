import kruskal as Graphe 

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
app_val = []

for i, som in enumerate(Matrix):
    for j, val in enumerate(som):
        if val != 0:
            app_val.append([[i, j], val])



sommet = [0,1,2,3,4,5]

# app_val = [[[1, 2], 1], [[2, 3], 2], [[1, 4], 3], [[3, 4], 1], [[2, 4], 4]]

app = []
val_dep = []

for i in range(len(app_val)):
    app.append(app_val[i][0])
    val_dep.append(app_val[i][1])

Graphe.affiche_graphe(app, val_dep, "Graphe d'origine")

app_couvrante, val = Graphe.kruskal(sommet, app_val)

Graphe.affiche_graphe(app_couvrante, val, "Graphe avec arbre couvrant minimal")

print("Fin")