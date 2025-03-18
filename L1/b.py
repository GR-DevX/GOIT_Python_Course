a=0
b='positive' if a>0 else 'not positive'
b='positive' if a>0 else ('negative' if a<0 else "zero")
print("a is", b)