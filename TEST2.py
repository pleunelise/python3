boodschappen = {"brood":2, "water":1, "sap":3}

prijs = 0
while prijs < 100:
    product = input("welk product wil je kopen?")
    if (product == 'm'):
        print("Totaal:", prijs, "euro")
        main()
        #main()
    if product in boodschappen:
        prijs += boodschappen[product]


