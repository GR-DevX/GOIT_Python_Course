class A:
    def __init__(self):
        self.name=self.name.upper()

class B(A):
    def __init__(self,name):
        self.name=name
        super().__init__()

    def get_name(self):
        return self.name

if __name__ == '__main__':
    b=B('hello')
    print(b.get_name())
    