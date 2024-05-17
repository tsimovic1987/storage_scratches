def get_valid_input(prompt: str, validate_func, error_msg: str) -> str:
    while True:
        user_input = input(prompt)
        if validate_func(user_input):
            return user_input
        print(error_msg)

artikel = get_valid_input(
    "Welchen Artikel möchten Sie lagern? (max. 3 Zeichen): ",
    lambda x: len(x) <= 3,
    "Mehr als drei Zeichen sind nicht erlaubt."
)

nummer = get_valid_input(
    "Welche Artikelnummer? (4 Ziffern): ",
    lambda x: x.isdigit() and len(x) == 4,
    "Es müssen genau 4 Ziffern sein."
)

menge = get_valid_input(
    "Wieviel soll eingelagert werden? (max. 99.999): ",
    lambda x: x.isdigit() and len(x) <= 5,
    "Mehr als 99.999 Einträge sind nicht erlaubt."
)

lagerort = get_valid_input(
    "Welcher Lagerort? (1 - 4): ",
    lambda x: x.isdigit() and 1 <= int(x) <= 4,
    "Nur Lagerort 1 - 4 verfügbar."
)
lagerort = int(lagerort)  # Convert to integer after validation

artikel = artikel.upper()

item = {
    'Artikelbezeichnung': artikel,
    'Artikelnummer': nummer,
    'Lagermenge': menge,
    'Lagerort': lagerort
}