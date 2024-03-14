# 使用copy()方法复制一个新的字典对象
dict_ages = {'Daming': 21, 'Lili': 20}
dict_new = dict_ages.copy()
print(dict_new)
dict_ages['Tom'] = 25
print(dict_new)
print(dict_ages)
