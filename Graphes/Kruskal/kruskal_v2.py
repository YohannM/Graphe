
import operator

def kruskal(liste_adj):

    app_val = []

    # on transforme la liste d'adjacence en liste de la forme : [[(1,2), 5], [(5,3), 15]]
    for s in liste_adj:
        noeud_connecte = s.suiv
        while noeud_connecte != None:
             app_val.append([(s.sommet, noeud_connecte.sommet), noeud_connecte.valuation])
             noeud_connecte = noeud_connecte.suiv

    # on trie cette liste sur la base des valuations         
    app_val = sorted(app_val, key=key_takeSecond)

    sommets_connectes = []
    app_val_acm = []

    # on applique Kruskal
    for app in app_val:
        if app[0][0] not in sommets_connectes or app[0][1] not in sommets_connectes:
            if app[0][0] not in sommets_connectes:
                sommets_connectes.append(app[0][0])
            if app[0][1] not in sommets_connectes:
                sommets_connectes.append(app[0][1])
            app_val_acm.append(app)

    # on trie la liste obtenue sur la base des sommmets de départ
    app_val_acm = sorted(app_val_acm, key=key_takeFirstInTuple)

    # on crée une matrice de taille identique à la matrice de départ
    list_adj_finale = [x for x in range(len(liste_adj))]

    # on crée tous les noeuds de départ
    for i in range(len(list_adj_finale)):
        list_adj_finale[i] = NoeudSommet(i, None, None)

    # on retransforme la liste des applications en liste d'adjacence
    # avec app_val_acm de la forme [[(1,2), 5], [(5,3), 15]]
    for s in app_val_acm:
        sommet_courant = list_adj_finale[s[0][0]]
        while sommet_courant.suiv != None:
            sommet_courant = sommet_courant.suiv
        sommet_courant.suiv = NoeudSommet(s[0][1], s[1], None)

    return list_adj_finale


def key_takeSecond(liste):
    return liste[1]

def key_takeFirstInTuple(liste):
    return liste[0][0]

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
affiche_liste_adj(kruskal(liste_adj))



