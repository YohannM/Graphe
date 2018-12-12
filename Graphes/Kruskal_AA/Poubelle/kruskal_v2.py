
import kruskal as k

class NoeudSommet:
    def __init__(self, sommet, valuation, suiv):
        self.sommet = sommet
        self.valuation = valuation
        self.suiv = suiv

    def setSuiv(self, suiv):
        self.suiv = suiv


# Pour afficher une liste d'adjacence
def affiche_liste_adj(liste_adj):
    for s in liste_adj:
        print("Pour le sommet", s.sommet)
        s_cour = s.suiv
        while s_cour != None:
            print("\tOn a un lien vers le sommet", s_cour.sommet, "de poids", s_cour.valuation)
            s_cour = s_cour.suiv
            


s0_1_2 = NoeudSommet(1, 20, None)
s0_1 = NoeudSommet(1, 9, s0_1_2)
s0 = NoeudSommet(0, None, s0_1)

s1_4_3 = NoeudSommet(4, 1, None)
s1_4_2 = NoeudSommet(4, 10, s1_4_3)
s1_4 = NoeudSommet(4, 5, s1_4_2)
s1 = NoeudSommet(1, None, s1_4)


liste_adj = [s0, s1]

print("AVANT KRUSKAL : ")
affiche_liste_adj(liste_adj)

print("\nAPRES KRUSKAL : ")
affiche_liste_adj(k.kruskal_liste_adj(liste_adj))



