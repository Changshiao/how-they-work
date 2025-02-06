import os
import json
import pandas as pd

# 定义 JSON 文件所在的文件夹路径
folder_path = r"VCDB-master\\data\\json\\validated"

# 初始化一个字典，用于存储结果
data_summary = {}

# 遍历文件夹中的每个 JSON 文件
for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):  # 确保只处理 JSON 文件
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                # 读取 JSON 文件并解析为字典
                data = json.load(file)

                # 提取受害国家和攻击来源国家
                victim_countries = data.get("victim", {}).get("country", [])
                attacker_countries = data.get("actor", {}).get("external", {}).get("country", [])

                # 确保 victim_countries 和 attacker_countries 是列表
                if not isinstance(victim_countries, list):
                    victim_countries = [victim_countries]
                if not isinstance(attacker_countries, list):
                    attacker_countries = [attacker_countries]

                # 更新统计数据
                for country in victim_countries:
                    if country not in ["Unknown", "Others"]:
                        if country not in data_summary:
                            data_summary[country] = {"victim_count": 0, "attacker_count": 0}
                        data_summary[country]["victim_count"] += 1

                for country in attacker_countries:
                    if country not in ["Unknown", "Others"]:
                        if country not in data_summary:
                            data_summary[country] = {"victim_count": 0, "attacker_count": 0}
                        data_summary[country]["attacker_count"] += 1

            except json.JSONDecodeError:
                print(f"无法解析文件：{file_name}")
            except Exception as e:
                print(f"处理文件 {file_name} 时出错: {e}")

# 将统计结果转换为 DataFrame
result_df = pd.DataFrame.from_dict(data_summary, orient="index").fillna(0)

# 计算受攻击次数占总计次数（受攻击 + 主动攻击）的比值
result_df["vulnerability_ratio"] = result_df["victim_count"] / (result_df["victim_count"] + result_df["attacker_count"])

# 按比值排序，最容易受攻击的国家排在最上面
result_df = result_df.sort_values("vulnerability_ratio", ascending=False)

# 保存结果到 CSV 文件
output_path = "network_vulnerability_ratio_summary.csv"
result_df.to_csv(output_path, encoding="utf-8")

print(f"统计完成，结果已保存到 {output_path}")
