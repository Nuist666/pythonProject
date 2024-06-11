import matplotlib.pyplot as plt
from shapely.ops import unary_union
import geopandas as gpd
import cartopy.crs as ccrs
# 读取GeoJSON文件
gdf = gpd.GeoDataFrame.from_file('circle.json', encoding='utf8') #也可以是shapefile
# 合并多边形
geom = unary_union([geom if geom.is_valid else geom.buffer(0) for geom in gdf['geometry']])

print(type(gdf['geometry']), len(gdf['geometry']))
print(type(geom))

# 将合并后的几何对象转换为GeoDataFrame
merged_gdf = gpd.GeoDataFrame(geometry=[geom], crs=gdf.crs)

# 绘制多边形
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': ccrs.PlateCarree()})
merged_gdf.plot(ax=ax, facecolor='blue', edgecolor='black')
plt.show()