class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    
    def setAge(self, age):
        if age < 18:
            self.__age = age
        else:
            raise ValueError("This student not allowed to take admission !")
        
    # Private methods are for internal use, can't be accessed outside.
    def __handicapped():
        print("This is a private method")
        

obj = Student('Raj', 22)
print(obj.age)
obj.setAge(15)
print(obj.age)
Student._Student__handicapped() # Not recommened way of accessing private method. 
#Python creating this _classname__methodname internally which is called mangling of classes.