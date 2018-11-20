#boodschappen progamma
boodschappen = {"brood":2, "water":1, "sap":3}

'''
print ("Start Len : %d" %  len(boodschappen))
boodschappen.clear()
print ("End Len : %d" %  len(boodschappen))
'''

def print_schermbreedte():
    schermbreedte = 50
    print("="* schermbreedte)

def main():
    print_schermbreedte()
    print("Bekijk producten, toets 1")
    print("Voeg producten toe, toets 2")
    print("Verwijder product, toets 3")
    print("Wijzig product, toets 4")
    print("Boodschappen doen, toets 5")
    print("Sla producten op, toets 6")
    print_schermbreedte()
    ant = input("Toets het getal dat je wilt uitvoeren:")

    if (ant == '1'):
        if (boodschappen == ''):
            print("Geen boodschappen beschikbaar")
        else:
            overzicht_producten()
    if (ant == '2'):
        add_product()
    if (ant == '3'):
        del_product()
    if (ant == '4'):
        wijzig_product()
    if (ant == '5'):
        winkelen()
    if (ant == '6'):
        opslaan()
    else:
        print("ERROR")

def overzicht_producten():
    print_schermbreedte()
    print(boodschappen.keys())
    print(boodschappen.values())
    main()

def add_product():
    print_schermbreedte()
    key = input("Naam product:")
    value = input("Prijs product:")
    boodschappen[key] = value
    main()

def del_product():
    print_schermbreedte()
    key = input("Welk product wil je verwijderen?")
    del boodschappen[key]
    main()

def wijzig_product():
    print_schermbreedte()
    key = input("Wat is de naam van het product?")
    newkey = input("Wat is de nieuwe naam van het product?")
    boodschappen[newkey] = boodschappen.pop(key)
    main()

def winkelen():
    print_schermbreedte()
    prijs = 0
    while prijs < 100:
        product = input("welk product wil je kopen?")
        if (product == 'm'):
            print("Totaal:", prijs, "euro")
            main()
            #main()
        if product in boodschappen:
            prijs += boodschappen[product]

def opslaan():
    print_schermbreedte()
    f = open('producten.txt', 'w')
    f.write(str(boodschappen))
    f.close()

main()
