# 对比列表解析式与传统for迭代方法
# 列表解析式
numbers = [(i, j) for i in range(2) for j in range(3)]
print(numbers)

# for迭代
numbers = []
for i in range(2):
    for j in range(3):
        numbers.append((i, j))
print(numbers)
