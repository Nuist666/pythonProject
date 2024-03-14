dict_hours = {
   'hour': 1,
   'day': 24,
   'week': 168
}
# 测试键是否存在
print('month' in dict_hours)
print(dict_hours.get('week'))
print(dict_hours.get('month'))
print(dict_hours.get('month', 'no month'))
