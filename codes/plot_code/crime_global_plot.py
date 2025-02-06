import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
import numpy as np

# 加载 CSV 数据
csv_path = "data\word_cybercrime_ranking&analysise.csv"  # 确保这个文件存在于正确的路径
try:
    attack_data = pd.read_csv(csv_path, index_col=0)
except FileNotFoundError:
    print(f"错误：找不到文件 '{csv_path}'")
    print("请确保文件路径正确且文件存在")
    exit(1)

# 将行名设置为国家名
attack_data.index.name = "iso_a2"  # 将国家名称调整为 ISO Alpha-2 格式

# 加载本地的世界地图数据
shapefile_path = "ne_10m_admin_0_countries"  # 将路径替换为实际文件路径
try:
    world = gpd.read_file(shapefile_path)
except Exception as e:
    print(f"错误：无法加载地图文件 '{shapefile_path}'")
    print(f"详细错误信息：{e}")
    exit(1)

# 确保地图数据使用 ISO Alpha-2 格式的国家代码
if "ISO_A2" in world.columns:  # 检查数据中是否有 Alpha-2 格式的列
    world = world.rename(columns={"ISO_A2": "iso_a2"})  # 将列名重命名为 'iso_a2'

# 合并地图数据和攻击数据
world = world.merge(attack_data, on="iso_a2", how="left")

# 对数据进行颜色映射处理，增加特定分段
def custom_color_mapping(column_data):
    bins = np.array([0, 20, 50, 75, 100])  # 自定义分段，20到50之间增加一段
    cmap = plt.cm.OrRd  # 使用 OrRd 颜色映射
    norm = BoundaryNorm(bins, cmap.N, extend="max")
    return cmap, norm

# 可视化功能，选择要绘制的列
def plot_world_map(column, title, cmap="OrRd"):
    column_data = world[column]
    cmap, norm = custom_color_mapping(column_data)

    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    world.boundary.plot(ax=ax, linewidth=0.5, color="gray")
    world.plot(column=column, ax=ax, legend=True, cmap=cmap, norm=norm,
               legend_kwds={"label": title, "orientation": "vertical", "shrink": 0.6},
               missing_kwds={"color": "lightgrey", "label": "No Data"})
    ax.set_title(title, fontsize=20, fontweight="bold", color="darkred")
    ax.axis("off")
    plt.tight_layout()
    plt.show()

# 示例：绘制易受攻击比值的地图
plot_world_map("Total", "Global Distribution of Cybercrime", cmap="OrRd")
