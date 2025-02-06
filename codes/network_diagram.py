import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Ellipse
import matplotlib.colors as mcolors
import numpy as np

# 创建一个空图
G = nx.Graph()

# 添加中心节点
central_node = "Cybercrime"
G.add_node(central_node)

# 添加其余节点
nodes = ["Politics", "Society", "Economy", "Technology", "Cybersecurity"]
G.add_nodes_from(nodes)

# 添加中心节点与其余节点的连线
for node in nodes:
    G.add_edge(central_node, node)

# 定义布局
pos = {
    "Cybercrime": (0, 0),
    "Politics": (0.6, 0.47), 
    "Society": (0.87, -0.33),
    "Economy": (-0.6, 0.47),
    "Technology": (-0.87, -0.33),
    "Cybersecurity": (0, -0.6)
}

# 绘制图形
plt.figure(figsize=(10, 6))
ax = plt.gca()

# 创建渐变颜色
def create_gradient_ellipse(ax, center, width, height, color1, color2, edge_color="black"):
    gradient = mcolors.LinearSegmentedColormap.from_list("gradient", [color1, color2])
    for i in range(100):
        color = gradient(i / 100)
        ellipse = Ellipse(center, width, height, color=color, alpha=1, zorder=1)
        ax.add_patch(ellipse)
    # 添加边框
    border = Ellipse(center, width, height, edgecolor=edge_color, facecolor="none", linewidth=1.5, zorder=2)
    ax.add_patch(border)

# 计算椭圆边缘上的点
def get_edge_point(center, width, height, angle):
    cx, cy = center
    angle_rad = np.deg2rad(angle)
    ex = cx + (width / 2) * np.cos(angle_rad)
    ey = cy + (height / 2) * np.sin(angle_rad)
    return ex, ey

# 绘制中心节点
cx, cy = pos[central_node]
create_gradient_ellipse(ax, (cx, cy), 0.6, 0.36, "darkred", "lightcoral")
plt.text(cx, cy, central_node, color="black", fontsize=12, fontweight="bold", ha="center", va="center", zorder=3)

# 绘制其他节点
node_ellipses = {}
for node in nodes:
    nx, ny = pos[node]
    create_gradient_ellipse(ax, (nx, ny), 0.6, 0.36, "deepskyblue", "lightblue")
    plt.text(nx, ny, node, color="black", fontsize=10, fontweight="bold", ha="center", va="center", zorder=3)
    node_ellipses[node] = (nx, ny, 0.6, 0.36)  # 存储椭圆的中心和尺寸

# 绘制边
for edge in G.edges():
    node1, node2 = edge
    x1, y1, w1, h1 = node_ellipses.get(node1, (cx, cy, 0.4, 0.24))
    x2, y2, w2, h2 = node_ellipses.get(node2, (cx, cy, 0.4, 0.24))

    # 计算连接椭圆边缘的点
    angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
    ex1, ey1 = get_edge_point((x1, y1), w1, h1, angle)
    ex2, ey2 = get_edge_point((x2, y2), w2, h2, angle + 180)

    plt.plot([ex1, ex2], [ey1, ey2], color="lightgray", linewidth=3, linestyle='--', alpha=0.7, zorder=0)

# 设置标题
plt.title("An Overview of Key Areas and Cybercrime Interconnections", fontsize=16, fontweight="bold", color="black")

# 调整图形
plt.axis("off")
plt.xlim(-1.8, 1.8)
plt.ylim(-1.0, 1.0)
plt.show()
