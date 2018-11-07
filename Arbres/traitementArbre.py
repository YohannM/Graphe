
import random
NBNOEUDS = 25 

class Noeud:

    def __init__(self, val):
        self.val = val 
        self.fg = None
        self.fd = None


def placerValABR(noeud, val):
    if val <= noeud.val:
        if noeud.fg == None:
            noeud.fg = Noeud(val)
        else :
            placerValABR(noeud.fg, val)
    else:
        if noeud.fd == None:
            noeud.fd = Noeud(val)
        else:
            placerValABR(noeud.fd, val)


def creerABR():
        listeNoeuds = []
        for i in range(25):
            listeNoeuds.append(random.randint(0, 150))

        racine = Noeud(listeNoeuds[0])

        for i in range(len(listeNoeuds)-1):
            placerValABR(racine, listeNoeuds[i+1])
        return racine

def parcoursInfixe(racine):
    if racine!= None:
        parcoursInfixe(racine.fg)
        print(racine.val)
        parcoursInfixe(racine.fd)

def parcoursPrefixe(racine):
    if racine != None:
        print(racine.val)
        parcoursPrefixe(racine.fg)
        parcoursPrefixe(racine.fd)

def hauteur(racine):
    if racine.fd == None and racine.fg == None:
        return 1
    elif racine.fd == None:
        return hauteur(racine.fg) + 1
    elif racine.fg == None:
        return hauteur(racine.fd) + 1
    else:
        return max(hauteur(racine.fg), hauteur(racine.fd)) + 1

def taille(racine):
    if racine.fd == None and racine.fg == None:
        return 1
    elif racine.fd == None:
        return taille(racine.fg) + 1
    elif racine.fg == None:
        return taille(racine.fd) + 1
    else:
        return taille(racine.fg) + taille(racine.fd) + 1

def supprimer(ABR, val):
    feuilleASupp = ABR 
    while feuilleASupp.val != val:
        if feuilleASupp.val > val:
            feuilleASupp = feuilleASupp.fg
        else:
            feuilleASupp = feuilleASupp.fd
    if feuilleASupp.fd != None:
        pereMin = feuilleASupp.fd
        if pereMin.fg != None:
            fMin = pereMin.fg
            while pereMin.fg.fg != None:
                pereMin = pereMin.fg
                fMin = pereMin.fg
            pereMin.fg = fMin.fd
        else :
            fMin = pereMin
            feuilleASupp.fd = pereMin.fd
        feuilleASupp.val = fMin.val
    elif feuilleASupp.fg != None:
        pereMax = feuilleASupp.fg
        if pereMax.fd != None :
            fMax = pereMax.fd
            while pereMax.fd.fd != None:
                pereMax = pereMax.fd
                fMax = pereMax.fd
            pereMax.fd = fMax.fg
        else :
            fMax = pereMax
            feuilleASupp = pereMax.fg
        feuilleASupp.val = fMax.val   
    else:
        feuilleASupp = None


def estArbreDeRecherche(racine):
    if racine != None:
        if racine.fg != None and racine.fd != None:
            return racine.fg.val <= racine.val and racine.fd.val >= racine.val and estArbreDeRecherche(racine.fg) and estArbreDeRecherche(racine.fd)
        elif racine.fg != None:
            return racine.fg.val <= racine.val and estArbreDeRecherche(racine.fg)
        elif racine.fd != None:
            return racine.fd.val >= racine.val and estArbreDeRecherche(racine.fd)
    return True


def sommeArbreDeRecherche(racine):
    if racine == None:
        return 0
    return racine.val + sommeArbreDeRecherche(racine.fg) + sommeArbreDeRecherche(racine.fd)


def regFile(maFile, abr):
    if abr != None:
        regFile(maFile, abr.fg)
        maFile.enqueue(abr.val)
        regFile(maFile, abr.fd)


if __name__ == '__main__':
    arbre = creerABR()
    print("hauteur : ", hauteur(arbre))
    print("taille : ", taille(arbre))
    parcoursPrefixe(arbre)
    print("\n\n")
    supprimer(arbre, arbre.fg.val)
    parcoursInfixe(arbre)
    print("taille : ", taille(arbre))

    #while True:
        #arbre = creerABR()
       # supprimer(arbre, arbre.val)
       # print("succes")


    