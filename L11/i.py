import csv
l=[]
with open('data0.tsv', 'r', newline="\n", encoding='utf-8') as f:
    reader=csv.reader(f,delimiter='\t')
    for row in reader:
        l.append(row)
print(l)