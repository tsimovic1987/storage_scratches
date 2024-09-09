class Lagerbestand:
    def __init__(self, artikel, artikelnummer, lagermenge, lagerort):
        self.artikel = artikel
        self.artikelnummer = artikelnummer
        self.lagermenge = lagermenge
        self.lagerort = lagerort

    def to_dict(self):
        return {
            'Artikelbezeichnung': self.artikel,
            'Artikelnummer': self.artikelnummer,
            'Lagermenge': self.lagermenge,
            'Lagerort': self.lagerort
        }