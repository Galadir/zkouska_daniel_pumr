# dotázání uživatele na možnost práce s desetinnými čísly
des = input('Napište "ANO", pokud chcete pracovat s desetinými čísly: ')

# dotázání uživatele na vstupní posloupnosti
print("Zapište posloupnosti. Čísla oddělte mezerou.")
a=input("Posloupnost 1: ")
b=input("Posloupnost 2: ")

# převedení hodnot na seznamy čísel a ošetření pro případ zadání nebhodných hodnot
try:
    if des=="ANO" or des=="ano" or des=="Ano":
        a = list(map(float, a.split()))
        b = list(map(float, b.split()))
    else:
        a = list(map(int, a.split()))
        b = list(map(int, b.split()))
except ValueError:
    print("Do některé z posloupností byly zadány jiné hodnoty než čísla, "
          "\nnebo byla zadána desetinná čísla, ačkoli nebylo nastaveno jejich zpracování. "
          "\nProgram byl ukončen")
    exit(2)

# tvorba seznamů pro průnik a doplňky
prunik=[]

doplnek_a=[]
doplnek_b=[]

# cykly rozřazující hodnoty do průniku nebo do doplnků
for i in a:
    if i in b:
        prunik.append(i)
    else:
        doplnek_a.append(i)

for i in b:
    if i not in a:
        doplnek_b.append(i)

# vytvoření sjednocení
sjednoceni=sorted(doplnek_a+prunik+doplnek_b)

# vytisknutí výsledných posloupností
print("Pro zadané posloupnosti je sjednocení tvořeno hodnotami {}\n"
      "průnik = {}\n"
      "doplněk poslupnosti 1 = {}\n"
      "doplněk posloupnosti 2 = {}\n".format(sjednoceni,sorted(prunik),sorted(doplnek_a),sorted(doplnek_b)))
