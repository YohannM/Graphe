
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def kruskal(sommet, app_val):
    
    print("Algorithme de Kruskal déployé...")

    app_arbre_courant = []
    rep_s = []

    val_return = []

    for s in sommet:
        rep_s.append(s)

    while len(app_arbre_courant) != len (sommet) - 1:
        app_val_loc = []
        val = []

        for i in range(len(app_val)):
            val.append(app_val[i][1]) # On ajoute les valuations
        val.sort()

        tmp = app_val

        for i in range(len(val)):
            for j in range(len(tmp)):
                if tmp[j][1] == val[i]:
                    app_val_loc.append(tmp[j]) # On trie les app_val en fct des valuations
                    tmp[j][1] == -1
                    break

        arrete = app_val_loc[0][0]

        if rep_s[arrete[0]-1] != rep_s[arrete[1]-1]:
            app_arbre_courant.append(arrete)
            val_return.append(app_val_loc[0][1])

            for rep in rep_s:
                if rep == rep_s[arrete[0]-1]:
                    rep = rep_s[arrete[1]-1]

        app_val_loc[0][1] = 500

    print("Kruskal terminé !")

    return app_arbre_courant, val_return

def affiche_graphe(app_val, val, nom):

    print(nom + " est en construction...")

    app_val_loc = app_val
    source = []
    but = []

    for i in range(len(app_val_loc)):
        source.append(str(app_val_loc[i][0]))
        but.append(str(app_val_loc[i][1]))
    
    G = nx.Graph()

    for i in range(len(source)):
        G.add_edge(str(source[i]), str(but[i]), weight=val[i])

    nx.draw_networkx_edge_labels(G,pos=nx.circular_layout(G), font_color = 'b')

    nx.draw_circular(G, with_labels=True, node_size=400, 
    node_color="skyblue", node_shape="s", alpha=0.5, linewidths=10)
    plt.show()



if __name__ == "__main__":
    try:
        nb_sommet = int(input("Rentrez le nombre de sommet du grapghe : \n"))
        assert nb_sommet > 0
    except ValueError:
        print("Saisie non valide\n")
        exit()
    except AssertionError:
        print("Nombre négatif ou nul\n")
        exit()

    sommet = []

    for i in range(nb_sommet):
        sommet.append(i+1)

    try:
        nb_app = int(input("Rentrez le nombre d'arrêtes\n"))
        assert nb_app > 0
    except ValueError:
        print("Erreur de saisie\n")
        exit()
    except AssertionError:
        print("Nombre négatif ou nul\n")
        exit()

    app_val = []

    for i in range(nb_app):
        nb_incorrect = True

        while nb_incorrect:
            try:
                s1 = int(input("Application {} : rentrez le sommet source (numéro attendu)\n".format(i+1)))
                s2 = int(input("Application {} : rentrez le sommet but (numéro attendu)\n".format(i+1)))
                assert s1 in sommet and s2 in sommet
                nb_incorrect = False
            except ValueError:
                print("Saisie incorrecte\n")
            except AssertionError:
                print("Sommet inconnu\n")
            
        nb_incorrect = True

        while nb_incorrect:
            try:
                val = int(input("Rentrez la valuation de l'application {}\n".format(i+1)))  
                nb_incorrect = False
            except ValueError:
                print("Saisie incorrecte\n")

        app_val.append([[s1,s2], val])

    app = []
    val_dep = []

    for i in range(len(app_val)):
        app.append(app_val[i][0])
        val_dep.append(app_val[i][1])

    affiche_graphe(app, val_dep, "Graphe d'origine")
    app_couvrante, val = kruskal(sommet, app_val)
    affiche_graphe(app_couvrante, val, "Graphe avec arbre couvrant minimal")

    print("Fin")

