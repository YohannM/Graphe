

# Pour afficher un graphe depuis une liste d'adjacence
def affiche_liste_adj(liste_adj):
    for s in liste_adj:
        print("Pour le sommet", s.sommet)
        s_cour = s.suiv
        while s_cour != None:
            print("\tOn a un lien vers le sommet", s_cour.sommet, "de poids", s_cour.valuation)
            s_cour = s_cour.suiv

# Pour afficher un graphe depuis une matrice
def affiche_matrice(matrice):
    for i, s in enumerate(matrice):
        print("Pour le sommet", i)
        for j, val in enumerate(s):
            print("\tOn a un lien vers le sommet", j, "de poids", val)