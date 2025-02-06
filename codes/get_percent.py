import pandas as pd
import numpy as np

# 加载数据
csv_path = "data\\cybercrime_country_ranking.xlsx"  # 修改为实际路径
data = pd.read_excel(csv_path)

# 数据归一化，将所有输入数据映射到 [0, 1]
data['x1'] = data['count'] / 350  # count：归一化到 [0, 1]
data['x2'] = data['avg_impact'] / 10  # avg_impact：归一化到 [0, 1]
data['x3'] = data['avg_professional'] / 10  # avg_professional：归一化到 [0, 1]
data['x4'] = data['avg_techskill'] / 10  # avg_techskill：归一化到 [0, 1]
data['x5'] = data['overall_score'] / 300  # overall_score：归一化到 [0, 1]

# 成功率（Success Rate）
# success_rate = 0.4 * x3 + 0.4 * x4 + 0.2 * x5
data['success_rate'] = 0.4 * data['x3'] + 0.4 * data['x4'] + 0.2 * data['x5']
data['success_rate'] = data['success_rate'].clip(0, 1)  # 确保在 [0, 1]

# 挫败率（Frustration Rate）
# frustration_rate = 1 - success_rate
data['frustration_rate'] = 1 - data['success_rate']
data['frustration_rate'] = data['frustration_rate'].clip(0, 1)  # 确保在 [0, 1]

# 举报率（Reported Rate）
# report_rate = 0.3 * x1 + 0.3 * x2 + 0.2 * (1 - x3) + 0.2 * (1 - x4)
data['report_rate'] = (
    0.3 * data['x1'] + 0.3 * data['x2'] +
    0.2 * (1 - data['x3']) + 0.2 * (1 - data['x4'])
)
data['report_rate'] = data['report_rate'].clip(0, 1)  # 确保在 [0, 1]

# 起诉率（Prosecution Rate）
# prosecution_rate = 0.5 * report_rate + 0.3 * frustration_rate + 0.2 * x5
data['prosecution_rate'] = (
    0.5 * data['report_rate'] +
    0.3 * data['frustration_rate'] +
    0.2 * data['x5']
)
data['prosecution_rate'] = data['prosecution_rate'].clip(0, 1)  # 确保在 [0, 1]

# 保存结果到 CSV 文件
output_path = "cybercrime_rates_model_output.csv"
data[['country', 'success_rate', 'frustration_rate', 'report_rate', 'prosecution_rate']].to_csv(output_path, index=False)

print(f"计算完成，结果已保存到 {output_path}")
