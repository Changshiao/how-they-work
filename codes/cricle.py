import matplotlib.pyplot as plt
import networkx as nx

# 数据定义
central_node = "F"
groups = {
    "A": ["a", "b", "c"],
    "B": ["d", "e", "f"],
    "C": ["g", "h"],
    "D": ["i", "j"],
    "E": ["k"],
}

# 初始化图
G = nx.DiGraph()

# 添加中心节点
G.add_node(central_node, layer=0)

# 添加每个组和其子节点
for group, sub_nodes in groups.items():
    G.add_node(group, layer=1)
    G.add_edge(group, central_node)  # 从组指向中心节点
    for sub_node in sub_nodes:
        G.add_node(sub_node, layer=2)
        G.add_edge(sub_node, group)  # 从子节点指向组

# 布局设置
pos = nx.shell_layout(G, nlist=[
    [central_node],  # 中心节点
    list(groups.keys()),  # 第一层（A, B, C, D, E）
    sum(groups.values(), []),  # 第二层（子节点）
])

# 绘制图形
plt.figure(figsize=(10, 10))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700, alpha=0.9)
nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.7, arrowsize=10)
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black', font_family='sans-serif')

# 标题和布局
plt.title("Radial Diagram Representing Relationships", fontsize=14)
plt.axis('off')
plt.show()
