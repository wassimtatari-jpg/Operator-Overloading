class Numbers:
    def __init__(self,value):
        self.value=value
    def __add__(self, other):
        return self.value+other.value
    def __sub__(self, other):
        return self.value-other.value
    def __mul__(self, other):
        return self.value*other.value
    def __truediv__(self, other):
        return self.value/other.value
    def __floordiv__(self, other):
        return self.value//other.value
    def __mod__(self, other):
        return self.value%other.value
    def __pow__(self, other):
        return self.value**other.value
a=Numbers(100)
b=Numbers(20)

print(f"Total sum : {a+b}")
print(f"Total Subtraction : {a-b}")
print(f"Total Multiplication : {a*b}")
print(f"Total Division : {a/b}")
print(f"Total Floor Division : {a//b}")
print(f"Total Modulo : {a%b} ")
print(f"Total square : {a**b:.2f}")


