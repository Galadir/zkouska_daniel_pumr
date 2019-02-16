des = input('Napište "ANO", pokud chcete pracovat s desetinými čísly: ')


print("Zapište posloupnosti. Čísla oddělte mezerou.")
a=input("Posloupnost 1: ")
b=input("Posloupnost 2: ")

try:
    if des=="ANO" or des=="ano":
        a = set(map(float, a.split()))
        b = set(map(float, b.split()))
    else:
        a = set(map(int, a.split()))
        b = set(map(int, b.split()))
except ValueError:
    print("Do některé z posloupností byly zadány jiné hodnoty než čísla, "
          "\nnebo byla zadána desetinná čísla, ačkoli nebylo nastaveno jejich zpracování. "
          "\nProgram byl ukončen")
    exit(2)

c={}
c=a.union(b)

print("Sjednocení posloupností 1 a 2 je {}.".format(sorted(c)))


