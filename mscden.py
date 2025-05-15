mesic = int(input("Zadej číslo měsíce (1–12): "))
if mesic in [1, 3, 5, 7, 8, 10, 12]:
    print("31 dní")
elif mesic == 2:
    print("28 nebo 29 dní")
else:
    print("30 dní")
