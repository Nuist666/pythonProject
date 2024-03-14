# 用continue语句跳过当前循环
n = 1
n_sum = 0
while n < 10:
    if n % 2 == 0:
        n = n + 1
        continue
    print(n, '不是偶数')
    n_sum = n_sum + n
    n = n + 1
print(n_sum)
