# sum=10 # G - Global 
def f():
    
    def g():
        sum=30 # L - Local
        print(sum)
    sum=20 # E - Enclosing
    g()
f()
print(sum) # B - Built-in