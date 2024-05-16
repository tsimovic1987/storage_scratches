import json




# Dictionary in eine JSON-Datei schreiben
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Dictionary aus einer JSON-Datei lesen
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

print(loaded_data)