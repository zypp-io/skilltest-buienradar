import sqlalchemy
import pandas as pd


class DataAnalysis:
    """
    Class to perform data analysis
    """

    def __init__(self):
        self.engine = sqlalchemy.create_engine('sqlite:///data/database.db', echo=False)
        self.conn = self.engine.connect()

    def run(self):
        """
        Run the analysis:

        1. Which weather station recorded the highest temperature ?
        2. What is the average temperature?
        3. What is the station with the biggest difference between feel temperature and the actual temperature?
        4. Which weather station is located in the North Sea?
        """
        print("\n1. Which weather station recorded the highest temperature ?")
        query = f"SELECT station_measurements.stationid, stationname, MAX(temperature) " \
                f"FROM station_measurements " \
                f"INNER JOIN weather_stations ON station_measurements.stationid = weather_stations.stationid"

        print(pd.read_sql_query(query, self.conn))

        print("\n2. What is the average temperature?")
        query = f"SELECT AVG(temperature) " \
                f"FROM station_measurements "

        print(pd.read_sql_query(query, self.conn))

        print("\n3. What is the station with the biggest difference between feel temperature and the actual temperature?")
        query = f"SELECT station_measurements.stationid, stationname, MAX(ABS(feeltemperature - temperature)) as diff " \
                f"FROM station_measurements " \
                f"INNER JOIN weather_stations ON station_measurements.stationid = weather_stations.stationid"

        print(pd.read_sql_query(query, self.conn))

        print("\n4. Which weather station is located in the North Sea?")
        query = f"SELECT * " \
                f"FROM weather_stations " \
                f"WHERE regio LIKE '%Noordzee%' "

        print(pd.read_sql_query(query, self.conn))


if __name__ == "__main__":
    Analysis = DataAnalysis()
    Analysis.run()
