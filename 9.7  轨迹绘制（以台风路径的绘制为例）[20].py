import os
import pandas as pd
import numpy as np
from pathlib import Path
from typing import List
from typing import Union
from typing import Tuple
from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker


#读取CMA热带气旋最佳路径数据集
def reader(
        typhoon_txt: os.PathLike, code: Union[str, int]
) -> Tuple[List[str], pd.DataFrame]:
    typhoon_txt = Path(typhoon_txt)
    if isinstance(code, int):
        code = "{:04}".format(code)
    with open(typhoon_txt, "r") as txt_handle:
        while True:
            header = txt_handle.readline().split()
            if not header:
                raise ValueError(f"没有在文件里找到编号为{code}的台风的数据")
            if header[4].strip() == code:
                break
            [txt_handle.readline() for _ in range(int(header[2]))]
        data_path = pd.read_table(
            txt_handle,
            sep=r"\s+",
            header=None,
            names=["TIME", "I", "LAT", "LONG", "PRES", "WND", "OWD"],
            nrows=int(header[2]),
            dtype={
                "I": np.int64,
                "LAT": np.float32,
                "LONG": np.float32,
                "PRES": np.float32,
                "WND": np.float32,
                "OWD": np.float32,
            },
            parse_dates=True,
            date_parser=lambda x: pd.to_datetime(x, format=f"%Y%m%d%H"),
            index_col="TIME",
        )
        data_path["LAT"] = data_path["LAT"] / 10
        data_path["LONG"] = data_path["LONG"] / 10
        return header, data_path


#读取0608号台风的数据（数据为超6小时的占风相关信息）
head, dat = reader('CH2006BST.txt', '0608')
lat = dat.LAT
lon = dat.LONG
level = dat.I
pressure = dat.PRES
#创建Figure
fig = plt.figure(figsize=(15, 12))
#绘制台风路径
ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.PlateCarree())
#设置ax1的范围
ax1.set_extent([100, 160, -10, 40])
#为ax1添加海岸线
#ax1.coastlines()
#ax1.add_feature(cfeature.LAND) #添加大陆特征
#为ax1添加地理经纬度标签及刻度
ax1.set_xticks(np.arange(100, 170, 10), crs=ccrs.PlateCarree())
ax1.set_yticks(np.arange(-10, 50, 10), crs=ccrs.PlateCarree())
ax1.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax1.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#绘制台风路径，并将标记逐6小时坐标点及其对应的台风强度
ax1.plot(lon, lat, linewidth=2)
s1 = ax1.scatter(lon, lat, c=pressure, s=(level + 1) * 13, cmap='Reds_r', vmax=1050, vmin=900, alpha=1)
fig.colorbar(s1, ax=ax1, fraction=0.04)
#绘制台风路径
ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.PlateCarree())
#设置ax2的范围
ax2.set_extent([100, 160, -10, 40])
#为ax2添加海岸线
#ax2.coastlines()
#ax2.add_feature(cfeature.LAND) #添加大陆特征
#为ax2添加地理经纬度标签及刻度
ax2.set_xticks(np.arange(100, 170, 10), crs=ccrs.PlateCarree())
ax2.set_yticks(np.arange(-10, 50, 10), crs=ccrs.PlateCarree())
ax2.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax2.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#将经纬度数据存入同一数组
points = np.array([lon, lat]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
#设置色标的标准化范围(即将Z维度的数据对应为颜色数组，Z维度指dat.WND[-1])
norm = plt.Normalize(0, 80)
#设置颜色线条
lc = LineCollection(segments, cmap='jet', norm=norm, transform=ccrs.PlateCarree())
lc.set_array(dat.WND[:-1])
#绘制线条
line = ax2.add_collection(lc)
fig.colorbar(lc, ax=ax2, fraction=0.04)
plt.show()
