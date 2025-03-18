def f():
    return 'f'
def g():
    return 'g'

def h(x):
    print(x())

h(g)
h(f)