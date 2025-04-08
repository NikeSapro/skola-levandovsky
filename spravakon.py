class Kontakt:
    def __init__(self, jmeno, telefon):
        self.jmeno = jmeno
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno}: {self.telefon}"

class SeznamKontaktu:
    def __init__(self):
        self.kontakty = []

    def pridej_kontakt(self, jmeno, telefon):
        kontakt = Kontakt(jmeno, telefon)
        self.kontakty.append(kontakt)

    def upravit_kontakt(self, jmeno, novy_telefon):
        for kontakt in self.kontakty:
            if kontakt.jmeno == jmeno:
                kontakt.telefon = novy_telefon
                print(f"Kontakt {jmeno} byl úspěšně upraven.")
                return
        print(f"Kontakt {jmeno} nenalezen.")

    def odstranit_kontakt(self, jmeno):
        for kontakt in self.kontakty:
            if kontakt.jmeno == jmeno:
                self.kontakty.remove(kontakt)
                print(f"Kontakt {jmeno} byl úspěšně odstraněn.")
                return
        print(f"Kontakt {jmeno} nenalezen.")

    def zobraz_kontakty(self):
        if not self.kontakty:
            print("Seznam kontaktů je prázdný.")
        else:
            print("Seznam kontaktů:")
            for kontakt in self.kontakty:
                print(kontakt)

def hlavni_program():
    seznam = SeznamKontaktu()

    while True:
        print("\n1. Přidat kontakt")
        print("2. Upravit kontakt")
        print("3. Odstranit kontakt")
        print("4. Zobrazit kontakty")
        print("5. Konec")
        
        volba = input("Vyberte akci (1-5): ")
        
        if volba == '1':
            jmeno = input("Zadejte jméno: ")
            telefon = input("Zadejte telefonní číslo: ")
            seznam.pridej_kontakt(jmeno, telefon)
        elif volba == '2':
            jmeno = input("Zadejte jméno kontaktu, který chcete upravit: ")
            novy_telefon = input("Zadejte nový telefonní číslo: ")
            seznam.upravit_kontakt(jmeno, novy_telefon)
        elif volba == '3':
            jmeno = input("Zadejte jméno kontaktu, který chcete odstranit: ")
            seznam.odstranit_kontakt(jmeno)
        elif volba == '4':
            seznam.zobraz_kontakty()
        elif volba == '5':
            print("Konec programu.")
            break
        else:
            print("Neplatná volba. Zkuste to znovu.")

# Spuštění hlavního programu
hlavni_program()
