#boodschappen progamma
boodschappen = {"brood":2, "water":1, "sap":3}

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
    print("Om te stoppen, toets s")
    print_schermbreedte()
    ant = input("Toets het getal in dat je wilt uitvoeren:")

    while ant != 's':
        if (ant == '1'):
            if (len(boodschappen) < 0):
                print("Geen boodschappen beschikbaar")
            else:
                overzicht_producten()
        elif (ant == '2'):
            add_product()
        elif (ant == '3'):
            del_product()
        elif (ant == '4'):
            wijzig_product()
        elif (ant == '5'):
            winkelen()
        elif (ant == '6'):
            opslaan()
        else:
            print("ERROR")

def overzicht_producten():
    print_schermbreedte()
    for key in boodschappen:
        print("{key} : {value}".format(key=key, value=boodschappen[key]))


def add_product():
    print_schermbreedte()
    key = input("Naam product:")
    value = input("Prijs product:")
    boodschappen[key] = value

def del_product():
    print_schermbreedte()
    key = input("Welk product wil je verwijderen?")
    del boodschappen[key]

def wijzig_product():
    print_schermbreedte()
    key = input("Wat is de naam van het product?")
    newkey = input("Wat is de nieuwe naam van het product?")
    boodschappen[newkey] = boodschappen.pop(key)

def winkelen():
    print_schermbreedte()
    prijs = 0
    while prijs < 100:
        product = input("welk product wil je kopen?")
        if (product == 'm'):
            print("Totaal:", prijs, "euro")
        if product in boodschappen:
            prijs += boodschappen[product]

def opslaan():
    print_schermbreedte()
    f = open('producten.txt', 'w')
    f.write(str(boodschappen))
    f.close()

main()
