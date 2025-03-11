def secti(a, b):
    return a + b

def odecti(a, b):
    return a - b

def nasob(a, b):
    return a * b

def deleni(a, b):
    if b != 0:
        return a / b
    else:
        return "Chyba: dělení nulou!"

def kalkulacka():
    print("Vyberte operaci:")
    print("1. Sčítání")
    print("2. Odčítání")
    print("3. Násobení")
    print("4. Dělení")

    volba = input("Zadejte číslo operace (1/2/3/4): ")

    if volba in ['1', '2', '3', '4']:
        try:
            a = float(input("Zadejte první číslo: "))
            b = float(input("Zadejte druhé číslo: "))

            if volba == '1':
                print(f"Výsledek: {secti(a, b)}")
            elif volba == '2':
                print(f"Výsledek: {odecti(a, b)}")
            elif volba == '3':
                print(f"Výsledek: {nasob(a, b)}")
            elif volba == '4':
                print(f"Výsledek: {deleni(a, b)}")
        except ValueError:
            print("Chyba: prosím zadejte platná čísla.")
    else:
        print("Neplatná volba.")

kalkulacka()
