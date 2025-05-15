rok = int(input("Zadej rok: "))
if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
    print("Přestupný rok.")
else:
    print("Nepřestupný rok.")
