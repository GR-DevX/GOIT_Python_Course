# s='   some nice text   '
# l1=['John   ',' Smith  ','  coolmail@mail.com   ', '+65846546531  ']
# l2=[]
# print('|',end='')
# print(s.rstrip(),end='')
# print('|')
# for el in l1:
#     l2.append(el.rstrip())
# print(l2)

# s='   some nice text nice nice   '
# s1=s.replace('nice','cool',1)
# s2=s.replace(' nice','')
# s3='cool'.join(s.split('nice'))
# print(s1)
# print(s2)
# print(s3)
# print(s)
s='some nice text'
s1='cool nice text'
s2='some nice texts'
# print(s.removeprefix('some '))
# print(s1.removeprefix('some '))
# print(s2.removeprefix('some '))

# print(s.removesuffix('text'))
# print(s1.removesuffix('text'))
# print(s2.removesuffix('text'))

# l=['1','2','n=2', 'n=3']
# for el in l:
#     print(el.removeprefix('n='))

orig='somenictxlg'
trans='50m3n1ctx16'
s='some nice text'
s1='cool nice text'
s2='some nice texts'
trans_tab=str.maketrans(orig,trans)
print('scanning...'.translate(trans_tab))