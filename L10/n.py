class myint(int):
    def __init__(self, value):
        self.value=int(value)

    # def __add__(me, not_me):
    #     return myint(str(me)+str(not_me))
    
    def __add__(me, not_me):
        return myint(int(me)+int(not_me))
    

if __name__ == '__main__':
    a=myint(5)
    b=myint(10)
    print(a+b+5+'5')
    print(myint(5)+'5')
    