# 用break语句结束循环
names = ['Daming', 'Lili', 'Tom', 'Liming']
i = 0
while True:
    if i >= len(names):
        print('找不到Tom')
        break
    elif names[i] == 'Tom':
        print('找到Tom了')
        break
    print(names[i], '不是Tom')
    i = i + 1
print('Tom 所对应的索引是', i)
