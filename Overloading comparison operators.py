class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __eq__(self, other):
        if isinstance(other,Person):
            return self.age==other.age
        return False
    def __lt__(self, other):
        if isinstance(other,Person):
            return self.age<other.age
        return False
person1=Person("alice",55)
person2=Person("Wassim",39)
person3=Person("Yassmine",13)

print(person1==person2)
print(person1<person3)
        
        