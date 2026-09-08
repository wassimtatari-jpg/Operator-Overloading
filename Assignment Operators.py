class Numbers:
    def __init__(self,value):
        self.value=value
    def __iadd__(self, other):
        self.value+=other.value
        return self
    def __isub__(self, other):
        self.value-=other.value
        return self
    def __imul__(self, other):
        self.value*=other.value
        return self
    def __itruediv__(self, other):
        self.value/=other.value
        return self
    def __ifloordiv__(self, other):
        self.value//=other.value
        return self
    def __imod__(self, other):
        self.value%=other.value
        return self
    def __ipow__(self, other):
        self.value**=other.value
        return self
a=Numbers(100)
b=Numbers(25)
a+=b
print(f"Total add:{a.value}")
a-=b
print(f"Total Subtraction {a.value}")
a*=b
print(f"Total multiplication : {a.value}")
a/=b
print(f"Total division : {a.value}")
a//=b
print(f"Total Floor division {a.value}")
a%=b
print(f"Total Modulo {a.value}")
a**=b
print(f"Total Exponentiation: {a.value}")
        
        