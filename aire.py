from math import sqrt

def calcule_surface(cote1,cote2,cote3):
    if cote1<cote2+cote3 and cote2<cote1+cote3 and cote3<cote1+cote2 :
        demi_perimetre = (cote1+cote2+cote3)/2
        surface = sqrt(demi_perimetre*(demi_perimetre-cote1)*(demi_perimetre-cote2)*(demi_perimetre-cote3))
        return surface
    else :
        return "Ce nést pas un triangle"

cote1 = int(input("entrer le cote 1"))
cote2 = int(input("entrer le cote 2"))
cote3 = int((input("ëntrer le cote 3")))

print(f"la surface est : {calcule_surface(cote1,cote2,cote3):}")
