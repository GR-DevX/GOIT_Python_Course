import re

# text = "Python - потужна, універсальна;\\ мова!"
# pattern = r"[;,\-:!\.]"
# replacement = ""
# modified_text = re.sub(pattern, replacement, text)

# print(modified_text)  
s="HPg!g_283+ 0281"
pat=r'[\d\+]' # '[\d\+]+' '[\d\+\s]+'
res1=re.findall(pat,s)
print(res1)
res=''.join(res1)
print(res)