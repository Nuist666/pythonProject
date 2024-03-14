# 将代码改写为装饰器的形式
def outer(func):
    def inner():
        func()
        print("I'm inner func")

    print("I'm outer func")
    return inner


@outer
def say_hi():
    print('Hi!')


print('下面执行say_hi')
say_hi()
print('再次执行say_hi')
say_hi()
