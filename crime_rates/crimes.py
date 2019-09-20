import matplotlib.pyplot as plt
import pandas as pd
from pywaffle import Waffle
import seaborn as sb

# Crimes data comes from the Police API: https://data.police.uk/docs/
df = pd.read_csv("all_data.csv")
crimes_order = list(df[df["region"] == "Salford"]["category"].value_counts().index)
colours = ["#DA291C", "#A3C1AD"]

# Plot crimes data
sb.catplot(data=df, y="category", hue="region", kind="count", order=crimes_order, palette=colours, legend=False)
plt.ylabel("")
plt.xlabel("Number of crimes committed", fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(title="Region:", title_fontsize=16, fontsize=14, loc=4, fancybox=True)
plt.gcf().set_size_inches(14, 8)

# Plot cycling data, from the Department for Transport:
# https://www.gov.uk/government/statistical-data-sets/walking-and-cycling-statistics-cw
cycling_data = {'Salford': 9.88, 'Cambridge': 57.49}

# N.B. pywaffle with "icons" specified effectively produces a pictogram
fig = plt.figure(
    FigureClass=Waffle,
    rows=10,
    values=cycling_data,
    colors=("#DA291C", "#A3C1AD"),
    icons='bicycle', icon_size=20,
)

plt.gca().get_legend().remove()
plt.title("% of people cycling\nat least once per week", fontsize=14)
fig.set_facecolor('#FFFFFF')
plt.show()
