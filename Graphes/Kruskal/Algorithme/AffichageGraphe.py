import networkx as nx
import matplotlib.pyplot as plt

# Pour afficher un graphe depuis une liste d'adjacence
def affiche_liste_adj(liste_adj):
    print("\n AFFICHAGE DU GRAPHE A PARTIR DE LA LISTE D'ADJACENCE\n")
    for s in liste_adj:
        print("Pour le sommet", s.sommet)
        s_cour = s.suiv
        while s_cour != None:
            print("\tOn a un lien vers le sommet", s_cour.sommet, "de poids", s_cour.valuation)
            s_cour = s_cour.suiv
    print("\n\n\n")

# Pour afficher un graphe depuis une matrice
def affiche_matrice(matrice):
    print("\n AFFICHAGE DU GRAPHE A PARTIR DE LA MATRICE\n")
    for i, s in enumerate(matrice):
        print("Pour le sommet", i)
        for j, val in enumerate(s):
            if val != None:
                print("\tOn a un lien vers le sommet", j, "de poids", val)
    print("\n\n\n")

# Pour afficher un graphe depuis une matrice dans une fenêtre
def affichage_Graphique_matrice(matrice, nom):
    G = nx.Graph()

    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] != None:
                G.add_edge(str(i), str(j), weight=matrice[i][j])

    nx.draw_networkx_edge_labels(G,pos=nx.circular_layout(G), font_color = 'b')

    nx.draw_circular(G, with_labels=True, node_size=400, 
    node_color="skyblue", node_shape="s", alpha=0.5, linewidths=10)
    plt.title(nom)
    plt.show()

# Pour afficher un graphe depuis une liste d'adjacence dans une fenêtre
def affichage_Graphique_liste_adj(liste_adj, nom):
    G = nx.Graph()

    for i in range(len(liste_adj)):
        sommet_dep = liste_adj[i].sommet
        noeud_courant = liste_adj[i]
        while noeud_courant.suiv != None:
            noeud_courant = noeud_courant.suiv
            G.add_edge(str(sommet_dep), str(noeud_courant.sommet), weight=noeud_courant.valuation)
            

    nx.draw_networkx_edge_labels(G,pos=nx.circular_layout(G), font_color = 'b')

    nx.draw_circular(G, with_labels=True, node_size=400, 
    node_color="skyblue", node_shape="s", alpha=0.5, linewidths=10)
    plt.title(nom)
    plt.show()