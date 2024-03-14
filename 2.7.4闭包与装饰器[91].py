# 根据放进工厂函数的不同的变量，生产出有不同作用的函数
def factory(n):
    def multiply(m):
        return n * m

    return multiply


x2 = factory(2)
print(x2(2))
print(x2(3))
x10 = factory(10)
print(x10(2))
print(x10(3))
