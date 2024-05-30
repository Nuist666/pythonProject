import cimiss
import numpy as np

# host 不带http前缀，通常为zero-ice服务的纯IP地址
client = cimiss.Query(user_id='myuserid', password='mypasswd', host='myhost')  # 请修改为你的账号、密码、IP地址
resp_array_2d = client.array_2d(
    interface_id="getSurfEleByTime",
    params={
        "dataCode": "SURF_CHN_MUL_HOR",
        "elements": "Station_ID_C,PRE_1h,PRS",
        "times": "20181224000000",
        "orderby": "Station_ID_C:ASC",
        "limitCnt": "3",
    },
    dtypes={'PRE_1h': np.float, 'PRS': np.float}
)
print(resp_array_2d)
