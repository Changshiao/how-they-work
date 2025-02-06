import pandas as pd

# 读取数据
data = pd.read_csv("data\wci_data.csv")

# 定义网络犯罪类型
crime_categories = ["Technical", "Attack", "Data", "Scams", "Cash"]

# 初始化国家统计字典
country_scores = {}

# 遍历每种犯罪类型，统计提名频率和评分
for category in crime_categories:
    for i in range(1, 6):  # 每种类型最多提名5个国家
        country_col = f"{category}{i}"
        impact_col = f"{category}{i}_impact"
        professional_col = f"{category}{i}_professional"
        techskill_col = f"{category}{i}_techskill"

        for index, row in data.iterrows():
            country = row[country_col]
            if pd.notna(country):  # 检查国家字段是否为空
                if country not in country_scores:
                    country_scores[country] = {"count": 0, "impact": 0, "professional": 0, "techskill": 0}

                # 累计提名次数
                country_scores[country]["count"] += 1

                # 累计评分
                country_scores[country]["impact"] += row[impact_col]
                country_scores[country]["professional"] += row[professional_col]
                country_scores[country]["techskill"] += row[techskill_col]

# 计算平均评分和综合得分
ranking = []
for country, scores in country_scores.items():
    avg_impact = scores["impact"] / scores["count"]
    avg_professional = scores["professional"] / scores["count"]
    avg_techskill = scores["techskill"] / scores["count"]

    # 计算综合得分 (提名次数权重为 80%，影响力权重为 15%，专业性和技术能力分别占 3% 和 2%)
    overall_score = (0.8 * scores["count"] + 0.15 * avg_impact + 0.03 * avg_professional + 0.02 * avg_techskill)

    ranking.append({
        "country": country,
        "count": scores["count"],
        "avg_impact": avg_impact,
        "avg_professional": avg_professional,
        "avg_techskill": avg_techskill,
        "overall_score": overall_score
    })

# 按综合得分排序
ranking_df = pd.DataFrame(ranking)
ranking_df = ranking_df.sort_values(by="overall_score", ascending=False)

# 输出为Excel文件
ranking_df.to_excel("cybercrime_country_ranking.xlsx", index=False)

# 打印结果
print(ranking_df)
