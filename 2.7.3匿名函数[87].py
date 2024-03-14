# 用lambda关键字定义匿名函数
func = lambda x: x ** 2
print(func(2))
# 或
greet = lambda: print('hello')
pos_ab = lambda a, b: print(a + b)
greet()
pos_ab(1, 2)
