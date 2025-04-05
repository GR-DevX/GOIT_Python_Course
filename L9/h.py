# поліморфізм
class A:
    def _f(self):
        print('a.f')
    def g(self):
        print('a.g')

class B(A):
    _f='test'


if __name__=='__main__':

    o=B()
    print(o._f)
    o.g()