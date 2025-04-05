#CSV - comma separated value  ,s
#TSV - tab separated value   \t
import csv

rows=[
    ['name',"age","Speciality"],
    ['Jason Statham',40,"Mechanic"],
    ['Neo 1234343dsd',35,"Developer"],
    ['Galileo',102,"Atrophysicist"],
]

with open('data0.csv',"w", newline='\n', encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerows(rows)
# outrows=[]
# for row in rows:
#     outrows.append(','.join([str(n) for n in row]))

# print(outrows)
# with open('data1.csv',"w", newline='\n', encoding="utf-8") as f:
#         f.write('\n'.join(outrows))
