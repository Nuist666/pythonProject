# 混合使用位置参数和关键字参数
def pos_abc(a, b, c):
    print('a is', a)
    print('b is', b)
    print('c is', c)


pos_abc(1, c=5, b=3)
