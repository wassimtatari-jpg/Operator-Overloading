class Numbers:
    def __init__(self,value):
        self.value=value
    def __add__(self, other):
        return self.value+other.value

a=Numbers(10)
b=Numbers(2)

print(f"Total :  {a+b}")
