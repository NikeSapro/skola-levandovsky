minuty = int(input("Zadej počet minut od půlnoci: "))
hodiny = minuty // 60
zbytek = minuty % 60
print(f"{hodiny:02d}:{zbytek:02d}")
