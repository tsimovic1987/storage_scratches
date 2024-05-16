import json

artikel = input("Artikel: ")
nummer = input("Nummer: ")
menge = input("Menge: ")
lagerort = input("Lagerort: ")


data = {
    "artikel": artikel,
    "nummer": nummer,
    "menge": menge,
    "lagerort": lagerort
}


# Dictionary in eine JSON-Datei schreiben
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Dictionary aus einer JSON-Datei lesen
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

print(loaded_data)