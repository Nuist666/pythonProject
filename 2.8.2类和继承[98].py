class Animal:
    def breathe(self):
        print('动物需要呼吸')


# 尝试创建一个Mouse类，用以覆盖父类的方法
class Mouse(Animal):
    def breathe(self):
        print('老鼠也需要呼吸')


jerry = Mouse()
jerry.breathe()
