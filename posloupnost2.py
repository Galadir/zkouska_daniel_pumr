des = input('Napište "ANO", pokud chcete pracovat s desetinými čísly: ')


print("Zapište posloupnosti. Čísla oddělte mezerou.")
a=input("Posloupnost 1: ")
b=input("Posloupnost 2: ")

try:
    if des=="ANO" or des=="ano":
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

prunik=[]

doplnek_a=[]
doplnek_b=[]

for i in a:
    if i in b:
        prunik.append(i)
    else:
        doplnek_a.append(i)

for i in b:
    if i not in a:
        doplnek_b.append(i)

sjednoceni=sorted(doplnek_a+prunik+doplnek_b)

print("Pro zadané posloupnosti je sjednocení tvořeno hodnotami {}\n"
      "průnik = {}\n"
      "doplněk poslupnosti 1 = {}\n"
      "doplněk posloupnosti 2 = {}\n".format(sjednoceni,sorted(prunik),sorted(doplnek_a),sorted(doplnek_b)))
