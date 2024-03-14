# 通过结合使用for...in语句与range()函数来代替while语句
i = 0
while i < 3:
    print('while重复3次')
    i = i + 1

for i in range(3):
    print('for重复3次')
