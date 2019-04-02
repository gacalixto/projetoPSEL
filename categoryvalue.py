import json

def total_value(json_file):
    file =open("outtotalestoque.txt","w")
    values = {"Eletrodomésticos":0,
                "Eletrônicos":0,
                'Acessórios':0,
                'Panelas':0
          
          }
    data = json.load(json_file)
    for p in data:
        if p['category'] == "Eletrodomésticos":
            values["Eletrodomésticos"] += p['price'] * p['quantity']
        elif p['category'] == "Eletrônicos":
            values["Eletrônicos"] += p['price'] * p['quantity']
        elif p['category'] == "Acessórios":
            values["Acessórios"] += p['price'] * p['quantity']
        elif p['category'] == "Panelas":
            values["Panelas"] += p['price'] * p['quantity']




    file.write("Valor total do Estoque de eletrodomesticos: " +str(values["Eletrodomésticos"])+"\n")
    file.write("Valor total do Estoque de Eletrônicos: "+str(values["Eletrônicos"])+"\n")
    file.write("Valor total do Estoque de Acessórios: "+str(values["Acessórios"])+"\n")
    file.write("Valor total do Estoque de Panelas: "+ str(values["Panelas"])+"\n")
    file.close()




filename = "databasefinal.json"
with open(filename) as json_file:
    total_value(json_file)