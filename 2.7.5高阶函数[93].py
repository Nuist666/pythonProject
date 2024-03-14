# 映射
def plus2(x):
    return x + 2


numbers = [1, 3, 5, 6]
new_numbers = map(plus2, numbers)
print(new_numbers)
print(list(new_numbers))


# 等效于
def plus2(x):
    return x + 2


numbers = [1, 3, 5, 6]
new_numbers = [plus2(n) for n in numbers]
print(new_numbers)
# 用匿名函数来实现
numbers = [1, 3, 5, 6]
new_numbers = map(lambda x: x + 2, numbers)
print(new_numbers)
print(list(new_numbers))
