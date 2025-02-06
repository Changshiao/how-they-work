import matplotlib.pyplot as plt

# Extended years and values for the plot
years = [
    1986, 1994, 1995, 1996, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 
    2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021, 2022, 2023
]
values = [
    5, 24, 56, 45, 88, 104, 113, 167, 194, 135, 175, 195, 245, 153, 314, 336, 573, 468, 996, 864, 
    1270, 707, 573, 467, 234, 211, 170, 357, 452, 747
]
predict_values = [
    None, None, None, None, None, None, None, None, None, None, None, None, 
    None, None, None, None, None, None, None, None, 1270, 1460, 1390, 1536, 1753, 1505, 1602, 1846, 2036, 2156
]

# Key cybersecurity policy years and names
policy_years = [1986, 1996, 2001, 2015, 2020]
policy_names = [
    "CFAA (1986)",
    "NIIPA (1996)",
    "Patriot Act (2001)",
    "CISA (2015)",
    "COVID-19"
]

# Plotting the data
plt.figure(figsize=(14, 8))

# Plot real values before 2015 and after 2015
plt.plot(years, values, marker='o', linestyle='-', linewidth=3, color='#456990', label="Actual Data")

# Plot predicted values only after 2015
plt.plot(years, predict_values, marker='x', linestyle='-', linewidth=3, color='#EF967A', label="Predicted Data")

# Mark cybersecurity policy years
plt.scatter(policy_years[:-1], [values[years.index(year)] for year in policy_years[:-1]],
            color='#88B04B', s=120, label="Cybersecurity Policies")
# Special marking for COVID-19
covid_year = 2020
plt.scatter(covid_year, values[years.index(covid_year)], color='#FF6F61', s=150, label="COVID-19")

# Annotating policy names
for year, name in zip(policy_years, policy_names):
    if year == 2015:
        plt.text(year + 1, values[years.index(year)] + 100, name, fontsize=10, ha='center', color='black')
    elif year == 2020:
        plt.text(year, values[years.index(year)] - 150, name, fontsize=12, ha='center', color='black', fontweight='bold')
    else:
        plt.text(year, values[years.index(year)] + 100, name, fontsize=10, ha='center', color='black')

# Adding titles and labels
plt.title("US Cybersecurity Policies and Trends (Actual vs Predicted)", fontsize=18, fontweight='bold', color='black')
plt.xlabel("Year", fontsize=14, fontweight='bold', color='black')
plt.ylabel("Value", fontsize=14, fontweight='bold', color='black')

# Customize ticks
plt.xticks(years[::2], rotation=45, fontsize=12, color='black')
plt.yticks(fontsize=12, color='black')

# Remove gridlines for a cleaner look
plt.grid(False)

# Adding a legend
plt.legend(fontsize=12, loc='upper left', frameon=True, shadow=True, edgecolor='black')

# Display the plot
plt.tight_layout()
plt.show()

