
import NoeudSommet as ns

# applique kruskal sur une liste de la forme : [[(1,2), 5], [(5,3), 15]]
def kruskal(app_val, taille):

    # on trie cette liste sur la base des valuations         
    app_val = sorted(app_val, key=key_takeSecond)

    representants = [x for x in range(taille)]
    sommet_connectes = [False for x in range(taille)]
    app_val_acm = []

    # on applique kruskal
    for app in app_val:
        if not sommet_connectes[app[0][0]] or not sommet_connectes[app[0][1]] or (representants[app[0][0]] != representants[app[0][1]]):
                app_val_acm.append(app)
                
                if not sommet_connectes[app[0][0]] and not sommet_connectes[app[0][1]]:
                    sommet_connectes[app[0][0]] = True  
                    sommet_connectes[app[0][1]] = True
                    representants[app[0][0]] = app[0][0]
                    representants[app[0][1]] = app[0][0]

                elif not sommet_connectes[app[0][0]]:
                    sommet_connectes[app[0][0]] = True 
                    representants[app[0][0]] = representants[app[0][1]]
                
                elif sommet_connectes[app[0][1]]:
                    sommet_connectes[app[0][1]] = True
                    representants[app[0][1]] = representants[app[0][0]]
                
                else:
                    rep = representants[app[0][0]]
                    rep2 = representants[app[0][1]]
                    for i in range(len(representants)):
                        if representants[i] == rep2:
                            representants[i] = rep

    return app_val_acm




def kruskal_liste_adj(liste_adj):

    app_val = []

    # on transforme la liste d'adjacence en liste de la forme : [[(1,2), 5], [(5,3), 15]]
    for s in liste_adj:
        noeud_connecte = s.suiv
        while noeud_connecte != None:
             app_val.append([(int(s.sommet), int(noeud_connecte.sommet)), int(noeud_connecte.valuation)])
             noeud_connecte = noeud_connecte.suiv

    # on appelle kruskal sur cette liste
    app_val_acm = kruskal(app_val, len(liste_adj))

    # on trie la liste obtenue sur la base des sommmets de départ
    app_val_acm = sorted(app_val_acm, key=key_takeFirstInTuple)

    # on crée une matrice de taille identique à la matrice de départ
    list_adj_finale = [x for x in range(len(liste_adj))]

    # on crée tous les noeuds de départ
    for i in range(len(list_adj_finale)):
        list_adj_finale[i] = ns.NoeudSommet(i, None, None)

    # on retransforme la liste des applications en liste d'adjacence
    # avec app_val_acm de la forme [[(1,2), 5], [(5,3), 15]]
    for s in app_val_acm:
        sommet_courant = list_adj_finale[s[0][0]]
        while sommet_courant.suiv != None:
            sommet_courant = sommet_courant.suiv
        sommet_courant.suiv = ns.NoeudSommet(s[0][1], s[1], None)

    return list_adj_finale





def kruskal_matrice(matrice):

    app_val = []

    # on transforme la matrice en liste de la forme : [[(1,2), 5], [(5,3), 15]]
    for i, s in enumerate(matrice):
        for j, val in enumerate(s):
            if val != None:
                app_val.append([(i, j), val])

    # on appelle kruskal sur cette liste
    app_val_acm = kruskal(app_val, len(matrice))

    # on trie la liste obtenue sur la base des sommmets de départ
    app_val_acm = sorted(app_val_acm, key=key_takeFirstInTuple)

    # on crée la matrice finale de la même taille que la première
    matrice_final = [[None for x in range(len(matrice[0]))] for y in range(len(matrice))]

    # on la remplit
    for app in app_val_acm:
        matrice_final[app[0][0]][app[0][1]] = app[1]

    return matrice_final






def key_takeSecond(liste):
    return liste[1]

def key_takeFirstInTuple(liste):
    return liste[0][0]



