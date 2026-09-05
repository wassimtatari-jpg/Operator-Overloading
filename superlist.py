class Superlist(list):
    def __init__(self, value):
        super().__init__(value)
    def __setitem__(self, key, value):
        if key>=len(self):
            super().append(value)
        elif key<0:
            super().insert(0,value)
        else:
            super().__setitem__(key,value)
my_list=Superlist([1,2,3,4])

my_list[5]=6
my_list[0]=0

my_list[10]=15

print(my_list)
        