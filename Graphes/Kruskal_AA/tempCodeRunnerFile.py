sommet, sommet_dest = ligne.split(':');
valuation = sommet_dest.split(',').sort()
for partie in valuation:
    matrice[sommet][partie.split('.')[0]] = partie.split('.')[1]