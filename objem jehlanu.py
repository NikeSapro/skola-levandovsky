import random

def objem_ctyrbokeho_jehlanu(a, v):
    if a <= 0 or v <= 0:
        return "Strana a i výška v musí být kladná čísla."
    objem = (1/3) * (a ** 2) * v
    objem_zaokrouhleny = round(objem, 2)
    return f"Strana a = {a:.2f}, výška v = {v:.2f} → Objem jehlanu = {objem_zaokrouhleny} jednotek krychlových"

# Generování náhodných reálných čísel v rozsahu 1 až 20
a = random.uniform(1, 20)
v = random.uniform(1, 20)

vysledek = objem_ctyrbokeho_jehlanu(a, v)
print(vysledek)
