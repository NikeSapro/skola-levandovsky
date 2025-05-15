minuty = int(input("Zadej počet minut: "))
hodiny = minuty // 60
zbytek = minuty % 60
print(f"{hodiny} h a {zbytek} min")
