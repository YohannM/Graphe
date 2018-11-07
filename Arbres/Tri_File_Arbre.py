
import random
import traitementArbre as ta
import queue as q

if __name__ == '__main__':

    arbre = ta.creerABR()
    print("")
    print(ta.estArbreDeRecherche(arbre))
    print("Somme =", ta.sommeArbreDeRecherche(arbre))
    #ta.parcoursInfixe(arbre)
    maFile = q.Queue()
    for i in range(25):
        maFile.enqueue(random.randint(0, 150))

    racine = ta.Noeud(maFile.getFirst())
    maFile.dequeue()

    while not maFile.isEmpty():
        ta.placerValABR(racine, maFile.getFirst())
        maFile.dequeue()

    ta.regFile(maFile, racine)

    while not maFile.isEmpty():
        print(maFile.getFirst())
        maFile.dequeue()

    