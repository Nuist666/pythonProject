# 使用生成器来进行迭代
numbers = (i for i in range(3))
for i in numbers:
    print(i)
print('第一次迭代完成')
for i in numbers:
    print(i)
