def fact(n):
    if n==1: return 1
    return n*fact(n-1)

print(fact(5))
# n!=n*(n-1)*(n-2)*...*3*2*1