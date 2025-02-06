import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# 加载数据
csv_path = "cybercrime_rates_model_output.csv"  # 修改为实际文件路径
data = pd.read_csv(csv_path)

# 清理数据：去掉无效行并创建副本
cleaned_data = data.dropna().copy()  # 添加 .copy() 创建数据的副本

# 替换国家名称以匹配 Natural Earth 数据集
country_name_map = {
    "United States": "United States of America",
    "Korea, North": "North Korea",
    "Korea, South": "South Korea",
    "Iran ": "Iran",  # 修复多余空格
    # 添加更多映射（如需要）
}
cleaned_data.loc[:, 'country'] = cleaned_data['country'].replace(country_name_map)

# 检查和格式化国家名称
cleaned_data.loc[:, 'country'] = cleaned_data['country'].str.strip()

# 加载世界地图数据
shapefile_path = "ne_10m_admin_0_countries"
world = gpd.read_file(shapefile_path)

# 合并数据
world = world.merge(cleaned_data, how="left", left_on="ADMIN", right_on="country")

# 绘制分布图
def plot_success_rate(column, title, cmap="OrRd"):
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    world.boundary.plot(ax=ax, linewidth=0.5, color="grey")
    world.plot(column=column, ax=ax, legend=True, cmap=cmap,
               legend_kwds={"label": "Frustration rate", "orientation": "vertical", "shrink": 0.6},
               missing_kwds={"color": "lightgrey", "label": "No Data"})
    ax.set_title(title, fontsize=20, fontweight="bold", color="darkred")
    ax.axis("off")
    plt.tight_layout()
    plt.show()

# 按照 Success Rate 绘制地图
plot_success_rate("frustration_rate", "Cybercrimes Frustration rate Distribution", cmap="viridis")
