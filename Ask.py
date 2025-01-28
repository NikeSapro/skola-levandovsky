name = input("What is your name? ")
age = int(input("How old are you? "))
city = input("What city do you live in? ")
message = f"Hello {name}, you are {age} years old and you live in {city}."
print(message)
if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor!")
