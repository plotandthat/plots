from iso3166 import countries_by_name
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb


def get_country_code(df_):
    c = df_["Country or Area"].upper()
    return countries_by_name[c].alpha3 if c in countries_by_name else "NOT FOUND"


def get_country_num(df_):
    c = df_["Country or Area"].upper()
    return countries_by_name[c].numeric if c in countries_by_name else "NOT FOUND"


# df = df[(df["Element"] == "Production") & (df["Year"] == 2017)]
#
# # Compute a new variable, alpha3 country code
# df["country_code"] = df.apply(get_country_code, axis=1)
# df.to_csv("processed_data_.csv")


# Compute a new variable, numerical country code
# df = pd.read_csv("processed_data.csv")
# df["country_num"] = df.apply(get_country_num, axis=1)
# df.to_csv("processed_new.csv")


pop_df = pd.read_csv("pop_data.csv", encoding="latin1")
aub_df = pd.read_csv("processed_new.csv")


def get_pop(df_):
    c_num = df_["country_num"]

    try:
        return pop_df[pop_df["Country code"] == c_num]["pop"].values[0]
    except KeyError:
        print(c_num)
        return "NOT FOUND"

aub_df["population"] = aub_df.apply(get_pop, axis=1)
aub_df.to_csv("full_data.csv")

# Define a function to make geographical (choropleth) plots, for a given variable
def geo_plot_means_by_country(df):
    # Get country data, exclude Antarctica, and re-project to Winkel-Tripel
    gdf = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
    gdf = gdf[(gdf.name != "Antarctica") & (gdf.name != "Fr. S. Antarctic Lands")]
    gdf = gdf.to_crs('+proj=wintri')

    merged = gdf.merge(df, left_on="iso_a3", right_on="country_code")

    # Plot the base map with the overlaid choropleth
    base = gdf.plot(color="0.75", edgecolor="black")
    merged.plot(ax=base, column=var, edgecolor="black", legend=True)

    # Format the resulting figure
    fig = plt.gcf()
    ax = plt.gca()
    ax.grid(False)
    ax.set_axis_off()
    ax.margins(0)
    ax.set_title("Aubergines per country")
    fig.set_size_inches(12, 6)


# df = pd.read_csv("processed_data.csv")
# print(df.head())
