
import NoeudSommet as ns

def readGraph():

    with open("graphe.txt", 'r') as f:
        prog = f.read().split('\n')

        taille = len(prog)

        matrice = [[None for x in range(taille)] for y in range(taille)]
        liste_adj = [x for x in range(taille)]

        for i in range(taille):
            liste_adj[i] = ns.NoeudSommet(i, None, None)

        for ligne in prog:
            sommet_depart, sommets_dest = ligne.split(':');
            liste_app = sommets_dest.split(',')
            
            # on remplit la matrice
            for partie in liste_app:

                sommet_arrive, valuation = partie.split('.')

                matrice[int(sommet_depart)][int(sommet_arrive)] = int(valuation)

                # on remplit la liste d'adjacence
                noeud_courant = liste_adj[int(sommet_depart)]
                while noeud_courant.suiv != None:
                    noeud_courant = noeud_courant.suiv
                noeud_courant.suiv = ns.NoeudSommet(sommet_arrive, valuation, None)

    return matrice, liste_adj