class A:

    def sum(self,a,b):
        return a+b

class B(A):
    pass
    # def init_counter(self):
    #     self.sum=0

    # def count(self):
    #     self.sum+=1

    # def tell_count(self):
    #     print(self.sum)


if __name__=='__main__':

    b=B()
    print('count' in dir(b))
    print(b.sum(2,3))
    ...
    # b.init_counter()
    # for i in range(10):
    #     b.count()
    # b.tell_count()
    ...
    print(b.sum(4,5))