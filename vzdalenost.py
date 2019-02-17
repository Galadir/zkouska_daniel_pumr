from math import radians, acos, sin, cos

print("V kilometrech zadejte poloměr referenční koule, na které bude počítána vzdálenost. "
      "\nPokud polomer nezadáte, nebo jej zadáte chybně, bude počítáno s hodnotou 6371,11 km")
try:
    r=float(input("Poloměr: "))
except ValueError:
    r= 6371.11

print("Je počítáno s průměrem {} km ".format(r))

try:
    print("Zadejte ve stupních souřadnice bodů.")
    p1=float(input("Šířka bodu A: "))
    while not (p1 >= -90 and p1 <= 90):
        print('Šířka neodpovídá možnému rozsahu, zkuste to znovu.')
        p1 = float(input('Šířka bodu A: '))
    l1=float(input("Délka bodu A: "))
    while not (l1 >= -180 and l1 <= 180):
        print('Délka neodpovídá možnému rozsahu, zkuste to znovu.')
        l1 = float(input('Délka bodu A: '))
    p2=float(input("Šířka bodu B: "))
    while not (p2 >= -90 and p2 <= 90):
        print('Šířka neodpovídá možnému rozsahu, zkuste to znovu.')
        p2 = float(input('Šířka bodu B: '))
    l2=float(input("Délka bodu B: "))
    while not (l2 >= -180 and l2 <= 180):
        print('Délka neodpovídá možnému rozsahu, zkuste to znovu.')
        l2 = float(input('Délka bodu B: '))
except ValueError:
    print("Některá ze souřadnic nebyla zadána jako platné číslo. Program byl ukončen.")
    exit(2)

print("Je počítána vzdálenost mezi bodem A o souřadnicích {}° šířky a {}° délky a bodem B o souřadnicích {}° šířky a {}° délky.".format(p1,l1,p2,l2))

x=acos(sin(radians(p1))*sin(radians(p2))+cos(radians(p1))*cos(radians(p2))*cos(radians(l2)-radians(l1)))
d=x*r

print("Vzdálenost mezi body A a B je {:.3f} km".format(d))
