import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

csv_path = "cybercrime_rates_model_output.csv"
data = pd.read_csv(csv_path)

cleaned_data = data.dropna()

country_name_map = {
    "United States": "United States of America",
    "Korea, North": "North Korea",
    "Korea, South": "South Korea",
    "Iran ": "Iran",
}
cleaned_data['country'] = cleaned_data['country'].replace(country_name_map)

shapefile_path = "ne_10m_admin_0_countries"
world = gpd.read_file(shapefile_path)

cleaned_data['country'] = cleaned_data['country'].str.strip()
world['ADMIN'] = world['ADMIN'].str.strip()

world = world.merge(cleaned_data, how="left", left_on="ADMIN", right_on="country")

def plot_success_rate(column, title, cmap="OrRd"):
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    world.boundary.plot(ax=ax, linewidth=0.5, color="grey")
    world.plot(column=column, ax=ax, legend=True, cmap=cmap,
               legend_kwds={"label": "Success Rate", "orientation": "vertical", "shrink": 0.6},
               missing_kwds={"color": "lightgrey", "label": "No Data"})
    ax.set_title(title, fontsize=20, fontweight="bold", color="darkred")
    ax.axis("off")
    plt.tight_layout()
    plt.show()

plot_success_rate("success_rate", "Cybercrimes successful Rate Distribution", cmap="Blues")