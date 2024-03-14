# 初始化方法
class Student:
    def __init__(self, name, age, deposit):
        self.name = name
        self.age = age
        self.__deposit = deposit


xiaoming = Student('小明', 12, 1000)
print(xiaoming.name)
