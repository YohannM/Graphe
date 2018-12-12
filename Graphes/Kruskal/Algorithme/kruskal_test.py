
import kruskal as kr 
import AffichageGraphe as ag
import fileReader as fr


if __name__ == '__main__':

    matrice, liste_adj = fr.readGraph()

    print("AVANT KRUSKAL :")

    ag.affiche_matrice(matrice)
    ag.affiche_liste_adj(liste_adj)
    ag.affichage_Graphique_matrice(matrice, "Graphe affiché à partir de la matrice avant Kruskal")
    ag.affichage_Graphique_liste_adj(liste_adj, "Graphe affiché à partir de la liste d'adjacence avant Kruskal")

    matrice, liste_adj = kr.kruskal_matrice(matrice), kr.kruskal_liste_adj(liste_adj)

    print("APRES KRUSKAL :")

    ag.affiche_matrice(matrice)
    ag.affiche_liste_adj(liste_adj)
    ag.affichage_Graphique_matrice(matrice, "Graphe affiché à partir de la matrice après Kruskal")
    ag.affichage_Graphique_liste_adj(liste_adj, "Graphe affiché à partir de la liste d'adjacence après Kruskal")
