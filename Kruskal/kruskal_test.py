import Graphe 

sommet = [1,2,3,4]

app_val = [[[1, 2], 1], [[2, 3], 2], [[1, 4], 3], [[3, 4], 1], [[2, 4], 4]]

app = []
val_dep = []

for i in range(len(app_val)):
    app.append(app_val[i][0])
    val_dep.append(app_val[i][1])

Graphe.affiche_graphe(app, val_dep, "Graphe d'origine")

app_couvrante, val = Graphe.kruskal(sommet, app_val)

Graphe.affiche_graphe(app_couvrante, val, "Graphe avec arbre couvrant minimal")

print("Fin")