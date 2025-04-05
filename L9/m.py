from l import A
class C(A):
    pass



if __name__=='__main__':
    print(C.mro())
    print(dir(C))
    print(C().f)