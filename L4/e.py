# прикласти cheat sheet
import re #regular expressions regex regexp

# s='1234+78998 7+++asd1234  ++ ++ 1234sdas 1231 123 123asdasd'
# pat1=r'\w+'
# # d - digit
# # + - 1 і більше
# res1=re.findall(pat1,s)
# res2=re.search(pat1,s)
# print(res1)
# print(res2.group())
# print(res2.span())
# s2='pi is 3.14 and it\'s a constant'\
#     ', .5 is also a constant but has no name'

# pat2=r'\d*\.\d+'
# print(re.findall(pat2,s2))

# mail="j.s_m_ith@stud.mail.com '; drop database; coll_11@10mituesmail.com"
# pat3=r'[\w\._]+@\w+\.\w+'
# clean_mail=re.match(pat3,mail).group()
# print(clean_mail)
# # pat3=r'^[\w\._]+@\w+\.\w+'
# pat3=r'[\w\.]+@\w+\.\w+$'
# clean=re.findall(pat3,mail)
# print(clean)

# phones='''+3806812345678
# +3806876543218
# +38(068)123-56-78'''
# pat=r'^\+\d{13}\s'
# res=[]
# for phone in phones.split('\n'):
#     print(phone)
#     found=re.findall(pat,phones)
#     print(found)
#     if found is not None:
#         res.extend(found)
# print(res)

# mails='''j.s_m_ith@stud.mail.com 
# '; drop database; 
# mail1@ukr.net
# mail2@i.ua
# coll_11@10mituesmail.com'''
# pat=r'([\w\._]+)@(\w+)\.(\w+)'
# print(re.findall(pat,mails))

# input=\
# '''
# l 123
# l 324
# r 1234
# r 234
# l 21
# r 123
# t 342
# l 234
# t 234
# '''
# pat=r'(?<=l\s)[\d]+' # Positive look behind  check,before,equal
# pat=r'(?<!l\s)[\d]+' # Negative look behind  check,before,Not equal
# pat=r'[a-z]+(?=\s234)' # Positive look ahead  check,equal
# pat=r'[a-z]+(?!\s234)' # Negative look ahead  check,notequal
input=\
'''name:john,lname:smith,mail:j.smith@mail.com,phone:+1234664654654
name:jane,lname:Roberton,mail:j.rob@mail.com,phone:+1235678648784
name:Steve,lname:friend,mail:andyourfriendsteve@mail.com,phone:+123867474
name:Snitch,lname:John,mail:j.snitch@mail.com,phone:+1234656789'''
# pat=r'(?<=name:)[A-Za-z]+'
# l1=re.findall(pat,input)
# print(l1)
# l1=l1[::2]
# print(l1)
# pat=r'[a-zA-Z]+'
# print(re.sub(pat,'',input))
# print(re.findall(pat,input))
print(re.split(r'[\n,:]',input))