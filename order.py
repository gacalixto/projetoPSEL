import json
from operator import itemgetter



def orderby_name_and_id(json_file):
        
    file = open("outorder.txt","w")
    data = json.load(json_file)
    list = sorted(data, key =itemgetter("category","id"))
    
    for p in list:
        file.write("Nome: "+p['name']+"\n")
    file.close()
       
filename = "databasefinal.json"
with open(filename) as json_file:
    orderby_name_and_id(json_file)