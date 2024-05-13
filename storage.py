import json

def write_list(a_list):
    print('saving data to json file')
    with open("storage.json", "w") as fp:
        json.dump(a_list, fp)
        print('data saved!')

def read_list(jsonname):
    # for reading also binary mode is important
    with open(jsonname, 'rb') as fp:
        storage_list = json.load(fp)
        return storage_list

artikel = input("Artikel: ")
nummer = input("Nummer: ")
menge = input("Menge: ")
lagerort = input("Lagerort: ")

storage = []
item = {
    "artikel": artikel,
    "nummer": nummer,
    "menge": menge,
    "lagerort": lagerort
}
storage.append(item)
write_list(storage)
read_list("storage.json")