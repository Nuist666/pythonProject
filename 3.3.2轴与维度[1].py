# 一维至三维数组的创建
import numpy as np

vector = np.array([1, 2, 3])
matrix = np.array([[1, 2, 3], [4, 5, 6]])
tensor = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print('\n---向量---\n')
print(vector)  # 向量
print('\n---矩阵---\n')
print(matrix)  # 矩阵
print('\n---张量---\n')
print(tensor)  # 张量
