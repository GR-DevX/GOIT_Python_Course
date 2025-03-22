# Замикання
def power(b):
    def inner_power(a):
        return a**b # return a**2 a**3
    return inner_power

#b:
f=power(2)
#f=(def inner_power(...)....)
g=power(3)
print()
#a:
print(f(2))
print(g(2))
print(g(3))