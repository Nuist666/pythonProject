# 同一个对象也可以被多个变量所指向
n = 1
m = n
print(m is n)
n = 2
print(m)
