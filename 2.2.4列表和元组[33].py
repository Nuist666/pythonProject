# 元组中元素不可增删和替换，并不代表元素对象不可以变化
tuple_hybrid = (1, 2, [])
print(tuple_hybrid)
print(tuple_hybrid[2])
tuple_hybrid[2].append('hello')
print(tuple_hybrid)
