import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# 基础数据
categories = [
    'Data Protection Policies', 'Cybersecurity Monitoring', 'Cybersecurity Education and Training', 
    'Critical Infrastructure Protection', 'Incident Response and Recovery', 'Cybersecurity Accountability', 
    'Highest Law Enforcement Efforts', 'Establishment of Regulatory Bodies', 'Talent Development', 
    'Information Sharing Platforms'
]

estimates_data = {
    "High Income": np.array([
        [0.31, 0.42, 0.27], [0.23, 0.14, 0.06], [0.36, 0.25, 0.58], [0.51, 0.28, 0.37],
        [0.68, 0.59, 0.81], [0.73, 0.62, 0.91], [0.57, 0.26, 0.63], [0.45, 0.38, 0.21],
        [0.53, 0.19, 0.18], [0.83, 0.63, 0.91]
    ]),
    "Middle Income": np.array([
        [0.35, 0.33, 0.24], [0.24, 0.15, 0.17], [0.43, 0.34, 0.49], [0.47, 0.19, 0.36],
        [0.55, 0.45, 0.66], [0.63, 0.54, 0.84], [0.46, 0.27, 0.58], [0.34, 0.29, 0.29],
        [0.42, 0.16, 0.25], [0.72, 0.53, 0.85]
    ]),
    "Low Income": np.array([
        [0.26, 0.21, 0.14], [0.18, 0.05, 0.09], [0.25, 0.15, 0.36], [0.33, 0.15, 0.26],
        [0.48, 0.35, 0.56], [0.58, 0.43, 0.76], [0.38, 0.18, 0.47], [0.24, 0.18, 0.16],
        [0.35, 0.07, 0.15], [0.65, 0.46, 0.73]
    ])
}

groups = ['High Income', 'Middle Income', 'Low Income']
group_colors = ['#1E88E5', '#43A047', '#F4511E']  # 美观的颜色
symbols = ['^', 'o', 's']  # 图标样式

# 绘图函数
def plot_estimates(estimates, title):
    # 创建随机误差：误差在±0.1之间波动，且设置最低误差阈值
    error_range = 0.15
    min_error_threshold = 0.05  # 设置最低误差阈值
    random_errors = np.abs(np.random.uniform(-error_range, error_range, estimates.shape))
    random_errors = np.maximum(random_errors, min_error_threshold)  # 确保误差不低于阈值

    fig, ax = plt.subplots(figsize=(7, 12))  # 调整图表为瘦高比例
    y_positions = []
    gap_between_items = 2
    current_y = 0

    for _ in range(len(categories)):
        y_positions.append(current_y)
        current_y += gap_between_items

    offset = np.linspace(-0.4, 0.4, len(groups))
    for i, (group, color, symbol) in enumerate(zip(groups, group_colors, symbols)):
        for cat_idx in range(len(categories)):
            ax.errorbar(estimates[cat_idx, i], y_positions[cat_idx] + offset[i],
                        xerr=random_errors[cat_idx, i], fmt=symbol, color=color,
                        label=group if cat_idx == 0 else "", capsize=3)

    # 添加背景色，每个项目的交替背景色
    for idx, pos in enumerate(y_positions):
        if idx % 2 == 0:
            ax.axhspan(pos - 1, pos + 1, color='#d0d0d0', zorder=0)
        else:
            ax.axhspan(pos - 1, pos + 1, color='#e0e0e0', zorder=0)

    ax.set_yticks(y_positions)
    ax.set_yticklabels(categories)
    ax.axvline(0, color='gray', linewidth=0.8, linestyle='--')
    ax.set_xlim(-1, 1)  # 固定横轴范围为 [-1, 1]
    ax.set_xlabel('Estimates', fontsize=14, fontweight='bold')
    ax.set_title(title, fontsize=16, fontweight='bold')

    # 图例设置
    legend_elements = [
        Line2D([0], [0], marker='^', color='w', markerfacecolor=group_colors[0], markersize=10, label='High Income'),    ]
    ax.legend(handles=legend_elements, title='Income Group', bbox_to_anchor=(0.5, -0.1), loc='upper center', frameon=False, ncol=3)
    ax.set_ylim(min(y_positions) - 2, max(y_positions) + 2)

    plt.tight_layout()
    plt.show()
for income_group, estimates in estimates_data.items():
    plot_estimates(estimates, f'Cybercrime Frustration')
