# 创建一个父类Animal以及子类Dog和Cat，通过继承创建衍生类的新功能
class Animal:
    def breathe(self):
        print('动物需要呼吸')


class Dog(Animal):
    def woof(self):
        print('汪汪汪')


class Cat(Animal):
    def meow(self):
        print('喵喵喵')


# 将Dog类和Cat类实例化
speike = Dog()
tom = Cat()
speike.breathe()
tom.breathe()
# Dog类和Cat类都继承自Animal类，它们都有breathe()方法
speike.woof()
tom.meow()
