# мультимножинне мультирівневе наслідування
class A:
    def f(self):
        pass

class A1:
    pass
class B(A1,A):
    def f(self):
        ...

class C(A):
    pass

class D(B,C):
    pass
if __name__=='__main__':

    print(D.mro())  # method resolution order
                # порядое пошуку метода