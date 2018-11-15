def gen():
    dict = {1: 1, 2: 4, 4: 16, 5: 25, 7: 49, 8: 64, 10: 100, 12:123, 13:1234, 15:255}
    getal = int(input("Voer een getal tussen de 1 en 16 in:"))
    if getal in dict.keys():
        print(True)
    else:
        print(False)
gen()
