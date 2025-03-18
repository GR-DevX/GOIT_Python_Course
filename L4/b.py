s="Hello shiny world!"
# print(s.find('l'))

# start=s.find('l')+1  # 2+1=3
# print(s.find('l',start)) #3

# start=s.find('l',start)+1 # 3+1
# print(s.find('l',start)) #15

# print(s.rfind('l')) #15
# print(s.count('l'))
s="Hello shiny world!"
# print(s.find('x',5))
# print(s.index('x',5))
# try:
#     print(s.index('c',5))
# except Exception as e:
#     print('Not Found@!')
input='Snitch John j.snitch@mail.com +1234656789'
l1=input.split()

# print(l1)
input2='''john,smith,j.smith@mail.com,+1234664654654
jane,Roberton,j.rob@mail.com,+1235678648784
Steve,friend,andyourfriendsteve@mail.com,+123867474
Snitch,John,j.snitch@mail.com,+1234656789'''
input2=input2.split('\n')
print(input2)
for line in input2:
    words=line.split(',')
    for i in range(len(words)):
        words[i]=words[i].upper()
    print('\t'.join(words))
# csv_line=','.join(l1) # comma-separated value
# print(csv_line)
