
ligne = "0:1.2,2.4,3.8,5.1"

sommet, sommet_dest = ligne.split(':');

w, h = 6, 1
Matrix = [[0 for x in range(w)] for y in range(h)]

sommet, sommet_dest = ligne.split(':');
valuation = sommet_dest.split(',')
for partie in valuation:
    Matrix[int(sommet)][int(partie.split('.')[0])] = partie.split('.')[1]

print(Matrix)