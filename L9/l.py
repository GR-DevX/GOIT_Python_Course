# наслідування і декоратори

class A:
    @property
    def f(self):
        return 0
    
class B(A):
    def fg(self):
        return 1

if __name__=='__main__':

    b=B()
    print(b.f)