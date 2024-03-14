# 创建列表的普通方式
numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)
# 或
numbers = list(range(10))
print(numbers)
# 使用列表解析式创建
numbers = [i for i in range(10)]
print(numbers)
numbers = [i ** 2 for i in range(10)]
print(numbers)
numbers = ['hi' for i in range(10)]
print(numbers)
numbers = [i for i in range(10) if i % 2 != 0]
print(numbers)
