import json

def correct_qts(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    for p in data:
        if 'quantity' in p:
            continue
        else:
            p['quantity'] = 0
             
    filename2 = "databasefinal.json"
    with open(filename2,'w') as outfile:
        json.dump(data,outfile,ensure_ascii= False,indent=4)

correct_qts('databaseprices.json')