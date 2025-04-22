# Jednoduchý to-do list v konzoli

todo_list = []

def zobraz_ukoly():
    if not todo_list:
        print("Žádné úkoly.")
    else:
        print("Tvoje úkoly:")
        for i, ukol in enumerate(todo_list, 1):
            print(f"{i}. {ukol}")

def pridej_ukol():
    ukol = input("Zadej nový úkol: ")
    todo_list.append(ukol)
    print("Úkol přidán.")

def smaz_ukol():
    zobraz_ukoly()
    try:
        cislo = int(input("Zadej číslo úkolu ke smazání: "))
        if 1 <= cislo <= len(todo_list):
            odstraneny = todo_list.pop(cislo - 1)
            print(f"Úkol '{odstraneny}' smazán.")
        else:
            print("Neplatné číslo.")
    except ValueError:
        print("Zadej platné číslo.")

def hlavni_menu():
    while True:
        print("\n1. Zobraz úkoly\n2. Přidej úkol\n3. Smaž úkol\n4. Konec")
        volba = input("Vyber akci: ")

        if volba == '1':
            zobraz_ukoly()
        elif volba == '2':
            pridej_ukol()
        elif volba == '3':
            smaz_ukol()
        elif volba == '4':
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba.")

hlavni_menu()
