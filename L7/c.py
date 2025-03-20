from collections import defaultdict
s='some text is long, some is short, but long and short are not some'
# OLD SLOW AND BORING WAY
# d={}
# for c in s:
#     if c not in d.keys():   <<<<<
#         d[c]=0              <<<<<
#     d[c]+=1
d=defaultdict(int) 
for c in s:
    #d[c].append(c)
    d[c]+=1
# d['qwerty']=[1,2,3,'a','b']
for k in d:
    print(f"{k}:{d[k]}")