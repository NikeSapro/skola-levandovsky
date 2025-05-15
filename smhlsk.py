text = input("Zadej text: ")
samohlasky = "aeiouáéěíóúůy"
pocet = 0
for znak in text.lower():
    if znak in samohlasky:
        pocet += 1
print("Počet samohlásek:", pocet)
