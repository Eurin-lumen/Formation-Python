#-*-coding:Latin-1 -*

annee = int(input("saissisez l'année : "))
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
    print("L'année saisie est bissextille")
else:
    print("L'année saisie n'est pas bissextile")


