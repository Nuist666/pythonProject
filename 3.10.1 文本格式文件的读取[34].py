# 读取没有列明的csv文件
import numpy as np

a = np.genfromtxt('save_csv.csv', delimiter=',')
print(a)
# 读取空格作为分隔符的文件
import numpy as np

a = np.genfromtxt('save_txt.txt', delimiter=' ')
print(a)
