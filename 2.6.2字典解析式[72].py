# 通过字典解析式创建字典
mapping = {i: i ** 2 for i in range(10)}
print(mapping)
mapping = {i: i ** 2 for i in range(10) if i ** 2 > 40}
print(mapping)
