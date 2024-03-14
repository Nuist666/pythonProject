# 字典的赋值与复制
dict_ages = {'Daming': 21, 'Lili': 20}
dict_new = dict_ages
print(dict_new)
dict_ages['Tom'] = 25
print(dict_new)
print(dict_ages)
