class Bestand:
    def __init__(self, einkauf, produktion):
        self.einkauf = einkauf
        self.produktion = produktion
        pass
        
        
class Einkauf:
    def __init__(self, artikelbezeichnung: str, artikelnummer: str, artikelmenge: int) -> None:
        self.artikelbezeichnung = artikelbezeichnung
        self.artikelnummer = artikelnummer
        self.artikelmenge = artikelmenge
        pass
    
    
class Lager(Bestand):
    def __init__(self, lagerort: str, charge: int) -> None:
        self.lagerort = lagerort
        self.charge = charge
        pass
    
    
##### vorläufiges Programm #####

# Resourcenliste nach der geschaut wird und bestellt bzw. produziert wird #
# Die Liste besteht aus einer Artikelbeschreibung und einer Artikelnummer #

# Lösung 1: #

artikel = [("artikelbezeichnung"), ["artikelnummer", "menge"]]
print(artikel)
print(type(artikel))

artikelbezeichnung = input("artikelbezeichnung: ")
bestand = (artikelbezeichnung,)
print(type(bestand))
print(bestand)

artikelnummer = input("artikelnummer: "), input("menge: ")
artikelliste = [artikelnummer]
print(type(artikelnummer))
print(artikelnummer)
print(type(artikelliste))
print(artikelliste)

def entf(liste: list, entf_obj: str, int) -> None: # nochmal nachschauen ob die zeile wirklich valid ist!
    liste.remove(entf_obj)
