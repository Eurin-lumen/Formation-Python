#-*-coding:Latin-1 -*

annee = int(input("saissisez l'ann�e : "))
bissextile = False
if annee %400 == 0 :
    bissextile = True
elif annee %100 == 0 :
    bissextile = False
elif annee %4 == 0:
    bissextile = True
else :
    bissextile = False
if bissextile :
    print("L'ann�e saisie est bissextille")
else:
    print("L'ann�e saisie n'est pas bissextile")


