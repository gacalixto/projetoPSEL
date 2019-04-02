import json

def correct_prices(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    for p in data:
        for k,v in p.items():
            if k == 'price':
                p[k] = float(v)
             
    filename2 = "databaseprices.json"
    with open(filename2,'w') as outfile:
        json.dump(data,outfile,ensure_ascii= False,indent=4)

correct_prices('databasenames.json')