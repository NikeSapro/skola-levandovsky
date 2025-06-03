import random
import math

def objem_kuzelu(r, v):
    if r <= 0 or v <= 0:
        return "Poloměr i výška musí být kladná čísla."
    objem = (1/3) * math.pi * r**2 * v
    objem_zaokrouhleny = round(objem, 2)
    return f"Poloměr r = {r:.2f}, výška v = {v:.2f} → Objem kužele = {objem_zaokrouhleny} jednotek krychlových"

# Generování náhodných reálných čísel pro r a v (v rozsahu 1 až 20)
r = random.uniform(1, 20)
v = random.uniform(1, 20)

vysledek = objem_kuzelu(r, v)
print(vysledek)
