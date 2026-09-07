class Numbers:
    def __init__(self,a):
        self.a=a
    def __neg__(self):
        return -self.a
    def __pos__(self):
        return self.a
    def __abs__(self):
        return abs(self.a)

a=Numbers(-1)
print(-a)
print(+a)
print(abs(a))