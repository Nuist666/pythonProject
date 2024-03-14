# 如果元组只有一个元素，那么元素后面一定要带上逗号，否则赋值给变量的将是元素本身，而不是“装有”单一元素的元组
tuple_wrong = ('wrong')
print(type(tuple_wrong))
tuple_right = ('right',)
print(type(tuple_right))
