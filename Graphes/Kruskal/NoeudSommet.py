
class NoeudSommet:
    def __init__(self, sommet, valuation, suiv):
        self.sommet = sommet
        self.valuation = valuation
        self.suiv = suiv

    def setSuiv(self, suiv):
        self.suiv = suiv