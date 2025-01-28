def accum(text):
    result = ""
    index = 0
    for znak in text:
        if result != "":
            result += "-"
        result += znak.upper()
        result += znak.lower() * index
        index += 1
    return result

print(accum("MrBandita"))