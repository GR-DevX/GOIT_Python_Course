class A:
    counter=0
    def __init__(self):
        print("A.__init__")
    
    @staticmethod
    def static_method():
        print("A.static_method")
    
    @classmethod
    def class_method(cls):
        cls.counter+=1
        print(f"A.class_method, counter={cls.counter}")

    def obj_method(self):
        print("A.obj_method")

if __name__ == '__main__':
    A.static_method() # класу
    a=A()
    b=A()
    a.class_method()  # всіи об’єктам класу одночасно
    b.class_method()
    print(a.class_method)
    print(b.class_method)
    print(a.obj_method) # свій у кожного об’єкта класу
    print(b.obj_method)