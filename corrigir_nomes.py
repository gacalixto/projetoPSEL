import json

def correct_name(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    for p in data:
        for letter in p['name']:
            if letter == 'æ':
                p['name'] = p['name'].replace(letter,'a')
            elif letter == '¢':
                p['name'] = p['name'].replace(letter,'c')
            elif letter == 'ø':
                p['name'] = p['name'].replace(letter,'o')
            elif letter == 'ß':
                p['name'] = p['name'].replace(letter,'b')
    
    filename2 = "databasenames.json"
    with open(filename2,'w') as outfile:
        json.dump(data,outfile,ensure_ascii= False,indent=4)


correct_name("broken-database.json")



    