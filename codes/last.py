import matplotlib.pyplot as plt
import networkx as nx

# 创建一个空的有向图
G = nx.DiGraph()

# 第一列 e1 到 e25
e_nodes = [f"e{i}" for i in range(1, 26)]

# 第二列 α1 到 α25
alpha_nodes = [f"α{i}" for i in range(1, 26)]

# 第三列的五个元素
third_col_nodes = ['Policy', 'Society', 'Economy', 'Technology', 'Cybersecurity']

# 向图中添加节点
G.add_nodes_from(e_nodes)
G.add_nodes_from(alpha_nodes)
G.add_nodes_from(third_col_nodes)

# 添加从第一列到第二列的箭头
for i in range(25):
    G.add_edge(e_nodes[i], alpha_nodes[i])

# 添加从第三列到第二列的箭头
for i, col in enumerate(third_col_nodes):
    start_idx = i * 5
    end_idx = start_idx + 5
    for j in range(start_idx, end_idx):
        G.add_edge(col, alpha_nodes[j])

# 添加从第三列指向 Cybercrime 的箭头
for col in third_col_nodes:
    G.add_edge(col, "Cybercrime")

# 添加单向箭头连接 'Policy', 'Society', 'Economy', 'Technology', 'Cybersecurity' 之间
for i in range(len(third_col_nodes) - 1):
    for j in range(i + 1, len(third_col_nodes)):
        G.add_edge(third_col_nodes[i], third_col_nodes[j])  # 只添加一个方向的边

# 设置图形布局
pos = {}
# 为每一列定义不同的位置
for i, node in enumerate(e_nodes):
    pos[node] = (-1.9, -i)
for i, node in enumerate(alpha_nodes):
    pos[node] = (-1.5, -i)
for i, node in enumerate(third_col_nodes):
    pos[node] = (1, -2 - i * 5)  # Adjusted to move third column nodes to the right
# 为 Cybercrime 节点定义位置
pos["Cybercrime"] = (4, -12)  # 给 Cybercrime 节点定义一个位置

# 绘制图形
plt.figure(figsize=(12, 12))

# 使用不同的节点样式进行绘制
node_shapes = {'circle': [], 's': [], 'p': []}  # 's' 为方形, 'p' 为椭圆形
for node in G.nodes():
    if node in e_nodes:
        node_shapes['circle'].append(node)  # 第一列使用圆形
    elif node in alpha_nodes:
        node_shapes['s'].append(node)  # 第二列使用圆角矩形（s表示方形）
    elif node in third_col_nodes:
        node_shapes['p'].append(node)  # 第三列使用椭圆形（p表示星形）
    else:
        node_shapes['circle'].append(node)

# 绘制圆形节点（第一列）
nx.draw_networkx_nodes(G, pos, nodelist=node_shapes['circle'], node_size=200, node_color='#55B7E6', node_shape='o')

# 绘制方形节点（第二列）
nx.draw_networkx_nodes(G, pos, nodelist=node_shapes['s'], node_size=200, node_color='#FAC795', node_shape='s')

# 绘制椭圆形节点（第三列）
nx.draw_networkx_nodes(G, pos, nodelist=node_shapes['p'], node_size=6000, node_color='#299D7A', node_shape='o')

# 绘制 Cybercrime 节点
nx.draw_networkx_nodes(G, pos, nodelist=["Cybercrime"], node_size=8000, node_color='#F09739', node_shape='o')

# 为边添加不同的连接样式
edges_with_arc = []
edges_with_straight = []

# 遍历边并分组
for u, v in G.edges():
    if u in third_col_nodes and v in third_col_nodes:
        edges_with_arc.append((u, v))  # 第三列之间的边
    else:
        edges_with_straight.append((u, v))  # 其他边

# 绘制有向边
nx.draw_networkx_edges(G, pos, edgelist=edges_with_straight, width=2, arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=edges_with_arc, width=2, arrows=True, connectionstyle='arc3,rad=0.7')

# 添加标签
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# 标题
plt.title("Graph based on user description with custom node shapes")
plt.axis('off')  # 不显示坐标轴
plt.show()
