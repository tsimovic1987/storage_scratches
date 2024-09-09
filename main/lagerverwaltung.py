import csv
from lagerbestand import Lagerbestand
from main import get_valid_input



class Lagerverwaltung:
    def __init__(self, csv_file="data.csv"):
        self.csv_file = csv_file
        self.fieldnames = ['Artikelbezeichnung', 'Artikelnummer', 'Lagermenge', 'Lagerort']

    def speichern(self, bestand: Lagerbestand):
        with open(self.csv_file, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)

            if file.tell() == 0:
                writer.writeheader()

            writer.writerow(bestand.to_dict())

    def eingabe(self):
        artikel = get_valid_input(
            "Welchen Artikel möchten Sie lagern? (max. 3 Zeichen): ",
            lambda x: len(x) <= 3,
            "Mehr als drei Zeichen sind nicht erlaubt."
        )
        artikel = artikel.upper()
        nummer = get_valid_input(
            "Welche Artikelnummer? (4 Ziffern): ",
            lambda x: x.isdigit() and len(x) == 4,
            "Es müssen genau 4 Ziffern sein."
        )
        menge = get_valid_input(
            "Wieviel soll eingelagert werden? (max. 99.999): ",
            lambda x: x.isdigit() and len(x) <= 5,
            "Nur Ziffern sind erlaubt. Mehr als 99.999 Einträge sind nicht erlaubt."
        )
        lagerort = get_valid_input(
            "Welcher Lagerort? (1 - 4): ",
            lambda x: x.isdigit() and 1 <= int(x) <= 4,
            "Nur Lagerort 1 - 4 verfügbar."
        )
        lagerort = int(lagerort)

        bestand = Lagerbestand(artikel, nummer, menge, lagerort)
        self.speichern(bestand)

        weitermachen = input("Möchten Sie einen weiteren Eintrag hinzufügen? (j/n): ")
        return weitermachen.lower() == 'j'