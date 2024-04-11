# 保存为csv文件
import numpy as np
a = np.array([[10.5, 13, 16.3],
            [12, 12.5, 15.5]])
np.savetxt('save_csv.csv', a, delimiter=',')
# 保存为空格作为分隔符的txt文件
import numpy as np
a = np.array([[10.5, 13, 16.3],
            [12, 12.5, 15.5]])
np.savetxt('save_txt.txt', a, delimiter=' ')