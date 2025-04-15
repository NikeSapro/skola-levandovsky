import random

postavy = ["kouzelník", "robot", "kočka", "pirát", "programátor", "drak"]
mista = ["v lese", "na Marsu", "v podzemí", "v opuštěném hradu", "na Měsíci"]
ukoly = ["našel poklad", "hacknul vládu", "zachránil svět", "ztratil se v čase", "vynalezl teleport", "zkrotil obřího medvěda"]
twisty = ["ale byl to jen sen", "a pak se všechno pokazilo", "a tím začala apokalypsa", "jenže to celé sledovali mimozemšťani", "a pak potkal sebe z budoucnosti"]

def vygeneruj_pribeh():
    postava = random.choice(postavy)
    misto = random.choice(mista)
    ukol = random.choice(ukoly)
    twist = random.choice(twisty)

    pribeh = f"Jednou {misto} žil {postava}, který {ukol}, {twist}."
    return pribeh

# Hlavní smyčka
print("✨ Generátor náhodných příběhů ✨\n")

while True:
    print(vygeneruj_pribeh())
    pokracovat = input("\nChceš další příběh? (a/n): ")
    if pokracovat.lower() != "a":
        print("Tak zase někdy! 📖")
        break
