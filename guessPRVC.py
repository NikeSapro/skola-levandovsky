n = int(input("Zadej číslo: "))
if n < 2:
    print("Není prvočíslo")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Není prvočíslo")
            break
    else:
        print("Je prvočíslo")
