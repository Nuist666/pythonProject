# 对于特殊格式的时间字符串的解析
import pandas as pd

a = pd.to_datetime(['2020年02月28日', '2020年03月28日'], format='%Y年%m月%d日')
b = pd.to_datetime(['202002(28)', '202003(28)'], format='%Y%m(%d)')
c = pd.to_datetime(['20200228(1200)', '20200328(1200)'], format='%Y%m%d(%H%M)')
print(a)
print(b)
print(c)
