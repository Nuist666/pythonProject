class Student:
    def __init__(self, name, age, deposit):
        self.name = name
        self.age = age
        self.__deposit = deposit

    def do_homework(self):
        # 做作业
        answer = self.__calculate(1, 1)
        print('做完作业了，答案是', answer)

    def wash_dishes(self, n_dishes):
        # 洗碗
        self.__deposit = self.__deposit + n_dishes * 10
        print('洗过碗了，又赚', n_dishes * 10, '元，现在有', self.__deposit)

    def __calculate(self, a, b):
        # 珠心算
        print('悄悄算算术，不告诉别人')
        return a + b


xiaoming = Student('小明', 12, 1000)
xiaoming.do_homework()
xiaoming.wash_dishes(1)
xiaoming.wash_dishes(5)
xiaoming.wash_dishes(3)
