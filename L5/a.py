# Bad Way
# f1=open('test.txt','w')
# f1.write('some\nfunny\ntext')
# f1.close()

# Python Way
# with open('test.txt','w') as f1:
#     f1.write('some\nfunny\ntext')
# with open('L5\\a.py','r') as f2:
#     text=[line.rstrip() for line in f2.readlines()]
#     for line in text:
#         print(line)
# w - Write     - (пере)створює і записує
# r - Read      - читає
# a - Append    - дописує
# b - Binary    - двійковий режим
# t - Text      - текстовий режи (зазвичай не вказують, використовується за промовчанням)
# + - Additional -  Відкриває для читання та запису (ADD)
# x - eXclusive - створює файл і відкриває на запис, якщо файл існнував - Exception!!!


# with open('test.txt','w+') as f1:      # w+ - може створити, стирає все і ставить курсор в кінець файлу
                                         # r+ - не створює, не стирає і ставить курсор в початок
                                         # a+ - створює, не стирає і ставить курсор в кінець
#     f1.write('some anoth\nfunny an joyfull\nvery big text')
#     print(f1.tell())
#     f1.seek(f1.tell()-4)
#     f1.write('book')
#     f1.seek(0)
#     print(f1.tell())
#     print(f1.read())
#     print(f1.tell())

# with open('test.txt','r+') as f1:
#     f1.write('some anoth\n   funny an joyfull\nvery big text')
#     f1.seek(0)
#     buf=None
#     while buf!='':  # while not eof(f1)
        # buf=f1.read(5)
        # buf=f1.readline().rstrip()
        # print(f"|{buf}|")
def process(x):
    # do nothing
    pass

# with open('test.txt','r+') as f1:
#     f1.write('some anoth\n   funny an joyfull\nvery big text')
#     f1.seek(0)
#     # NOT GOOD
#     text=f1.read()
#     lines=text.split('\n')
#     words=[line.split(' ') for line in lines ]
#     process(words)
#     print(words)
#     # GOOD
#     f1.seek(0)
#     buf=None
#     words=[]
#     while buf!='':  # while not eof(f1)
#         buf=f1.readline()
#         buf_l=buf.rstrip().split()
#         process(buf_l)  # 1
#         words.append(buf_l) #2
                                # або 1, або2, або і 1, і 2
#         #print(f"|{buf_l}|")
#     print(words)
