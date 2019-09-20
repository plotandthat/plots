import joypy
import matplotlib.pyplot as plt
import pandas as pd

# Daily temperature data (from 1938 onwards so that fewer distributions are drawn)
df = pd.read_csv("Complete_TAVG_daily.csv", comment="%")
df = df[df["Year"] >= 1938]

# Compute a new variable, mean-centered temperature
df["temp_scaled"] = df.groupby("Year")["Anomaly"].transform(lambda x: (x - x.mean()))

# Make some space around the plot itself
plt.subplots_adjust(left=0, right=1, top=1.5, bottom=1)
plt.margins(1)

fig, axes = joypy.joyplot(df, by="Year", column="temp_scaled", ylabels=False, xlabels=False,
                          grid=False, color="black", background="black", linecolor="white", linewidth=1.3,
                          legend=False, figsize=(12, 6), kind="counts", bins=60)

for a in axes[:-1]:
    a.set_xlim([-8, 8])

plt.show()
