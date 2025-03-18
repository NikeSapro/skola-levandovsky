import random

def hrat_hru():
    print("Vítejte v hře Hádej číslo!")
    print("Myslím si číslo mezi 1 a 100. Zkuste ho uhodnout.")
    
    tajne_cislo = random.randint(1, 100)
    pokusy = 0
    
    while True:
        try:
            tip = int(input("Zadejte svůj tip: "))
            pokusy += 1
            if tip < tajne_cislo:
                print("Příliš nízké, zkuste znovu!")
            elif tip > tajne_cislo:
                print("Příliš vysoké, zkuste znovu!")
            else:
                print(f"Gratuluji! Uhodli jste číslo {tajne_cislo} za {pokusy} pokusů.")
                break
        except ValueError:
            print("Prosím zadejte platné číslo.")

hrat_hru()
