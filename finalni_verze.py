import math
from math import sqrt, fabs

#funkce 1, kružnice splývají
x1 = float(input("Zadejte souřadnici x1: "))
y1 = float(input("Zadejte souřadnici y1: "))
r1 = float(input("Zadej poloměr r1: "))

x2 = float(input("Zadejte souřadnici x2: "))
y2 = float(input("Zadejte souřadnici y2: "))
r2 = float(input("Zadej poloměr r2: "))

if math.isclose(x1, x2) and math.isclose(y1, y2) and math.isclose(r1,r2):
    print("Kružnice splývají")
else: 
    print("Kružnice nesplývají")

#funkce2, jedna kružnice leží zcela uvnitř druhé
x1 = float(input("Zadejte souřadnici x1: "))
y1 = float(input("Zadejte souřadnici y1: "))
r1 = float(input("Zadej poloměr r1: "))

x2 = float(input("Zadejte souřadnici x2: "))
y2 = float(input("Zadejte souřadnici y2: " ))
r2 = float(input("Zadej poloměr r2: "))

vzdalenost_stredu = (sqrt((x2-x1)**2 + (y2-y1)**2))

rozdil_polomeru = fabs(r1-r2)

if vzdalenost_stredu < rozdil_polomeru:
    print("Kružnice 2 leží zcela uvnitř kružnice 1")
else:
    print("Kružnice 2 neleží zcela uvnitř kružnice 1")



#funkce3, jedna kružnice se zevnitř dotýká druhé

x1 = float(input("Zadejte souřadnici x1: "))
y1 = float(input("Zadejte souřadnici y1: "))
r1 = float(input("Zadej poloměr r1: "))

x2 = float(input("Zadejte souřadnici x2: "))
y2 = float(input("Zadejte souřadnici y2: " ))
r2 = float(input("Zadej poloměr r2: "))

vzdalenost_stredu = (sqrt((x2-x1)**2 + (y2-y1)**2))

rozdil_polomeru = fabs(r1-r2)

if vzdalenost_stredu == rozdil_polomeru:
    print("Jedna kružnice se zevnitř dotýká druhé")
else:
    print("Jedna kružnice se zevnitř nedotýká druhé")



#funkce4, kružnice se protínají

x1 = float(input("Zadejte souřadnici x1: "))
y1 = float(input("Zadejte souřadnici y1: "))
r1 = float(input("Zadej poloměr r1: "))

x2 = float(input("Zadejte souřadnici x2: "))
y2 = float(input("Zadejte souřadnici y2: " ))
r2 = float(input("Zadej poloměr r2: "))

vzdalenost_stredu = (sqrt((x2-x1)**2 + (y2-y1)**2))

rozdil_polomeru = fabs(r1-r2)

soucet_polomeru = r1 + r2

if rozdil_polomeru < vzdalenost_stredu < soucet_polomeru:
    print("Kružnice se protínají")
else:
    print("Kružnice se neprotínají")



#funkce 5, kružnice se dotýkají zvenku

x1 = float(input("Zadejte souřadnici x1: "))
y1 = float(input("Zadejte souřadnici y1: "))
r1 = float(input("Zadej poloměr r1: "))

x2 = float(input("Zadejte souřadnici x2: "))
y2 = float(input("Zadejte souřadnici y2: " ))
r2 = float(input("Zadej poloměr r2: "))

vzdalenost_stredu = (sqrt((x2-x1)**2 + (y2-y1)**2))

soucet_polomeru = r1 + r2

if vzdalenost_stredu == soucet_polomeru:
    print("Kružnice se dotýkají zvenku")
else:
    print("Kružnice se nedotýkají zvenku")

# funkce 6, kružnice leží zcela mimo sebe.

x1 = float(input("Zadejte souřadnici x1: "))
y1 = float(input("Zadejte souřadnici y1: "))
r1 = float(input("Zadej poloměr r1: "))

x2 = float(input("Zadejte souřadnici x2: "))
y2 = float(input("Zadejte souřadnici y2: " ))
r2 = float(input("Zadej poloměr r2: "))

vzdalenost_stredu = (sqrt((x2-x1)**2 + (y2-y1)**2))

soucet_polomeru = r1 + r2

if vzdalenost_stredu > soucet_polomeru:
    print("Kružnice leží zcela mimo sebe")
else:
    print("Kružnice neleží mimo sebe")