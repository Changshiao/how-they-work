import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# 加载 CSV 数据
csv_path = "network_vulnerability_ratio_summary.csv"  # 输入的 CSV 文件路径
attack_data = pd.read_csv(csv_path, index_col=0)

# 将行名设置为国家名
attack_data.index.name = "name"

# 加载世界地图数据
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# 合并地图数据和攻击数据
world = world.merge(attack_data, on="name", how="left")

# 可视化功能，选择要绘制的列
def plot_world_map(column, title, cmap="YlOrRd"):
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    world.boundary.plot(ax=ax, linewidth=1, color="black")
    world.plot(column=column, ax=ax, legend=True, cmap=cmap, 
               missing_kwds={"color": "lightgrey", "label": "No Data"})
    ax.set_title(title, fontsize=16)
    ax.axis("off")
    plt.show()

# 示例：绘制易受攻击比值的地图
plot_world_map("vulnerability_ratio", "Vulnerability Ratio by Country")
