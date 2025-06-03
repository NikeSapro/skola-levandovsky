import random

def reseni_linearni_rovnice(a, b):
    if a == 0:
        if b == 0:
            return f"Rovnice {a}x + {b} = 0 má nekonečně mnoho řešení."
        else:
            return f"Rovnice {a}x + {b} = 0 nemá žádné řešení."
    else:
        x = -b / a
        return f"Řešením rovnice {a}x + {b} = 0 je x = {x}"

# Generování náhodných reálných čísel pro a a b
a = random.uniform(-10, 10)
b = random.uniform(-10, 10)

vysledek = reseni_linearni_rovnice(a, b)
print(vysledek)
