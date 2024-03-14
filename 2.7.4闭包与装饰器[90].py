# 创建一个新的函数say_hi()作为参数放进outer()函数
def outer(func):
    def inner():
        func()
        print("I'm inner func")

    print("I'm outer func")
    return inner


def say_hi():
    print('Hi!')


say_hi = outer(say_hi)
print('下面执行say_hi')
say_hi()
print('再次执行say_hi')
say_hi()
