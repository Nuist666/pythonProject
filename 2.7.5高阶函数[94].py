# 过滤
def lt_5(x):
    return x < 5


numbers = [1, 3, 5, 6]
new_numbers = filter(lt_5, numbers)
print(new_numbers)
print(list(new_numbers))


# 等效于
def lt_5(x):
    return x < 5


numbers = [1, 3, 5, 6]
new_numbers = [n for n in numbers if lt_5(n)]
print(new_numbers)
