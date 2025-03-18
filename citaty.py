import random

def nahodny_citat():
    citaty = [
        "Život není o čekání na to, až bouře přejde, ale o tom, jak se naučíme tancovat v dešti.",
        "Největší sláva v životě není v tom, že nikdy nepadneme, ale že se zvedneme pokaždé, když padneme.",
        "Úspěch není konečný, neúspěch není fatální: je to odvaha pokračovat, co se počítá.",
        "Nejlepším způsobem, jak předpovědět svou budoucnost, je vytvořit ji.",
        "Můžeš mít cokoli, co chceš, pokud tomu věnuješ dostatek času a úsilí."
    ]
    citat = random.choice(citaty)
    print(f"Náhodný citát: {citat}")

nahodny_citat()
