# Сеттири, геттери, делеттери
class Some:
    def __init__(self):
        self.__f=None

    @property
    def file(self):
        return self.__f
    
    @file.setter
    def file(self,filename):
        self.__f=open(filename,'w')

    @file.deleter
    def file(self):
        self.__f.close()

if __name__=='__main__':
    o=Some()
    o.file='OOP.txt'
    o.file.write('OOP TEST')
    del o.file