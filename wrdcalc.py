a = float(input("První číslo: "))
b = float(input("Druhé číslo: "))
operace = input("Operace (+, -, *, /): ")

if operace == "+":
    print(a + b)
elif operace == "-":
    print(a - b)
elif operace == "*":
    print(a * b)
elif operace == "/":
    print(a / b)
else:
    print("Neznámá operace.")
