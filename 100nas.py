cislo = int(input("Zadej číslo: "))
for i in range(1, 101):
    if i % cislo == 0:
        print(i)
