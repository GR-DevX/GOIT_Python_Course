import csv,json

l=[]
with open('data0.tsv','r',newline="\n",encoding="utf-8") as f:
    reader=csv.DictReader(f,delimiter='\t',fieldnames=['name',"age","Speciality"])

    for row in reader:
        l.append(row)
print(l)
with open('data0.tsv.json','w',encoding="utf-8") as f:
    json.dump(l,f)