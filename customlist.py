class Customlist:
    def __init__(self,data):
        self.data=data
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key]=value
    def __delitem__(self, key):
        del self.data[key]
    def __repr__(self):
        return repr(self.data)
my_list=Customlist([1,2,3,4,5,6])

print(my_list[1])

my_list[0]=10
print(my_list)

del my_list[4]
print(my_list)
        