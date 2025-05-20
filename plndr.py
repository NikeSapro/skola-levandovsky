text = input("Zadej slovo: ")
if text == text[::-1]:
    print("Je to palindrom.")
else:
    print("Není to palindrom.")
