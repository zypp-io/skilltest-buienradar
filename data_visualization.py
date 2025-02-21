import seaborn as sns

import sqlalchemy
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("TkAgg")  # Prevents crashing of python when showing plot


class DataVisualization:
    """
    Class to perform data visualization
    """

    def __init__(self):
        self.engine = sqlalchemy.create_engine('sqlite:///data/database.db', echo=False)
        self.conn = self.engine.connect()

    def plot_temperature(self, df: pd.DataFrame) -> None:
        """
        Plot the temperature of weather stations in the Netherlands.
        """
        average_temperature = df["temperature"].mean()
        max_temperature = df.loc[df["temperature"] == max(df["temperature"]), "temperature"]

        # Make the plot
        g = sns.barplot(df.sort_values("regio"), x="regio", y="temperature")
        plt.xticks(rotation=90)
        g.axhline(y=average_temperature, color="red")
        plt.text(x=40,
                 y=average_temperature,
                 s=f"Average: \n{'{:.2f}'.format(average_temperature)}",
                 color="red")
        plt.text(x=max_temperature.index[0] - 1.5,
                 y=max_temperature.iloc[0] + 0.1,
                 s=f"Max: \n{'{:.2f}'.format(max_temperature.iloc[0])}",
                 color="orange")
        plt.title(f"Temperature in the Netherlands on {' at '.join(df['timestamp'][0].split('T'))}")
        plt.tight_layout()
        g.axes.spines['top'].set_visible(False)
        g.axes.spines['right'].set_visible(False)
        plt.savefig("graphs/temperature.png")
        plt.close()

    def plot_temperature_difference(self, df: pd.DataFrame, exclude_na=True) -> None:
        """
        Plot the difference in actual & feel temperature
        """
        if exclude_na:
            df = df.loc[(df["temperature"].notna()) & (df["feeltemperature"].notna())].copy()

        # Format plot data
        df["windspeedBft"] = df["windspeedBft"].fillna(-1)
        df["regio"] = df["regio"] + "(" + df.windspeedBft.astype(int).astype(str) + ")"
        plot_data = pd.melt(df,
                            id_vars=["regio", "windspeedBft"],
                            value_vars=["temperature", "feeltemperature"],
                            value_name="Temperature")

        # Make the plot
        g = sns.barplot(plot_data.sort_values(["windspeedBft", "regio"]), x="regio", y="Temperature", hue="variable")
        plt.xticks(rotation=90)
        plt.title(f"Difference in actual & feel temperature, sorted by Windspeed (Bft)")
        plt.tight_layout()
        g.axes.spines['top'].set_visible(False)
        g.axes.spines['right'].set_visible(False)
        plt.savefig("graphs/temperature_difference.png")
        plt.close()

    def plot_weather_stations(self, df: pd.DataFrame) -> None:
        """
        Plot the location & temperature of weather stations in the Netherlands.
        """
        g = sns.scatterplot(df, x="lon", y="lat", hue="temperature", palette=sns.color_palette("icefire", as_cmap=True))

        plt.title(f"Temperature in the Netherlands on {' at '.join(df['timestamp'][0].split('T'))}")
        plt.tight_layout()
        g.axes.legend(bbox_to_anchor=(1.1, 1.05))
        g.axes.spines['top'].set_visible(False)
        g.axes.spines['bottom'].set_visible(False)
        g.axes.spines['left'].set_visible(False)
        g.axes.spines['right'].set_visible(False)
        plt.gca().set_aspect('equal')
        plt.savefig("graphs/weather_stations.png")
        plt.close()

    def run(self):
        # Collect data in a dataframe
        query = f"SELECT * " \
                f"FROM station_measurements " \
                f"INNER JOIN weather_stations ON station_measurements.stationid = weather_stations.stationid"

        df = pd.read_sql_query(query, self.conn)

        self.plot_temperature(df)
        self.plot_temperature_difference(df)
        self.plot_weather_stations(df)


if __name__ == "__main__":
    Visualization = DataVisualization()
    Visualization.run()
