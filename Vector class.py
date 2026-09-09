class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        result=Vector(self.x+other.x,self.y+other.y)
        return result
    def __sub__(self, other):
        result=Vector(self.x-other.x,self.y-other.y)
        return result
    def __mul__ (self, other):
        result=Vector(self.x*other,self.y*other)
        return result
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    def __ne__(self, other):
        return self.x!=other.x or self.y!=other.y
        
    def __neg__(self):
        result=Vector(-self.x,-self.y)
        return result
    def __abs__(self):
        result=Vector(abs(self.x),abs(self.y))
        return result
    def __getitem__(self, key):
        if key==0:
            return self.x
        elif key==1:
            return self.y
        else:
            raise IndexError("Vector Indexing out of range")        
    def __repr__(self):
        return f"Vectors A :{self.x}, B:{self.y}"


v1=Vector(50,25)
v2=Vector(25,15)
print(f"Total Add :{v1+v2}")
print(f"Total sub : {v1-v2}")
print(f"Total v1*2 is {v1*2}")
print(f"Check is equal {v1==v2}")
print(f"Check is not equal {v1!=v2}")
print(-v1,-v2)
print(abs(v1))
print(abs(v2))
print(v1[0])
print(v1[1])

