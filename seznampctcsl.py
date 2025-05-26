seznam = [5, 12, 7, 20, 3, 9]
mez = int(input("Zadej mezní hodnotu: "))
vetsi = [x for x in seznam if x > mez]
print("Čísla větší než", mez, "jsou:", vetsi)
