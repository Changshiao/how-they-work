import matplotlib.pyplot as plt
import numpy as np

# 数据准备
categories = {
    'Policy': {'Political stability': 6, 'Supervision quality': 7, 'Law measures': 9},
    'Society': {'Population': 36, 'Employment rate': 2, 'Education level': 19},
    'Economy': {'GDP growth': 14, 'purchasing power': 6},
    'Technology': {'Infrastructure': 23, 'Internet users': 8},
    'Cybersecurity': {'Cybersecurity Index': 9}
}


category_colors = {
    'Policy': ['#f2d7d5', '#e6b0aa', '#cd6155'],
    'Society': ['#d4e6f1', '#85c1e9', '#3498db'],
    'Economy': ['#d5f5e3', '#82e0aa'],
    'Technology': ['#fcf3cf', '#f9e79f'],
    'Cybersecurity': ['#d7bde2']
}

def plot_2d_pie_with_subcategories():
    # 准备数据，将每个子项独立出来
    sub_categories = []
    sub_category_labels = []
    sub_category_colors = []
    sub_category_main_labels = []

    for main_label, sub_items in categories.items():
        for sub_label, sub_value in sub_items.items():
            sub_categories.append(sub_value)
            sub_category_labels.append(sub_label)  # 只显示子项名称
            sub_category_colors.append(category_colors[main_label][list(sub_items.keys()).index(sub_label)])
            sub_category_main_labels.append(main_label)

    # 计算每个子项的总和
    total_size = sum(sub_categories)

    fig, ax = plt.subplots(figsize=(12, 10))

    # 计算间隔角度
    offset_angle = 10  # 调整此值以控制大类之间的间隔

    start_angle = 90
    wedges = []
    texts = []
    autotexts = []

    # 绘制每个大类的子项
    for i, (main_label, sub_items) in enumerate(categories.items()):
        sub_total = sum(sub_items.values())
        main_angle = (sub_total / total_size) * 360

        # 添加间隙
        start_angle += offset_angle  # 增加起始角度来创建间隔

        # 绘制每个大类的子项
        for j, (sub_label, sub_value) in enumerate(sub_items.items()):
            sub_angle = (sub_value / total_size) * 360
            wedges.append(ax.pie(
                [sub_value, sub_total - sub_value], 
                radius=1, 
                startangle=start_angle,
                colors=[sub_category_colors[i], 'white'],  # 修复颜色传递问题
                wedgeprops={'linewidth': 0}
            ))

            # 更新起始角度
            start_angle += sub_angle

        # 在大类的中心添加标签
        angle = start_angle - main_angle / 2
        x = 1.5 * np.cos(np.radians(angle))  # 调整这个值来控制标签的水平位置
        y = 1.5 * np.sin(np.radians(angle))  # 调整这个值来控制标签的垂直位置
        
        # 让 Technology 和 Cybersecurity 的位置稍微向左或者右调整，以避免重叠
        if main_label == 'Technology':
            x *= 1.9  # 向右调整
            y *= 0.7
        elif main_label == 'Cybersecurity':
            x *= 0.1  # 向左调整
            y *= 1.1
        elif main_label == 'Economy':
            x *= 0.9  # 向左调整
            y *= 3.4

        ax.text(x, y, main_label, ha='center', fontsize=14, fontweight='bold', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))

    # 绘制子项的比例
    wedges, texts, autotexts = ax.pie(
        sub_categories,
        labels=sub_category_labels,
        colors=sub_category_colors,
        autopct='%d%%',  # 保留整数
        startangle=90,
        wedgeprops={'linewidth': 0}  # 删除边沿线
    )

    # 自定义文本和样式
    for text in texts:
        text.set_fontsize(10)
        text.set_color("black")
        text.set_weight("bold")
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_color("black")  # 比例文本设置为黑色
        autotext.set_weight("bold")

    # 设置标题

    # 调整纵横比以模拟偏移效果
    ax.set_aspect(0.75)  # 使图表呈现椭圆形状，视觉上偏移

    plt.tight_layout()
    plt.show()

plot_2d_pie_with_subcategories()
