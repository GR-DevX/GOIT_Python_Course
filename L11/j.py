import csv

l=[{'name':'Jason Statham','age':40,"Speciality":'Mechanic'},
{'name':'Neo 1,34343dsd','age':35,"Speciality":'Developer'},
{'name':'Galileo','age':102,"Speciality":'Atrophysicist'}]

with open('data2.csv','w',newline="\n",encoding="utf-8") as f:
    fieldnames = list(l[0].keys())
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    
    writer.writeheader()
    for human in l:
        writer.writerow(human)