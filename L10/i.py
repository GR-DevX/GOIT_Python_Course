class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'
    
    def __str__(self):
        return f"Point with coordinates x={self.x}, y={self.y}"
    
if __name__ == '__main__':
    p = Point(x=1, y=2)
    print(repr(p)) # Point(1, 2)
    print(p)
    
    p2 = eval(repr(p)) # create the same object
    print(repr(p2)) # Point(1, 2)
    print(p2)

    s=str(p)
    print(s)
   
   