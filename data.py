# Interger Exception
def get_integer_input(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Nur Zahlen als Eingabe gültig")

# Artikelbezeichnung
while True:
    artikel = input("Welchen Artikel möchten Sie lagern? : ")
    if len(artikel) <= 3:
        break
    else:
        print("Mehr wie drei Zeichen sind nicht erlaubt.")

# Artikelnummer
while True:
    nummer = input("Welche Artikelnummer? : ")
    if nummer.isdigit() and len(nummer) == 4:
        break
    else:
        print("Es müssen genau 4 Ziffern sein.")

# Lagermenge
while True:
    menge = input("Wieviel soll eingelagert werden? : ")
    if menge.isdigit() and len(menge) <= 5:
        break
    else:
        print("Mehr wie 99.999 Einträge sind nicht erlaubt.")

# Lagerort
while True:
    lagerort = get_integer_input("Welcher Lagerort? (1 - 4) : ")
    if lagerort < 5:
        break
    else:
        print("Nur Lagerort 1 - 4 verfügbar.")

# Dictionary Data
item = {
    'Artikelbezeichnung': artikel,
    'Artikelnummer': nummer,
    'Lagermenge': menge,
    'Lagerort': lagerort
}

menge = menge.upper()