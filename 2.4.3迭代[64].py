# 用continue语句跳过当前迭代
fruits = ['apple', 'orange', 'banana']
for fruit in fruits:
    if fruit == 'orange':
        continue
print(fruit)
