# 没有return语句，则在函数执行结束之后自动返回None
def greet(clock):
    if clock < 12:
        return 'good morning'
    elif clock < 18:
        return 'good afternoon'
    elif clock < 21:
        return 'good evening'
    else:
        return 'good night'


greeting = greet(13)
print(greeting)


# 对比
def say_hi():
    print('Hi')


print(say_hi())
